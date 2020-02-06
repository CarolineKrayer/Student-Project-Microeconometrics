import pandas as pd
import numpy as np

class regout(object):

	def __init__(self, **kwargs):
		self.__dict__.update(kwargs)



stat_names=['coeff', 'se', 't', 'p>t', 'CI_low', 'CI_high']
var_names=['mpg', 'length', '_cons']
liml_std = regout(
summary=pd.DataFrame(np.array([
[-2883.485724395141,
5736.949960235051,
-.5026165025634982,
.6167893963364323,
-14322.63904926804,
8555.667600477756,
],
[-561.1914219781756,
1262.970349885851,
-.4443425152687845,
.6581464352023914,
-3079.482774918735,
1957.099930962384,
],
[173041.7784742117,
359459.7850372744,
.4813939853001025,
.6317169039765493,
-543700.6759080754,
889784.2328564988,
],
]),
columns=stat_names,
index=var_names),
vce=pd.DataFrame(np.array([
[32912594.84624095,
7238707.669577062,
-2061337257.276809,
],
[7238707.669577062,
1595094.104690788,
-453934824.3404015,
],
[-2061337257.276809,
-453934824.3404015,
129211337059.0436,
],
]),
columns=var_names,
index=var_names),
N=74,
r2=np.nan,
r2_a=np.nan,
mss=-6452353337.012137,
tss=np.nan,
rss=7087418733.133758,
kappa=1.003869278067604,
F=1.004921031139624,
pF=.3712199957893489,
)
liml_robust = regout(
summary=pd.DataFrame(np.array([
[-2883.485724395141,
9782.004628173405,
-.2947745205609839,
.7690263310468843,
-22388.2489769767,
16621.27752818642,
],
[-561.1914219781756,
2125.8470700299,
-.2639848509753255,
.7925563185482027,
-4800.010088318348,
3677.627244361996,
],
[173041.7784742117,
607512.0672069436,
.2848367757858323,
.7765983822485902,
-1038302.878819259,
1384386.435767682,
],
]),
columns=stat_names,
index=var_names),
vce=pd.DataFrame(np.array([
[95687614.5456059,
20788482.10331459,
-5941786208.955258,
],
[20788482.10331459,
4519225.765154713,
-1291436616.40693,
],
[-5941786208.955258,
-1291436616.40693,
369070911802.054,
],
]),
columns=var_names,
index=var_names),
N=74,
r2=np.nan,
r2_a=np.nan,
mss=-6452353337.012137,
tss=np.nan,
rss=7087418733.133758,
kappa=1.003869278067604,
F=.7898880420543719,
pF=.457843156074147,
)
liml_cluster = regout(
summary=pd.DataFrame(np.array([
[-2883.485724395141,
8819.325864658204,
-.3269508087857565,
.7456524626556127,
-20787.66908406108,
15020.6976352708,
],
[-561.1914219781756,
1931.700235224021,
-.2905168264438782,
.7731353760228708,
-4482.751384509515,
3360.368540553163,
],
[173041.7784742117,
550665.2533557557,
.3142413243248863,
.7552032861505424,
-944868.1181752922,
1290951.675123716,
],
]),
columns=stat_names,
index=var_names),
vce=pd.DataFrame(np.array([
[77780508.70702916,
17028976.85657852,
-4855525327.740576,
],
[17028976.85657852,
3731465.798764537,
-1063671099.509924,
],
[-4855525327.740576,
-1063671099.509924,
303232221253.3586,
],
]),
columns=var_names,
index=var_names),
N=74,
r2=np.nan,
r2_a=np.nan,
mss=-6452353337.012137,
tss=np.nan,
rss=7087418733.133758,
kappa=1.003869278067604,
F=.820341839024799,
pF=.4485680388523306,
)
