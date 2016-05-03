# Lab 7 Report
Abhay Shankar Anand

## Background
Lab 7 consists of the design and analysis of microstrip Wilkinson Power Divider and a Copper Tape implementation of a basic 90&#176; and 180&#176; Phase Shifter

1. __Wilkinson Power Divider:__ A Wilkinson Power Divider (WPD) is designed as described in class with a 3 dB loss on both the output ports.
2. __Phase Shifter:__ A basic Phase Shifter is implemented using Copper Tape on FR4 substrate with interchangable 90&#176; and 180&#176; phase shifts.

## Design
### WPD Design
#### Given constraints
* __Z<sub>0</sub>__ = 50 &#937;
* __&#949;<sub>r</sub>__ = 4.1
* __FR4 thickness__ = 62 mils = 1.5748 mm
* __f<sub>c</sub>__ = 2.5 GHz
* __Attenuation__ = 3 dB power split
* __Reference Plane__ = 15 mm from edge

### Phase Shifter Design
#### Given constraints
* Fifth order 0.5 dB equi-ripple BSF
* __Z<sub>0</sub>__ = 50 &#937;
* __&#949;<sub>r</sub>__ = 4.1
* __FR4 thickness__ = 62 mils = 1.5748 mm
* __f<sub>c</sub>__ = 2.5 GHz
* __Phase Shift__ = 90&#176; and 180&#176;
* __Reference Plane__ = 15 mm from edge

### Procedure
#### WPD Design and Implementation

The power divider that is being designed is meant to have equal port split on ports 2 and 3 and it is a 3dB split (half of the input power goes to port 2 and the other half goes to port 3). As per a WPD design for a 3 dB split, the input port is forked into two transmission lines of impedence **&#8730;2 Z<sub>0</sub>**. In this case, for a 50 &#937; system this turns out to be 70.71 &#937;. The length of these transmission lines are to be **&#955;/2**.<br>

At the end of these transmission lines, a resistor of resistance **2 Z<sub>0</sub>** is added, joining these two T-lines. This resistor is essential in achieving a good isolation between ports 2 and 3 and minimizes the reflections at these ports. Fropm this point, transmission lines of impedences 50 &#937; emerge, forming the output ports 2 and 3.<br>

This powerdivider is simulated in HFSS to analyze its S-parameters:
![Wilkinson-HFSS](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/abhaysanand/Lab7/results/Wilkinson_HFSS.png)

The lengths and widths of the **&#8730;2 Z<sub>0</sub>** lines are obtained using the online Microstrip Line Calculator. These values gave good enough results without the need for tweaking the values.

#### Phase Shifter Design and Implementation

The phase shifter that was designed and implemented in lab used T-line phases to obtain the required 90&#176; and 180&#176; phase shifts.<br>

To achieve a 90&#176; phase shift, a total length of **&#955;/4** of microstrip line is to be added to the existing T-line and for 180&#176; shift, **&#955;/2** length of microstrip is to be added to the existing T-line. These extentions are achieved by adding legs to each of the additional T-lines as shown below:
![PhaseShifter_Design](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/abhaysanand/Lab7/results/PhaseShifter_Design.png)

Each of the legs of the extended T-lines are of length:
* __&#955;/8__ for 90&#176; shift to yield a total electrical length of **&#955;/4**
* __&#955;/4__ for 180&#176; shift to yield a total electrical length of **&#955;/2**

The required joints are solderes and S-parameters are read from the VNA.

## Results and Discussion
### Results
#### Wilkinson Power Divider
**WPD Reflections**
![WPD_Reflections](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/abhaysanand/Lab7/results/Wilkinson_Reflection.png)

**WPD Isolation**
![WPD_Isolation](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/abhaysanand/Lab7/results/Wilkinson_Isolation.png)

**WPD Transmission**
![WPD_Transmission](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/abhaysanand/Lab7/results/Wilkinson_Transmission.png)

At 2.5 GHz, the isolation and reflections have a pretty low, though not quite as same as the milled version. This could be because of the differences between HFSS modeling of a resistor and the actual resistor. The widths and lengths used in the milled version would have been larger than the simulated and hence the down shift in the frequency. The transmission parameters seem to be, however, in much greater accordance and give an approximate half power output.

#### Phase Shifter
**Phase Shifter THRU S-Parameters**
![PS_THRU](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/abhaysanand/Lab7/results/PhaseShifter_Thru.png)

**Phase Shifter 90&#176; and 180&#176; phase shifts S-Parameters**
![PS_THRU2](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/abhaysanand/Lab7/results/PhaseShifter_90_180.png)

At 2.5 GHz, &#8736;S21 for Thru2 , 90&#176; and 180&#176;

Config | &#8736;S21 | Difference
------ | ------ | ------
Thru2 | -373.22&#176; | 0&#176;
90&#176; shift | -438.18&#176; | 65&#176;
180&#176; shift | -149.68&#176; | 223&#176;

The main reason for the mismatch in the phase shift could be due to the inaccuracy in cutting the copper tape. The length of the Cu strip for 90&#176; shift is smaller than required and for 180&#176; shift, it's slightly larger than required. These results are however acceptable for an on-the-fly phase shifter.

### Questions
1. **Why do we need the resistor in the power divider design?**<br>
The resistor is the reason why the output ports (2 and 3) are matched and have a very good isolation. Without this, the reflections would have been very high in the circuit and power loss due to isolation would have been significant.
2. **What modifications did you have to make to the T-line widths/lengths to improve your simulated results?**<br>
There was no change required as the initial simulated results with values obtained from the online stripline calculated had good results.
3. **How did the presence of the additional microstrip lines affect the Thru measurement (difference between Thru and Thru2)?**<br>
The shift was very minimal for magnitude and phase of S21. And the magnitude of S11 had very slight variations; however, there was some amount of deviated phase shift for S11 after adding the coupled striplines. This could be that the coupled lines affect the impedence matching, but since it is just coupled energy, the magnitude seems to remain more-or-less the same.
4. **How could you improve the performance of your phase shifter if you had time to make a new one?**<br>
If I had time to make a new one, I would have made better accurate Cu tape cuttings and would have used PIN diodes to control the phase shift. Diodes would be oriented such that positive bias woule give a 90&#176; shift and negative bias would give a 180&#176; shift.

## Conclusion
1. There are minor variations in the realization of Wilkinson Power Divider when compared to the simulated results, but at the target frequency, the performance is good
2. The phase shifter gave a phase shift of crudely the required value.

## Hindsight
The concept of Phase Shifter is well understood, but implementation of that is would have been more accurate with laser cutters :).
