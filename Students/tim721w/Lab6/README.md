#Lab 6 Report

Chung-Huan Huang

## Background
Two designs of low pass filter and band stop filter will be simulated and band stop filter will be implemented on substrate FR4. The results are conducted within the report. <br>

## Design,Procedure and Results

Task 1: Synthesis and implementation of a maximally-flat low-pass filter. <br>
In this exercise, a maximally-flat low-pass filter with a cut-off frequency fc = 2.5GHz and a minimum attenuation of 10 dB at 3.25 GHz was conducted.<br>

Step 1: First, calculate the order N of the filter required to meet the specification of providing 10 dB isolation at 3.25 GHz.<br>
Ans: abs(w/wc)-1 = abs(3.25/2.5)-1 = 0.3 <br>
     It can be found out that N = 5 from attenuation figure. <br>

Step 2: Next, use the Butterworth(Maximally Flat) Low-Pass Filter Prototypes table to determine the filter coefficients. <br>
Ans: For N = 5, coefficients are chosen as following: <br>
     g1 = 0.6180, g2 = 1.6180, g3 = 2.0000, g4 = 1.6180, g5 = 0.6180, g6 = 1.0000 <br>

Step 3: Assemble the prototype LC ladder network. <br>
Ans: In order to simplify the ladder network, the network is replaced by table shown in Lab6 manual.<br>

Step 4: Use Richard's Transformation to convert the capacitors into open circuit stubs and the inductors into short circuit stubs. <br>
Ans: Open circuit stubs and short circuit stubs are transformed in Lab6 manual. <br>

Step 5: Use Kuroda's identities to convert series stubs to shunt stubs. This is a multi-step process, but the filter coefficients are symmetric in so we only need to transform one side of the filter and then capitalize on the symmetry. This will begin at the load and/or source side and work to the center of the filter (note: the center element is a shunt open-circuit stub, so it will remain untouched in this process). <br> 
Step 5.1: Insert unit elements source and load sides of the circuit to separate z1 from z2 and z5 from z4.<br>
Step 5.2: Insert two more unit element source and load sides of the circuit. This will separate z2 from z3 and z4 from z3, then separate z4 from z5 and z1 from z2. This process will also convert z1, z2, z4, and z5 into shunt OC stubs.<br>
Step 5.3: Perform impedance scaling for the transmission line. <br>
Ans: By going through process from Step 5.1 to Step 5.3, impedance scaling for the transmission is shown in the following table: <br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/tim721w/Lab6/imped_scaling_Task1.png)<br>

Step 6: Calculate the widths of the transmission lines and enter these into the design “N5_MaxFlat_LPF_T-Line” within the HFSS project “ECEN452_Lab6_Filters.hfss”. You will also need to enter this information into the “N5_MaxFlat_LPF_T-Line.zov” Z0lver assignment.<br>
Ans: Calculate widths of the transmission using Microstrip line Calculator (http://www1.sphere.ne.jp/i-lab/ilab/tool/ms_line_e.htm), and input parameters into "N5_MazFlat_LPF_T-Line" HFSS file. <br>
     Parameters are shown in the following table: <br>
     
     Name   Value	     Name   Value    	     Name   Value           Name    Value <br>
     W0	    3.127929688	     L1     8.635694914      wUE1   0.53918457      UE_L1   8.897579027<br>
     W1     0.084247589	     L2	    8.635694914      wUE2   0.53918457	    UE_L2   8.897579027<br>
     W2     3.961914063      L3     8.635694914	     wUE3   1.75921631      UE_L3   8.897579027<br>
     W3     8.396484375      L4     8.635694914      wUE4   1.75921631	    UE_L4   8.897579027<br>
     W4	    3.961914063      L5     8.635694914<br>				
     W5     0.084247589<br>						
  ![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/tim721w/Lab6/N5_MaxFlat_LPF_T-Line_S1_S21_dB.PNG) (br)
  ![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/tim721w/Lab6/N5_MaxFlat_LPF_T-Line_S1_S21_phase.PNG) (br)

Step 7: Perform impedance and frequency scaling for the lumped element prototype I found in Step 2 and enter these into the "N5_MaxFlat_LPF_LC.zov" Z0lver assignment.<br>
Ans: From Step 2, coefficients can be determined as g1 = 0.6180, g2 = 1.6180, g3 = 2.0000, g4 = 1.6180, g5 = 0.6180, g6 = 1.0000 (N = 5) <br>
     
     For impedance scaling:<br>
	C1' = C5' = C1/(w_c*RL) = 0.618/(2*pi*2.5*10^9*50) = 0.78686 pF<br>
	L2' = L4' = L2*RL/w_c = 80.9*50/(2*pi*2.5*10^9) = 5.15035 nH<br>
	C3' = 2/(2*pi*2.5*10^9*50) = 2.54648 pF<br>
     S parameters will be plotted and compared with Step 8.

Step 8: Calculate the values x1, x2, x3, x4, and x5 (e.g., the electrical length of the stubs) for the modified low pass filter design "N5_MaxFlat_LPF_T-Line_Tapped_Stubs” that uses tapped stubs with a 1 mm width (Z0 = 89 ohm).<br>
Ans: The electrical lengths of the open stubs can be calculated using following formula:<br>
     ![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/tim721w/Lab6/Task1_Step8_length_calculated.PNG) <br>

     The lengths are:<br>
     l_x1 = 0.03837 = 2.69531 mm <br>
     l_x2 = 0.12773 = 8.97242 mm <br>
     l_x3 = 0.16854 = 11.83912 mm <br>
     l_x4 = 0.12773 = 8.97242 mm <br>
     l_x5 = 0.03837 = 2.69531 mm <br>

  ![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/tim721w/Lab6/N5_MaxFlat_LPF_LC_T-Line_Tapped_Stubs_S11_S21_dB.PNG) <br>

  ![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/tim721w/Lab6/N5_MaxFlat_LPF_LC_T-Line_Tapped_Stubs_S11_S21_phase.PNG) <br>

Task 2: Synthesis and implementation of an equi-ripple band-stop filter.<br>
In this exercise, I will synthesize a fifth-order 0.5 dB equi-ripple band-pass filter with a center frequency fc = 3.0 GHz and a bandwidth of 2.25 GHz to 3.75 GHz (e.g., delta = 0.5), and then implement my design using microstrip transmission lines for a Z0 = 50 Ohm reference impedance on a 62 mil thick FR4 (er = 4.1, tan_d = 0.01). <br>

Step 1: First, use the 0.5 dB Ripple table to determine the element values of the low pass prototype.<br>
Ans: For N = 5, we get g1 = 1.7058, g2 = 1.2296, g3 = 2.5408, g4 = 1.2296, g5 = 1.7058, g6 = 1.0000 <br>

Step 2: Assemble the prototype LC ladder network.<br>
Ans: The LC ladder network is shown in Lab6 manual.<br>

Step 3: Convert this to a band-stop filter topology by replacing shunt elements with shunted LC series networks, and series LC parallel networks.<br>
Ans: The topology is shown is Lab6 manual.<br>

Step 4: Use inverters (e.g., quarter-wave transformers) to provide separation between the series elements and convert series stubs into shunt stubs. <br>
Ans: The stubs are shown is Lab6 manual.<br>

Step 5: Calculate the scaled impedance values of the equivalent open-circuit stubs using <br>
Ans: By using equation, <br>
     ![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/tim721w/Lab6/Task2_Step5_impedance.PNG) <br>
     Impedances are calculated as following:<br>
     z1 = 75 ohm<br>
     z2 = 104 ohm<br>
     z3 = 50 ohm<br>
     z4 = 104 ohm<br>
     z5 = 75 ohm<br>

  ![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/tim721w/Lab6/N5_MaxFlat_BSF_T-Line_S11_S21_dB.PNG)<br>
  ![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/tim721w/Lab6/N5_MaxFlat_BSF_T-Line_S11_S21_phase.PNG)<br>

## Conclusion
In this lab, I learn how to design filters on microstrip line, among them are LPF and BSF. Furthermore, I also learn how to fabricate my design and understand more the process of implementing a filter. Although the simulated results are not exactly the same as hardware design, and this may due to measurement error, hand made error, I still gain a lot of knowledge from this lab.  

## Hindsight
I wish I could have more time doing calculation before starting the Lab. That can make the troubleshooting more easily if all the parameters are more precisely.

## Reflection
The most challenging part of the lab was theoretical calculation. However, doing step by step makes me feel it's not quite hard.<br> 
Furthermore, there are some contents should be corrected in Lab6 manual: N1 should be corrected as 1+z1/ue1, N2 should be corrected as 1+z5/ue2 in Step 5.1 and N3 should be corrected as 1+ue3/z1', N4 should be corrected as 1+ue4/z5', N5 should be corrected as 1+ue1'/z2, N6 should be corrected as 1+ue2'/z4.

