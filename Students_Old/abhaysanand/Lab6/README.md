# Lab 6 Report
Abhay Shankar Anand

## Background
Lab 6 consists of the design and analysis of microstrip Low Pass Filters and Band Stop Filters

1. __Low Pass Filters:__ There are two types of LPFs that are designed in this exercise, viz., standard T-Line LPF and a Balanced Stub T-Line LPF; both of which are designed to be Butterworth (Maximally Flat) filters.
2. __Band Pass Filters:__ An Equi-Ripple BSF is implemented in this exercise

## Design
### LPF Design
#### Given constraints
* __Z<sub>0</sub>__ = 50 &#937;
* __&#949;<sub>r</sub>__ = 4.1
* __FR4 thickness__ = 62 mils = 1.5748 mm
* __Freq Range__ = 1 GHz to 5 GHz
* __f<sub>c</sub>__ = 2.5 GHz
* __Attenuation__ = minimum of 10dB at 3.25 GHz
* __Reference Plane__ = 15 mm from edge

### BSF Design
#### Given constraints
* Fifth order 0.5 dB equi-ripple BSF
* __Z<sub>0</sub>__ = 50 &#937;
* __&#949;<sub>r</sub>__ = 4.1
* __FR4 thickness__ = 62 mils = 1.5748 mm
* __Freq Range__ = 1 GHz to 5 GHz
* __f<sub>c</sub>__ = 3 GHz
* __Bandwidth:__ 1.5 GHz (2.25 GHz to 3.75 GHz)
* __Reference Plane__ = 15 mm from edge

### Procedure
#### LPF Design

1. Given the constraint that we need 10 dB attenuation at 3.25 GHz, we determine the order of the filter using the relation:<br>
**|&#969;/&#969;<sub>c</sub>| - 1 = |f<sub>10dB</sub>/f<sub>c</sub>| - 1**
2. From the graph given the instructions PDF, we find that **N = 5** curve closely satisfies this relation at 10dB. Hence, a 5 order filter is the objective of this lab exercise.
3. Next, we are to determine the filter coefficients for a fifth order Butterworth LPF. From the table, we obtain the following values:<br>
**g<sub>1</sub> = 0.6180**<br>
**g<sub>2</sub> = 1.6180**<br>
**g<sub>3</sub> = 2.0000**<br>
**g<sub>4</sub> = 1.6180**<br>
**g<sub>5</sub> = 0.6180**<br>
**g<sub>6</sub> = 1.0000**
4. With these element values, we construct an LC filter ladder network consisting of **shunt C1, series L2, shunt C3, series L4 and shunt C5**, in that order from generator to load.
5. Using **Richardson's Transformation**, these lumped components are converted to T-Line elements with Open Circuit (OC) for capacitances and Short Circuit (SC) for inductances.
6. Using **Unit Elements** and **Kuroda's Identities**, the Series SCs are converted Shunt OCs (which are easier and more feasible to design on microstrip patch).
7. Once these conversions are complete, we are left with five Shunt OCs, each separated by Unit Elements with varying characteristic impedences, although symmetric w.r.t. center element.
8. The obtained element values are then scaled to **Z<sub>0</sub>** and each of the impedences are obtained.
9. Given this design, we extend this to implement Balanced Stub LPF.
10. We know the impedences of each of the Shunt elements and we are required to design each of the balanced stubs with a __Z<sub>0</sub>__ = 89 &#937;. We use the following relation:<br>
__Z<sub>oc</sub> = -j Z<sub>0</sub> cot(&#946;l)__<br>
__-j . 2 . 181 &#937; = -j . 89 . cot(&#946;l)__<br>
__tan(&#946;l) = 89/362__<br>
__2&#960;/&#955; . x&#955; = tan<sup>-1</sup>(89/362)__<br>
__&#8756; x<sub>1</sub> = 0.0383 = x<sub>5</sub>__<br>
This same process is followed for each of the other balanced stub. These x represent the length of each stubs normalized to &#955;.
11. These widths and length are entered for both the designs in HFSS and the simulated results are obtained.

#### BSF Design

1. With the 0.5 dB Ripple filter table given in the instructions PDF, we obtain the element values for a fifth order filter.<br>
**g<sub>1</sub> = 1.7058**<br>
**g<sub>2</sub> = 1.2296**<br>
**g<sub>3</sub> = 2.5408**<br>
**g<sub>4</sub> = 1.2296**<br>
**g<sub>5</sub> = 1.7058**<br>
**g<sub>6</sub> = 1.0000**
2. Just as performed in the LPF, an LC Ladder network is used which is then transformed into Shunted Series LC network for Shunt C and Series Parallel LC network for Series L elements.
3. Inverters, in the form of quarter wave transformers (as they essentially transform L to C and vice versa) are used to convert series stubs into shunt stubs.
4. We, therefore, obtain five Shunt OCs of different impedences, each separated by quarter wave transformers of __Z<sub>0</sub>__ impedence
5. All of the Shunt OC stubs are of length 0.25 &#955;.
6. These widths and lengths are enteren in HFSS and simulated results are obtained.

## Results and Discussion
### Results
#### LPF Designs
**Standard LPF Design**
![LPF HFSS](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/abhaysanand/Lab6/results/LPF_HFSS.png)

**Balanced Stub LPF Design**
![Balanced Stub LPF HFSS](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/abhaysanand/Lab6/results/LPF_TappedStub_HFSS.png)

**Comparison of S11 and S21 between Simulated and Measured**
![LPF Python](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/abhaysanand/Lab6/results/LPF_Python.png)

#### BSF Design
**BSF Design**
![BSF HFSS](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/abhaysanand/Lab6/results/BSF_HFSS.png)

**Comparison of S11 and S21 between Simulated and Measured**
![BSF Python](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/abhaysanand/Lab6/results/BSF_Python.png)

### Observations
1. The Balanced Stub gave a much better filter response (conforming to the 10dB requirement) when compared to the standard LPF design. One main reason for this is due the low impedences used in the standard LPF design. As the impedences are as low as 25 &#937;, the width is large, thus affecting the effective lengths of unit elements. In the balanced stubs, however, all of the stub impedences are constant and greater than __Z<sub>0</sub>__, therefore having a small width and giving a constant length for inverters.
2. The frequency response of the copper tape BSF is slightly left shifted. This could be due excess lengths of stubs and strip lines of the copper tape.

## Conclusion
1. From simulation and hardware realization of LPF, we can conclude that a balanced stub LPF has much better performance when compared to standard LPF (greater symmetry always triumphs :) )
2. The simulated results of BSF are in close conformance with the milled data and bandwidth requirements have been met inspite of the slight shift in the center frequency of result.

## Hindsight
This lab helped me understand the use of Richardson's Transformations and Kudora's Identities to design a "good enough" filter. This lab could have also had a small description about the working of slot filters and their advantages/disadvantages over these filters.
