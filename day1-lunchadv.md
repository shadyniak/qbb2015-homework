1. For the first 100 features, report the chromosome, strand, start, end, and length. 

$ awk '{print $1 "\t" $7 "\t" $4 "\t" $5 "\t" ($5-$4+1)}' BDGP6.Ensembl.81.gtf | head -100 

3R	-	722370	722621	252
3R	-	722370	722621	252
3R	-	722370	722621	252
3R	+	835381	2503907	1668527
3R	+	835381	2503907	1668527
3R	+	835381	835491	111
3R	+	835381	835491	111
3R	+	835381	835383	3
3R	+	869486	869548	63
3R	+	869486	869548	63
3R	+	895786	895893	108
3R	+	895786	895893	108
3R	+	947426	947570	145
3R	+	947426	947570	145
3R	+	1025040	1025614	575
3R	+	1025040	1025614	575
3R	+	1138730	1138972	243
3R	+	1138730	1138972	243
3R	+	1191610	1191975	366
3R	+	1191610	1191975	366
3R	+	1342196	1342317	122
3R	+	1342196	1342317	122
3R	+	1454572	1455091	520
3R	+	1454572	1455091	520
3R	+	1467146	1467258	113
3R	+	1467146	1467258	113
3R	+	1588295	1588538	244
3R	+	1588295	1588538	244
3R	+	1845561	1846163	603
3R	+	1845561	1846163	603
3R	+	1861194	1861417	224
3R	+	1861194	1861417	224
3R	+	1938067	1938205	139
3R	+	1938067	1938205	139
3R	+	1961120	1961515	396
3R	+	1961120	1961515	396
3R	+	2136430	2137402	973
3R	+	2136430	2137402	973
3R	+	2307285	2307583	299
3R	+	2307285	2307583	299
3R	+	2413805	2414131	327
3R	+	2413805	2414131	327
3R	+	2461182	2461592	411
3R	+	2461182	2461592	411
3R	+	2503677	2503907	231
3R	+	2503677	2503904	228
3R	+	2503905	2503907	3
3R	+	1031171	1031354	184
3R	+	1031171	1031354	184
3R	+	1031171	1031354	184
3R	-	2156916	2157206	291
3R	-	2156916	2157206	291
3R	-	2156916	2157206	291
3R	-	2554124	3263573	709450
3R	-	2554124	3263573	709450
3R	-	3263513	3263573	61
3R	-	3263513	3263573	61
3R	-	3263571	3263573	3
3R	-	3263195	3263456	262
3R	-	3263195	3263456	262
3R	-	3262923	3263146	224
3R	-	3262923	3263146	224
3R	-	3262750	3262870	121
3R	-	3262750	3262870	121
3R	-	3262573	3262692	120
3R	-	3262573	3262692	120
3R	-	3262114	3262480	367
3R	-	3262114	3262480	367
3R	-	3170422	3170666	245
3R	-	3170422	3170666	245
3R	-	3168995	3169540	546
3R	-	3168995	3169540	546
3R	-	3061773	3062322	550
3R	-	3061773	3062322	550
3R	-	3061235	3061718	484
3R	-	3061235	3061718	484
3R	-	3060393	3061173	781
3R	-	3060393	3061173	781
3R	-	3031406	3031536	131
3R	-	3031406	3031536	131
3R	-	2940913	2941229	317
3R	-	2940913	2941229	317
3R	-	2743787	2744070	284
3R	-	2743787	2744070	284
3R	-	2743154	2743729	576
3R	-	2743154	2743729	576
3R	-	2690093	2690237	145
3R	-	2690093	2690237	145
3R	-	2557978	2558354	377
3R	-	2557978	2558354	377
3R	-	2554470	2555023	554
3R	-	2554470	2555023	554
3R	-	2554124	2554398	275
3R	-	2554127	2554398	272
3R	-	2554124	2554126	3

2. Calculate the average length of all feaures 