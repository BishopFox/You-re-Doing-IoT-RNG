## ESP32

### Results

Overall, good. As long as you spinloop all calls to the RNG.

The few "weak" results from Dieharder were not consistent across multiple runs, so they appear to be an expected statistical outlier.

```
dieharder -g 201 -a -f Huzzah32randData0.bin
```

```
#=============================================================================#
#            dieharder version 3.31.1 Copyright 2003 Robert G. Brown          #
#=============================================================================#
   rng_name    |           filename             |rands/second|
 file_input_raw|           Huzzah32randData0.bin|  4.44e+07  |
#=============================================================================#
        test_name   |ntup| tsamples |psamples|  p-value |Assessment
#=============================================================================#
   diehard_birthdays|   0|       100|     100|0.79216278|  PASSED  
      diehard_operm5|   0|   1000000|     100|0.41143024|  PASSED  
  diehard_rank_32x32|   0|     40000|     100|0.24100867|  PASSED  
# The file file_input_raw was rewound 1 times
    diehard_rank_6x8|   0|    100000|     100|0.18088157|  PASSED  
# The file file_input_raw was rewound 1 times
   diehard_bitstream|   0|   2097152|     100|0.39601784|  PASSED  
# The file file_input_raw was rewound 2 times
        diehard_opso|   0|   2097152|     100|0.78063526|  PASSED  
# The file file_input_raw was rewound 2 times
        diehard_oqso|   0|   2097152|     100|0.15492207|  PASSED  
# The file file_input_raw was rewound 2 times
         diehard_dna|   0|   2097152|     100|0.80611832|  PASSED  
# The file file_input_raw was rewound 2 times
diehard_count_1s_str|   0|    256000|     100|0.32704865|  PASSED  
# The file file_input_raw was rewound 3 times
diehard_count_1s_byt|   0|    256000|     100|0.53799968|  PASSED  
# The file file_input_raw was rewound 3 times
 diehard_parking_lot|   0|     12000|     100|0.60849546|  PASSED  
# The file file_input_raw was rewound 3 times
    diehard_2dsphere|   2|      8000|     100|0.29073320|  PASSED  
# The file file_input_raw was rewound 3 times
    diehard_3dsphere|   3|      4000|     100|0.93462279|  PASSED  
# The file file_input_raw was rewound 4 times
     diehard_squeeze|   0|    100000|     100|0.38531482|  PASSED  
# The file file_input_raw was rewound 4 times
        diehard_sums|   0|       100|     100|0.00096205|   WEAK   
# The file file_input_raw was rewound 4 times
        diehard_runs|   0|    100000|     100|0.22237377|  PASSED  
        diehard_runs|   0|    100000|     100|0.48268843|  PASSED  
# The file file_input_raw was rewound 4 times
       diehard_craps|   0|    200000|     100|0.34701812|  PASSED  
       diehard_craps|   0|    200000|     100|0.97986549|  PASSED  
# The file file_input_raw was rewound 12 times
 marsaglia_tsang_gcd|   0|  10000000|     100|0.87700514|  PASSED  
 marsaglia_tsang_gcd|   0|  10000000|     100|0.20006840|  PASSED  
# The file file_input_raw was rewound 12 times
         sts_monobit|   1|    100000|     100|0.05048459|  PASSED  
# The file file_input_raw was rewound 12 times
            sts_runs|   2|    100000|     100|0.80516365|  PASSED  
# The file file_input_raw was rewound 12 times
          sts_serial|   1|    100000|     100|0.58883790|  PASSED  
          sts_serial|   2|    100000|     100|0.90073904|  PASSED  
          sts_serial|   3|    100000|     100|0.23658362|  PASSED  
          sts_serial|   3|    100000|     100|0.01774142|  PASSED  
          sts_serial|   4|    100000|     100|0.23503004|  PASSED  
          sts_serial|   4|    100000|     100|0.82663770|  PASSED  
          sts_serial|   5|    100000|     100|0.51528331|  PASSED  
          sts_serial|   5|    100000|     100|0.30747804|  PASSED  
          sts_serial|   6|    100000|     100|0.97847365|  PASSED  
          sts_serial|   6|    100000|     100|0.89146909|  PASSED  
          sts_serial|   7|    100000|     100|0.46247419|  PASSED  
          sts_serial|   7|    100000|     100|0.43675605|  PASSED  
          sts_serial|   8|    100000|     100|0.64328946|  PASSED  
          sts_serial|   8|    100000|     100|0.55349759|  PASSED  
          sts_serial|   9|    100000|     100|0.89167097|  PASSED  
          sts_serial|   9|    100000|     100|0.11214838|  PASSED  
          sts_serial|  10|    100000|     100|0.51393576|  PASSED  
          sts_serial|  10|    100000|     100|0.45205597|  PASSED  
          sts_serial|  11|    100000|     100|0.31023365|  PASSED  
          sts_serial|  11|    100000|     100|0.98027847|  PASSED  
          sts_serial|  12|    100000|     100|0.52675698|  PASSED  
          sts_serial|  12|    100000|     100|0.29748334|  PASSED  
          sts_serial|  13|    100000|     100|0.56846347|  PASSED  
          sts_serial|  13|    100000|     100|0.03161541|  PASSED  
          sts_serial|  14|    100000|     100|0.23336791|  PASSED  
          sts_serial|  14|    100000|     100|0.32428561|  PASSED  
          sts_serial|  15|    100000|     100|0.37864437|  PASSED  
          sts_serial|  15|    100000|     100|0.02723856|  PASSED  
          sts_serial|  16|    100000|     100|0.33371321|  PASSED  
          sts_serial|  16|    100000|     100|0.89786222|  PASSED  
# The file file_input_raw was rewound 12 times
         rgb_bitdist|   1|    100000|     100|0.37950958|  PASSED  
# The file file_input_raw was rewound 12 times
         rgb_bitdist|   2|    100000|     100|0.51711489|  PASSED  
# The file file_input_raw was rewound 12 times
         rgb_bitdist|   3|    100000|     100|0.76677348|  PASSED  
# The file file_input_raw was rewound 12 times
         rgb_bitdist|   4|    100000|     100|0.65902294|  PASSED  
# The file file_input_raw was rewound 13 times
         rgb_bitdist|   5|    100000|     100|0.92577869|  PASSED  
# The file file_input_raw was rewound 13 times
         rgb_bitdist|   6|    100000|     100|0.11377774|  PASSED  
# The file file_input_raw was rewound 14 times
         rgb_bitdist|   7|    100000|     100|0.29619522|  PASSED  
# The file file_input_raw was rewound 14 times
         rgb_bitdist|   8|    100000|     100|0.50067197|  PASSED  
# The file file_input_raw was rewound 15 times
         rgb_bitdist|   9|    100000|     100|0.79163106|  PASSED  
# The file file_input_raw was rewound 16 times
         rgb_bitdist|  10|    100000|     100|0.99041916|  PASSED  
# The file file_input_raw was rewound 17 times
         rgb_bitdist|  11|    100000|     100|0.76790749|  PASSED  
# The file file_input_raw was rewound 18 times
         rgb_bitdist|  12|    100000|     100|0.42683605|  PASSED  
# The file file_input_raw was rewound 18 times
rgb_minimum_distance|   2|     10000|    1000|0.05540869|  PASSED  
# The file file_input_raw was rewound 18 times
rgb_minimum_distance|   3|     10000|    1000|0.66124576|  PASSED  
# The file file_input_raw was rewound 18 times
rgb_minimum_distance|   4|     10000|    1000|0.52935066|  PASSED  
# The file file_input_raw was rewound 18 times
rgb_minimum_distance|   5|     10000|    1000|0.41805489|  PASSED  
# The file file_input_raw was rewound 18 times
    rgb_permutations|   2|    100000|     100|0.19464844|  PASSED  
# The file file_input_raw was rewound 18 times
    rgb_permutations|   3|    100000|     100|0.41691451|  PASSED  
# The file file_input_raw was rewound 18 times
    rgb_permutations|   4|    100000|     100|0.72388492|  PASSED  
# The file file_input_raw was rewound 19 times
    rgb_permutations|   5|    100000|     100|0.13320061|  PASSED  
# The file file_input_raw was rewound 19 times
      rgb_lagged_sum|   0|   1000000|     100|0.54817431|  PASSED  
# The file file_input_raw was rewound 20 times
      rgb_lagged_sum|   1|   1000000|     100|0.48315820|  PASSED  
# The file file_input_raw was rewound 21 times
      rgb_lagged_sum|   2|   1000000|     100|0.37562551|  PASSED  
# The file file_input_raw was rewound 22 times
      rgb_lagged_sum|   3|   1000000|     100|0.44117997|  PASSED  
# The file file_input_raw was rewound 24 times
      rgb_lagged_sum|   4|   1000000|     100|0.86110270|  PASSED  
# The file file_input_raw was rewound 26 times
      rgb_lagged_sum|   5|   1000000|     100|0.95357345|  PASSED  
# The file file_input_raw was rewound 29 times
      rgb_lagged_sum|   6|   1000000|     100|0.38233996|  PASSED  
# The file file_input_raw was rewound 32 times
      rgb_lagged_sum|   7|   1000000|     100|0.88166199|  PASSED  
# The file file_input_raw was rewound 35 times
      rgb_lagged_sum|   8|   1000000|     100|0.14341771|  PASSED  
# The file file_input_raw was rewound 39 times
      rgb_lagged_sum|   9|   1000000|     100|0.50778678|  PASSED  
# The file file_input_raw was rewound 43 times
      rgb_lagged_sum|  10|   1000000|     100|0.43484460|  PASSED  
# The file file_input_raw was rewound 48 times
      rgb_lagged_sum|  11|   1000000|     100|0.89564684|  PASSED  
# The file file_input_raw was rewound 52 times
      rgb_lagged_sum|  12|   1000000|     100|0.81520461|  PASSED  
# The file file_input_raw was rewound 58 times
      rgb_lagged_sum|  13|   1000000|     100|0.43236916|  PASSED  
# The file file_input_raw was rewound 63 times
      rgb_lagged_sum|  14|   1000000|     100|0.67365140|  PASSED  
# The file file_input_raw was rewound 69 times
      rgb_lagged_sum|  15|   1000000|     100|0.08369604|  PASSED  
# The file file_input_raw was rewound 76 times
      rgb_lagged_sum|  16|   1000000|     100|0.99680421|   WEAK   
# The file file_input_raw was rewound 82 times
      rgb_lagged_sum|  17|   1000000|     100|0.10166488|  PASSED  
# The file file_input_raw was rewound 89 times
      rgb_lagged_sum|  18|   1000000|     100|0.94566597|  PASSED  
# The file file_input_raw was rewound 97 times
      rgb_lagged_sum|  19|   1000000|     100|0.63249488|  PASSED  
# The file file_input_raw was rewound 105 times
      rgb_lagged_sum|  20|   1000000|     100|0.78499384|  PASSED  
# The file file_input_raw was rewound 113 times
      rgb_lagged_sum|  21|   1000000|     100|0.96310221|  PASSED  
# The file file_input_raw was rewound 121 times
      rgb_lagged_sum|  22|   1000000|     100|0.39182516|  PASSED  
# The file file_input_raw was rewound 130 times
      rgb_lagged_sum|  23|   1000000|     100|0.10467114|  PASSED  
# The file file_input_raw was rewound 140 times
      rgb_lagged_sum|  24|   1000000|     100|0.19233586|  PASSED  
# The file file_input_raw was rewound 149 times
      rgb_lagged_sum|  25|   1000000|     100|0.02423793|  PASSED  
# The file file_input_raw was rewound 159 times
      rgb_lagged_sum|  26|   1000000|     100|0.92144784|  PASSED  
# The file file_input_raw was rewound 170 times
      rgb_lagged_sum|  27|   1000000|     100|0.84892921|  PASSED  
# The file file_input_raw was rewound 181 times
      rgb_lagged_sum|  28|   1000000|     100|0.73719500|  PASSED  
# The file file_input_raw was rewound 192 times
      rgb_lagged_sum|  29|   1000000|     100|0.62279279|  PASSED  
# The file file_input_raw was rewound 203 times
      rgb_lagged_sum|  30|   1000000|     100|0.07855016|  PASSED  
# The file file_input_raw was rewound 215 times
      rgb_lagged_sum|  31|   1000000|     100|0.00068363|   WEAK   
# The file file_input_raw was rewound 227 times
      rgb_lagged_sum|  32|   1000000|     100|0.42053740|  PASSED  
# The file file_input_raw was rewound 227 times
     rgb_kstest_test|   0|     10000|    1000|0.25243184|  PASSED  
# The file file_input_raw was rewound 228 times
     dab_bytedistrib|   0|  51200000|       1|0.66804414|  PASSED  
# The file file_input_raw was rewound 228 times
             dab_dct| 256|     50000|       1|0.87779154|  PASSED  
Preparing to run test 207.  ntuple = 0
# The file file_input_raw was rewound 229 times
        dab_filltree|  32|  15000000|       1|0.81957185|  PASSED  
        dab_filltree|  32|  15000000|       1|0.00240829|   WEAK   
Preparing to run test 208.  ntuple = 0
# The file file_input_raw was rewound 229 times
       dab_filltree2|   0|   5000000|       1|0.09367962|  PASSED  
       dab_filltree2|   1|   5000000|       1|0.06607378|  PASSED  
Preparing to run test 209.  ntuple = 0
# The file file_input_raw was rewound 229 times
        dab_monobit2|  12|  65000000|       1|0.10505251|  PASSED  
```

Byte Histogram looks normal:

![ESP](/ESP/byte_histogram_esp.png)

bitcounter:

```
Total bits:  8595614560
Ones:  4297806358
Percentage:  0.49999989273600004
```
