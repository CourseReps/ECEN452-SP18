# Lab 7: Quadrature Hybrid Coupler and Rat Race Coupler
Divya Acharya 

#Task1: Design of Quadrature Hybrid Coupler

## Background
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/DivyaNAcharya/Lab8_Completed/HybridBackground.PNG)

Quadrature hybrids are 3dB  directional couplers with 90 degrees phase difference in the outputs of through and coupled arms. With all ports matched, the power entering port 1 is evenly divided between ports 2 and 3 with 90 degrees phase shift between the outputs. Port 4 is isolated and recieves no power from port 1.
The structure of this coupler is highly symmetric allowing any of the ports to be used as input ports. 



## Design
**Given**
- Center Frequency= 2.5GHz
- Zo=50ohms

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/DivyaNAcharya/Lab8_Completed/Hybrid.PNG)

**Calculations**
- Characteristic Impedance of horizontal strips =Z0/sqrt(2) =35.35ohms
- Width of horizontal strips =5.25mm
- Length of horizontal strips =16.5mm
- Width of 50ohms strips =3.1mm
- Length of 50 ohms strips =16.9mm


##Procedure
- Calculated design values were entered in HFSS file and simulated.
- Values were adjusted to get best response at center frequency
- David took VNA measurements of the milled coupler.




## Results and Discussion
1. Magnitude of reflection coefficients drops below -25dB at 2.5GHz for all ports showing good matching:
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/DivyaNAcharya/Lab8_Completed/HMatch.png)

2. Plots show S21 and S31 at about -3dB for both Milled and HFSS results as required. Hence power is being split equally. Isolation at port 4 is clear by the fact that S41 drops below -35dB:
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/DivyaNAcharya/Lab8_Completed/HIC.png)

3. The phase difference of output signals at ports 2 and 3 is about 90deg as required for both Milled and HFSS results. The bandwidth for which the phase difference remains close to 90 is lesser for milled results compared to HFSS results.
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/DivyaNAcharya/Lab8_Completed/HybridPhase.png)


## Observations
- The length of y trace (35.5ohms line) was adjusted from 16.5 to 20mm to get best response at 2.5GHz frequency.

#Task2: Design of Rat Race Coupler

## Background
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/DivyaNAcharya/Lab8_Completed/RRBackground.PNG)

The rat race coupler provides 180 degrees or a 0degree phase shift between output ports depending on the input port used.The two input ports are called "sum" and "difference" input ports when used as a combiner.

## Design
**Given**
- Center Frequency= 2.5GHz
- Zo =50ohms

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/DivyaNAcharya/Lab8_Completed/RatRace.PNG)

**Calculations**
- Impedance of circular strip =Zo*sqrt(2)=70.7ohms
- Total circumference of the strip = 3lambda/4 + lambda/4 +lambda/4 + lambda/4 =6lambda/4 =104.1mm
- Width of the circular strip = 1.68mm

##Procedure
- Calculated design values were entered in HFSS file and simulated.
- David took VNA measurements of the milled coupler.


## Results and Discussion
1. Magnitude of reflection coefficients drops below -25dB at 2.5GHz for all ports showing good matching:
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/DivyaNAcharya/Lab8_Completed/RMatch.png)


2. Plots show S21 and S31 at about -3dB for both Milled and HFSS results as required. Hence power is being split equally. Isolation at port 4 in the HFSS result is clear by the fact that S41 drops to -40dB. The isolation observed for milled result is relatively lower.
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/DivyaNAcharya/Lab8_Completed/RIC.png)

3. The phase difference at output ports due to inputs at port 1 or 4 should be 0deg or 180deg respectively. Milled and HFSS results agree to this as required:
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/DivyaNAcharya/Lab8_Completed/OutpuPhases.png)



## Observations
- The calculated values gave good results without any need to tweak the values.

## Conclusion
- The labs helped understand the design working and differences between the two types of coupler.


