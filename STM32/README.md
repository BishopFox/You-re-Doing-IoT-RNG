# Getting Started

Following instructions here to get started: https://github.com/davisjp1822/stm32_nucleo_linux

# Results

One curious failure from the `rgb_minimum_distance` test. Likely the result of some sort of subtle pattern, but we haven't picked up on what it is.

```
$ ./dieharder_norewind.sh STM32L432randData.4gb.32768trans.fullblocking.bin
#=============================================================================#
#            dieharder version 3.31.1 Copyright 2003 Robert G. Brown          #
#=============================================================================#
   rng_name    |           filename             |rands/second|
 file_input_raw|STM32L432randData.4gb.32768trans.fullblocking.bin|  2.38e+07  |
#=============================================================================#
        test_name   |ntup| tsamples |psamples|  p-value |Assessment
#=============================================================================#
   diehard_birthdays|   0|       100|     100|0.42576907|  PASSED  

   rng_name    |           filename             |rands/second|
 file_input_raw|STM32L432randData.4gb.32768trans.fullblocking.bin|  2.02e+07  |
#=============================================================================#
        test_name   |ntup| tsamples |psamples|  p-value |Assessment
#=============================================================================#
  diehard_rank_32x32|   0|     40000|     100|0.53335276|  PASSED  

   rng_name    |           filename             |rands/second|
 file_input_raw|STM32L432randData.4gb.32768trans.fullblocking.bin|  2.17e+07  |
#=============================================================================#
        test_name   |ntup| tsamples |psamples|  p-value |Assessment
#=============================================================================#
    diehard_rank_6x8|   0|    100000|     100|0.20635346|  PASSED  

   rng_name    |           filename             |rands/second|
 file_input_raw|STM32L432randData.4gb.32768trans.fullblocking.bin|  1.83e+07  |
#=============================================================================#
        test_name   |ntup| tsamples |psamples|  p-value |Assessment
#=============================================================================#
   diehard_bitstream|   0|   2097152|     100|0.14283731|  PASSED  

   rng_name    |           filename             |rands/second|
 file_input_raw|STM32L432randData.4gb.32768trans.fullblocking.bin|  1.80e+07  |
#=============================================================================#
        test_name   |ntup| tsamples |psamples|  p-value |Assessment
#=============================================================================#
        diehard_opso|   0|   2097152|     100|0.10865122|  PASSED  

   rng_name    |           filename             |rands/second|
 file_input_raw|STM32L432randData.4gb.32768trans.fullblocking.bin|  2.04e+07  |
#=============================================================================#
        test_name   |ntup| tsamples |psamples|  p-value |Assessment
#=============================================================================#
        diehard_oqso|   0|   2097152|     100|0.53252423|  PASSED  

   rng_name    |           filename             |rands/second|
 file_input_raw|STM32L432randData.4gb.32768trans.fullblocking.bin|  1.92e+07  |
#=============================================================================#
        test_name   |ntup| tsamples |psamples|  p-value |Assessment
#=============================================================================#
         diehard_dna|   0|   2097152|     100|0.10061253|  PASSED  

   rng_name    |           filename             |rands/second|
 file_input_raw|STM32L432randData.4gb.32768trans.fullblocking.bin|  1.92e+07  |
#=============================================================================#
        test_name   |ntup| tsamples |psamples|  p-value |Assessment
#=============================================================================#
diehard_count_1s_str|   0|    256000|     100|0.43964937|  PASSED  

   rng_name    |           filename             |rands/second|
 file_input_raw|STM32L432randData.4gb.32768trans.fullblocking.bin|  2.16e+07  |
#=============================================================================#
        test_name   |ntup| tsamples |psamples|  p-value |Assessment
#=============================================================================#
diehard_count_1s_byt|   0|    256000|     100|0.44000615|  PASSED  

   rng_name    |           filename             |rands/second|
 file_input_raw|STM32L432randData.4gb.32768trans.fullblocking.bin|  1.95e+07  |
#=============================================================================#
        test_name   |ntup| tsamples |psamples|  p-value |Assessment
#=============================================================================#
 diehard_parking_lot|   0|     12000|     100|0.95063855|  PASSED  

   rng_name    |           filename             |rands/second|
 file_input_raw|STM32L432randData.4gb.32768trans.fullblocking.bin|  1.47e+07  |
#=============================================================================#
        test_name   |ntup| tsamples |psamples|  p-value |Assessment
#=============================================================================#
    diehard_2dsphere|   2|      8000|     100|0.68597513|  PASSED  

   rng_name    |           filename             |rands/second|
 file_input_raw|STM32L432randData.4gb.32768trans.fullblocking.bin|  1.26e+07  |
#=============================================================================#
        test_name   |ntup| tsamples |psamples|  p-value |Assessment
#=============================================================================#
    diehard_3dsphere|   3|      4000|     100|0.44926796|  PASSED  

   rng_name    |           filename             |rands/second|
 file_input_raw|STM32L432randData.4gb.32768trans.fullblocking.bin|  1.74e+07  |
#=============================================================================#
        test_name   |ntup| tsamples |psamples|  p-value |Assessment
#=============================================================================#
     diehard_squeeze|   0|    100000|     100|0.59982077|  PASSED  

   rng_name    |           filename             |rands/second|
 file_input_raw|STM32L432randData.4gb.32768trans.fullblocking.bin|  1.84e+07  |
#=============================================================================#
        test_name   |ntup| tsamples |psamples|  p-value |Assessment
#=============================================================================#
        diehard_runs|   0|    100000|     100|0.63520648|  PASSED  
        diehard_runs|   0|    100000|     100|0.24949661|  PASSED  

   rng_name    |           filename             |rands/second|
 file_input_raw|STM32L432randData.4gb.32768trans.fullblocking.bin|  1.81e+07  |
#=============================================================================#
        test_name   |ntup| tsamples |psamples|  p-value |Assessment
#=============================================================================#
       diehard_craps|   0|    200000|     100|0.75567934|  PASSED  
       diehard_craps|   0|    200000|     100|0.48021350|  PASSED  

   rng_name    |           filename             |rands/second|
 file_input_raw|STM32L432randData.4gb.32768trans.fullblocking.bin|  1.97e+07  |
#=============================================================================#
        test_name   |ntup| tsamples |psamples|  p-value |Assessment
#=============================================================================#
# The file file_input_raw was rewound 1 times
 marsaglia_tsang_gcd|   0|  10000000|     100|0.88204840|  PASSED  
 marsaglia_tsang_gcd|   0|  10000000|     100|0.63548621|  PASSED  

   rng_name    |           filename             |rands/second|
 file_input_raw|STM32L432randData.4gb.32768trans.fullblocking.bin|  1.91e+07  |
#=============================================================================#
        test_name   |ntup| tsamples |psamples|  p-value |Assessment
#=============================================================================#
         sts_monobit|   1|    100000|     100|0.71799846|  PASSED  

   rng_name    |           filename             |rands/second|
 file_input_raw|STM32L432randData.4gb.32768trans.fullblocking.bin|  2.13e+07  |
#=============================================================================#
        test_name   |ntup| tsamples |psamples|  p-value |Assessment
#=============================================================================#
            sts_runs|   2|    100000|     100|0.98692556|  PASSED  

   rng_name    |           filename             |rands/second|
 file_input_raw|STM32L432randData.4gb.32768trans.fullblocking.bin|  1.88e+07  |
#=============================================================================#
        test_name   |ntup| tsamples |psamples|  p-value |Assessment
#=============================================================================#
          sts_serial|   1|    100000|     100|0.71799846|  PASSED  
          sts_serial|   2|    100000|     100|0.82559537|  PASSED  
          sts_serial|   3|    100000|     100|0.46719497|  PASSED  
          sts_serial|   3|    100000|     100|0.57047084|  PASSED  
          sts_serial|   4|    100000|     100|0.93763316|  PASSED  
          sts_serial|   4|    100000|     100|0.91718920|  PASSED  
          sts_serial|   5|    100000|     100|0.94994566|  PASSED  
          sts_serial|   5|    100000|     100|0.91048845|  PASSED  
          sts_serial|   6|    100000|     100|0.67174655|  PASSED  
          sts_serial|   6|    100000|     100|0.92174063|  PASSED  
          sts_serial|   7|    100000|     100|0.95050896|  PASSED  
          sts_serial|   7|    100000|     100|0.98838068|  PASSED  
          sts_serial|   8|    100000|     100|0.96482166|  PASSED  
          sts_serial|   8|    100000|     100|0.87156131|  PASSED  
          sts_serial|   9|    100000|     100|0.32109420|  PASSED  
          sts_serial|   9|    100000|     100|0.17188841|  PASSED  
          sts_serial|  10|    100000|     100|0.76149020|  PASSED  
          sts_serial|  10|    100000|     100|0.33538118|  PASSED  
          sts_serial|  11|    100000|     100|0.77339014|  PASSED  
          sts_serial|  11|    100000|     100|0.97329436|  PASSED  
          sts_serial|  12|    100000|     100|0.99316166|  PASSED  
          sts_serial|  12|    100000|     100|0.84424102|  PASSED  
          sts_serial|  13|    100000|     100|0.66083679|  PASSED  
          sts_serial|  13|    100000|     100|0.37289812|  PASSED  
          sts_serial|  14|    100000|     100|0.25605683|  PASSED  
          sts_serial|  14|    100000|     100|0.18849999|  PASSED  
          sts_serial|  15|    100000|     100|0.73721734|  PASSED  
          sts_serial|  15|    100000|     100|0.33802784|  PASSED  
          sts_serial|  16|    100000|     100|0.68283703|  PASSED  
          sts_serial|  16|    100000|     100|0.81569165|  PASSED  

   rng_name    |           filename             |rands/second|
 file_input_raw|STM32L432randData.4gb.32768trans.fullblocking.bin|  1.72e+07  |
#=============================================================================#
        test_name   |ntup| tsamples |psamples|  p-value |Assessment
#=============================================================================#
rgb_minimum_distance|   0|     10000|    1000|0.00000000|  FAILED  

   rng_name    |           filename             |rands/second|
 file_input_raw|STM32L432randData.4gb.32768trans.fullblocking.bin|  1.42e+07  |
#=============================================================================#
        test_name   |ntup| tsamples |psamples|  p-value |Assessment
#=============================================================================#
    rgb_permutations|   5|    100000|     100|0.46848082|  PASSED  

   rng_name    |           filename             |rands/second|
 file_input_raw|STM32L432randData.4gb.32768trans.fullblocking.bin|  1.88e+07  |
#=============================================================================#
        test_name   |ntup| tsamples |psamples|  p-value |Assessment
#=============================================================================#
      rgb_lagged_sum|   0|   1000000|     100|0.38071579|  PASSED  

   rng_name    |           filename             |rands/second|
 file_input_raw|STM32L432randData.4gb.32768trans.fullblocking.bin|  1.82e+07  |
#=============================================================================#
        test_name   |ntup| tsamples |psamples|  p-value |Assessment
#=============================================================================#
     rgb_kstest_test|   0|     10000|    1000|0.40217339|  PASSED
```

```
$ python3 bitcounter.py --file ../../STM32L432randData.4gb.32768trans.fullblocking.bin && python3 bytecounter.py --file ../../STM32L432randData.4gb.32768trans.fullblocking.bin
100%|█████████████████████████████████████████| 4294968000/4294968000 [4:00:02<00:00, 298203.50it/s]
Total bits:  34359744000
Ones:  17180081374
Percentage:  0.5000060935843992
100%|█████████████████████████████████████████| 4294968000/4294968000 [2:19:48<00:00, 512017.90it/s]
Byte   0	16778094	0.3906%
Byte   1	16774565	0.3906%
Byte   2	16771061	0.3905%
Byte   3	16775214	0.3906%
Byte   4	16769145	0.3904%
Byte   5	16773097	0.3905%
Byte   6	16779734	0.3907%
Byte   7	16779017	0.3907%
Byte   8	16771986	0.3905%
Byte   9	16775147	0.3906%
Byte   10	16769240	0.3904%
Byte   11	16780749	0.3907%
Byte   12	16780143	0.3907%
Byte   13	16778296	0.3907%
Byte   14	16772831	0.3905%
Byte   15	16782495	0.3907%
Byte   16	16778323	0.3907%
Byte   17	16778572	0.3907%
Byte   18	16780934	0.3907%
Byte   19	16773362	0.3905%
Byte   20	16775393	0.3906%
Byte   21	16780141	0.3907%
Byte   22	16775078	0.3906%
Byte   23	16773754	0.3905%
Byte   24	16775147	0.3906%
Byte   25	16768748	0.3904%
Byte   26	16781290	0.3907%
Byte   27	16783424	0.3908%
Byte   28	16781594	0.3907%
Byte   29	16777374	0.3906%
Byte   30	16775053	0.3906%
Byte   31	16780035	0.3907%
Byte   32	16781338	0.3907%
Byte   33	16775004	0.3906%
Byte   34	16779432	0.3907%
Byte   35	16774973	0.3906%
Byte   36	16773241	0.3905%
Byte   37	16771135	0.3905%
Byte   38	16777458	0.3906%
Byte   39	16777747	0.3906%
Byte   40	16782140	0.3907%
Byte   41	16772068	0.3905%
Byte   42	16775441	0.3906%
Byte   43	16774639	0.3906%
Byte   44	16778675	0.3907%
Byte   45	16787604	0.3909%
Byte   46	16779818	0.3907%
Byte   47	16777062	0.3906%
Byte   48	16784284	0.3908%
Byte   49	16771808	0.3905%
Byte   50	16771870	0.3905%
Byte   51	16775518	0.3906%
Byte   52	16778576	0.3907%
Byte   53	16780993	0.3907%
Byte   54	16777353	0.3906%
Byte   55	16775957	0.3906%
Byte   56	16794177	0.391%
Byte   57	16784088	0.3908%
Byte   58	16774974	0.3906%
Byte   59	16779283	0.3907%
Byte   60	16782491	0.3907%
Byte   61	16783347	0.3908%
Byte   62	16783786	0.3908%
Byte   63	16776835	0.3906%
Byte   64	16781915	0.3907%
Byte   65	16778969	0.3907%
Byte   66	16776931	0.3906%
Byte   67	16772335	0.3905%
Byte   68	16774999	0.3906%
Byte   69	16777369	0.3906%
Byte   70	16776739	0.3906%
Byte   71	16784345	0.3908%
Byte   72	16772425	0.3905%
Byte   73	16774014	0.3906%
Byte   74	16774369	0.3906%
Byte   75	16777229	0.3906%
Byte   76	16772218	0.3905%
Byte   77	16768315	0.3904%
Byte   78	16775248	0.3906%
Byte   79	16780806	0.3907%
Byte   80	16782485	0.3907%
Byte   81	16776908	0.3906%
Byte   82	16784198	0.3908%
Byte   83	16785465	0.3908%
Byte   84	16782625	0.3908%
Byte   85	16785119	0.3908%
Byte   86	16778992	0.3907%
Byte   87	16778932	0.3907%
Byte   88	16777006	0.3906%
Byte   89	16775164	0.3906%
Byte   90	16774901	0.3906%
Byte   91	16769756	0.3905%
Byte   92	16778682	0.3907%
Byte   93	16775087	0.3906%
Byte   94	16778778	0.3907%
Byte   95	16777278	0.3906%
Byte   96	16781382	0.3907%
Byte   97	16777587	0.3906%
Byte   98	16771254	0.3905%
Byte   99	16774703	0.3906%
Byte   100	16773402	0.3905%
Byte   101	16776412	0.3906%
Byte   102	16775987	0.3906%
Byte   103	16775326	0.3906%
Byte   104	16769959	0.3905%
Byte   105	16781150	0.3907%
Byte   106	16777892	0.3906%
Byte   107	16772427	0.3905%
Byte   108	16775488	0.3906%
Byte   109	16783560	0.3908%
Byte   110	16780277	0.3907%
Byte   111	16775146	0.3906%
Byte   112	16783936	0.3908%
Byte   113	16772763	0.3905%
Byte   114	16777447	0.3906%
Byte   115	16783776	0.3908%
Byte   116	16773720	0.3905%
Byte   117	16777910	0.3906%
Byte   118	16775170	0.3906%
Byte   119	16776254	0.3906%
Byte   120	16778866	0.3907%
Byte   121	16780006	0.3907%
Byte   122	16777134	0.3906%
Byte   123	16777819	0.3906%
Byte   124	16773913	0.3905%
Byte   125	16778255	0.3906%
Byte   126	16780900	0.3907%
Byte   127	16775445	0.3906%
Byte   128	16776493	0.3906%
Byte   129	16777224	0.3906%
Byte   130	16765272	0.3903%
Byte   131	16773811	0.3905%
Byte   132	16772419	0.3905%
Byte   133	16771196	0.3905%
Byte   134	16778818	0.3907%
Byte   135	16772394	0.3905%
Byte   136	16776789	0.3906%
Byte   137	16777065	0.3906%
Byte   138	16773539	0.3905%
Byte   139	16771885	0.3905%
Byte   140	16779607	0.3907%
Byte   141	16774170	0.3906%
Byte   142	16779235	0.3907%
Byte   143	16776806	0.3906%
Byte   144	16771255	0.3905%
Byte   145	16776022	0.3906%
Byte   146	16775639	0.3906%
Byte   147	16779923	0.3907%
Byte   148	16777592	0.3906%
Byte   149	16777823	0.3906%
Byte   150	16776210	0.3906%
Byte   151	16771638	0.3905%
Byte   152	16785794	0.3908%
Byte   153	16772325	0.3905%
Byte   154	16782092	0.3907%
Byte   155	16781883	0.3907%
Byte   156	16779619	0.3907%
Byte   157	16773060	0.3905%
Byte   158	16779298	0.3907%
Byte   159	16776669	0.3906%
Byte   160	16775805	0.3906%
Byte   161	16781337	0.3907%
Byte   162	16774915	0.3906%
Byte   163	16774526	0.3906%
Byte   164	16778840	0.3907%
Byte   165	16778410	0.3907%
Byte   166	16773902	0.3905%
Byte   167	16780077	0.3907%
Byte   168	16778774	0.3907%
Byte   169	16780019	0.3907%
Byte   170	16777308	0.3906%
Byte   171	16774869	0.3906%
Byte   172	16779620	0.3907%
Byte   173	16776230	0.3906%
Byte   174	16782865	0.3908%
Byte   175	16770280	0.3905%
Byte   176	16772017	0.3905%
Byte   177	16775301	0.3906%
Byte   178	16777050	0.3906%
Byte   179	16781709	0.3907%
Byte   180	16776432	0.3906%
Byte   181	16775790	0.3906%
Byte   182	16779515	0.3907%
Byte   183	16787712	0.3909%
Byte   184	16780923	0.3907%
Byte   185	16777328	0.3906%
Byte   186	16777488	0.3906%
Byte   187	16776557	0.3906%
Byte   188	16776969	0.3906%
Byte   189	16777071	0.3906%
Byte   190	16780780	0.3907%
Byte   191	16779762	0.3907%
Byte   192	16777475	0.3906%
Byte   193	16774586	0.3906%
Byte   194	16775101	0.3906%
Byte   195	16780383	0.3907%
Byte   196	16776390	0.3906%
Byte   197	16772046	0.3905%
Byte   198	16772050	0.3905%
Byte   199	16777198	0.3906%
Byte   200	16774880	0.3906%
Byte   201	16784042	0.3908%
Byte   202	16775225	0.3906%
Byte   203	16772901	0.3905%
Byte   204	16772478	0.3905%
Byte   205	16776126	0.3906%
Byte   206	16781514	0.3907%
Byte   207	16769612	0.3904%
Byte   208	16776356	0.3906%
Byte   209	16775609	0.3906%
Byte   210	16783187	0.3908%
Byte   211	16772977	0.3905%
Byte   212	16783140	0.3908%
Byte   213	16777953	0.3906%
Byte   214	16784816	0.3908%
Byte   215	16773444	0.3905%
Byte   216	16777543	0.3906%
Byte   217	16769103	0.3904%
Byte   218	16772959	0.3905%
Byte   219	16775260	0.3906%
Byte   220	16773272	0.3905%
Byte   221	16776106	0.3906%
Byte   222	16777001	0.3906%
Byte   223	16779131	0.3907%
Byte   224	16777931	0.3906%
Byte   225	16780208	0.3907%
Byte   226	16780911	0.3907%
Byte   227	16773017	0.3905%
Byte   228	16774522	0.3906%
Byte   229	16774985	0.3906%
Byte   230	16778228	0.3906%
Byte   231	16775230	0.3906%
Byte   232	16772416	0.3905%
Byte   233	16772958	0.3905%
Byte   234	16778527	0.3907%
Byte   235	16778922	0.3907%
Byte   236	16777052	0.3906%
Byte   237	16772625	0.3905%
Byte   238	16773421	0.3905%
Byte   239	16790258	0.3909%
Byte   240	16778502	0.3907%
Byte   241	16785847	0.3908%
Byte   242	16779333	0.3907%
Byte   243	16778183	0.3906%
Byte   244	16777680	0.3906%
Byte   245	16772286	0.3905%
Byte   246	16783122	0.3908%
Byte   247	16781050	0.3907%
Byte   248	16768227	0.3904%
Byte   249	16771599	0.3905%
Byte   250	16781572	0.3907%
Byte   251	16785754	0.3908%
Byte   252	16783371	0.3908%
Byte   253	16779387	0.3907%
Byte   254	16784547	0.3908%
Byte   255	16775700	0.3906%
```
