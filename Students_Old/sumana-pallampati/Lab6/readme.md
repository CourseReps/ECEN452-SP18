# Lab 6 Report
Sumana Pallampati

## Background
* Low Pass Filter - It allows all frequencies below the cutoff frequency to pass through it.
* High Pass Filter - It allows all frequencies above the cutoff frequency to pass through.
* Band Pass Filter - It allows all frequencies lying in the range of a low cutoff frequency and high cutoff frequency to pass through.
* Band Stop Filter - It does not allow frequencies lying in the range of a low cutoff frequency and high cutoff frequency to pass through.

We studied low pass and band stop filters in this lab.

## Design
All the designs are impelmented on 62 mil FR 4 with eps_r = 4.1, tan delta = 0.01
1. A fifth order maximally flat lowpass filter with a cutoff frequency of 2.5 GHz and a minimum attenuation of 10 dB at 3.25 GHz was designed. The lengths and widths of the shunt open circuit stubs and unit elements were obtained as follows -

* 181 ohms stub - w=0.06 mm; l=9.3 mm
* 69 ohms UE - w=1.73 mm; l=8.66 mm
* 43 ohms stub - w=3.93 mm; l=8.37 mm
* 112 ohms UE - w=0.517 mm; l=8.9635 mm
* 25 ohms stub - w=8.371 mm; l=8.051 mm 

The lengths of all the stubs were modified to 12.75 mm to get a 3dB cutoff frequency at 2.5 GHz.

2. For the tapped stub design, the width of all the open circuit shunt stubs is 1 mm (89 ohms). The lengths are obtained using the formula (z_oc=z_0/2*cot(2*pi*l/lambda)) and tabulated below-

* Shunt OC stub 1 - l=2.7039 mm
* 69 ohms UE - w=1.73 mm; l=8.66 mm
* Shunt OC stub 2 - l=9.01734 mm
* 112 ohms UE - w=0.517 mm; l=8.9635 mm
* Shunt OC stub 3 - l=11.89827 mm 

3. A fifth-order 0.5 dB equi-ripple band-stop filter with a center frequency fc = 3.0 GHz and a bandwidth of 2.25 GHz to 3.75 GHz.
The lengths of the stubs are as follows - 

* 75 ohms stub - w=1.454 mm; l=14.61 mm
* 50 ohms inverter - w=3.1 mm; l=14.07 mm
* 104 ohms stub - w=0.648 mm; l=14.85 mm

The lengths of all the stubs were increased to 15 mm to get a desired response in HFSS.

## Procedure
We measured the magnitude and phase of S11 and S21 milled version of tapped stub low pass filter and band stop filter in the lab. We also designed a copper tape version of the band stop filter. For this, we first measured the S11 and S21 of a 50 ohm line on FR 4 board. Then we cut the stubs of required lengths and widths and created the filter. The lengths and widths were obtained using the online microstrip line calculator. We soldered at the joint between the stub and the 50 ohm line. We soldered the connectors on both the ports. We measured the S21 and S11 of the filter to get the filter response.

## Results and Discussion
![Plot_Name](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/sumana-pallampati/Lab6/S11_LPF.png)
![Plot_Name](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/sumana-pallampati/Lab6/S21_LPF.png)
![Plot_Name](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/sumana-pallampati/Lab6/S11_phase_LPF.png)
![Plot_Name](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/sumana-pallampati/Lab6/S21_phase_LPF.png)
![Plot_Name](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/sumana-pallampati/Lab6/S11_dB_BSF.png)
![Plot_Name](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/sumana-pallampati/Lab6/S21_BSF.png)
![Plot_Name](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/sumana-pallampati/Lab6/S11_phase_BSF.png)
![Plot_Name](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/sumana-pallampati/Lab6/S21_phase_BSF.png)

The copper tape design got its minimum S21 at 3.4 GHz which is off by 0.4 GHz and this can be attributed to the inaccuracy in measuring and cutting of the copper tape. The milled design has its minimum at 2.7 GHz. This can be due to the inaccuracy in the FR4 board. The milled LPF has its cut off at 3.5 GHz. This can be due to the inaccuracy in HFSS simulation and due to other external factors. The phases of the designs dont match as it depends on the reference plane from which we start measuring and they might be different.

## Conclusion
We got a fair understanding of how a microstrip design of low pass and band stop filters work and the step by step design process. 

## Hindsight 
I understood the design process better after completing the lab and it would have been better if we could design the filter on our own.

## Reflection
The most challenging part were the issues with copper tape while fabricating the design. It also took a lot of time to arrive at the optimized design solution (lengths of the stubs) in HFSS for the low pass filter design.

