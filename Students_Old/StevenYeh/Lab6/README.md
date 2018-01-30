<b>ECEN 452-500: Ultra High Frequency Techniques</b><br>
Spring 2016 – Prof. Huff<br>
Lab 6

Pull the Lab 6 subdirectory in the ECEN 452 GitHub directory Labs and locate the HFSS project files “ECEN452_Lab6_Filters.hfss”. Open each project file (File-Open…), then save them to the local drive of the computer you are running your simulations on and rename it by appending your team number to each file (e.g., “ECEN452_LabX_TopicY_TeamZ”).<br>
In this lab you will be completing two designs of a low pass filter and the design of a band stop. These are found in your “ECEN452_Lab6_Filters_GroupX.hfss” project file. These design files are named “N5_MaxFlat_LPF_T-Line”, “N5_MaxFlat_LPF_TLine_Tapped”, and “N5_MaxFlat_BSF_T-Line”. You will be designing these for a Z0 = 50 Ohm reference impedance on the 62 mil thick FR4 (er = 4.1, tan_d = 0.01) substrate.<br>
Task 1: Synthesis and implementation of a maximally-flat low-pass filter.<br>
In this exercise you will synthesize a maximally-flat low-pass filter with a cut-off frequency fc = 2.5 GHz and a minimum attenuation of 10 dB at 3.25 GHz.<br>
<br>Step 1: First, calculate the order N of the filter required to meet the specifications of providing 10 dB isolation at 3.25 GHz using abs(w/w_c)-1 = abs(f_10dB/f_c)-1 and the figure below.<br>
<b>Ans:<br>
abs(w/w_c) - 1= abs(3.25-2.5) - 1 = 0.3<br>
After check the table, n = 5 can provide at leat 10 dB attenuation at 3.25 GHz.<br></b>

<br>Step 2: Next, use the table on the following page to determine the filter coefficients for the (hint: five-element) low-pass prototype.<br>
<b>Ans:<br>
For n = 5, g1 = 0.6180, g2 = 1.6180, g3 = 2.0000, g4 = 1.6180, g5 = 0.6180, g6 = 1.0000<br></b>

<br>Step 3: Assemble the prototype LC ladder network.
To simplify the analysis (visually), we will replace this ladder network will the table shown below.



<br>Step 4: Use Richard’s Transformation to convert the capacitors into open circuit stubs and the inductors into short circuit stubs.



<br>Step 5: Use Kuroda’s identities to convert series stubs to shunt stubs. This is a multi-step process, but the filter coefficients are symmetric in so we only need to transform one side of the filter and then capitalize on the symmetry. This will begin at the load and/or source side and work to the center of the filter (note: the center element is a shunt open-circuit stub, so it will remain untouched in this process).


<br>Step 5.1 Insert unit elements source and load sides of the circuit to separate z1 from z2 and z5 from z4.


<br>Step 5.2 Insert two more unit element source and load sides of the circuit. This will separate z2 from z3 and z4 from z3, then separate z4 from z5 and z1 from z2. This process will also convert z1, z2, z4, and z5 into shunt OC stubs.


<br>Step 5.3 Perform impedance scaling for the transmission line.


<br>Step 6: Calculate the widths of the transmission lines and enter these into the design “N5_MaxFlat_LPF_T-Line” within the HFSS project “ECEN452_Lab6_Filters.hfss”. You will also need to enter this information into the “N5_MaxFlat_LPF_T-Line.zov” Z0lver assignment.<br>
<b>Ans:<br>
The original design parameters are shown in the following figures. Obviously, the results doesn't meet the requirement.<br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/StevenYeh/Lab6/maximally_flat_parameter.jpg)<br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/StevenYeh/Lab6/original_maximally_flat_tline_amp_S11_S21.jpg) <br><br>
Also, the Zolver design layout and simulation results are shown in the following figures.<br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/StevenYeh/Lab6/N5_MaxFlat_LPF_Tline_Design.jpg)<br><br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/StevenYeh/Lab6/N5_MaxFlat_LPF_Tline_Result.jpg)<br><br><br>
After some tuning works, the new design parameters are illustrated below and also the results.<br>
The new Z1 = 80.9 (lumda/8 = 8.7278mm), UE3 = 130.9 (lumda/8 = 8.9679mm), Z2 = 80.9 (lumda/8 = 8.7278mm), UE1 = 50 (lumda/8 = 8.4416mm), Z3 = 25 (lumda/8 = 8.04mm), UE2 = 130.9 (lumda/8 = 8.9679mm), Z4 = 80.9 (lumda/8 = 8.7278mm), UE4 = 50 (lumda/8 = 8.4416mm), Z5 = 80.9 (lumda/8 = 8.7278mm) (Ohm)<br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/StevenYeh/Lab6/maximally_flat_tline_parameters.jpg)<br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/StevenYeh/Lab6/maximally_flat_tline_amp_S11.jpg) <br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/StevenYeh/Lab6/maximally_flat_tline_amp_S21.jpg) <br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/StevenYeh/Lab6/maximally_flat_tline_phase_S11.jpg) <br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/StevenYeh/Lab6/maximally_flat_tline_phase_S21.jpg) <br></b>

<br>Step 7: Perform impedance and frequency scaling for the lumped element prototype you found in Step 2 and enter these into the “N5_MaxFlat_LPF_LC.zov” Z0lver assignment.<br>
<b>Ans:<br>
For n = 5, g1 = 0.6180, g2 = 1.6180, g3 = 2.0000, g4 = 1.6180, g5 = 0.6180, g6 = 1.0000<br>
impedance scaling:<br>
Rs = 50, RL = 50, C1 = 0.618/50 = 0.01236, L2 = 50 * 1.618 = 80.9, C3 = 2/50 = 0.04, L4 = 80.9, C5 = 0.01236<br>
Frequency Scaling:<br>
C1' = C5' = C1/w_c = 0.01236/(2 * pi * 2.5 * 10^9) = 0.787 pF<br>
L2' = L4' = L2/w_c = 80.9/(2 * pi * 2.5 * 10^9) = 5.15 nH<br>
C3' = 0.04/(2 * pi * 2.5 * 10^9) = 2.55 pF<br><br>
The Zolver design layout and simulation results are shown in the following figures.<br></b>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/StevenYeh/Lab6/N5_MaxFlat_LPF_LC_Design.jpg)<br><br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/StevenYeh/Lab6/N5_MaxFlat_LPF_LC_Result.jpg)<br><br><br>
<br>Step 8: Calculate the values x1, x2, x3, x4, and x5 (e.g., the electrical length of the stubs) for the modified low pass filter design “N5_MaxFlat_LPF_T-Line_Tapped_Stubs” that uses tapped stubs with a 1 mm width (Z0 = 89 W).<br>
<b>Ans:<br>
for Z_in_x1 = -362j, characteristic impedance of x1 = 89 Ohm, l_x1 = 0.038, lumda = 2.6693 mm<br>
l_x1 = l_x5<br>
for Z_in_x2 = -86j, characteristic impedance of x2 = 89 Ohm, l_x2 = 0.1277, lumda = 8.9703 mm<br>
l_x2 = l_x4<br>
for Z_in_x3 = -50j, characteristic impedance of x3 = 89 Ohm, l_x3 = 0.1685, lumda = 11.8363 mm<br>

The design parameters are shown in the following figures.<br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/StevenYeh/Lab6/maximally_flat_tapped_stub_parameter.jpg) <br><br>

The HFSS simulation results are as follows.
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/StevenYeh/Lab6/maximally_flat_tapered_stubs_amp_S11.jpg) <br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/StevenYeh/Lab6/maximally_flat_tapered_stubs_amp_S21.jpg) <br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/StevenYeh/Lab6/maximally_flat_tapered_stubs_phase_S11.jpg) <br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/StevenYeh/Lab6/maximally_flat_tapered_stubs_phase_S21.jpg) <br></b>

<br>Task 2: Synthesis and implementation of an equi-ripple band-stop filter.
In this exercise you will synthesize a fifth-order 0.5 dB equi-ripple band-pass filter with a center frequency fc = 3.0 GHz and a bandwidth of 2.25 GHz to 3.75 GHz (e.g., delta = 0.5), and then implement your design using microstrip transmission lines for a Z0 = 50 Ohm reference impedance on a 62 mil thick FR4 (er = 4.1, tan_d = 0.01).

<br>Step 1: First, use the table on the following page to determine the element values of the low pass prototype.


<br>Step 2: Assemble the prototype LC ladder network.
To simplify the analysis (visually), we will replace this ladder network will the table shown below.


<br>Step 3: Convert this to a band-stop filter topology by replacing shunt elements with shunted LC series networks, and series LC parallel networks.


<br>Step 4: Use inverters (e.g., quarter-wave transformers) to provide separation between the series elements and convert series stubs into shunt stubs.


<br>Step 5: Calculate the scaled impedance values of the equivalent open-circuit stubs using<br>
<b>Ans:<br>
The design parameters are shown in the following figures.<br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/StevenYeh/Lab6/equal_ripple_parameter.jpg) <br><br>

The HFSS simulation results are as follows.
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/StevenYeh/Lab6/equal_ripple_amp_S11.jpg) <br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/StevenYeh/Lab6/equal_ripple_amp_S21.jpg) <br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/StevenYeh/Lab6/equal_ripple_phase_S11.jpg) <br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/StevenYeh/Lab6/equal_ripple_phase_S21.jpg) <br></b>


<b>Conclusion:<br>

1. Two filters are designed using the insertion loss method in this lab. One is the maximally flat LPF and another is the Equal-Ripple BSF.<br>
2. Different filter transformations are involved in the filter design. For the maximally LPF, the impedance and frequency scaling are needed. Also, the Richard's transformation and Kuroda's identities are involved to successfully implement the LPF design. On the other hand, the BSF needs one extra process from the prototype filter. The inductor should convert to an inductor parallel with a capacitor and a capacitor should convert to an inductor in series with a capacitor.
3. The lumped LC used in Task 1 step 7 only works well at low frequency. At high frequency, the distributed components are prefered.</b>
