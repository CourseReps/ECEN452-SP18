# Lab 6: Filter Design
Divya Acharya 

#Task: Design of Low Pass and Band Stop Filters

## Background
- Filters can be classified into Low-Pass, High-Pass, Band-Pass and Band-Stop based on the range of frequencies that they allow to pass. 
- This lab focussed on design LPF filters with microstrip, open circuit stubs using Richards' Transformation and Kuroda's identities. 
- The physical design of BPF was implemented using copper tapes on substrate.

## Design
**Given:**
- Low Pass Filter: There are two designs implemented for LPF in this lab. One consists of synthesized Zo values for each of the stub of length 0.125 lambda and the other is tapped LPF filter where Zo for each stub is fixed and length of stub is adjusted to achieve equivalent impedance.
- Cut Off Frequency =2.5Ghz (Attenuation 3dB)
- Minimum attenuation at 3.25GHz is 10dB

**LPF Design values:**

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/DivyaNAcharya/Lab6_Completed/LPFDesign1.JPG)

**Conversion to Tapped Filter design:**
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/DivyaNAcharya/Lab6_Completed/LPFDesign2.JPG)

**Band Stop Filter**
- Cut Off Frequency =3Ghz (Attenuation 3dB)
- Stop Band =2.25GHz to 3.75GHz

- Calculated Values:

| Stub | Impedance | Length | Width  |
| ---- | --------- | ------ | ------ |
| L1   | 75 ohms   | 14.06mm| 1.47mm |
| L2   | 104 ohms  | 14.84mm| 0.654mm|
| L3   | 50 ohms   | 14.5mm | 3.1mm  |
| L4   | 104 ohms  | 14.84mm| 0.654mm|
| L5   | 75 ohms   | 14.06mm| 1.47mm |


##Procedure
**Low Pass Filter**
- Low Pass filter and Tapped Low pass filter designs were simulated in HFSS

**Band Stop Filter**
- Copper tape with width 50 ohms line was placed and measured
- Strips corresponding to 75ohms, 50ohms and 104 ohms were placed on the 50ohms line
- Center to Center spacing between the strips is lambda/4 (14.1mm)
- The copper tapes had to be soldered to keep them in place


## Results and Discussion
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/DivyaNAcharya/Lab6_Completed/LPF_S11.png)
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/DivyaNAcharya/Lab6_Completed/LPF_S21.png)
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/DivyaNAcharya/Lab6_Completed/BSF_S11.png)
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/DivyaNAcharya/Lab6_Completed/BSF_S11_Phase.png)
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/DivyaNAcharya/Lab6_Completed/BSF_S21.png)
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/DivyaNAcharya/Lab6_Completed/BSF_S21_Phase.png)

## Observations
1. The Copper Taped Band Stop filter made in lab had a center frequency close to 3.5GHz instead of 3GHz. The length of the strips should have been longer to get center frequency at 3GHz.
2. HFSS simulation for normal LPF design was not providing as good result as tapped stub design.

## Conclusion
For Band Stop design, HFSS milled and Copper tape filter plots don't coincide but there is adequate attenuation in the range 2.25GHz to 3.75GHz. Tapped Stubs are a better design for low pass filter since it is simpler and easier to implement.

