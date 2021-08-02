#include <stdio.h>
#include <stdint.h>
#include "nrf_delay.h"
#include "app_error.h"
#include "nrf_drv_rng.h"
#include "nrf_assert.h"


#include "nrf_log.h"
#include "nrf_log_ctrl.h"
#include "nrf_log_default_backends.h"


#define RANDOM_BUFF_SIZE    16      /**< Random numbers buffer size. */

/** @brief Function for getting vector of random numbers.
 *
 * @param[out] p_buff       Pointer to unit8_t buffer for storing the bytes.
 * @param[in]  length       Number of bytes to take from pool and place in p_buff.
 *
 * @retval     Number of bytes actually placed in p_buff.
 */
static uint8_t random_vector_generate(uint8_t * p_buff, uint8_t size)
{
    uint32_t err_code;
    uint8_t  available;

    nrf_drv_rng_bytes_available(&available);
    uint8_t length = MIN(size, available);

    // Use this line instead if you want to spinloop waiting for device
    //  It doesn't matter though, since we check the bytes available above
    // nrf_drv_rng_block_rand()p_buff, length;
    // err_code = NRF_SUCCESS;
    err_code = nrf_drv_rng_rand(p_buff, length);
    APP_ERROR_CHECK(err_code);

    return length;
}

/** @brief Function for main application entry.
 */
int main(void)
{
    uint32_t err_code;

    err_code = NRF_LOG_INIT(NULL);
    APP_ERROR_CHECK(err_code);

    NRF_LOG_DEFAULT_BACKENDS_INIT();

    err_code = nrf_drv_rng_init(NULL);
    APP_ERROR_CHECK(err_code);

    NRF_LOG_INFO("RNG example started.");

    while (true)
    {
        uint8_t p_buff[RANDOM_BUFF_SIZE];
        uint8_t length = random_vector_generate(p_buff,RANDOM_BUFF_SIZE);
        NRF_LOG_INFO("Random Vector:");
        NRF_LOG_HEXDUMP_INFO(p_buff, length);
        NRF_LOG_INFO("");
        NRF_LOG_FLUSH();
        nrf_delay_ms(100);
    }
}
