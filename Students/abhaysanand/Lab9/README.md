# Lab 9 Report
Abhay Shankar Anand

## Background
Lab 9 consists of the design and analysis of a coaxial probe microstrip patch Antenna as well as an implementation of feedline Copper Tape patch antenna.

## Design
### Given constraints
* __Z<sub>0</sub>__ = 50 &#937;
* __&#949;<sub>r</sub>__ = 4.1
* __FR4 thickness__ = 62 mils = 1.5748 mm
* __f<sub>c</sub>__ = 3 GHz
* __VSWR__ < 1.2 at 3 GHz
* __Reference Plane__ = 15 mm from edge

### Procedure
#### HFSS Simulation

Using the following equations, get the length and width of the probe for 3 GHz<br>
![AntennaEqn](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/abhaysanand/Lab9/dev/AntennaEquations.png)<br>

Initial values:<br>
* __Width__ = 31.2826 mm
* __Length__ = 24.2557 mm
* __Probe location__ = 3.75 mm from center

To attain resonance at 3 GHz, length of patch was changed to 23.7. And for impedence matching, probe location was shifted to 5.7 mm form the center. These values gave a very low S11 at 3 GHz as can be seen from the Smith Chart (in the results section).

![HFSS_antenna](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/abhaysanand/Lab9/results/CoaxFeedAntenna.png)

#### Copper Tape Implementation

The values as given above are used to cut out the length and width of the Cu Tape. Since the antenna is edge fed through a microstrip line, a stripline of 50 &#937; is cut out with length of about 50 mm.

An SMA connector was then soldered onto the feedline and S11 measured for this unmatched antenna.

We were asked to match this antenna using a single stub. Here, a different approach is used to match the antenna when compared to the conventional single stub matching process. As we are unaware of the input impedence of the antenna, we are to match the stub from the generator and travel towards the load.

![CuTapeAntenna](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/abhaysanand/Lab9/results/CuTapeAntenna.jpg)

## Results and Discussion

![SmithChart](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/abhaysanand/Lab9/results/SmithChart_Antenna.png)

![VSWR](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/abhaysanand/Lab9/results/VSWR.png)

* The resonant frequency of the Cu Tape antenna was slightly lesser than 3 GHz. This would most likely be due the excess length of the patch.
* Stub matching brought down the reflections significantly.

## Conclusion
Microstrip patch antenna was simulated to a good deal of accuracy in HFSS ans was implemented using Copper Tape in the lab.

## Hindsight
We were initially skeptical with the reverse single stub matching technique though logically it made sense and were quite thrilled at the matched output.
