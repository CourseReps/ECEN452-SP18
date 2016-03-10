# Lab 7 Phase Shifter Measurement Error

As many of you know, there was a significant error in the S21 phase measurement for most of the phase shifters that were made during the lab. This document explains the source of the error and provides help on how to correct your measurements in order to accurately compare the data in your lab reports.

## Summary of Error
The phase of the 90 degree and 180 degree segments are supposed to be more negative than the reference phase because those lines are longer than the initial "Thru" line. However, many of the measured phases of those segments were actually less negative than the reference phase, which lead to much confusion.

## Error Explanation
After making my own phase shifter and reading through the network analyzer help documentation, I have determined the source of the measurement error. According to the documentation, the network analyzer calculates the unwrapped phase point-by-point starting with the first measurement point (1 GHz in our case). There is a note in the documentation that warns of inaccurate measurements if the first measurement point is greater than 180 degrees from DC. <br>

At 1 GHz, 180 degrees of phase corresponds to approximately 85 mm with our microstrip specifications. This means that line lengths greater than 85 mm will have a 360 degree phase error in the measurement. The boards that we are using are about 100 mm long, which means that, after de-embedding by 15 mm on each side, the Thru length is 70 mm. Since 70 mm is less than 85 mm, this would give us a valid reference phase measurement. However, the line length you need to add to get a 90 degree phase shift is approximately 14 mm which brings the total length of that path to 84 mm. This calculated line length is within 1 mm of causing a phase measurement error, and we all know by now how difficult it can be to cut and solder the copper tape with that kind of precision. The figures below illustrate how the network analyzer calculates the unwrapped phase from the regular phase measurement which is restricted to a range of -180 to +180 degrees. <br>

In the first figure, the line length is 82 mm which has a phase of less than 180 degrees at 1 GHz. The unwrapped phase simply extrapolates this line past -180 degrees instead of wrapping back to +180 degrees and we get a valid measurement. 
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Resources/Lab7_Error_Explanation_Graph1.png)

In the second figure, the line length is 85 mm which has a phase that is slightly more than 180 degrees at 1 GHz and thus the phase has already wrapped back to +180 degrees before our first measurement point. Now, the unwrapped phase extrapolates this line from the first measurement point and we have a 360 degree error in our measurement at 3 GHz.
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Resources/Lab7_Error_Explanation_Graph2.png)

## Error Correction
You will need to correct this error when plotting the data for your lab reports. When you open your .csv data file, if the S21 phase measurement at 1 GHz (the first data point) is a positive number, then subtract 360 degrees from each point in that column to correct the error. This will allow you to correctly compare the three segments and get accurate values for the phase shifts.
