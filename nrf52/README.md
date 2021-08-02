## SDK Gotchas

Contiki-NG: The OS for Next Generation IoT Devices

https://github.com/contiki-ng/contiki-ng

Uses libc rand as the random number generator. Seeded using the hwRNG:

https://github.com/contiki-ng/contiki-ng/blob/48a3799e2d2c52e91cb7153b163bb26dfd9a4b4f/arch/cpu/nrf52840/dev/random.c

And yes, this insecure rand() is used to generate crypto keys:

https://github.com/contiki-ng/contiki-ng/blob/48a3799e2d2c52e91cb7153b163bb26dfd9a4b4f/examples/platform-specific/cc2538-common/pka/ecc-ecdh.c

Disclosed to the Contiki-ng team.

## Statistical Findings

TODO
