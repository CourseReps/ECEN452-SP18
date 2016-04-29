# Lab 7 Report
Joshua Ruff

## Background
The Wilkinson Power Divider (WPD) splits all power input to port one between ports two and three. Conversely, any power input to ports two and three is combined and output to port one. Ideally, ports two and three are isolated from one another in this device. 

The phase shifter uses a 50 ohm through as a reference phase, and then uses two longer lines to provide 90 degrees and 180 degrees of phase shift respectively. 

## Design
Both devices had a design frequency of fo=2.5 GHz. 

###Wilkinson Power Divider
The lumped element model for the Wilkinson Power Divider is a simple resistive divider. Transforming these resistors into transmission lines offers better power transfer and isolation. Aditionally, a resistor passed between ports 2 and 3 offers complete isolation between ports 2 and three. The resulting device schematic appears as follows: 

![WPD_Schematic](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/joshruff/Lab7/WPD.jpg)<br>

Zo of the feedlines is 50 Ohms. The characteristic impedance of the quarter wave transformers is 70.1 Ohms. The resistor strung between points two and three is 2*Zo or 100 Ohms. 

To implement this device in microstrip, the phsyical widths of each microstrip line is calculated based on the impeadance. A microstrip line calculator is used to expedite this process. The substrate used is FR4 with a relative permittivity of 4.1 and a height of 62 mil. Thus, the Width of the feedlines comes out to be 3.13 mm. The width of the quarter wave transformers is 1.71 mm, and the length of the quarter wave transformers is 24.4 mm (Later adjusted). 

###Phase Shifter
The 50 Ohm line will be used as a reference length for 0 degrees phase. To add 90 degrees, an extra quarter wave of line is added to this path. To add 180 degrees, an extra half wave of line is necessary. All parts of the phase shifter are implemented on 3.13 mm 50 Ohm line. The extra phase length for each path is split between two vertical sections of line (Thus, the 90 degree path will have an eigth-wave separation from the center, and the 180 degree path will have a quarter wave separation. Because two sections of microstrip are necessary to connect the shifted microstrip to the center, this length doubles to the extra length required for the desired pase shift.) 

These paramters led to a 90 degree shift segment physically separated from the center by a length of 7.02 mm, and a 180 degree segment phsyically separated from the center by 14.04 meters. 

## Procedure
The WPD was created to the above design specifications in HFSS and simulated. This was compared to measurements taken on a version of this device which David milled. 

The Phase shifter was constructed on FR4 in lab. First the 50 Ohm line was constructed and measured. Then the 90 degree line was measured. Lastly, the 180 degree line was measured.

## Results and Discussion
###WPD

![Reflection](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/joshruff/Lab7/Reflections.png)<br>
This graph shows the reflection at each of the three ports. At the design frequency, all of the reflections are well below 10dB, which means very little power is reflected here.  This is a desired characteristic for this device. 
![Divide](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/joshruff/Lab7/Division.png)<br>
S21 and S31 are both nearly -3dB at the design frequency. This demonstrates an approximately half power split between these ports, which was the ratio the power divider was designed for. The measured, milled version correlates fairly closely to the simulated version for these S-Parameters. 
![Isolation](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/joshruff/Lab7/Isolation.png)<br>
This Graph demonstrates the isolation of ports 2 and 3. This isolation is seen most obviously at the resonance at 2.45 GHz, which shows very little power leaks between ports 2 and 3 around the design frequency. 

###Phase Shifter
![PS_Taped](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/joshruff/Lab7/Phase_Shifter.jpg)<br>
Both my lab partner and I had issues soldiering the connections using the heat gun during this lab. The result was a burnt up substrate, and several segments of the copper tape shrunk below their measured length, which likely threw off the measurements. THe graph of the phase shifted measurements is shown below: 

## Conclusion
Summarize the key points in the design and results. Also mention unexpected challenges (if any) in the design and how you overcame them. 

## Hindsight
I need more soldiering practice. 

