# Lab 5: TRL & RF PIN diode series switch
Divya Acharya 

#Task1: Design of a TRL calibration kit

## Background
TRL (Thru, Reflect, Line) represents a family of calibration techniques that measure two transmission standards and one reflection standard to determine the 2-port 12-term error coefficients.TRL Cal is most often performed when you require a high level of accuracy and do not have calibration standards in the same connector type as your DUT.

## Design
**Given:**
- Substrate Dielectric constant er = 4.1
- Substrate Dielectric Loss Tangent tan∂ = 0.01
- Substrate thickness=62mil (~1.57mm)
- Characteristic impedance of strips=50Ω
- Frequency range= 1GHz to 5GHz
- Center frequency= (f1+f2)/2 = (1+5)/2 =3GHz
- Distance to reference plane=15mm

**Values:**

| Standard | Length |
| --- | --- |
| Thru | 30mm |
| Reflect | 15mm |
| Line (Calculated) | 44.06mm |
|Line (Simulated)|43.8mm|
|Width (Calculated)|3.09mm|
|Width (Simulated)|3.37mm|

##Procedure
1. David demonstrated the TRL calibration for Network Analyzer(NA) using the kit he designed and fabricated.
2. Steps in NA: Select Response->Cal->Cal Kit->Edit Kit->Enter Kit Name->Enter Kit Description. Choose Connector->SMA female and Freq Range 1GHz to 5GHz.
3. Coefficiencts corresponding to Reflect standard calculated using Python curve fitting program is entered in NA
4. Set OPEN (for Reflect standard), Set THRU for 0 delay THRU standard and then set THRU again for Line. (Rename this THRU to LINE)
5. Stimulus->Sweep->4001 points; Response->Cal->Start Cal
6. Select the TRL kit created.
7. Save data in .csv file for each calibration
8. For simulation in HFSS, change the width and lengths of the strips to calculated values and vary the lengths until optimum results are obtained.
9. De-embedding the port to reference plane is important to get correct results.
10. Export the Im(Z) plot data of Reflect standard to be used by Python program to find the 3rd order polynomial that fits the capacitance data

## Results and Discussion
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/DivyaNAcharya/Lab5_Completed/TRLThruPhase.png)
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/DivyaNAcharya/Lab5_Completed/TRLLineMagnitude.png)
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/DivyaNAcharya/Lab5_Completed/TRLLinePhase.png)
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/DivyaNAcharya/Lab5_Completed/TRLThruMagnitude.png)
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/DivyaNAcharya/Lab5_Completed/TRLThruPhase.png)
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/DivyaNAcharya/Lab5_Completed/TRL%20Capacitance.png)

## Observations
1. To obtain a Z0 close to 50Ω, width had to be modified to 3.37mm. 
2. Phase of 89.76 degrees was obtained for line with λ/4 = 13.8mm. 
3. Slight changes in length of Line led to inversion of phase sign.
4. 89.76 was the closest that was obtained iteratively changing values of line.

## Conclusion
HFSS & measured results were almost identical for the TRL calibration kit.

#Task2: Design of RF PIN diode series switch

## Background
The PIN diode switch switches the transmission line 'ON' or 'OFF' based on DC voltage given to the switch. The quality of ON and OFF condition can be checked by measuring the S11 and S21 in the two conditions.

## Design
**Given:**
-Substrate Dielectric constant er = 4.1
-Substrate Dielectric Loss Tangent tan∂ = 0.01
-Substrate thickness=62mil (~1.57mm)
-Characteristic impedance of strips=50Ω
-Center frequency=2.5GHz
-Distance to reference plane=15mm

| Length | Value |
| Width Zo=50ohms (calculated) | 3.1mm|
| Width Zo=100ohms (calculated)| 0.72mm|
| Width Zo=50ohms (simulated)| 3.35mm|
| Width Zo=100ohms (simulated)| 0.8mm|
| Length of 100ohms Line (calculated)| 17.79mm|
| Length of 100ohms Line (simulated)| 18mm

##Procedure
1. David demonstrated the S11 and S21 of PIN switch he designed and fabricated on the network analyzer
2. DC Blocks need to be added to the connectors while measuring the RF PIN diode series switch. Although the VNA has internal DC block, we take this precautionary measure.
3. In HFSS, The "SCGroundStub" and "SCBiasStub" files were simulated individually to get optimum results and these values were used in the complete design"PINSeriesSwitch".
4. The simulated and measured data is plotted using python program.

## Results and Discussion
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/DivyaNAcharya/Lab5_Completed/PIN%20S11%20OFF.png)
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/DivyaNAcharya/Lab5_Completed/PIN%20S11%20ON.png)
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/DivyaNAcharya/Lab5_Completed/PIN%20S21%20OFF.png)
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/DivyaNAcharya/Lab5_Completed/PIN%20S21%20ON.png)

#Observation
1. Width of micro-strip for 50Ω lines is calculated to be 3.1mm.To obtain a Z0 close to 50Ω, width had to be modified to 3.35mm. 
2. Width of micro-strip for 50Ω lines is calculated to be 0.72mm.To obtain a Z0 close to 100Ω, width had to be modified to 0.8mm. 

#Conclusion
Design and working of RF PIN diode series switch was demonstrated and understood in this task. The simulated results are better than the measured values.
