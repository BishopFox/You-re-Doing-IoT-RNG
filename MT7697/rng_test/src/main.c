/* Copyright Statement:
 *
 * (C) 2005-2016  MediaTek Inc. All rights reserved.
 *
 * This software/firmware and related documentation ("MediaTek Software") are
 * protected under relevant copyright laws. The information contained herein
 * is confidential and proprietary to MediaTek Inc. ("MediaTek") and/or its licensors.
 * Without the prior written permission of MediaTek and/or its licensors,
 * any reproduction, modification, use or disclosure of MediaTek Software,
 * and information contained herein, in whole or in part, shall be strictly prohibited.
 * You may only use, reproduce, modify, or distribute (as applicable) MediaTek Software
 * if you have agreed to and been bound by the applicable license agreement with
 * MediaTek ("License Agreement") and been granted explicit permission to do so within
 * the License Agreement ("Permitted User").  If you are not a Permitted User,
 * please cease any access or use of MediaTek Software immediately.
 * BY OPENING THIS FILE, RECEIVER HEREBY UNEQUIVOCALLY ACKNOWLEDGES AND AGREES
 * THAT MEDIATEK SOFTWARE RECEIVED FROM MEDIATEK AND/OR ITS REPRESENTATIVES
 * ARE PROVIDED TO RECEIVER ON AN "AS-IS" BASIS ONLY. MEDIATEK EXPRESSLY DISCLAIMS ANY AND ALL
 * WARRANTIES, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF
 * MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE OR NONINFRINGEMENT.
 * NEITHER DOES MEDIATEK PROVIDE ANY WARRANTY WHATSOEVER WITH RESPECT TO THE
 * SOFTWARE OF ANY THIRD PARTY WHICH MAY BE USED BY, INCORPORATED IN, OR
 * SUPPLIED WITH MEDIATEK SOFTWARE, AND RECEIVER AGREES TO LOOK ONLY TO SUCH
 * THIRD PARTY FOR ANY WARRANTY CLAIM RELATING THERETO. RECEIVER EXPRESSLY ACKNOWLEDGES
 * THAT IT IS RECEIVER'S SOLE RESPONSIBILITY TO OBTAIN FROM ANY THIRD PARTY ALL PROPER LICENSES
 * CONTAINED IN MEDIATEK SOFTWARE. MEDIATEK SHALL ALSO NOT BE RESPONSIBLE FOR ANY MEDIATEK
 * SOFTWARE RELEASES MADE TO RECEIVER'S SPECIFICATION OR TO CONFORM TO A PARTICULAR
 * STANDARD OR OPEN FORUM. RECEIVER'S SOLE AND EXCLUSIVE REMEDY AND MEDIATEK'S ENTIRE AND
 * CUMULATIVE LIABILITY WITH RESPECT TO MEDIATEK SOFTWARE RELEASED HEREUNDER WILL BE,
 * AT MEDIATEK'S OPTION, TO REVISE OR REPLACE MEDIATEK SOFTWARE AT ISSUE,
 * OR REFUND ANY SOFTWARE LICENSE FEES OR SERVICE CHARGE PAID BY RECEIVER TO
 * MEDIATEK FOR SUCH MEDIATEK SOFTWARE AT ISSUE.
 */

#include <stdint.h>
#include <stdio.h>
#include <string.h>
#include <time.h>

#include "FreeRTOS.h"
#include "task.h"
#include "task_def.h"
#include "syslog.h"

#include "sys_init.h"
#include "wifi_api.h"
#include "wifi_lwip_helper.h"
#include "httpclient.h"
#include "hal_lp.h"
#include "hal_trng.h"

#define WIFI_SSID                ("TODO_YOUR_WIFI")
#define WIFI_PASSWORD            ("TODO_YOUR_PASSWORD")

#define BUF_SIZE        (1024 * 1)
#define HTTP_GET_URL    "TODO_YOUR_IP"

log_create_module(http_client_retrieve_example, PRINT_LEVEL_INFO);

uint32_t get_random_number_from_hardware(void)
{
    uint32_t            number;
    hal_trng_status_t   status = HAL_TRNG_STATUS_ERROR;

    while(status != HAL_TRNG_STATUS_OK) {
        status = hal_trng_get_generated_random_number(&number);
    }

    return number;
}

/**
  * @brief      Http client connect to test server and test "retrieve" function.
  * @param      None
  * @return     None
  */
void httpclient_test_retrieve(void)
{
    char *get_url = HTTP_GET_URL;
    HTTPCLIENT_RESULT ret;
    httpclient_t client = {0};
    char *buf, *payload;
    httpclient_data_t client_data = {0};
    int count = 0;
    char *content_type = "text/csv";
    uint32_t payload_size = 1024 * 64;

    // Connect to server
    ret = httpclient_connect(&client, get_url);
    buf = pvPortMalloc(BUF_SIZE);
    payload = malloc(payload_size);

    for(int i = 0; i < 1000; i++) {
        // Generate out payload of random numbers
        for (int i = 0; i < payload_size; i += sizeof(uint32_t)) {
          uint32_t number = get_random_number_from_hardware();
          memcpy(payload + i, &number, sizeof(uint32_t));
        }

        if (!ret) {
            client_data.response_buf = buf;
            client_data.response_buf_len = BUF_SIZE;
            client_data.post_content_type = content_type;
            client_data.post_buf = payload;
            client_data.post_buf_len = payload_size;

            // Send request to server
            ret = httpclient_send_request(&client, get_url, HTTPCLIENT_POST, &client_data);
            if (ret < 0) {
    			     goto fail;
            }

            do {
                // Receive response from server
                ret = httpclient_recv_response(&client, &client_data);
                if (ret < 0)
                    goto fail;
                count += strlen(client_data.response_buf);
            } while (ret == HTTPCLIENT_RETRIEVE_MORE_DATA);
            // LOG_I(http_client_retrieve_example, "total length: %d", client_data.response_content_len);
        }
    }

fail:
    // Close http connection
    httpclient_close(&client);
    free(payload);
    vPortFree(buf);
}

/**
  * @brief      Create a task for http client retrieve example
  * @param[in]  void *args: Not used
  * @return     None
  */
void app_entry(void *args)
{
    lwip_net_ready();

    // Httpclient "retrieve" feature test
    httpclient_test_retrieve();

    while (1) {
        vTaskDelay(1000 / portTICK_RATE_MS); // release CPU
    }
}

/**
  * @brief      Main program
  * @param      None
  * @return     None
  */
int main(void)
{
    /* Do system initialization, eg: hardware, nvdm, logging and random seed. */
    system_init();

    hal_trng_status_t   rng_status;
    rng_status = hal_trng_init();
    if (rng_status != HAL_TRNG_STATUS_OK) {
        LOG_I(http_client_retrieve_example, "trng init failed\n");
        exit(1);
    }

    /* system log initialization.
        * This is the simplest way to initialize system log, that just inputs three NULLs
        * as input arguments. User can use advanved feature of system log along with NVDM.
        * For more details, please refer to the log dev guide under /doc folder or projects
        * under project/mtxxxx_hdk/apps/.
        */
    log_init(NULL, NULL, NULL);

    LOG_I(http_client_retrieve_example, "FreeRTOS Running");

    /* User initial the parameters for wifi initial process,  system will determin which wifi operation mode
        * will be started , and adopt which settings for the specific mode while wifi initial process is running
        */
    wifi_config_t config = {0};
    config.opmode = WIFI_MODE_STA_ONLY;
    strcpy((char *)config.sta_config.ssid, WIFI_SSID);
    strcpy((char *)config.sta_config.password, WIFI_PASSWORD);
    config.sta_config.ssid_length = strlen(WIFI_SSID);
    config.sta_config.password_length = strlen(WIFI_PASSWORD);

    /* Initialize wifi stack and register wifi init complete event handler,
        * notes:  the wifi initial process will be implemented and finished while system task scheduler is running.
        */
    wifi_init(&config, NULL);

    /* Tcpip stack and net interface initialization,  dhcp client, dhcp server process initialization. */
    lwip_network_init(config.opmode);
    lwip_net_start(config.opmode);

    /* Create a user task for demo when and how to use wifi config API  to change WiFI settings,
        * Most WiFi APIs must be called in task scheduler, the system will work wrong if called in main(),
        * For which API must be called in task, please refer to wifi_api.h or WiFi API reference.
        * xTaskCreate(user_wifi_app_entry,
        *       UNIFY_USR_DEMO_TASK_NAME,
        *       UNIFY_USR_DEMO_TASK_STACKSIZE / 4,
        *       NULL, UNIFY_USR_DEMO_TASK_PRIO, NULL);
        */
    xTaskCreate(app_entry, APP_TASK_NAME, APP_TASK_STACKSIZE/sizeof(portSTACK_TYPE), NULL, APP_TASK_PRIO, NULL);

    /* Start the scheduler. */
    vTaskStartScheduler();

    /* If all is well, the scheduler will now be running, and the following line
        * will never be reached.  If the following line does execute, then there was
        * insufficient FreeRTOS heap memory available for the idle and/or timer tasks
        * to be created.  See the memory management section on the FreeRTOS web site
        * for more details.
        */
    for ( ;; );
}
