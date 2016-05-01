# Lab 7 Report
Lisa Smith

## Background

The Wilkinson power divider is a 3 port device that equally divides the input power. The device can also be used as a divider by adding the power from the output ports in the input port. A Phase Shifter is a device that can change the outputted phase of an input. In this lab, the desired phase shifts are 0°, 90°, and 180°.

## Design

For the Wilkinson Power Divider:

Below are the calculated values used for simulation at 2.5 Ghz. The values were found using an online calculator.

![lab_7_values1](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/lisamsmith/lab-7/lab_7_values1.PNG)

This design was made using the given HFSS files and substituting the calculated values above.
 
For the Phase Shifter:

A 50 Ohm line was created for the 0° phase shift. From there, the additional lengths needed to achieve the desired phase shift were calculated using the equation below.
Reference Length: 102 mm (length of board)
Width at 50 ? : 3.118 mm
Frequency of Operation: 3 GHz

![lab_7_eq](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/lisamsmith/lab-7/lab_7_eq.PNG)

![lab_7_values2](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/lisamsmith/lab-7/lab_7_values2.PNG)

This design was made in lab using the calculated values above.

## Procedure
In lab, the phase shifter was designed using the values above. First a 50 Ohm line was created and measured. The lengths of the two phase shift Transmission Lines was calculated and put onto the board (unconnected). Then each of the 3 phase shifts were measured, connecting and disconnecting the transmission lines as needed.

## Results and Discussion
Here the simulated and measured result line up well for the S21 and S31 parameters. The other parameters have varied results for which frequencies the measured and simulated results match. The measured results have more dips in the magnitude at more frequencies.  This is a result the line lengths being too long (typically a shift a lower frequency.) All of the S11, S22, and S33 values show port matching, the S21 and S31 are the power division, and the S32 shows isolation.

![lab_7_graph1](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/lisamsmith/lab-7/lab_7_graph1.PNG)

The Phase shifter had problems with the length being too short for both the 90° and 180°. In addition there were problems with attaching/ detaching the copper strips that contribute to the error in the shifts. When the network analyzer unwraps the phase measurement, it did it incorrectly resulting in 360° needed to be added to the phase values. Still, the measured shifts were less than desired which reflects in a phase shift length that is too short.

![lab_7_graph2](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/lisamsmith/lab-7/lab_7_graph2.PNG)

## Conclusion
In this lab, both types of filter were simulated in HFSS and had similar results to the premade maximally flat low pass filter and the constructed band stop filter. Because the measured devices did not have the exact same design dimensions as the simulated models, there are some discrepancies in the results.

## Hindsight
The major problem with constructing the phase shifter was the accuracy in cutting out the lengths and widths of the transmission lines. Copper tape is not forgiving if the dimensions are cut slightly wrong. Also cutting straight lines is difficult.

## Reflection
This lab did give good insight to the operation of power dividers and phase shifters and the advantages to each type of device and how they are designed.
