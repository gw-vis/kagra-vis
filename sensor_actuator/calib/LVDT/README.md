# Calibration factors of LVDT 
This document describe the calibration factors of LVDT. The purpose of this document is to check the consistency of the factors among the information in klog and the values embedded in medm.

LVDT[1]

1. Tariq, Hareem, et al. "The linear variable differential transformer (LVDT) position sensor for gravitational wave interferometer low-frequency controls." Nuclear Instruments and Methods in Physics Research Section A: Accelerators, Spectrometers, Detectors and Associated Equipment 489.1-3 (2002): 570-576.


## How to calibrate the LVDTs

Memo

* LVDT and Voice Drivers [2]
* Enzo のマニュアル[1], Joris のマニュアル[3]

1. [JGW-E1707287](https://gwdoc.icrr.u-tokyo.ac.jp/cgi-bin/private/DocDB/ShowDocument?docid=7287)
2. [JGW-D1301467](https://gwdoc.icrr.u-tokyo.ac.jp/cgi-bin/private/DocDB/ShowDocument?docid=1467)
3. [JGW-T1604798](https://gwdoc.icrr.u-tokyo.ac.jp/cgi-bin/private/DocDB/ShowDocument?docid=4798)
4. 

## How to obtain the actual calibration factor
### Fitting data
![Example](./example.png)

Fitting data with linear function defined below.

```
c = a0*(x - a1)
 - x [um]      : Displacement [1], 
 - c [cnt]     : LVDT count in digital system, 
 - a0 [cnt/mm] : Calibration factor from mm to cnt, 
 - a1 [mm]     : Displacement when the count is 0.
 
Linear sensor range (x_min, x_max) 
 - x_min, x_max : Minimum and maximum displacement.

[1] from where? It depends on people who measure.
```


### Calculate the gain and the offset
We want to know a factor from count to um. So, we resolve Equation 1 in terms of c.

```
x = b0*(c + b1)  <--- (Eq.1)
 - x [um]      : Displacement [1], 
 - c [cnt]     : LVDT count in digital system, 
 - b0 [um/cnt] : Calibration factor from count to um 
                 (gain value in the input filter)
 - b1 [cnt]    : LVDT count when the emitter coil is at 0 mm.
 
Linear sensor range (c_min, c_max) 
 - c_min, c_max : Minimum and maximum count of the LVDT count.

[1] from where? It depends on people who measure.
```

For example, we can get paramters from example plot shown above.

```
b0 = 1/(a0*1000) = +0.379 [um/cnt]
b1 = (a1*1000)/a0 = +1.64e4 [cnt]
```
**1) Gain**

We select b0 as the gain in the input filter.

**2) Offset**

We do not select b1 as the offset in the input filter. The offsets are selected to produce a readout of zero at the nominal position of the keystone according to the 3D CAD, according to Fabian's post in [Issue#7](https://github.com/gw-vis/kagra-vis/issues/7).

<font color='Red'>[Warning]</font> Please modify the offset values below tables. <font color='Red'>[Warning]</font>

## Calibration factors
### How to see the table

* If the factors put on MEDM differ the factors posted on klog, the MEDM values are colored by <font color='Red'>red</font>. 
* 

### ETMX


| Item | Gain [um/cnt]<br> (klog, medm)| Offset [cnt] <br> (klog, medm)| Linear Range [cnt]<br>(c\_min, c\_max)|Description |
| :--|:--|:--|:---|:--|
| IP_H1 | (-0.258, -0.2582) [*1]| (xxxx, 0) | (-2e4, +3e4) | [[wiki](http://gwwiki.icrr.u-tokyo.ac.jp/JGWwiki/KAGRA/Subgroups/VIS/TypeA/ETMX)] |
| IP_H2 | (-0.252, -0.252) [*1]| (xxxx, 0) | (-2e4, +3e4) | [[wiki](http://gwwiki.icrr.u-tokyo.ac.jp/JGWwiki/KAGRA/Subgroups/VIS/TypeA/ETMX)]  |
| IP_H3 | (-0.232, -0.233) [*1] | (xxxx, 0) | (-2e4, +3e4) | [[wiki](http://gwwiki.icrr.u-tokyo.ac.jp/JGWwiki/KAGRA/Subgroups/VIS/TypeA/ETMX)]  |
| F0_GAS | (-0.248, <font color='red'>-0.172</font>) [*1]| (xxxx,0) | (-1e4, +3e4) | [[wiki](http://gwwiki.icrr.u-tokyo.ac.jp/JGWwiki/KAGRA/Subgroups/VIS/TypeA/ETMX)] |
| F1_GAS | (-0.223, <font color='red'>-0.215</font>) [*2]| (xxxx,+2000) | (-2e4, +3e4)| [[wiki](http://gwwiki.icrr.u-tokyo.ac.jp/JGWwiki/KAGRA/Subgroups/VIS/TypeA/ETMX),[3330](http://klog.icrr.u-tokyo.ac.jp/osl/?r=3330)] |
| F2_GAS | (-0.243, -0.243) | (xxxx,+2000) | (-2e4, +2e4) | [[wiki](http://gwwiki.icrr.u-tokyo.ac.jp/JGWwiki/KAGRA/Subgroups/VIS/TypeA/ETMX),[3276](http://klog.icrr.u-tokyo.ac.jp/osl/?r=3276)] |
| F3_GAS | (-0.225, -0.2247) | (xxxx,0) | (-2e4, +3e4)| [[wiki](http://gwwiki.icrr.u-tokyo.ac.jp/JGWwiki/KAGRA/Subgroups/VIS/TypeA/ETMX),[3205](http://klog.icrr.u-tokyo.ac.jp/osl/?r=3205)] |
| BF_GAS | (+0.204, +0.2035) | (xxxx,0) | (-2e4, +3e4)| [[wiki](http://gwwiki.icrr.u-tokyo.ac.jp/JGWwiki/KAGRA/Subgroups/VIS/TypeA/ETMX),[3205](http://klog.icrr.u-tokyo.ac.jp/osl/?r=3205)] |
| BF_H1 | (+0.406, +0.406) | (xxxx,0) | (-2e4, +2e4)| [[wiki](http://gwwiki.icrr.u-tokyo.ac.jp/JGWwiki/KAGRA/Subgroups/VIS/TypeA/ETMX),[3205](http://klog.icrr.u-tokyo.ac.jp/osl/?r=3205)] |
| BF_H2 | (+0.382, <font color='red'>-0.382</font>) [*3]| (xxxx,0) | (-2e4, +2e4) | [[wiki](http://gwwiki.icrr.u-tokyo.ac.jp/JGWwiki/KAGRA/Subgroups/VIS/TypeA/ETMX),[3205](http://klog.icrr.u-tokyo.ac.jp/osl/?r=3205)] |
| BF_H3 | (+0.363, <font color='red'>-0.363</font>) [*3]| (xxxx,0) | (-2e4, +2e4) | [[wiki](http://gwwiki.icrr.u-tokyo.ac.jp/JGWwiki/KAGRA/Subgroups/VIS/TypeA/ETMX),[3205](http://klog.icrr.u-tokyo.ac.jp/osl/?r=3205)]|
| BF_V1 | (+0.378, <font color='red'>-0.379</font>) [*3]| (xxxx,0) | (-2e4, +2e4) | [[wiki](http://gwwiki.icrr.u-tokyo.ac.jp/JGWwiki/KAGRA/Subgroups/VIS/TypeA/ETMX),[3205](http://klog.icrr.u-tokyo.ac.jp/osl/?r=3205)]|
| BF_V2 | (+0.385, +0.385)| (xxxx,0) | (-2e4, +2e4) | [[wiki](http://gwwiki.icrr.u-tokyo.ac.jp/JGWwiki/KAGRA/Subgroups/VIS/TypeA/ETMX),[3205](http://klog.icrr.u-tokyo.ac.jp/osl/?r=3205)] |
| BF_V3 | (+0.390, +0.3902)| (xxxx,0) | (-2e4, +2e4) | [[wiki](http://gwwiki.icrr.u-tokyo.ac.jp/JGWwiki/KAGRA/Subgroups/VIS/TypeA/ETMX),[3205](http://klog.icrr.u-tokyo.ac.jp/osl/?r=3205)] |

1. <font color='Red'>Where should we refer this value?</font> I could not find the calibration information in klog only in the JGW wiki.
2. <font color='Red'>Where should we refer this value?</font> 
3. <font color='Red'>Where should we refer this value?</font>  Polarity is filipped.

### ETMY

| Item | Gain [um/cnt]<br> (klog, medm)| Offset [cnt] <br> (klog, medm)| Linear Range [cnt] <br>(c\_min, c\_max)|Description |
| :--|:--|:--|:---|:--|
| IP_H1 | (-0.948, -0.948 ) | (xxxx, 0) |(-7e3, 9e3)| [[8086](http://klog.icrr.u-tokyo.ac.jp/osl/?r=8086)] |
| IP_H2 | (+0.850, +0.8497) | (xxxx, 0) |(-7e3, 8e3)| [[8086](http://klog.icrr.u-tokyo.ac.jp/osl/?r=8086)] |
| IP_H3 | (-0.190, -0.1899) | (xxxx, 0) |(-2e4, 3e4)| [[8086](http://klog.icrr.u-tokyo.ac.jp/osl/?r=8086)] |
| F0_GAS | (-0.125, -0.125) | (<font color="Red">????</font>, +1906.0) [*4] | <font color="Red">(????, ????)</font> [*4]| [[8085](http://klog.icrr.u-tokyo.ac.jp/osl/?r=8085), [9378](http://klog.icrr.u-tokyo.ac.jp/osl/?r=9378)]|
| F1_GAS | (????, <font color="Red">-0.661</font>) [*3]| (????, -9688.0) |(????, ????)| ???? |
| F2_GAS | (+0.719, +0.719) | (xxxx, +6850.0) |(-9e3, +4e3)| [[2665](http://klog.icrr.u-tokyo.ac.jp/osl/?r=2665)] |
| F3_GAS | (-0.612, -0.612) | (xxxx, -11762.0) |(-2e3, +1e4)| [[2575](http://klog.icrr.u-tokyo.ac.jp/osl/?r=2575)]|
| BF_GAS | (-0.848, -0.848)|  | [*1]| [[15789](http://klog.icrr.u-tokyo.ac.jp/osl/?r=15789)] |
| BF_H1 | (-0.5, +0.488) [*2]| (xxxx, -500.0) |(-1.6e4, +1.3e4)| [[7603](http://klog.icrr.u-tokyo.ac.jp/osl/?r=7603)] |
| BF_H2 | (+0.5, -0.476) [*2]| (xxxx, +4135.0) |(-1.1e4, +1.1e4)| [[7603](http://klog.icrr.u-tokyo.ac.jp/osl/?r=7603)] |
| BF_H3 | (-0.5, +0.458) [*2]| (xxxx, -2410.0) |(-1.6e4, +1.3e4)| [[7603](http://klog.icrr.u-tokyo.ac.jp/osl/?r=7603)] |
| BF_V1 | (+0.4, +0.409) [*2]| (xxxx, +1871.0) |(-1.1e4, 0.8e4)| [[7603](http://klog.icrr.u-tokyo.ac.jp/osl/?r=7603)] |
| BF_V2 | (+0.4, +0.439) [*2]| (xxxx, +1602.0) |(-1.3e4, +0.8e4)| [[7603](http://klog.icrr.u-tokyo.ac.jp/osl/?r=7603)] |
| BF_V3 | (-0.4, -0.385) [*2]| (xxxx, -692.0) |(-0.8e4, +1.1e4)| [[7603](http://klog.icrr.u-tokyo.ac.jp/osl/?r=7603)]|

1. Nominal position is setted at 70 mm but the zero cross point is 69 mm according to the plot#1 in klog. Additionally, The linear range is from 65 mm to 75 mm. 
2. Correct value is used. But, values should have one significant figure according to original data in #7603. 
3. <font color='Red'>Where should we refer this value?</font> I could not find in klog. 
4. <font color='Red'>Where should we refer this value?</font> 値が更新されているが、その値に関係した測定がklogにない。古い方(#8085)なら測定の情報がかいてあるが、これは使われていない。

### ITMX
| Item | Gain [um/cnt]<br> (klog, medm)| Offset [cnt] <br> (klog, medm)| Linear Range [cnt] <br>(c\_min, c\_max)|Description |
| :--|:--|:--|:---|:--|
| IP_H1 | (+0.299, +0.2987) | (xxxx, 0) |(-1.3e4, +1.7e4)| [[5131](http://klog.icrr.u-tokyo.ac.jp/osl/?r=5131)] |
| IP_H2 | (-0.1669, -0.1669) | (xxxx, 0) |(-1.7e4, +2.2e4)| [[5131](http://klog.icrr.u-tokyo.ac.jp/osl/?r=5131)] |
| IP_H3 | (+0.232, +0.2323) | (xxxx, 0) |(-1.7e4, +2.0e4)| [[5131](http://klog.icrr.u-tokyo.ac.jp/osl/?r=5131)] |
| F0_GAS | (-0.22, -0.22) | (<font color='red'>????</font>, 0) [*3]|<font color='red'>(????, ????)</font>| [[8862](http://klog.icrr.u-tokyo.ac.jp/osl/?r=8862)]  |
| F1_GAS | (-0.363, <font color='red'>-0.18</font>) [*3]| (<font color='Red'>????</font>, 0) [*3]|<font color='red'>(????, ????)</font> [*3]| [[8862](http://klog.icrr.u-tokyo.ac.jp/osl/?r=8862)]  |
| F2_GAS | (-0.430, <font color='red'>-0.215</font>) [*1] | (????, 0) |(????, ????)| [[4406](http://klog.icrr.u-tokyo.ac.jp/osl/?r=4406), [8862](http://klog.icrr.u-tokyo.ac.jp/osl/?r=8862)] |
| F3_GAS | (+0.389, <font color='Red'>+0.194</font>) [*2]| (xxxx, 0) |(-1.6e4, +3.2e4)| [[4257](http://klog.icrr.u-tokyo.ac.jp/osl/?r=4257), [8862](http://klog.icrr.u-tokyo.ac.jp/osl/?r=8862)] |
| BF_GAS | (-0.592, <font color='Red'>-0.296</font>) [*2]| (xxxx, 0) |(-2.0e4, +2.0e4)| [[4211](http://klog.icrr.u-tokyo.ac.jp/osl/?r=4211), [8862](http://klog.icrr.u-tokyo.ac.jp/osl/?r=8862)]  |
| BF_H1 | (+0.371, +0.371) | (xxxx, 0) |(-2e4, +2e4)| [[5002](http://klog.icrr.u-tokyo.ac.jp/osl/?r=5002)]|
| BF_H2 | (+0.381, <font color='red'>-0.440</font>) [*5]| (xxxx, 0) |(-2e4, +2e4)| [[5002](http://klog.icrr.u-tokyo.ac.jp/osl/?r=5002)] |
| BF_H3 | (+0.387, <font color='red'>+0.404</font>) [*5]| (xxxx, 0) |(-2e4, +2e4)| [[5002](http://klog.icrr.u-tokyo.ac.jp/osl/?r=5002)] |
| BF_V1 | (-0.354, -0.354) | (xxxx, 0) |(-2e4, +2e4)| [[5002](http://klog.icrr.u-tokyo.ac.jp/osl/?r=5002)]|
| BF_V2 | (-0.367, -0.367) | (xxxx, 0) |(-2e4, +2e4)| [[5002](http://klog.icrr.u-tokyo.ac.jp/osl/?r=5002)]|
| BF_V3 | (+0.385, <font color='red'>-0.385</font>) [*4]| (xxxx, 0) |(-2e4, +2e4)| [[5002](http://klog.icrr.u-tokyo.ac.jp/osl/?r=5002), [6847](http://klog.icrr.u-tokyo.ac.jp/osl/?r=6847)] |

1. <font color='Red'>Where should we refer this value?</font> 最新の値に関係した測定の情報が見当たらない。#8862 で値が最新に更新されているが、測定の情報はklogにはみつからなかった。ちなみにもし、#4406の古い測定の値を c2v(=0.6104e-3) を使って計算すると、0.8 [um/cnt] が入る。が、再測定が必要と記述があるので、やはり最新の値を使うべきと思う。
2. 古い情報が残っているとおもう。Modified new values are posted on #8862. Old ones are calculated by wrong c2v which is a half of the correct value. Correct value is 40/2**16 (=0.6104e-3). However, I think old ones posted on #4257 and #4211 are still used in the actual values on medm, respectively.
3. <font color='Red'>Where should we refer this value?</font> I could not find measurement imformation related F0 and F1 GAS in klog. I just found the calibration factor only in #8862.
4. 間違った符号が入っていると #6847 報告があったが、どうやら再び、間違った値が medm に入っている。正しい値は "+0.385" であり、 "-0.385" ではない。
5. <font color='Red'>Where should we refer this value?</font> I could not find the values on klog. 


### ITMY
| Item | Gain [um/cnt]<br> (klog, medm)| Offset [cnt] <br> (klog, medm)| Linear Range [cnt] <br>(c\_min, c\_max)|Description |
| :--|:--|:--|:---|:--|
| IP_H1 | (-0.268, -0.268) | (<font color="Red">????</font>, 0) |<font color="Red">(????, ????)</font>| [[5822](http://klog.icrr.u-tokyo.ac.jp/osl/?r=5822)] |
| IP_H2 | (-0.208, -0.208) | (<font color="Red">????</font>, 0) |<font color="Red">(????, ????)</font>| [[5822](http://klog.icrr.u-tokyo.ac.jp/osl/?r=5822)]|
| IP_H3 | (+0.237, +0.237) | (<font color="Red">????</font>, 0) |<font color="Red">(????, ????)</font>| [[5822](http://klog.icrr.u-tokyo.ac.jp/osl/?r=5822),[5829](http://klog.icrr.u-tokyo.ac.jp/osl/?r=5829)]|
| F0_GAS | (<font color="Red">????</font>, -0.300) | (<font color="Red">????</font>, 0) |<font color="Red">(????, ????)</font>| [[5822](http://klog.icrr.u-tokyo.ac.jp/osl/?r=5822)]|
| F1_GAS | (-0.342, -0.342) | (0, 0) |(-1e4, +1e4)| [[5587](http://klog.icrr.u-tokyo.ac.jp/osl/?r=5587)] |
| F2_GAS | (+0.951, <font color="Red">+0.0979</font>) [*1]| (<font color="Red">????</font>, 0) |<font color="Red">(????, ????)</font>| [[5494](http://klog.icrr.u-tokyo.ac.jp/osl/?r=5494)] |
| F3_GAS | (+0.219, +0.219) [*2]| (0, 0) |(-0.8e4, +0.8e4)| [[5325](http://klog.icrr.u-tokyo.ac.jp/osl/?r=5325)]|
| BF_GAS | (+0.452, <font color="Red">+0.321</font>) [*3]| (<font color="Red">????</font>, 0) |<font color="Red">(????, ????)</font>| [[5249](http://klog.icrr.u-tokyo.ac.jp/osl/?r=5249)] |
| BF_H1 | (-0.304, -0.304) | (0, 0) |(-2e4, 2e4)| [[5756](http://klog.icrr.u-tokyo.ac.jp/osl/?r=5756)] |
| BF_H2 | (-0.337, <font color="Red">+0.334</font>) [*4]| (xxxx, 0) |(-2e4, 2e4)| [[5756](http://klog.icrr.u-tokyo.ac.jp/osl/?r=5756)] |
| BF_H3 | (-0.321, -0.320) | (xxxx, 0) |(-2e4, 2e4) | [[5756](http://klog.icrr.u-tokyo.ac.jp/osl/?r=5756)]|
| BF_V1 | (+0.373, +0.374) | (xxxx, 0) |(-2e4, 2e4)| [[5756](http://klog.icrr.u-tokyo.ac.jp/osl/?r=5756)]|
| BF_V2 | (-0.313, <font color="Red">+0.313</font>) [*4]| (xxxx, 0) |(-2e4, 2e4)| [[5756](http://klog.icrr.u-tokyo.ac.jp/osl/?r=5756)] |
| BF_V3 | (-0.323, -0.323) | (xxxx, 0) |(-2e4, 2e4)| [[5756](http://klog.icrr.u-tokyo.ac.jp/osl/?r=5756)]|

1. <font color='Red'>Where should we refer this value?</font> #5494のグラフより、-2.5Vをノミナル位置として±1Vの線形範囲をもつことがわかる。この範囲での係数は0.951 [um/cnt]。だがmedmではは0V位置をノミナルにしているので、この係数は使えない。使うには0V付近でフィッティングした係数を使う必要あり。
2. Use correct c2v.
3. <font color='Red'>Where should we refer this value?</font> According to #5249, value should be +0.452. But, actual value on medm does not same as it.
4. <font color='Red'>Where should we refer this value?</font> According to #5756, value should be "-0.337" and "-0.313" for BF\_H2 and BF\_V2, respectively. But, actual value on medm does not same as these.


### BS
| Item | Gain [um/cnt]<br> (klog, medm)| Offset [cnt] <br> (klog, medm)| Linear Range [cnt] <br>(c\_min, c\_max)|Description |
| :--|:--|:--|:---|:--|
| IP_H1 | (+0.327, +0.327)  | (xxxx, -1122.9) |(-1.5e4, +1.5e4)| [[7656](http://klog.icrr.u-tokyo.ac.jp/osl/?r=7656)] |
| IP_H2 | (+0.299, +0.299)  | (xxxx, -1264.2) |(-1.5e4, +1.5e4)| [[7656](http://klog.icrr.u-tokyo.ac.jp/osl/?r=7656)] |
| IP_H3 | (+0.396, +0.396)  | (xxxx, -868.5) |(-1.0e4, +1.0e4)| [[7656](http://klog.icrr.u-tokyo.ac.jp/osl/?r=7656)] |
| F0_GAS | (+1.116, +1.116)  | (xxxx, +870.0) |(-2000, +2000)| [[7694](http://klog.icrr.u-tokyo.ac.jp/osl/?r=7694)] |
| F1_GAS | (+0.772, +0.771)  | (xxxx, -1090.0) |(+200, +2000)| [[3358](http://klog.icrr.u-tokyo.ac.jp/osl/?r=3358)] |
| BF_GAS | (+0.427, +0.427)  | (xxxx, -350.0) |(-2000, +4000)| [[3280](http://klog.icrr.u-tokyo.ac.jp/osl/?r=3280)] |




### SRM
| Item | Gain [um/cnt]<br> (klog, medm)| Offset [cnt] <br> (klog, medm)| Linear Range [cnt] <br>(c\_min, c\_max)|Description |
| :--|:--|:--|:---|:--|
| IP_H1 | (+0.294, +0.294)  | (xxxx, -373.0) |(-2e4, +2e4)| [[7087](http://klog.icrr.u-tokyo.ac.jp/osl/?r=7087)]|
| IP_H2 | (+0.315, +0.315)  | (xxxx, -1253.0) |(-2e4, +2e4)| [[7087](http://klog.icrr.u-tokyo.ac.jp/osl/?r=7087)]|
| IP_H3 | (+0.317, +0.317)  | (xxxx, -146.0) |(-2e4, +2e4)| [[7087](http://klog.icrr.u-tokyo.ac.jp/osl/?r=7087)]|
| F0_GAS | (-0.186, +0.185)  | (xxxx, +2551.0) |(-1.5e4, +2.5e4)| [[7427](http://klog.icrr.u-tokyo.ac.jp/osl/?r=7427)] [1]|
| F1_GAS | (+0.141, +0.141)  | (xxxx, -4005.0) |(-1.5e4, +2.5e4)| [[4688](http://klog.icrr.u-tokyo.ac.jp/osl/?r=4688)] |
| BF_GAS | (+0.156, +0.156)  | (xxxx, +2058.2) |(-1.5e4, +2.5e4)| [[4688](http://klog.icrr.u-tokyo.ac.jp/osl/?r=4688)] |

1. According to [Issue#7](https://github.com/gw-vis/kagra-vis/issues/7), sign flip is accepted.


### SR2
| Item | Gain [um/cnt]<br> (klog, medm)| Offset [cnt] <br> (klog, medm)| Linear Range [cnt] <br>(c\_min, c\_max)|Description |
| :--|:--|:--|:---|:--|
| IP_H1 | (+0.281, +0.281)  | (xxxx, +2057.0) |(-2e4, +2e4)| [[6078](http://klog.icrr.u-tokyo.ac.jp/osl/?r=6078)] |
| IP_H2 | (+0.306, +0.306)  | (xxxx, -2552.0) |(-2e4, +2e4)| [[6078](http://klog.icrr.u-tokyo.ac.jp/osl/?r=6078)] |
| IP_H3 | (+0.301, +0.301)  | (xxxx, -2022.0) |(-2e4, +2e4)| [[6078](http://klog.icrr.u-tokyo.ac.jp/osl/?r=6078)] |
| F0_GAS | (+0.178, +0.178)  | (xxxx, -10214.0) |(-2e4, +3e4)| [[6080](http://klog.icrr.u-tokyo.ac.jp/osl/?r=6080)] |
| F1_GAS | (+0.090, +0.090)  | (xxxx, -4740.0) |(-2e4, +2e4)| [[4365](http://klog.icrr.u-tokyo.ac.jp/osl/?r=4365)] |
| BF_GAS | (+0.160, +0.160)  | (xxxx, +886.0) |(-1e4, +2e4)| [[4166](http://klog.icrr.u-tokyo.ac.jp/osl/?r=4166)] |


### SR3
| Item | Gain [um/cnt]<br> (klog, medm)| Offset [cnt] <br> (klog, medm)| Linear Range [cnt] <br>(c\_min, c\_max)|Description |
| :--|:--|:--|:---|:--|
| IP_H1 | (+0.262, +0.262)  | (xxxx, -876.4) |(-2e4, +2e4)| [[5551](http://klog.icrr.u-tokyo.ac.jp/osl/?r=5551)]|
| IP_H2 | (+0.240, +0.240)  | (xxxx, -877.8) |(-2e4, +2e4)| [[5551](http://klog.icrr.u-tokyo.ac.jp/osl/?r=5551)]|
| IP_H3 | (+0.253, +0.253)  | (xxxx, -1188.6) |(-2e4, +2e4)| [[5551](http://klog.icrr.u-tokyo.ac.jp/osl/?r=5551)]|
| F0_GAS | (-0.182, +0.181) [*1]  | (xxxx, -677.0) |(-2e4, +2e4)| [[5529](http://klog.icrr.u-tokyo.ac.jp/osl/?r=5529)] |
| F1_GAS | (+0.088, +0.088)  | (xxxx, -1690.0) |(-2e4, +2e4)| [[4650](http://klog.icrr.u-tokyo.ac.jp/osl/?r=4650)] |
| BF_GAS | (+0.055, +0.055)  | (xxxx, -5170.0) |(-2e4, +2e4)| [[4650](http://klog.icrr.u-tokyo.ac.jp/osl/?r=4650)]|

1. According to [Issue#7](https://github.com/gw-vis/kagra-vis/issues/7), sign flip is accepted.


### PRM
| Item | Gain [um/cnt]<br> (klog, medm)| Offset [cnt] <br> (klog, medm)| Linear Range [cnt] <br>(c\_min, c\_max)|Description |
| :--|:--|:--|:---|:--|
| SF_GAS | (+0.251, <font color='Red'>+1.000</font>) [*1] | (????, 0) |(????, ????)| [[8399](http://klog.icrr.u-tokyo.ac.jp/osl/?r=8399)]|
| BF_GAS | (+0.241, +0.241)  | (xxxx, 0) |(-2e4, +2e4)| [[3290](http://klog.icrr.u-tokyo.ac.jp/osl/?r=3290)] |
| BF_H1 | (-0.973, -0.973)  | (xxxx, 0) |(-0.4e4, +0.4e4)| [[2926](http://klog.icrr.u-tokyo.ac.jp/osl/?r=2926)] |
| BF_H2 | (-0.940, -0.940)  | (xxxx, 0) |(-0.5e4, +0.5e4)| [[2926](http://klog.icrr.u-tokyo.ac.jp/osl/?r=2926)] |
| BF_H3 | (-0.945, -0.945)  | (xxxx, 0) |(-0.5e4, +0.5e4)| [[2926](http://klog.icrr.u-tokyo.ac.jp/osl/?r=2926)] |
| BF_V1 |  (+0.941, +0.941)  | (xxxx, 0) |(-0.5e4, +0.5e4)| [[2926](http://klog.icrr.u-tokyo.ac.jp/osl/?r=2926)] |
| BF_V2 |  (-0.956, -0.956)  | (xxxx, 0) |(-0.4e4, +0.4e4)| [[2926](http://klog.icrr.u-tokyo.ac.jp/osl/?r=2926)] |
| BF_V3 |  (-0.954, <font color="Red">+0.954</font>) [*2] | (xxxx, 0) |(-0.5e4, +0.5e4)| [[2926](http://klog.icrr.u-tokyo.ac.jp/osl/?r=2926)]|

1. <font color='Red'>Where should we refer to this value?</font> According to #8399 the calibration factor should be +0.251. But actual value on medm disagree with it. The medm value is not reported on klog.
2. <font color='Red'>Why is the sign reversed?</font> According to #2926, value should be "-0.954". But, actual value on medm does not same as it.


### PR2
| Item | Gain [um/cnt]<br> (klog, medm)| Offset [cnt] <br> (klog, medm)| Linear Range [cnt] <br>(c\_min, c\_max)|Description |
| :--|:--|:--|:---|:--|
| SF_GAS | (-0.322, -0.322)  | (xxxx, 0) |(-0.5e4, 1.0e4)| [[3132](http://klog.icrr.u-tokyo.ac.jp/osl/?r=3132)] |
| BF_GAS | (+0.414, +0.414)  | (<font color='Red'>????</font>, 0) [*1] |<font color='Red'>(????, ????)</font> [*1]| [[3077](http://klog.icrr.u-tokyo.ac.jp/osl/?r=3077)]|
| BF_H1 | (-1.229, <font color='Red'>+1.229</font>) [*2] | (xxxx, +44.1) |(-0.4e4,+0.4e4)| [[2906](http://klog.icrr.u-tokyo.ac.jp/osl/?r=2906)]|
| BF_H2 | (-1.250, <font color='Red'>+1.250</font>) [*2] | (xxxx, +419.2) |(-0.4e4,+0.4e4)| [[2906](http://klog.icrr.u-tokyo.ac.jp/osl/?r=2906)]|
| BF_H3 | (-1.216, -1.216)  | (xxxx, +30.6) |(-0.4e4,+0.4e4)| [[2906](http://klog.icrr.u-tokyo.ac.jp/osl/?r=2906)] |
| BF_V1 | (+1.203, <font color='Red'>-1.202</font>) [*3] | (xxxx, +1103.5) |(-0.5e4,+0.3e4)| [[2906](http://klog.icrr.u-tokyo.ac.jp/osl/?r=2906), [8956](http://klog.icrr.u-tokyo.ac.jp/osl/?r=8956)]|
| BF_V2 | (+1.229, +1.229)  | (xxxx, -516.7) |(-0.4e4,+0.4e4)| [[2906](http://klog.icrr.u-tokyo.ac.jp/osl/?r=2906)] |
| BF_V3 | (+1.224, <font color='Red'>-1.224</font>) [*3] | (xxxx, +142.9) |(-0.4e4,+0.4e4)| [[2906](http://klog.icrr.u-tokyo.ac.jp/osl/?r=2906), [8956](http://klog.icrr.u-tokyo.ac.jp/osl/?r=8956)] |

1. <font color='Red'>Where should we refer this value?</font> I could not find measurement in klog.
2. <font color='Red'>Where should we refer this value?</font> Polarity is changed. And according to [3], BF-H was not changed. These also should be same as #2906.
3. <font color='Red'>Where should we refer this value?</font> Polarity is changed. BF-V do not seem to be changed from the first calibration work in #2906. After this work, at May 22nd 2019, BF-V was renewed as posted in #8956. But, in this modification, BF-V LVDT board was tuned so that transfer function from BF-Vexc to BF-V1/V2/V3 had same amplitude before/after this work. So, BF-V1/V3 should be same as the first work. (Absorute value must be same, but sign may not be.) 



### PR3
| Item | Gain [um/cnt]<br> (klog, medm)| Offset [cnt] <br> (klog, medm)| Linear Range [cnt] <br>(c\_min, c\_max)|Description |
| :--|:--|:--|:---|:--|
| SF_GAS | (+0.337, +0.337)  | (xxxx, 0) |(-1.5e4, +1.0e4)| [[2739](http://klog.icrr.u-tokyo.ac.jp/osl/?r=2739)] |
| BF_GAS | (-0.342, <font color='Red'>+0.342</font>) [*1] | (xxxx, 0) |(-1.5e4,0)| [[2670](http://klog.icrr.u-tokyo.ac.jp/osl/?r=2670)]|
| BF_H1 | (-1.659, -1.658)  | (xxxx, 0) |(-0.4e4, +0.2e4)| [[2627](http://klog.icrr.u-tokyo.ac.jp/osl/?r=2627)] |
| BF_H2 | (-1.645, <font color='Red'>+1.645</font>) [*1] | (xxxx, 0) |(-0.3e4, +0.2e4)| [[2627](http://klog.icrr.u-tokyo.ac.jp/osl/?r=2627)]|
| BF_H3 | (-1.681, <font color='Red'>+1.681</font>)  [*1]| (xxxx, 0) |(-0.35e4, +0.25e4)| [[2627](http://klog.icrr.u-tokyo.ac.jp/osl/?r=2627)] |
| BF_V1 | (+1.722, +1.722)  | (xxxx, 0) |(-0.25e4, +0.25e4)| [[2627](http://klog.icrr.u-tokyo.ac.jp/osl/?r=2627)]|
| BF_V2 | (-1.730, -1.730)  | (xxxx, 0) |(-0.3e4, +0.3e4)| [[2627](http://klog.icrr.u-tokyo.ac.jp/osl/?r=2627)]|
| BF_V3 | (+1.611, +1.611)  | (xxxx, 0) |(-0.3e4, +0.3e4)| [[2627](http://klog.icrr.u-tokyo.ac.jp/osl/?r=2627)]|

1. <font color='Red'>Where should we refer this value?</font> Polarity is changed.





