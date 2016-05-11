Undergraduate Final Project: Patch Antenna Array

Background:

Antenna arrays are used for a broad variety of applications in wireless signal transmission.  The purpose of creating an antenna array is to increase the antenna gain and directivity over that of an individual antenna.  By constructing a phase controlled array in which each the phase of the signal is adjusted at each individual antenna, the beam of the antenna can be adjusted by modifications in phase along the antenna array.  This allows for beamsteering, allowing the signal beam from the antenna to be swept across a range of directions.  The antennas concentrate power in this beam, as well as in other maxima, while other areas of space experience destructive interference and become dead zones.

Design:

The phase shifted antenna array was designed by connecting matched 50 ohm patch antennas to hybrid coupler circuits.  The hybrid coupler ports 2 and 3 were connected to identical varactor based phase shifting circuits in order to allow the phase of the signal to be shifted and controlled.  The class was broken into 2 teams of undergraduate and graduate students, respectively.  Each team submitted 2 designs for a total of 4 antennas in the array.

The first undergraduate phase shifter design consisted of two transmission lines of characteristic impedances 30 ohms and 20 ohms.  Identical inductive lines with series varactor diodes were run from the junction between the lines and from the end of the second line.  By controlling the DC biasing of the varactor diodes through application of 1-5VDC, the  capacitance could be controlled to adjust the phase.

The second undergraduate design was a lumped element model consisting of a similar transmission line circuit with the inductive lines replaced by series inductances.  This second design was significantly less effective than the distributed element circuit.

Procedure:

Each of the hybrid coupler phase shifters was hooked to an antenna and the phase shift was measured across a range of frequencies at increments of 1V.  The results were recorded and plotted.

Results:

![Undergraduate Design 1 Magnitude](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/FINAL_PROJECT/Undergrad/Design1/Undergrad_Design1_Mag.png)
![Undergraduate Design 1 Phase](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/FINAL_PROJECT/Undergrad/Design1/Undergrad_Design1_Phase.png)
![Undergraduate Design 2](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/FINAL_PROJECT/Undergrad/Design2/Undergrad%20Design%202%20plots.pdf)

By way of comparison, below are the graduate designs:
![Graduate Design 1](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/FINAL_PROJECT/Graduate/Design1/Graduate1_Plot.png)
![Graduate Design 1 at 2.5GHz](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/FINAL_PROJECT/Graduate/Design1/Graduate1_Plot_2.5GHz.png)
This design shows a phase shift of approximately 310 degrees; note that the phase wraps between 2V and 3V.  The circuit shows an attenuation of between 3dB and 5dB.

Conclusion:

In this lab, the students designed a phase shifted array.  Ultimately, the designs submitted by the graduate students were more effective than those submitted by the undergraduates.  There were significant challenges in applying our knowledge to the design of a practical circuit within a short timeframe.  However, we worked as a team to distribute workloads in order to put in the time to create the designs.

Hindsight:

More time to design and simulate the antenna array may have allowed for better results.  Additionally, it would have been interesting to see the full array assembled.

Reflection:

The most rewarding part of this lab was applying our knowledge to a practical design problem.  The greatest challenge was the HFSS design of the models.  Additional challenges of determining the nature of the malfunctions within the design were curtailed by a lack of time to conduct iterated testing.
