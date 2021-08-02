# MediaTek 7697

# Results

Histogram of how often each byte occurs. Bytes 0 -> 255 on the X axis.

![MT](/MT7697/pics/mt7697_pattern.png)

Biased towards zero: .503 vs .497 it seems.

## Insecure Usage in Example Code

Most developers don't write new code from complete scratch. They use the example code provided by the manufacturer and build from there. The following snippet is from the Linkit public SDK version 4.6.1. (Latest)

```
/**
* @brief       This function is to get random seed.
* @param[in]   None.
* @return      None.
*/
static void _main_sys_random_init(void)
{
/*This option is to enable TRNG(Ture Random Number Generator).*/
#if defined(HAL_TRNG_MODULE_ENABLED)
    uint32_t            seed;
    hal_trng_status_t   s;

    s = hal_trng_init();

    if (s == HAL_TRNG_STATUS_OK) {
        s = hal_trng_get_generated_random_number(&seed);
    }

    if (s == HAL_TRNG_STATUS_OK) {
        srand((unsigned int)seed);
    }

    if (s != HAL_TRNG_STATUS_OK) {
        LOG_I(common, "trng init failed\n");
    }
#endif /* HAL_TRNG_MODULE_ENABLED */
}
```

This example code shows using the hardware entropy source to seed libc `rand()`, which is then used as the pRNG going forward. This will produce a wildly insecure device when used this way.

# Building new firmware

linkit7697 runs x86. So no cross-compiling needed! yay

Download the SDK. You can find it on the MediaTek website here: https://docs.labs.mediatek.com/resource/mt7687-mt7697/en/get-started-linkit-7697-hdk/gcc-arm-embedded-linkit-7697/get-linkit-sdk-linkit-7697
It's under "For Public Users (Public SDK Package)".
- Unzip the SDK
- Modify the RNG testing code to work for you.
  - In this repository, edit the file: `mediatek_mt7897/rng_test/src/main.c`
  - It will contain three values you need to change, each starting with the word TODO.
      - WIFI_SSID, WIFI_PASSWORD, and HTTP_GET_URL
  - We'll explain what these are in the next section. You can try compiling this as-is for now, but you'll need to fix this eventually in order to make it work.
- Copy the custom RNG testing source code into the correct folder.
  - Modified code is under: `/rng_test`
  - Copy that into: `/LinkIt_SDK_V4.6.1_public/project/linkit7697_hdk/apps/`
- Now run the build script that's in `/LinkIt_SDK_V4.6.1_public`:
  - `./build.sh linkit7697_hdk rng_test`
- This will make a firmware file in the folder:
  - `LinkIt_SDK_V4.6.1_public/out/linkit7697_hdk/rng_test/rng_test.bin`

# Flashing the firmware
Now we just need to move the program over to the linkit dev board. It uses serial to flash, so figure out what device the serial port comes back as.

On my machine, it was `/dev/ttyUSB0`

The flashing utility is a Python (v2) script that's over in `/mt76x7-uploader`

Run the utility like:
- `python upload.py -p mt7697 -t cm4 -c /dev/ttyUSB0 -f YOUR_BIN_FILE_FROM_ABOVE`

And that's it! The board may need a reboot after flashing.

# Getting numbers

What the code on the dev board does is read 65kB of random data, and then connect to a Wi-Fi network nearby and make an HTTP post with the contents of the data. This means that in order to actually get the bits out, you're going to need to setup a Wi-Fi network (or just use an existing one, it doesn't need anything special).

Also, you're going to need to run the `server.py` script provided here. What it does is listen on port 8080 and take any data that it receives via a POST and concatenates it to the file `randomnumbers.bin`. If you're running this on your laptop, make sure that your firewall settings aren't blocking you. Also make sure that Wi-Fi AP-isolation is off.

TL;DR: The LinkIt dev board connects to Wi-Fi and does an HTTP post with the random bits to a server you have to run. The board keeps running so long as it has power, so just let it run and the server will accumulate bits.  
