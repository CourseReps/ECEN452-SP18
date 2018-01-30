# Lab 5 Report
Abhay Shankar Anand

## Background
Lab 5 consists of the design and analysis of a TRL calibration kit and an RF switch (Bias Tee)

1. TRL calibration is a smart technique for the calibration of a Vector Network Analyzer (VNA) which exploits the usage of shifting reference planes and is, to a large extent, impervious to changes in port cables/connectors.
2. RF Switch is designed using a PIN diode which operates with the help of a DC bias network. If the diode is forward biased, then it allows the RF to pass through with little loss and if the diode is reverse biased, the reflections at the input port is high and transmission is reduced significantly.

## Design
### TRL Design
#### Given constraints
* __Z<sub>0</sub>__ = 50 &#937;
* __&#949;<sub>r</sub>__ = 4.1
* __FR4 thickness__ = 62 mils = 1.5748 mm
* __Freq Range__ = 1 GHz to 5 GHz
* __f<sub>c</sub>__ = 3 GHz
* __Reference Plane__ = 15 mm from edge

#### Calculated Values
* __T-Line width__ for Z<sub>0</sub> = 3.074 mm (Using [Microstrip Calculator](http://www1.sphere.ne.jp/i-lab/ilab/tool/ms_line_e.htm))
* __&#949;<sub>eff</sub>__ = 3.146 (Using [Microstrip Calculator](http://www1.sphere.ne.jp/i-lab/ilab/tool/ms_line_e.htm))
* __&#955;/4__ = 14.095 mm (Using [Microstrip Calculator](http://www1.sphere.ne.jp/i-lab/ilab/tool/ms_line_e.htm))
* Length of **Thru** = 15 mm + 15 mm = 30 mm
* Length of **Reflect** = 15 mm
* Length of **Line** = Length of Thru + &#955;/4 = 44.095 mm

### RF Switch Design
#### Given Constraints
* __Z<sub>0</sub>__ = 50 &#937;
* __&#949;<sub>r</sub>__ = 4.1
* __FR4 thickness__ = 62 mils = 1.5748 mm
* __Freq Range__ = 1 GHz to 5 GHz
* __f<sub>c</sub>__ = 2.5 GHz
* __Reference Plane__ = 15 mm from edge

#### Calculated Values
* __T-Line width__ for __Z<sub>0</sub>__ = 3.087 mm (Using [Microstrip Calculator](http://www1.sphere.ne.jp/i-lab/ilab/tool/ms_line_e.htm))
* __T-Line width__ for __100 &#937;__ = 0.706 mm (Using [Microstrip Calculator](http://www1.sphere.ne.jp/i-lab/ilab/tool/ms_line_e.htm))
* __&#955;/4__ for 100 &#937; line = 17.874 mm (Using [Microstrip Calculator](http://www1.sphere.ne.jp/i-lab/ilab/tool/ms_line_e.htm))

## Procedure
###TRL Calibration Kit

1. Port deembedding of **15 mm** of for all ports in the HFSS designs (Reflect, Thru and Line) was performed.
2. Reflect was first analyzed: Length of the line was set to **15 mm**, width adjested for **Z<sub>0</sub>**.
3. This was design simulated and the result of Im(Z) exported as CSV format.
4. This exported data was read using a [python program](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/abhaysanand/Lab5/dev/TRL_capacitance.py) and all Im(Z) values are converted to Capacitances using the formula
**C = 1/j&#969;Z**
5. A 3 degree polynomial fit was performed for this Capacitance curve and these would then be used to enter into the VNA.
6. Thru line is analyzed next: Length is set to 30 mm and width as used for Reflect line.
7. After the simulation is complete, the result showed a phase of 7&#176; at 3 GHz.
8. To rectify this, the width of the line was increased to 3.09 mm. This yielded an acceptable result of less than 0.5&#176; at 3 GHz.
9. This width was used for the Reflect line and steps 3, 4, and 5 were repeated.
10. Next, the Line design was analyzed. Here, all previously designed and rectified values were incorporated.
11. After simulation, the results gave a phase of 95&#176; at 3 GHz.
12. Since the width was modified for the Thru design, the additional length of 14.095 mm was reduced to 13.95 mm.
13. This change resulted in a phase of around 90.3&#176; at 3 GHz.
14. All simulation results were exported as CSV formats and using [python code](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/abhaysanand/Lab5/dev/TRL_S11_S21_Plotter.py), they were compared to measured values.
15. With this new length, the delay was calculated using the phase and excess line length. This delay in pico-seconds would be an essential input parameter for calibration of VNA using TRL kit.

### RF Switch Design

1. Port deembedding of **15 mm** of for all ports in the HFSS designs (Reflect, Thru and Line) was checked.
2. Widths of all __Z<sub>0</sub>__ T-Lines in all designs were changed to 3.087 mm.
3. Widths of all __100 &#937;__ T-Lines in all designs were changed to 0.706 mm.
4. With these modified parameters, **SCGroundStub** and **SCBiasedStub** designs were simulated.
5. As the results were as expected, these modified values were incorporated into the **PINSeriesSwitch** design.
6. This design was simulated and S11 and S22 for **ON** and **OFF** state were exported for comparison with measured data.
7. The comparison was performed using a [python code](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/abhaysanand/Lab5/dev/PinDiode_S11_S21_Plotter.py).

## Results and Discussion
### TRL Design
#### Results
**Capacitance Curve**
![TRL Capacitance](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/abhaysanand/Lab5/results/TRL_Capacitance.jpeg)

**Comparison of S11 and S22 between Simulated and Measured**
![TRL Comparison](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/abhaysanand/Lab5/results/TRL_results.jpeg)

#### Observation
1. All of the simulated results align very closely with the measured data.
2. Modifications in line widths and excess line length were calculated using trial-error method. The results were not in direct conformance with the expected values initially.
3. Sometimes, the phase of Line at 3 GHz would switch from around -90&#176; to around +90&#176;.

### RF Switch Design
#### Results
**PINDiode Results**
![PINDiode Results](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/abhaysanand/Lab5/results/PinDiode_results.jpeg)

#### Observations
1. The simulated data agrees with the measured data to a good degree.
2. The OFF state could have a better response - S21 is around -12dB which is around 15% of input power.

## Conclusion
1. The simulated TRL calibration kit has very close conformance with the actual kit.
2. The simulated RF Switch has an agreeable conformance with the actual kit.

## Hindsight
As opposed to the TRL data, the simulated data for RF Switch is not as close to the measured data. This could be because of the use of Lumped elements. The exact characterization of Lumped elements in RF is quite difficult and this is a systematic error that needs to be considered for future designs.
