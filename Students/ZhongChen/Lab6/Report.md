#Lab 6 Report

Zhong Chen

## Background

In this lab,I will complete two designs of a low pass filter and the design of a band stop. I will be designing these for a Z0=50 Ohms reference impedance on the 62 mil thick FR4 substrate.

## Design,Procedure and Results

Task 1: Synthesis and implementation of a maximally-flat low-pass filter. <br>
In this exercise I will synthesize a maximally-flat low-pass filter with a cut-off frequency fc = 2.5GHz and a minimum attenuation of 10 dB at 3.25 GHz.<br>

Step 1: First, calculate the order N of the filter required to meet the specification of providing 10 dB isolation at 3.25 GHz.<br>

abs(w/wc)-1 = abs(3.25/2.5)-1 = 0.3, then check the figure, we can obtain N = 5.<br>

Step 2: Next, use the Butterworth(Maximally Flat) Low-Pass Filter Prototypes table to determine the filter coefficients. <br>

For N = 5, g1 = 0.6180,g2 = 1.6180,g3 = 2.0000, g4 = 1.6180, g5 = 0.6180, g6 = 1.0000. <br>

Step 3: Assemble the prototype LC ladder network. <br>

Step 4: Use Richard¡¯s Transformation to convert the capacitors into open circuit stubs and the inductors into short circuit stubs. <br>

Step 5: Use Kuroda¡¯s identities to convert series stubs to shunt stubs. This is a multi-step process, but the filter coefficients are symmetric in so we only need to transform one side of the filter and then capitalize on the symmetry. This will begin at the load and/or source side and work to the center of the filter (note: the center element is a shunt open-circuit stub, so it will remain untouched in this process). <br> 

Step 5.1: Insert unit elements source and load sides of the circuit to separate z1 from z2 and z5 from z4.<br>

Step 5.2: Insert two more unit element source and load sides of the circuit. This will separate z2 from z3 and z4 from z3, then separate z4 from z5 and z1 from z2. This process will also convert z1, z2, z4, and z5 into shunt OC stubs.<br>

Step 5.3: Perform impedance scaling for the transmission line. <br>

Step 6: Calculate the widths of the transmission lines and enter these into the design ¡°N5_MaxFlat_LPF_T-Line¡± within the HFSS project ¡°ECEN452_Lab6_Filters.hfss¡±. You will also need to enter this information into the ¡°N5_MaxFlat_LPF_T-Line.zov¡± Z0lver assignment.<br>

The original design parameters are shown in the following figure. Obviously,the results do not meet the requirement fully. 

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/ZhongChen/Lab6/MaxFlat_LPF_T-Line_Final_Parameters.png) (br)

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/ZhongChen/Lab6/LPF_1.png) (br)

After some tuning work, the new design parameters are illustrated below and also the results.


![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/ZhongChen/Lab6/MaxFlat_LPF_T-Line_Final_Parameters.png) (br)

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/ZhongChen/Lab6/LPF_S11_dB.png) (br)

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/ZhongChen/Lab6/LPF_S21_dB.png) (br)

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/ZhongChen/Lab6/LPF_S11_Phase.png) (br)

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/ZhongChen/Lab6/LPF_S21_Phase.png) (br)


Step 7: Perform impedance and frequency scaling for the lumped element prototype I found in Step 2 and enter these into the ¡°N5_MaxFlat_LPF_LC.zov¡± Z0lver assignment.<br>

For n = 5, g1 = 0.6180, g2 = 1.6180, g3 = 2.0000, g4 = 1.6180, g5 = 0.6180, g6 = 1.0000<br>
impedance scaling:<br>
Rs = 50, RL = 50, C1 = 0.618/50 = 0.01236, L2 = 50 * 1.618 = 80.9, C3 = 2/50 = 0.04, L4 = 80.9, C5 = 0.01236<br>
Frequency Scaling:<br>
C1' = C5' = C1/w_c = 0.01236/(2 * pi * 2.5 * 10^9) = 0.787 pF<br>
L2' = L4' = L2/w_c = 80.9/(2 * pi * 2.5 * 10^9) = 5.15 nH<br>
C3' = 0.04/(2 * pi * 2.5 * 10^9) = 2.55 pF<br>

Step 8: Calculate the values x1, x2, x3, x4, and x5 (e.g., the electrical length of the stubs) for the modified low pass filter design ¡°N5_MaxFlat_LPF_T-Line_Tapped_Stubs¡± that uses tapped stubs with a 1 mm width (Z0 = 89 W).<br>

For Z_in_x1 = -362j, characteristic impedance of x1 = 89 Ohm, l_x1 = 0.038, lambda/4 = 17.56388, L1 = l_x1*lambda = 2.6693 mm<br>
L1 = L5; <br>
for Z_in_x2 = -86j, characteristic impedance of x2 = 89 Ohm, l_x2 = 0.1277, lambda/4 = 17.56388, L2 = l_x2*lambda = 8.9703 mm<br>
L2 = L4; <br>
for Z_in_x3 = -50j, characteristic impedance of x3 = 89 Ohm, l_x3 = 0.1685, lambda/4 = 17.56388, L3 = l_x3*lambda = 11.8363 mm<br>

The design parameters and results are shown in the following figures.<br>

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/ZhongChen/Lab6/MaxFlat_LPF_T-Line_tap__Original_Parameters.png) (br)

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/ZhongChen/Lab6/LPF_Tap_dB.png) (br)

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/ZhongChen/Lab6/LPF_Tap_phase.png) (br)

Task 2: Synthesis and implementation of an equi-ripple band-stop filter.<br>
In this exercise I will synthesize a fifth-order 0.5 dB equi-ripple band-pass filter with a center frequency fc = 3.0 GHz and a bandwidth of 2.25 GHz to 3.75 GHz (e.g., delta = 0.5), and then implement my design using microstrip transmission lines for a Z0 = 50 Ohm reference impedance on a 62 mil thick FR4 (er = 4.1, tan_d = 0.01). <br>

Step 1: First, use the 0.5 dB Ripple table to determine the element values of the low pass prototype.<br>

Step 2: Assemble the prototype LC ladder network.<br>

Step 3: Convert this to a band-stop filter topology by replacing shunt elements with shunted LC series networks, and series LC parallel networks.<br>

Step 4: Use inverters (e.g., quarter-wave transformers) to provide separation between the series elements and convert series stubs into shunt stubs. <br>

Step 5: Calculate the scaled impedance values of the equivalent open-circuit stubs using <br>

The design parameters are shown in the following figures.<br>

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/ZhongChen/Lab6/BSF_T-Line_tap__Original_Parameters.png) (br)

The HFSS simulation results are as follows.

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/ZhongChen/Lab6/BSF_S11_dB.png) (br)

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/ZhongChen/Lab6/BSF_S21_dB.png) (br)

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/ZhongChen/Lab6/BSF_S11_phase.png) (br)

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/ZhongChen/Lab6/BSF_S21_phase.png) (br)

## Conclusion
The LPF simulation results are acceptable. However, for the BSF, the simulation results are appropriate to the copper taped results, but a little far from the milled results.

## Reflection
The most difficult part of this lab was just the fine tunning of the simulations because one small change sometimes gave different results that made sense but at other times they would not. However, once that was overcame it was rewarding to learn the beginning steps of the whole design and testing process.<br>


