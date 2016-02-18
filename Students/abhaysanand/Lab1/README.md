# Lab 1 Report
## 1. Python Test
Python environment has been setup. CSV import and MatPlotLib are functional.
![Python Test Image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/abhaysanand/Lab1/results/CSVPlotter_Result.jpeg)

## 2. GitHub Account
Account created - [abhaysanand](https://github.com/abhaysanand)

## 3. HFSS & Z0lver
HFSS and Z0lver files have been downloaded from Resources folder and simulations have been executed.

**HFSS Files:**
![HFSS Model] (https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/abhaysanand/Lab1/results/HFSS_Model.jpg)
![HFSS Simulation S11] (https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/abhaysanand/Lab1/results/HFSS_S11.jpg)
![HFSS Simulation S21] (https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/abhaysanand/Lab1/results/HFSS_S21.jpg)

**Z0lver Files:**
![Z0lver A with Result](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/abhaysanand/Lab1/results/Z0lver_1.png)
![Z0lver B with Result](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/abhaysanand/Lab1/results/Z0lver_2.png)

## 4. Two-Port S & ABCD Matrix for Series Impedence Z = 10 + j25 &#937;
* S11 = S22 = 0.24&#8736;55.39&#176; ( Z/(Z+2Z0) )
* S12 = S21 = 0.89&#8736;-12.84&#176; ( 2Z/(Z+2Z0) )

S | Port 1 | Port 2
------ | ------- | -------
**Port 1** | 0.24&#8736;55.39&#176; | 0.89&#8736;-12.84&#176;
**Port 2** | 0.89&#8736;-12.84&#176; | 0.24&#8736;55.39&#176;

ABCD | V Out | I Out
------ | ------- | -------
**V In** | 1 | 26.93&#8736;68.20&#176;
**I In** | 1 | 0

## 5. Shift reference plane: *L1* = 0.8&#955; and *L2* = 0.25&#955;
* &#952;1 = &#946; *L1* = 2&#960;*0.8 = 1.6&#960; = 288&#176;
* &#952;2 = &#946; *L2* = 2&#960;*0.25 = 0.5&#960; = 90&#176;

The shift in reference planes will affect only the angle of each of the S paremeters. The magnitude will remain unaffected.
* S11 is shifted by -2*&#952;1 = -2 * 288&#176; &#8801; 144&#176;
* S12 and S21 are shifted by -(&#952;1 + &#952;2) = -(288&#176; + 90&#176;) &#8801; -18&#176;
* S22 is shifted by -2*&#952;2 = -2 * 90&#176; &#8801; -180&#176;

S | Port 1 | Port 2
------ | ------- | -------
**Port 1** | 0.24&#8736;-160.61&#176; | 0.89&#8736;-30.8&#176;
**Port 2** | 0.89&#8736;-30.8&#176; | 0.24&#8736;-124.61&#176;

## 6. Comparison of S11 & S21 (Analytical, HFSS and Z0lver)
![S11 Comparison](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/abhaysanand/Lab1/results/S11Comparison.jpeg)
![S21 Comparison](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/abhaysanand/Lab1/results/S21Comparison.jpeg)

## 7. Substrates, their Relative Permittivities and Dielectric Losses
Substrate | Fr4 | Duroid 5880 | Duroid 6006 | Duroid 6010.2
--------- | --- | ----------- | ----------- | -------------
**&#949;r** | 4.8 | 2.2 | 6.45 | 10.7
**tan &#948;** | 0.017 | 0.0004 | 0.0027 | 0.023

## 8. Connector types and mating configurations
Connectors | Type N | SMA | 3.5 mm | 2.92 mm | 2.4 mm | 1.85 mm
---------- | ------ | --- | ------ | ------- | ------ | -------
**Type N** | **Y** | N | N | N | N | N
**SMA** | N | **Y** | **Y** | **Y** | N | N
**3.5 mm** | N | **Y** | **Y** | **Y** | N | N
**2.92 mm** | N | **Y** | **Y** | **Y** | N | N
**2.4 mm** | N | N | N | N | **Y** | **Y**
**1.85 mm** | N | N | N | N | **Y** | **Y**
