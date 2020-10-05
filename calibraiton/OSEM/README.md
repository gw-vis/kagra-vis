# Calibration factors of OSEM
This document describe the calibration factors of OSEM. The purpose of this document is to check the consistency of the factors among the information in klog and the values embedded in medm.

OSEM[1]

1. 


## How to calibrate the LVDTs

Memo

* 

1. 

## How to obtain the actual calibration factor
### Fitting data



## Calibration factors
### How to see the table

* If the factors put on MEDM differ the factors posted on klog, the MEDM values are colored by <font color='Red'>red</font>. 
* 

### ETMX


| Item | Gain [um/cnt]<br> (klog, medm)| Offset [cnt] <br> (klog, medm)| Linear Range [cnt]<br>(c\_min, c\_max)|Description |
| :--|:--|:--|:---|:--|
| IP_H1 | (-0.258, -0.2582) | (-5000, <font color="Red">0</font>) | (-2e4, +3e4) | [[wiki](http://gwwiki.icrr.u-tokyo.ac.jp/JGWwiki/KAGRA/Subgroups/VIS/TypeA/ETMX)] [1] |
| IP_H2 | (-0.252, -0.252) | (-5000, <font color="Red">0</font>) | (-2e4, +3e4) | [[wiki](http://gwwiki.icrr.u-tokyo.ac.jp/JGWwiki/KAGRA/Subgroups/VIS/TypeA/ETMX)] [1] |
| IP_H3 | (-0.232, -0.233) | (-5000, <font color="Red">0</font>) | (-2e4, +3e4) | [[wiki](http://gwwiki.icrr.u-tokyo.ac.jp/JGWwiki/KAGRA/Subgroups/VIS/TypeA/ETMX)] [1] |
| F0_GAS | (-0.248, <font color='red'>-0.172</font>) | (-5000,<font color="Red">0</font>) | (-1e4, +3e4) | [[wiki](http://gwwiki.icrr.u-tokyo.ac.jp/JGWwiki/KAGRA/Subgroups/VIS/TypeA/ETMX)] [1] |
| F1_GAS | (-0.223, <font color='red'>-0.215</font>) | (-5000,<font color="Red">+2000</font>) | (-2e4, +3e4)| [[wiki](http://gwwiki.icrr.u-tokyo.ac.jp/JGWwiki/KAGRA/Subgroups/VIS/TypeA/ETMX),[3330](http://klog.icrr.u-tokyo.ac.jp/osl/?r=3330)] |
| F2_GAS | (-0.243, -0.243) | (-5000,<font color="Red">+2000</font>) | (-2e4, +2e4) | [[wiki](http://gwwiki.icrr.u-tokyo.ac.jp/JGWwiki/KAGRA/Subgroups/VIS/TypeA/ETMX),[3276](http://klog.icrr.u-tokyo.ac.jp/osl/?r=3276)] |
| F3_GAS | (-0.225, -0.2247) | (-5000,<font color="Red">0</font>) | (-2e4, +3e4)| [[wiki](http://gwwiki.icrr.u-tokyo.ac.jp/JGWwiki/KAGRA/Subgroups/VIS/TypeA/ETMX),[3205](http://klog.icrr.u-tokyo.ac.jp/osl/?r=3205)] |
| BF_GAS | (+0.204, +0.2035) | (-5000,<font color="Red">0</font>) | (-2e4, +3e4)| [[wiki](http://gwwiki.icrr.u-tokyo.ac.jp/JGWwiki/KAGRA/Subgroups/VIS/TypeA/ETMX),[3205](http://klog.icrr.u-tokyo.ac.jp/osl/?r=3205)] |
| BF_H1 | (+0.406, +0.406) | (0,0) | (-2e4, +2e4)| [[wiki](http://gwwiki.icrr.u-tokyo.ac.jp/JGWwiki/KAGRA/Subgroups/VIS/TypeA/ETMX),[3205](http://klog.icrr.u-tokyo.ac.jp/osl/?r=3205)] |
| BF_H2 | (+0.382, <font color='red'>-0.382</font>)| (0,0) | (-2e4, +2e4) | [[wiki](http://gwwiki.icrr.u-tokyo.ac.jp/JGWwiki/KAGRA/Subgroups/VIS/TypeA/ETMX),[3205](http://klog.icrr.u-tokyo.ac.jp/osl/?r=3205)] [2]|
| BF_H3 | (+0.363, <font color='red'>-0.363</font>)| (0,0) | (-2e4, +2e4) | [[wiki](http://gwwiki.icrr.u-tokyo.ac.jp/JGWwiki/KAGRA/Subgroups/VIS/TypeA/ETMX),[3205](http://klog.icrr.u-tokyo.ac.jp/osl/?r=3205)] [2]|
| BF_V1 | (+0.378, <font color='red'>-0.379</font>)| (0,0) | (-2e4, +2e4) | [[wiki](http://gwwiki.icrr.u-tokyo.ac.jp/JGWwiki/KAGRA/Subgroups/VIS/TypeA/ETMX),[3205](http://klog.icrr.u-tokyo.ac.jp/osl/?r=3205)] [2]|
| BF_V2 | (+0.385, +0.385)| (0,0) | (-2e4, +2e4) | [[wiki](http://gwwiki.icrr.u-tokyo.ac.jp/JGWwiki/KAGRA/Subgroups/VIS/TypeA/ETMX),[3205](http://klog.icrr.u-tokyo.ac.jp/osl/?r=3205)] |
| BF_V3 | (+0.390, +0.3902)| (0,0) | (-2e4, +2e4) | [[wiki](http://gwwiki.icrr.u-tokyo.ac.jp/JGWwiki/KAGRA/Subgroups/VIS/TypeA/ETMX),[3205](http://klog.icrr.u-tokyo.ac.jp/osl/?r=3205)] |

1. <font color='Red'>Where should we refer this value?</font> I could not find the calibration information in klog only in the JGW wiki.
2. <font color='Red'>Where should we refer this value?</font>  Polarity is filipped.

### ETMY

| Item | Gain [um/cnt]<br> (klog, medm)| Offset [cnt] <br> (klog, medm)| Linear Range [cnt] <br>(c\_min, c\_max)|Description |
| :--|:--|:--|:---|:--|
| IP_H1 | (-0.948, -0.948 ) | (-1000, <font color="Red">0</font>) |(-7e3, 9e3)| [[8086](http://klog.icrr.u-tokyo.ac.jp/osl/?r=8086)] |
| IP_H2 | (+0.850, +0.8497) | (-500, <font color="Red">0</font>) |(-7e3, 8e3)| [[8086](http://klog.icrr.u-tokyo.ac.jp/osl/?r=8086)] |
| IP_H3 | (-0.190, -0.1899) | (-5000, <font color="Red">0</font>) |(-2e4, 3e4)| [[8086](http://klog.icrr.u-tokyo.ac.jp/osl/?r=8086)] |
| F0_GAS | (-0.125, -0.125) | (????, <font color="Red">+1906.0</font>) |(????, ????)| [[8085](http://klog.icrr.u-tokyo.ac.jp/osl/?r=8085), [9378](http://klog.icrr.u-tokyo.ac.jp/osl/?r=9378)] [4]|
| F1_GAS | (????, <font color="Red">-0.661</font>) | (????, <font color="Red">-9688.0</font>) |(????, ????)| [3] |
| F2_GAS | (+0.719, +0.719) | (+2500, <font color="Red">+6850.0</font>) |(-9e3, +4e3)| [[2665](http://klog.icrr.u-tokyo.ac.jp/osl/?r=2665)] |
| F3_GAS | (-0.612, -0.612) | (-4000, <font color="Red">-11762.0</font>) |(-2e3, +1e4)| [[2575](http://klog.icrr.u-tokyo.ac.jp/osl/?r=2575)]|
| BF_GAS | (-0.882, -0.883) | (+2000, <font color="Red">-10585.0</font>) |(-7e3, +3e3)| [[2499](http://klog.icrr.u-tokyo.ac.jp/osl/?r=2499)] [1]|
| BF_H1 | (-0.5, +0.488) | (+1500, <font color="Red">-500.0</font>) |(-1.6e4, +1.3e4)| [[7603](http://klog.icrr.u-tokyo.ac.jp/osl/?r=7603)] [2]|
| BF_H2 | (+0.5, -0.476) | (0, <font color="Red">+4135.0</font>) |(-1.1e4, +1.1e4)| [[7603](http://klog.icrr.u-tokyo.ac.jp/osl/?r=7603)] [2]|
| BF_H3 | (-0.5, +0.458) | (+1500, <font color="Red">-2410.0</font>) |(-1.6e4, +1.3e4)| [[7603](http://klog.icrr.u-tokyo.ac.jp/osl/?r=7603)] [2]|
| BF_V1 | (+0.4, +0.409) | (+1500, <font color="Red">+1871.0</font>) |(-1.1e4, 0.8e4)| [[7603](http://klog.icrr.u-tokyo.ac.jp/osl/?r=7603)] [2]|
| BF_V2 | (+0.4, +0.439) | (+2500, <font color="Red">+1602.0</font>) |(-1.3e4, +0.8e4)| [[7603](http://klog.icrr.u-tokyo.ac.jp/osl/?r=7603)] [2]|
| BF_V3 | (-0.4, -0.385) | (-1500, <font color="Red">-692.0</font>) |(-0.8e4, +1.1e4)| [[7603](http://klog.icrr.u-tokyo.ac.jp/osl/?r=7603)] [2]|

1. <font color='Red'>Wrong c2v (10/2\*\*15 = 0.3052e-3) is used</font>. Correct one is 40/2\**16 = 0.6104e-3. It should be modified to correct value. 
2. Correct value is used. But, values should have one significant figure according to original data in #7603. 
3. <font color='Red'>Where should we refer this value?</font> I could not find in klog. 
4. <font color='Red'>Where should we refer this value?</font> 値が更新されているが、その値に関係した測定がklogにない。古い方(#8085)なら測定の情報がかいてあるが、これは使われていない。

### ITMX
| Item | Gain [um/cnt]<br> (klog, medm)| Offset [cnt] <br> (klog, medm)| Linear Range [cnt] <br>(c\_min, c\_max)|Description |
| :--|:--|:--|:---|:--|
| IP_H1 | (+0.299, +0.2987) | (-2000, <font color='red'>0</font>) |(-1.3e4, +1.7e4)| [[5131](http://klog.icrr.u-tokyo.ac.jp/osl/?r=5131)] |
| IP_H2 | (-0.1669, -0.1669) | (-2500, <font color='red'>0</font>) |(-1.7e4, +2.2e4)| [[5131](http://klog.icrr.u-tokyo.ac.jp/osl/?r=5131)] |
| IP_H3 | (+0.232, +0.2323) | (-1500, <font color='red'>0</font>) |(-1.7e4, +2.0e4)| [[5131](http://klog.icrr.u-tokyo.ac.jp/osl/?r=5131)] |
| F0_GAS | (-0.22, -0.22) | (????, <font color='red'>0</font>) |(????, ????)| [[8862](http://klog.icrr.u-tokyo.ac.jp/osl/?r=8862)] [3] |
| F1_GAS | (-0.363, <font color='red'>-0.18</font>)| (????, <font color='red'>0</font>) |(????, ????)| [[8862](http://klog.icrr.u-tokyo.ac.jp/osl/?r=8862)] [3] |
| F2_GAS | (-0.430, <font color='red'>-0.215</font>) | (????, <font color='red'>0</font>) |(????, ????)| [[4406](http://klog.icrr.u-tokyo.ac.jp/osl/?r=4406), [8862](http://klog.icrr.u-tokyo.ac.jp/osl/?r=8862)] [1] |
| F3_GAS | (+0.389, <font color='Red'>+0.194</font>) | (-8000, <font color='red'>0</font>) |(-1.6e4, +3.2e4)| [[4257](http://klog.icrr.u-tokyo.ac.jp/osl/?r=4257), [8862](http://klog.icrr.u-tokyo.ac.jp/osl/?r=8862)] [2]|
| BF_GAS | (-0.592, <font color='Red'>-0.296</font>) | (0, 0) |(-2.0e4, +2.0e4)| [[4211](http://klog.icrr.u-tokyo.ac.jp/osl/?r=4211), [8862](http://klog.icrr.u-tokyo.ac.jp/osl/?r=8862)] [2] |
| BF_H1 | (+0.371, +0.371) | (0, 0) |(-2e4, +2e4)| [[5002](http://klog.icrr.u-tokyo.ac.jp/osl/?r=5002)]|
| BF_H2 | (+0.381, <font color='red'>-0.440</font>)| (0, 0) |(-2e4, +2e4)| [[5002](http://klog.icrr.u-tokyo.ac.jp/osl/?r=5002)] [5]|
| BF_H3 | (+0.387, <font color='red'>+0.404</font>) | (0, 0) |(-2e4, +2e4)| [[5002](http://klog.icrr.u-tokyo.ac.jp/osl/?r=5002)] [5]|
| BF_V1 | (-0.354, -0.354) | (0, 0) |(-2e4, +2e4)| [[5002](http://klog.icrr.u-tokyo.ac.jp/osl/?r=5002)]|
| BF_V2 | (-0.367, -0.367) | (0, 0) |(-2e4, +2e4)| [[5002](http://klog.icrr.u-tokyo.ac.jp/osl/?r=5002)]|
| BF_V3 | (+0.385, <font color='red'>-0.385</font>) | (0, 0) |(-2e4, +2e4)| [[5002](http://klog.icrr.u-tokyo.ac.jp/osl/?r=5002), [6847](http://klog.icrr.u-tokyo.ac.jp/osl/?r=6847)] [4]|

1. <font color='Red'>Where should we refer this value?</font> 最新の値に関係した測定の情報が見当たらない。#8862 で値が最新に更新されているが、測定の情報はklogにはみつからなかった。ちなみにもし、#4406の古い測定の値を c2v(=0.6104e-3) を使って計算すると、0.8 [um/cnt] が入る。が、再測定が必要と記述があるので、やはり最新の値を使うべきと思う。
2. 古い情報が残っているとおもう。Modified new values are posted on #8862. Old ones are calculated by wrong c2v which is a half of the correct value. Correct value is 40/2**16 (=0.6104e-3). However, I think old ones posted on #4257 and #4211 are still used in the actual values on medm, respectively.
3. <font color='Red'>Where should we refer this value?</font> I could not find measurement imformation related F0 and F1 GAS in klog. I just found the calibration factor only in #8862.
4. 間違った符号が入っていると #6847 報告があったが、どうやら再び、間違った値が medm に入っている。正しい値は "+0.385" であり、 "-0.385" ではない。
5. <font color='Red'>Where should we refer this value?</font> I could not find the values on klog. 


### ITMY
| Item | Gain [um/cnt]<br> (klog, medm)| Offset [cnt] <br> (klog, medm)| Linear Range [cnt] <br>(c\_min, c\_max)|Description |
| :--|:--|:--|:---|:--|
| IP_H1 | (????, <font color="Red">-0.268</font>) | (????, <font color='Red'>0</font>) |(????, ????)| [2] |
| IP_H2 | (????, <font color="Red">-0.208</font>) | (????, <font color='Red'>0</font>) |(????, ????)| [2]|
| IP_H3 | (????, <font color="Red">+0.237</font>) | (????, <font color='Red'>0</font>) |(????, ????)| [2]|
| F0_GAS | (????, <font color="Red">-0.300</font>) | (????, <font color='Red'>0</font>) |(????, ????)| [2] |
| F1_GAS | (-0.342, -0.342) | (0, 0) |(-1e4, +1e4)| [[5587](http://klog.icrr.u-tokyo.ac.jp/osl/?r=5587)] |
| F2_GAS | (+0.951, <font color="Red">+0.0979</font>) | (????, <font color='Red'>0</font>) |(????, ????)| [[5494](http://klog.icrr.u-tokyo.ac.jp/osl/?r=5494)] [1] |
| F3_GAS | (+0.219, +0.219) | (0, 0) |(-0.8e4, +0.8e4)| [[5325](http://klog.icrr.u-tokyo.ac.jp/osl/?r=5325)] [3]|
| BF_GAS | (+0.452, <font color="Red">+0.321</font>) | (????, <font color='Red'>0</font>) |(????, ????)| [[5249](http://klog.icrr.u-tokyo.ac.jp/osl/?r=5249)] [4]|
| BF_H1 | (-0.304, -0.304) | (0, 0) |(-2e4, 2e4)| [[5756](http://klog.icrr.u-tokyo.ac.jp/osl/?r=5756)] |
| BF_H2 | (-0.337, <font color="Red">+0.334</font>) | (0, 0) |(-2e4, 2e4)| [[5756](http://klog.icrr.u-tokyo.ac.jp/osl/?r=5756)] [5]|
| BF_H3 | (-0.321, -0.320) | (0, 0) |(-2e4, 2e4) | [[5756](http://klog.icrr.u-tokyo.ac.jp/osl/?r=5756)]|
| BF_V1 | (+0.373, +0.374) | (0, 0) |(-2e4, 2e4)| [[5756](http://klog.icrr.u-tokyo.ac.jp/osl/?r=5756)]|
| BF_V2 | (-0.313, <font color="Red">+0.313</font>) | (0, 0) |(-2e4, 2e4)| [[5756](http://klog.icrr.u-tokyo.ac.jp/osl/?r=5756)] [5]|
| BF_V3 | (-0.323, -0.323) | (0, 0) |(-2e4, 2e4)| [[5756](http://klog.icrr.u-tokyo.ac.jp/osl/?r=5756)]|

1. <font color='Red'>Where should we refer this value?</font> #5494のグラフより、-2.5Vをノミナル位置として±1Vの線形範囲をもつことがわかる。この範囲での係数は0.951 [um/cnt]。だがmedmではは0V位置をノミナルにしているので、この係数は使えない。使うには0V付近でフィッティングした係数を使う必要あり。
2. <font color='Red'>Where should we refer this value?</font> I could not find the values on klog. 
3. Use correct c2v.
4. <font color='Red'>Where should we refer this value?</font> According to #5249, value should be +0.452. But, actual value on medm does not same as it.
5. <font color='Red'>Where should we refer this value?</font> According to #5756, value should be "-0.337" and "-0.313" for BF\_H2 and BF\_V2, respectively. But, actual value on medm does not same as these.


### BS
| Item | Gain [um/cnt]<br> (klog, medm)| Offset [cnt] <br> (klog, medm)| Linear Range [cnt] <br>(c\_min, c\_max)|Description |
| :--|:--|:--|:---|:--|
| IP_H1 | (+0.327, +0.327)  | (0, <font color="Red">-1122.9</font>) |(-1.5e4, +1.5e4)| [[7656](http://klog.icrr.u-tokyo.ac.jp/osl/?r=7656)] |
| IP_H2 | (+0.299, +0.299)  | (0, <font color="Red">-1264.2</font>) |(-1.5e4, +1.5e4)| [[7656](http://klog.icrr.u-tokyo.ac.jp/osl/?r=7656)] |
| IP_H3 | (+0.396, +0.396)  | (0, <font color="Red">-868.5</font>) |(-1.0e4, +1.0e4)| [[7656](http://klog.icrr.u-tokyo.ac.jp/osl/?r=7656)] |
| F0_GAS | (+0.886, <font color="Red">+1.116</font>)  | (0, <font color="Red">+870.0</font>) |(-2000, +2000)| [[7072](http://klog.icrr.u-tokyo.ac.jp/osl/?r=7072)] [1] |
| F1_GAS | (+0.772, +0.771)  | (-900, <font color="Red">-1090.0</font>) |(+200, +2000)| [[3358](http://klog.icrr.u-tokyo.ac.jp/osl/?r=3358)] |
| BF_GAS | (+0.427, +0.427)  | (-1000, <font color="Red">-350.0</font>) |(-2000, +4000)| [[3280](http://klog.icrr.u-tokyo.ac.jp/osl/?r=3280)] |

1. <font color='Red'>Where should we refer this value?</font> According to #7072, value should be +0.886. But, actual value on medm does not same as it.

### SRM
| Item | Gain [um/cnt]<br> (klog, medm)| Offset [cnt] <br> (klog, medm)| Linear Range [cnt] <br>(c\_min, c\_max)|Description |
| :--|:--|:--|:---|:--|
| IP_H1 | (+0.294, +0.294)  | (0, <font color="Red">-373.0</font>) |(-2e4, +2e4)| [[7087](http://klog.icrr.u-tokyo.ac.jp/osl/?r=7087)]|
| IP_H2 | (+0.315, +0.315)  | (0, <font color="Red">-1253.0</font>) |(-2e4, +2e4)| [[7087](http://klog.icrr.u-tokyo.ac.jp/osl/?r=7087)]|
| IP_H3 | (+0.317, +0.317)  | (0, <font color="Red">-146.0</font>) |(-2e4, +2e4)| [[7087](http://klog.icrr.u-tokyo.ac.jp/osl/?r=7087)]|
| F0_GAS | (-0.186, <font color="Red">+0.185</font>)  | (-5000, <font color="Red">+2551.0</font>) |(-1.5e4, +2.5e4)| [[7427](http://klog.icrr.u-tokyo.ac.jp/osl/?r=7427)] [1]|
| F1_GAS | (+0.141, +0.141)  | (-5000, <font color="Red">-4005.0</font>) |(-1.5e4, +2.5e4)| [[4688](http://klog.icrr.u-tokyo.ac.jp/osl/?r=4688)] |
| BF_GAS | (+0.156, +0.156)  | (-5000, <font color="Red">+2058.2</font>) |(-1.5e4, +2.5e4)| [[4688](http://klog.icrr.u-tokyo.ac.jp/osl/?r=4688)] |

1. <font color='Red'>Where should we refer this value?</font> According to #7427, value should be -0.186. But, actual value on medm does not same as it.


### SR2
| Item | Gain [um/cnt]<br> (klog, medm)| Offset [cnt] <br> (klog, medm)| Linear Range [cnt] <br>(c\_min, c\_max)|Description |
| :--|:--|:--|:---|:--|
| IP_H1 | (+0.281, +0.281)  | (0, <font color='Red'>+2057.0</font>) |(-2e4, +2e4)| [[6078](http://klog.icrr.u-tokyo.ac.jp/osl/?r=6078)] |
| IP_H2 | (+0.306, +0.306)  | (0, <font color='Red'>-2552.0</font>) |(-2e4, +2e4)| [[6078](http://klog.icrr.u-tokyo.ac.jp/osl/?r=6078)] |
| IP_H3 | (+0.301, +0.301)  | (0, <font color='Red'>-2022.0</font>) |(-2e4, +2e4)| [[6078](http://klog.icrr.u-tokyo.ac.jp/osl/?r=6078)] |
| F0_GAS | (+0.178, +0.178)  | (-5000, <font color='Red'>-10214.0</font>) |(-2e4, +3e4)| [[6080](http://klog.icrr.u-tokyo.ac.jp/osl/?r=6080)] |
| F1_GAS | (+0.090, +0.090)  | (0, <font color='Red'>-4740.0</font>) |(-2e4, +2e4)| [[4365](http://klog.icrr.u-tokyo.ac.jp/osl/?r=4365)] |
| BF_GAS | (+0.160, +0.160)  | (-5000, <font color='Red'>+886.0</font>) |(-1e4, +2e4)| [[4166](http://klog.icrr.u-tokyo.ac.jp/osl/?r=4166)] |

1. Fine! 

### SR3
| Item | Gain [um/cnt]<br> (klog, medm)| Offset [cnt] <br> (klog, medm)| Linear Range [cnt] <br>(c\_min, c\_max)|Description |
| :--|:--|:--|:---|:--|
| IP_H1 | (+0.262, +0.262)  | (0, <font color='Red'>-876.4</font>) |(-2e4, +2e4)| [[5551](http://klog.icrr.u-tokyo.ac.jp/osl/?r=5551)]|
| IP_H2 | (+0.240, +0.240)  | (0, <font color='Red'>-877.8</font>) |(-2e4, +2e4)| [[5551](http://klog.icrr.u-tokyo.ac.jp/osl/?r=5551)]|
| IP_H3 | (+0.253, +0.253)  | (0, <font color='Red'>-1188.6</font>) |(-2e4, +2e4)| [[5551](http://klog.icrr.u-tokyo.ac.jp/osl/?r=5551)]|
| F0_GAS | (-0.182, +0.181)  | (0, <font color='Red'>-677.0</font>) |(-2e4, +2e4)| [[5529](http://klog.icrr.u-tokyo.ac.jp/osl/?r=5529)]|
| F1_GAS | (+0.088, +0.088)  | (0, <font color='Red'>-1690.0</font>) |(-2e4, +2e4)| [[4650](http://klog.icrr.u-tokyo.ac.jp/osl/?r=4650)] |
| BF_GAS | (+0.055, +0.055)  | (0, <font color='Red'>-5170.0</font>) |(-2e4, +2e4)| [[4650](http://klog.icrr.u-tokyo.ac.jp/osl/?r=4650)]|

1. Fine!


### PRM
| Item | Gain [um/cnt]<br> (klog, medm)| Offset [cnt] <br> (klog, medm)| Linear Range [cnt] <br>(c\_min, c\_max)|Description |
| :--|:--|:--|:---|:--|
| BF_GAS | (+0.241, +0.241)  | (0, 0) |(-2e4, +2e4)| [[3290](http://klog.icrr.u-tokyo.ac.jp/osl/?r=3290)] |
| SF_GAS | (+0.251, <font color='Red'>+1.000</font>)  | (????, <font color='Red'>0</font>) |(????, ????)| [[8399](http://klog.icrr.u-tokyo.ac.jp/osl/?r=8399)] [1]|
| BF_H1 | (-0.973, -0.973)  | (0, 0) |(-0.4e4, +0.4e4)| [[2926](http://klog.icrr.u-tokyo.ac.jp/osl/?r=2926)] |
| BF_H2 | (-0.940, -0.940)  | (0, 0) |(-0.5e4, +0.5e4)| [[2926](http://klog.icrr.u-tokyo.ac.jp/osl/?r=2926)] |
| BF_H3 | (-0.945, -0.945)  | (0, 0) |(-0.5e4, +0.5e4)| [[2926](http://klog.icrr.u-tokyo.ac.jp/osl/?r=2926)] |
| BF_V1 |  (+0.941, +0.941)  | (0, 0) |(-0.5e4, +0.5e4)| [[2926](http://klog.icrr.u-tokyo.ac.jp/osl/?r=2926)] |
| BF_V2 |  (-0.956, -0.956)  | (0, 0) |(-0.4e4, +0.4e4)| [[2926](http://klog.icrr.u-tokyo.ac.jp/osl/?r=2926)] |
| BF_V3 |  (-0.954, <font color="Red">+0.954</font>)  | (0, 0) |(-0.5e4, +0.5e4)| [[2926](http://klog.icrr.u-tokyo.ac.jp/osl/?r=2926)] [2]|

1. <font color='Red'>Where should we refer this value?</font> According to #8399 the calibration factor is +0.251, but there are no information about it.  
2. <font color='Red'>Where should we refer this value?</font> According to #2926, value should be "-0.954". But, actual value on medm does not same as it.


### PR2
| Item | Gain [um/cnt]<br> (klog, medm)| Offset [cnt] <br> (klog, medm)| Linear Range [cnt] <br>(c\_min, c\_max)|Description |
| :--|:--|:--|:---|:--|
| SF_GAS | (-0.322, -0.322)  | (-2500, <font color='Red'>0</font>) |(-0.5e4, 1.0e4)| [[3132](http://klog.icrr.u-tokyo.ac.jp/osl/?r=3132)] |
| BF_GAS | (+0.414, +0.414)  | (????, <font color='Red'>0</font>) |(????, ????)| [[3077](http://klog.icrr.u-tokyo.ac.jp/osl/?r=3077)] [1]|
| BF_H1 | (-1.229, <font color='Red'>+1.229</font>)  | (0, <font color='Red'>+44.1</font>) |(-0.4e4,+0.4e4)| [[2906](http://klog.icrr.u-tokyo.ac.jp/osl/?r=2906)] [2,4]|
| BF_H2 | (-1.250, <font color='Red'>+1.250</font>)  | (0, <font color='Red'>+419.2</font>) |(-0.4e4,+0.4e4)| [[2906](http://klog.icrr.u-tokyo.ac.jp/osl/?r=2906)] [2,4]|
| BF_H3 | (-1.216, -1.216)  | (0, <font color='Red'>+30.6</font>) |(-0.4e4,+0.4e4)| [[2906](http://klog.icrr.u-tokyo.ac.jp/osl/?r=2906)] |
| BF_V1 | (+1.203, <font color='Red'>-1.202</font>)  | (+1000, <font color='Red'>+1103.5</font>) |(-0.5e4,+0.3e4)| [[2906](http://klog.icrr.u-tokyo.ac.jp/osl/?r=2906) [8956](http://klog.icrr.u-tokyo.ac.jp/osl/?r=8956)] [2,3]|
| BF_V2 | (+1.229, +1.229)  | (0, <font color='Red'>-516.7</font>) |(-0.4e4,+0.4e4)| [[2906](http://klog.icrr.u-tokyo.ac.jp/osl/?r=2906)] |
| BF_V3 | (+1.224, <font color='Red'>-1.224</font>)  | (0, <font color='Red'>+142.9</font>) |(-0.4e4,+0.4e4)| [[2906](http://klog.icrr.u-tokyo.ac.jp/osl/?r=2906), [8956](http://klog.icrr.u-tokyo.ac.jp/osl/?r=8956)] [2,3]|

1. <font color='Red'>Where should we refer this value?</font> I could not find measurement in klog.
2. <font color='Red'>Where should we refer this value?</font> Polarity is changed. 
3. BF-V do not seem to be changed from the first calibration work in #2906. After this work, at May 22nd 2019, BF-V was renewed as posted in #8956. But, in this modification, BF-V LVDT board was tuned so that transfer function from BF-Vexc to BF-V1/V2/V3 had same amplitude before/after this work. So, BF-V1/V3 should be same as the first work. (Absorute value must be same, but sign may not be.)
4. According to [3], BF-H was not changed. These also should be same as #2906.



### PR3
| Item | Gain [um/cnt]<br> (klog, medm)| Offset [cnt] <br> (klog, medm)| Linear Range [cnt] <br>(c\_min, c\_max)|Description |
| :--|:--|:--|:---|:--|
| SF_GAS | (+0.337, +0.337)  | (+2500, <font color='Red'>0</font>) |(-1.5e4, +1.0e4)| [[2739](http://klog.icrr.u-tokyo.ac.jp/osl/?r=2739)] |
| BF_GAS | (-0.342, <font color='Red'>+0.342</font>)  | (+7500, <font color='Red'>0</font>) |(-1.5e4,0)| [[2670](http://klog.icrr.u-tokyo.ac.jp/osl/?r=2670)] [1]|
| BF_H1 | (-1.659, -1.658)  | (+1000, <font color='Red'>0</font>) |(-0.4e4, +0.2e4)| [[2627](http://klog.icrr.u-tokyo.ac.jp/osl/?r=2627)] |
| BF_H2 | (-1.645, <font color='Red'>+1.645</font>)  | (+500, <font color='Red'>0</font>) |(-0.3e4, +0.2e4)| [[2627](http://klog.icrr.u-tokyo.ac.jp/osl/?r=2627)] [1]|
| BF_H3 | (-1.681, <font color='Red'>+1.681</font>)  | (+500, <font color='Red'>0</font>) |(-0.35e4, +0.25e4)| [[2627](http://klog.icrr.u-tokyo.ac.jp/osl/?r=2627)] [1]|
| BF_V1 | (+1.722, +1.722)  | (0, 0) |(-0.25e4, +0.25e4)| [[2627](http://klog.icrr.u-tokyo.ac.jp/osl/?r=2627)]|
| BF_V2 | (-1.730, -1.730)  | (0, 0) |(-0.3e4, +0.3e4)| [[2627](http://klog.icrr.u-tokyo.ac.jp/osl/?r=2627)]|
| BF_V3 | (+1.611, +1.611)  | (0, 0) |(-0.3e4, +0.3e4)| [[2627](http://klog.icrr.u-tokyo.ac.jp/osl/?r=2627)]|

1. <font color='Red'>Where should we refer this value?</font> Polarity is changed.





