# Lab 11 Report
Thomas Darden

## Background
For this lab, we shall be finding the dielectric constant of a solid material. A free space callibration was achieved by performing a GRL callibration. We then transmitted a signal through the signal and measured the response of the through and the reflected wave to find the permittivity. 

## Design
We did not design anything for this lab.

## Procedure
We first attach cables to the horn antennas, and callibrate them with a short, open, line, and thru calibration. We do this to remove any noise that may be tranmitted through the cables. The GRL calibration begins with placing a sheet of plexiglass between the horns followed by a piece of metal that to act as the reflecting surface. We then use a Fourier transform to manipulate the data to place the gates for the calibration. We also measured the air and cardboard.

## Results and Discussion
From the pre GRL data from the S11 graph, the time gate reflection occurs at 3.67ns. The information this information allows us to understand where the gating should occur for more accurate measurements. As seen in the post-GRL data for the S21 parameter, the S21 is nearly zero, meaning the signal is being reflected.
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/td2016/Lab11/Pre.png)<br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/td2016/Lab11/Post.png)<br>

The graph below show the values of the dielectric constant for the air, plexiglass, and cardboard from a frequency range of 1 to 5 GHZ.
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/td2016/Lab11/All.png)<br>

## Conclusion
I was able to see in the S21 graph that we still have a value that goes above zero around 3.17Ghz, indicating error after callibration. A possible solution to this issue is a better test setup with better horn antennas and a better SOLT callibration.

## Hindsight
N/A

## Reflections
From this lab, I was able to learn how we find the dielectric constants of solid as opposed to Lab 10, where we found the dieletric constants of liquids.
