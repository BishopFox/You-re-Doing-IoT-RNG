## LPC54628

### Results

Overall, good. As long as you follow the quirks listed below and spinloop on your RNG calls.

The few "weak" results from Dieharder were not consistent across multiple runs, so they appear to be an expected statistical outlier.

```
dieharder -g 201 -a -f LPC54628randData.bin0.bin
```
```
#=============================================================================#
#            dieharder version 3.31.1 Copyright 2003 Robert G. Brown          #
#=============================================================================#
   rng_name    |           filename             |rands/second|
 file_input_raw|       LPC54628randData.bin0.bin|  4.11e+07  |
#=============================================================================#
        test_name   |ntup| tsamples |psamples|  p-value |Assessment
#=============================================================================#
   diehard_birthdays|   0|       100|     100|0.95401257|  PASSED  
      diehard_operm5|   0|   1000000|     100|0.50107099|  PASSED  
  diehard_rank_32x32|   0|     40000|     100|0.73277433|  PASSED  
# The file file_input_raw was rewound 1 times
    diehard_rank_6x8|   0|    100000|     100|0.85605474|  PASSED  
# The file file_input_raw was rewound 1 times
   diehard_bitstream|   0|   2097152|     100|0.04061945|  PASSED  
# The file file_input_raw was rewound 2 times
        diehard_opso|   0|   2097152|     100|0.42402001|  PASSED  
# The file file_input_raw was rewound 2 times
        diehard_oqso|   0|   2097152|     100|0.91565940|  PASSED  
# The file file_input_raw was rewound 2 times
         diehard_dna|   0|   2097152|     100|0.85778825|  PASSED  
# The file file_input_raw was rewound 2 times
diehard_count_1s_str|   0|    256000|     100|0.83569697|  PASSED  
# The file file_input_raw was rewound 3 times
diehard_count_1s_byt|   0|    256000|     100|0.90057563|  PASSED  
# The file file_input_raw was rewound 3 times
 diehard_parking_lot|   0|     12000|     100|0.82688871|  PASSED  
# The file file_input_raw was rewound 3 times
    diehard_2dsphere|   2|      8000|     100|0.99845334|   WEAK   
# The file file_input_raw was rewound 3 times
    diehard_3dsphere|   3|      4000|     100|0.87467818|  PASSED  
# The file file_input_raw was rewound 4 times
     diehard_squeeze|   0|    100000|     100|0.11021778|  PASSED  
# The file file_input_raw was rewound 4 times
        diehard_sums|   0|       100|     100|0.00094639|   WEAK   
# The file file_input_raw was rewound 4 times
        diehard_runs|   0|    100000|     100|0.27890787|  PASSED  
        diehard_runs|   0|    100000|     100|0.06670090|  PASSED  
# The file file_input_raw was rewound 4 times
       diehard_craps|   0|    200000|     100|0.64682538|  PASSED  
       diehard_craps|   0|    200000|     100|0.93505556|  PASSED  
# The file file_input_raw was rewound 12 times
 marsaglia_tsang_gcd|   0|  10000000|     100|0.26582127|  PASSED  
 marsaglia_tsang_gcd|   0|  10000000|     100|0.55258500|  PASSED  
# The file file_input_raw was rewound 12 times
         sts_monobit|   1|    100000|     100|0.92462996|  PASSED  
# The file file_input_raw was rewound 12 times
            sts_runs|   2|    100000|     100|0.27269505|  PASSED  
# The file file_input_raw was rewound 12 times
          sts_serial|   1|    100000|     100|0.42489426|  PASSED  
          sts_serial|   2|    100000|     100|0.73886421|  PASSED  
          sts_serial|   3|    100000|     100|0.79370523|  PASSED  
          sts_serial|   3|    100000|     100|0.48706321|  PASSED  
          sts_serial|   4|    100000|     100|0.95108490|  PASSED  
          sts_serial|   4|    100000|     100|0.99118094|  PASSED  
          sts_serial|   5|    100000|     100|0.53923082|  PASSED  
          sts_serial|   5|    100000|     100|0.96429031|  PASSED  
          sts_serial|   6|    100000|     100|0.98078728|  PASSED  
          sts_serial|   6|    100000|     100|0.88201646|  PASSED  
          sts_serial|   7|    100000|     100|0.08417248|  PASSED  
          sts_serial|   7|    100000|     100|0.00077385|   WEAK   
          sts_serial|   8|    100000|     100|0.90826373|  PASSED  
          sts_serial|   8|    100000|     100|0.40876459|  PASSED  
          sts_serial|   9|    100000|     100|0.77042002|  PASSED  
          sts_serial|   9|    100000|     100|0.25819083|  PASSED  
          sts_serial|  10|    100000|     100|0.97227631|  PASSED  
          sts_serial|  10|    100000|     100|0.54883739|  PASSED  
          sts_serial|  11|    100000|     100|0.26863891|  PASSED  
          sts_serial|  11|    100000|     100|0.10063423|  PASSED  
          sts_serial|  12|    100000|     100|0.15467822|  PASSED  
          sts_serial|  12|    100000|     100|0.64357545|  PASSED  
          sts_serial|  13|    100000|     100|0.99056787|  PASSED  
          sts_serial|  13|    100000|     100|0.48016718|  PASSED  
          sts_serial|  14|    100000|     100|0.93748624|  PASSED  
          sts_serial|  14|    100000|     100|0.65801030|  PASSED  
          sts_serial|  15|    100000|     100|0.92152772|  PASSED  
          sts_serial|  15|    100000|     100|0.97466026|  PASSED  
          sts_serial|  16|    100000|     100|0.06940721|  PASSED  
          sts_serial|  16|    100000|     100|0.03047522|  PASSED  
# The file file_input_raw was rewound 12 times
         rgb_bitdist|   1|    100000|     100|0.81028378|  PASSED  
# The file file_input_raw was rewound 12 times
         rgb_bitdist|   2|    100000|     100|0.48961501|  PASSED  
# The file file_input_raw was rewound 12 times
         rgb_bitdist|   3|    100000|     100|0.70922784|  PASSED  
# The file file_input_raw was rewound 12 times
         rgb_bitdist|   4|    100000|     100|0.95659683|  PASSED  
# The file file_input_raw was rewound 13 times
         rgb_bitdist|   5|    100000|     100|0.75917772|  PASSED  
# The file file_input_raw was rewound 13 times
         rgb_bitdist|   6|    100000|     100|0.24510855|  PASSED  
# The file file_input_raw was rewound 14 times
         rgb_bitdist|   7|    100000|     100|0.22043988|  PASSED  
# The file file_input_raw was rewound 14 times
         rgb_bitdist|   8|    100000|     100|0.87690966|  PASSED  
# The file file_input_raw was rewound 15 times
         rgb_bitdist|   9|    100000|     100|0.75438828|  PASSED  
# The file file_input_raw was rewound 16 times
         rgb_bitdist|  10|    100000|     100|0.35564966|  PASSED  
# The file file_input_raw was rewound 17 times
         rgb_bitdist|  11|    100000|     100|0.99082405|  PASSED  
# The file file_input_raw was rewound 18 times
         rgb_bitdist|  12|    100000|     100|0.55252261|  PASSED  
# The file file_input_raw was rewound 18 times
rgb_minimum_distance|   2|     10000|    1000|0.37649725|  PASSED  
# The file file_input_raw was rewound 18 times
rgb_minimum_distance|   3|     10000|    1000|0.94121733|  PASSED  
# The file file_input_raw was rewound 18 times
rgb_minimum_distance|   4|     10000|    1000|0.69913288|  PASSED  
# The file file_input_raw was rewound 18 times
rgb_minimum_distance|   5|     10000|    1000|0.34454747|  PASSED  
# The file file_input_raw was rewound 18 times
    rgb_permutations|   2|    100000|     100|0.37163955|  PASSED  
# The file file_input_raw was rewound 18 times
    rgb_permutations|   3|    100000|     100|0.26163837|  PASSED  
# The file file_input_raw was rewound 18 times
    rgb_permutations|   4|    100000|     100|0.42708201|  PASSED  
# The file file_input_raw was rewound 19 times
    rgb_permutations|   5|    100000|     100|0.25052746|  PASSED  
# The file file_input_raw was rewound 19 times
      rgb_lagged_sum|   0|   1000000|     100|0.75596673|  PASSED  
# The file file_input_raw was rewound 20 times
      rgb_lagged_sum|   1|   1000000|     100|0.70511135|  PASSED  
# The file file_input_raw was rewound 21 times
      rgb_lagged_sum|   2|   1000000|     100|0.41293879|  PASSED  
# The file file_input_raw was rewound 22 times
      rgb_lagged_sum|   3|   1000000|     100|0.71482916|  PASSED  
# The file file_input_raw was rewound 24 times
      rgb_lagged_sum|   4|   1000000|     100|0.56378937|  PASSED  
# The file file_input_raw was rewound 26 times
      rgb_lagged_sum|   5|   1000000|     100|0.11977843|  PASSED  
# The file file_input_raw was rewound 29 times
      rgb_lagged_sum|   6|   1000000|     100|0.59246977|  PASSED  
# The file file_input_raw was rewound 32 times
      rgb_lagged_sum|   7|   1000000|     100|0.64162601|  PASSED  
# The file file_input_raw was rewound 35 times
      rgb_lagged_sum|   8|   1000000|     100|0.92707627|  PASSED  
# The file file_input_raw was rewound 39 times
      rgb_lagged_sum|   9|   1000000|     100|0.10529620|  PASSED  
# The file file_input_raw was rewound 43 times
      rgb_lagged_sum|  10|   1000000|     100|0.62178846|  PASSED  
# The file file_input_raw was rewound 48 times
      rgb_lagged_sum|  11|   1000000|     100|0.31152928|  PASSED  
# The file file_input_raw was rewound 53 times
      rgb_lagged_sum|  12|   1000000|     100|0.58704950|  PASSED  
# The file file_input_raw was rewound 58 times
      rgb_lagged_sum|  13|   1000000|     100|0.93281704|  PASSED  
# The file file_input_raw was rewound 63 times
      rgb_lagged_sum|  14|   1000000|     100|0.00008205|   WEAK   
# The file file_input_raw was rewound 69 times
      rgb_lagged_sum|  15|   1000000|     100|0.58153871|  PASSED  
# The file file_input_raw was rewound 76 times
      rgb_lagged_sum|  16|   1000000|     100|0.23027895|  PASSED  
# The file file_input_raw was rewound 82 times
      rgb_lagged_sum|  17|   1000000|     100|0.00874786|  PASSED  
# The file file_input_raw was rewound 89 times
      rgb_lagged_sum|  18|   1000000|     100|0.63637882|  PASSED  
# The file file_input_raw was rewound 97 times
      rgb_lagged_sum|  19|   1000000|     100|0.00681733|  PASSED  
# The file file_input_raw was rewound 105 times
      rgb_lagged_sum|  20|   1000000|     100|0.60709526|  PASSED  
# The file file_input_raw was rewound 113 times
      rgb_lagged_sum|  21|   1000000|     100|0.14437881|  PASSED  
# The file file_input_raw was rewound 121 times
      rgb_lagged_sum|  22|   1000000|     100|0.83121224|  PASSED  
# The file file_input_raw was rewound 130 times
      rgb_lagged_sum|  23|   1000000|     100|0.02960773|  PASSED  
# The file file_input_raw was rewound 140 times
      rgb_lagged_sum|  24|   1000000|     100|0.06003605|  PASSED  
# The file file_input_raw was rewound 149 times
      rgb_lagged_sum|  25|   1000000|     100|0.71643466|  PASSED  
# The file file_input_raw was rewound 159 times
      rgb_lagged_sum|  26|   1000000|     100|0.67401231|  PASSED  
# The file file_input_raw was rewound 170 times
      rgb_lagged_sum|  27|   1000000|     100|0.62444186|  PASSED  
# The file file_input_raw was rewound 181 times
      rgb_lagged_sum|  28|   1000000|     100|0.87425746|  PASSED  
# The file file_input_raw was rewound 192 times
      rgb_lagged_sum|  29|   1000000|     100|0.78001993|  PASSED  
# The file file_input_raw was rewound 203 times
      rgb_lagged_sum|  30|   1000000|     100|0.80257554|  PASSED  
# The file file_input_raw was rewound 215 times
      rgb_lagged_sum|  31|   1000000|     100|0.43101504|  PASSED  
# The file file_input_raw was rewound 228 times
      rgb_lagged_sum|  32|   1000000|     100|0.84288690|  PASSED  
# The file file_input_raw was rewound 228 times
     rgb_kstest_test|   0|     10000|    1000|0.82000438|  PASSED  
# The file file_input_raw was rewound 228 times
     dab_bytedistrib|   0|  51200000|       1|0.24969556|  PASSED  
# The file file_input_raw was rewound 228 times
             dab_dct| 256|     50000|       1|0.39135931|  PASSED  
Preparing to run test 207.  ntuple = 0
# The file file_input_raw was rewound 229 times
        dab_filltree|  32|  15000000|       1|0.69230032|  PASSED  
        dab_filltree|  32|  15000000|       1|0.12173466|  PASSED  
Preparing to run test 208.  ntuple = 0
# The file file_input_raw was rewound 229 times
       dab_filltree2|   0|   5000000|       1|0.93515518|  PASSED  
       dab_filltree2|   1|   5000000|       1|0.07752618|  PASSED  
Preparing to run test 209.  ntuple = 0
# The file file_input_raw was rewound 229 times
        dab_monobit2|  12|  65000000|       1|0.84920311|  PASSED  
```

Byte Histogram looks normal:

![LPC](/LPC/byte_histogram.png)

bitcounter results:
```
Total bits:  8589936000
Ones:  4294909795
Percentage:  0.49999322404730373
```

## Quirks

The LPC requires that you discard numbers in a weird way. There's no way a developer could possibly be expected to read page 1106 of this 1152 page manual to find this out:

```
The quality of randomness (entropy) of the numbers generated by the Random Number Generator relies on the initial states of internal logic. If a 128 bit or 256 bit random number is required, it is not recommended to concatenate several words of 32 bits to form the number. For example, if two 128 bit words are concatenated, the hardware RNG will not
provide 2 times 128 bits of entropy.

Table 1073 shows the entropy distribution that is supported.

Table 1073. Entropy distribution

Number of 128 bit words Entropy
1 128
2 256

To constitute one 128 bit number, a 32 bit random number is read, then the next 32 numbers are read but not used. The next 32 bit number is read and used and so on. Thus 32 32-bit random numbers are skipped between two 32-bit numbers that are used.
```

Failing to do this lead to extremely vulnerable results.
