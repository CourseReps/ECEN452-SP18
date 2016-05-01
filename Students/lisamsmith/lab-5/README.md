# Lab 5 Report
Lisa Smith

## Background
In this lab, the TRL kit from before will be designed and simulated in HFSS and compared to the measured results of the TRL. The TRL calibration uses three standards (thru, reflect, and line,) to solve for the error coefficient when using a network analyzer. The TRL calibration accounts for transition effects due to the coax-microstrip connection and allows you to set a reference plane some distance along the feed line. The reference plane is the reflect standard and the thru standard is twice this length. The Line standard then has an extra length added that allows it to operate at frequencies from -20 degrees to -160 degrees from the center frequency.
In addition, an RF PIN diode series switch is designed and simulated in HFSS and compared to the measured results. This design is bases on a bias tee and can be used to direct the input signal to the desired output port.

## Design
For the TRL:

![lab_5_eq1](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/lisamsmith/lab-5/lab_5_eq1.PNG)

The Thru has a S21 phase of -.71° at 3 GHz and the Line has a S21 phase of -91.9° at 3 GHz with the length above, it is 89.5.° at 3 GHz with the Line set to 43.925 mm. The length was shortened to decrease the phase. 

![lab_5_eq2](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/lisamsmith/lab-5/lab_5_eq2.PNG)

Using the imaginary part of the impedance of the Reflect, the polynomial model of the capacitive open circuit termination was found.

![lab_5_graph1](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/lisamsmith/lab-5/lab_5_graph1.PNG)

For the RF PIN Diode Series Switch:
![lab_5_eq3](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/lisamsmith/lab-5/lab_5_eq3.PNG)

Each of these designs were made using the given HFSS files and subsituting the calucated values above.

## Procedure
In lab, a TRL calibration kit was already designed. Students learned how to calibrate the network analyzer using the TRL kit. Each standard was attached and the magnitude and phase of the S-parameters was measured. The RF PIN diode serires switch was then attched and the magnitude and phase of the S-parameters was measured.

## Results and Discussion
The simulated and measured results line up fairly well for the TRL kit. The differences can be accounted for in slight variations of the simulated widths and lengths and the actual widths and lengths of the TRL kit.

![lab_5_graph2](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/lisamsmith/lab-5/lab_5_graph2.PNG)

The simulated and measured results line up fairly well. The differences can be accounted for in slight variations of the simulated widths and lengths and the actual widths and lengths of the PIN diode Switch. This switch could be drastically improved because at the design frequency, 2.5 GHz, the S21 barely gets below -10 dB.

![lab_5_graph3](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/lisamsmith/lab-5/lab_5_graph3.PNG)

## Conclusion

## Hindsight

## Reflection
