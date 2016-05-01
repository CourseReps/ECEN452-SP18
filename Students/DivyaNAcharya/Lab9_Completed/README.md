# Lab 9: Edge fed Patch Antenna Design
Divya Acharya 

## Background
Microstrip patch Antenna is designed by empirical equations that calculate the width and length of the antenna based on resonant half wavelength, effective dielectric constant and fringing fields. Quarter wave transformer or single stub matching can be used for impedance matching.

## Design
**Given**
- Operating Frequency= 3GHz
- Zo=50ohms
- VSWR=1
- Quarter wave transformer is used for impedance matching
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/DivyaNAcharya/Lab9_Completed/Design.PNG)

**Calculated Values**
- Width = 31.3mm
- Length = 24.2mm
- 50 ohms line width =3.1mm
- Quarter Wave Transformer:
- Length =18.42mm
- Width = 6.1mm
- Distance from connector = 33.424mm (length fo quarter wave strip + length of reference plane)

**Simulated Values**
- Width = 23.7mm
- Length = 31.3mm 
- Distance of probe from center = 5.7mm

##Procedure
- Microstrip patch of above dimensions were placed on the substrate along with a 50ohms feedline
- The feed and coax connector are soldered
- The resulting antenna is measured in VNA to check impedance at feed
- The impedance found is used to calculate the distance, length and characteristic impedance of the quarter wave strip
- The impedance matched antenna is measured using VNA for VSWR
- HFSS Simulation consisted of a probe fed patch antenna design that needed optimizing the design by changing the distance of probe.

## Results and Discussion
VSWR: Both HFSS and implemented Patch have good VSWR (below 1.2)
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/DivyaNAcharya/Lab9_Completed/VSWR.png)

Smith Chart (HFSS) shows good impedance matching as shown below
<br>![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/DivyaNAcharya/Lab9_Completed/SmithChart.PNG)

## Observations
- The operating frequency measured was greater than required. This could be resolved by decreasing the length L of the patch
- Quarter wave matching gives a good VSWR in the measurements
- In HFSS simulation, the length of patch needed to be adjusted (reduced) to get resonance at 3GHz and position of probe was adjusted to get impedance matching.

## Conclusion
- Patch Antenna design was understood and implemented in this lab. The design is simple and quick to implement and good results can be obtained even with copper tape.

## Hindsight
- Should have used a slightly smaller length of the patch to get resonance at 3GHz

## Reflection
- Understanding implementation of Quarter Wave matching was interesting and something that only lab could have explained. 
