ECEN 452-500: Ultra High Frequency Techniques<br>
Spring 2016 – Prof. Huff<br>
Lab 5<br>
Go to the Lab 5 subdirectory in the ECEN 452 GitHub directory Labs and download the HFSS project files “ECEN452_Lab5_TRL.hfss” and “ECEN452_Lab5_PIN.hfss”. Open each project file (File-Open…), then save them to the local drive of the computer you are running your simulations on and rename it by appending your team number to each file (e.g., “ECEN452_LabX_TopicY_TeamZ”).<br><br>

Task 1: Design of a TRL calibration kit.<br>
In this exercise you will complete the design of the Thru, Line, and Reflect microstrip calibration fixtures found in your “ECEN452_Lab5_TRL_GroupX.hfss” project file. These design files are named “Thru”, “Line”, and “Reflect”. You will be designing these
for a Z0 = 50  reference impedance on the 62 mil thick FR4 (er = 4.1, tan d = 0.01) substrate to support a frequency range of 1 GHz to 5 GHz and provide a 15mm reference plane beyond the SMA end launch connectors.<br><br>

Step 1: Calculate the physical width w of the microstrip lines required for this calibration kit and change all line widths in the design files.<br>
<b>Ans:<br>
For Z0 = 50 ohm, microstrip line width = 3.12 mm<br></b>

<br>Step 2: Calculate the design frequency of the calibration and the effective dielectric constant, and then use this information to determine the physical length (in mm) for a quarter-wavelength section of transmission line. Use this quarterwavelength distance and the desired reference plane distance to set the lengths of the three calibration fixtures.<br>
<b>Ans:<br>
f0 = (fL + fH)/2 = (1G + 5G)/2 = 3 GHz<br>
For Z0 = 50 Ohm @ 3 GHz, effective dielectric constant = 3.17<br>
lumda/4 = 14.04mm<br></b>

Step 3: Simulate all three designs using the simulation parameters provided in the design files.<br>
<b>Ans:<br>
Initially, the simulation is run under the following parameters.<br>
line_width = 3.12 mm<br>
reflect_length = 15 mm<br>
thru_length = 30 mm<br>
line_length = 44.04 mm<br><br>

Results:<br>
for the reflect: S11 = -0.2263 dB, im(Z11) = 10.2862 @ 3 GHz<br>
for the through: S11 = -40.9004 dB, S21 = -0.1462 dB, S21_phase = -193.9517 degrees @ 3 GHz<br>
for the line: S21_phase = -284.8875 degrees, S11 =  -37.8750 dB, S21 = -0.2212  dB @ 3 GHz<br></b>

<br>Step 4: Use the de-embedding feature at each port (in each design file) and examine the S-parameters of each calibration fixture. First, verify that the Thru standard has zero phase and loss at the design frequency (but observe the behavior across the bandwidth).
Next, verify that the Line standard is exactly 90 Deg. at the design frequency; if it is not, adjust this length of this section accordingly. Once you have determined the correct length, use the S-parameters to calculate the phase velocity of the line and the delay of the line standard. Last, examine the S-parameters of the Reflect standard and use them to extract the polynomial model of the capacitive open-circuit termination. (Hint: export the Im(Z) plot data and convert reactance to capacitance. Then, use a curve fitting tool such as MATLAB or Excel to generate a 3rd order polynomial that fits the capacitance data)<br>
<b>Ans:<br>
Apply the de-embedding features on each port, where deembed distance = 15 mm<br>
Also change the line_length to 43.92 mm<br>
Results:<br>
for the reflect: S11 = -0.0922 dB, im(Z11) = -620.5008 @ 3 GHz<br>
for the through: S11 = -40.7654 dB, S21 = -0.0116 dB, S21_phase = -0.8115 degrees @ 3 GHz<br>
for the line: S21_phase = -90.5442 degrees, S11 =  -44.9875 dB, S21 = -0.0836  dB @ 3 GHz<br>
effective dielectric constant = square(lumda/lumda_g) = square(100mm/(13.92mm*4)) = 3.23<br>
phase velocity = c/square_root(effective dielectric constant) = 3 * 10^8 / square_root(3.23) = 1.67 * 10^8 m/s<br>
delay time = 13.92 mm/1.67 * 10^8 = 8.34 * 10^-11 s<br><br>
After using the polyfit and polyval function in Matlab to get the best estimation of the curve fitting values. We derived the 3rd order polynomial => y = 0.0013 * x^3 - 0.0145 * x^2 + 0.0547 * x^1 + 0.0186<br>
where x is the frequency in GHz, y is the capacitance in pF.<br></b>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/StevenYeh/Lab5/curve_fitting.jpg) <br>

<br>Step 5: In lab, the TA will measure the three standards and provide you with the measured results.<br>
Reporting Items: Provide a brief accounting of the activities in this section, including any calculations, etc. that you made. Discuss any modifications that were made after simulating the design, and include your rationale for making these modifications. Include plots of the magnitude and phase of the de-embedded calibration standards, and discuss any differences between the measured and simulated data.<br>
<b>Ans:<br>

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/StevenYeh/Lab5/S21_line_dB.jpg) <br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/StevenYeh/Lab5/S21_line_phases.jpg) <br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/StevenYeh/Lab5/S21_thru_dB.jpg) <br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/StevenYeh/Lab5/S21_thru_phase.jpg) <br></b>

Task 2: Design of an RF PIN diode series switch.<br>
In this exercise you will examine the design of a PIN diode switch using quarter-wave bias tees found in your “ECEN452_Lab5_PIN_GroupX.hfss” project file, and compare simulated results to a fabricated design. You will be designing this switch for a reference impedance Z0 = 50 Ohm on the 62 mil thick FR4 and a center frequency f0 = 2.5 GHz. Your design should maintain a 10mm separation from the 15mm reference planes set by the TRL calibration.<br>

<br>Step 1: Calculate the physical width w of the 50 ohm microstrip line, and the physical width wc for the two high impedance microwave chokes (quarter-wave short circuited stubs with Z0 = 100<br>
<b>Ans:<br>
w = 3.13 mm<br>
wc = 0.75 mm<br></b>

<br>Step 2: Calculate the physical length of the quarter-wavelength transmission lines used for the bias tees, and modify the design files “SCGroundStub” (this is the bias tee connected to RF and DC ground using a via) and “SCBiasStub” (this is the bias tee terminating with a bias capacitor CBias = 47 nF in series with a via and a bias resistor RBias = 510 ohm with a via). Simulate these lines, and alter the length of the lines lSCG and lSCB to minimize the insertion loss through both structures at the design frequency.<br>
<b>Ans:<br>
Calculated results: Z0 = 100 ohm, effective dielectric constant = 2.88, lumda/4 = 17.68 mm<br>

Simulated results: SCGround_length = 18 mm, SCBias_length = 18 mm<br></b>

<br>Step 3: Modify the design file “PINSeriesSwitch” with the lengths and widths you obtained, and simulate the file. This file contains a global variable that has been set up to run the diode in both the “ON” and “OFF” states (by altering the equivalent circuit of the diode in the design). Observe the results.<br>
<b>Ans:<br>
Simulation is run under the following parameters.<br>
feed_line_width = 3.13 mm<br>
SCBias_width = SCGround_width = 0.75 mm<br>
SCGround_length = 18 mm<br>
SCBias_length = 18 mm<br></b>

<br>Step 4: In lab, the TA will measure the PIN diode switch with you and provide the measured results. Reporting Items: Provide a brief accounting of the activities in this section, including any calculations, etc. that you made. Discuss any modifications that were made after simulating the design, and include your rationale for making these modifications. Include plots of the switch in the “ON” and “OFF” states (magnitude in dB), and discuss any differences between the measured and simulated data.<br>
http://www.skyworksinc.com/uploads/documents/Design_With_PIN_Diodes_200312D.pdf<br>
http://literature.cdn.keysight.com/litweb/pdf/5091-1943E.pdf<br>
<b>Ans:<br>
Measured and simulated results are very similar, as shown in the following figures.<br></b>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/StevenYeh/Lab5/switch_on_s11.jpg) <br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/StevenYeh/Lab5/switch_on_s21.jpg) <br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/StevenYeh/Lab5/switch_off_s11.jpg) <br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/StevenYeh/Lab5/switch_off_s21.jpg) <br>


<b>Conclusion:<br>
1. Traditional calibration kit (short, open, matched load) used to calibrate the VNA can cause some errors if the kit deviated from the factory standard. It's more obvious at HF. Therefor the TRL calibration kit can provide an alternative way other than the tradional one. It uses the thru, reflect and line connections to estimate VNA's error boxes.<br>
2. One critical factor in designing a TRL kit is the repeatability of each connection such as the soldering and so on.<br>
3. The 2nd task is to design a phase shifter using a PIN diode. Two major problems on designing this MW devices are the DC block and RF choke design. One popular method is to use the quarter-wave transformer to implement the RF choke and use the capacitor to realize the DC block.</b><br>
