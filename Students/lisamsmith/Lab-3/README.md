# Lab 3 Report
Lisa Smith

## Background
The TRL calibration uses three standards (thru, reflect, and line,) to solve for the error coefficient when using a network analyzer. The TRL calibration accounts for transition effects due to the coax-microstrip connection and allows you to set a reference plane some distance along the feed line. The reference plane is the reflect standard and the thru standard is twice this length. The Line standard then has an extra length added that allows it to operate at frequencies from -20 degrees to -160 degrees from the center frequency.  

## Design
The following are the values given for the TRL kit that was pre-made for lab.
Reflect Length (11 mm) 
Thru Length (22 mm) 
Line Length (28.44 mm) 
Line-Thru = 6.44 mm (**This is the physical length measured after the reference planes are established) 
Substrate thickness (62 mil)

These equations will be used to find the desired values using the measured data.

![lab_3_eq](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/lisamsmith/Lab-3/lab_3_eq.PNG)

## Procedure
In lab, a TRL calibration kit was already designed. Students learned how to calibrate the network analyzer using the TRL kit. Each standard was attached and the magnitude and phase of the S-parameters was measured. The S21 data for the line standard was then used to find the operational frequency range, effective dielectric, phase velocity, and attenuation.

## Results and Discussion
In this lab, the TRL kit was pre-made and no simulations were required. Below are the graphs for the log magnitude of S21 and the phase of S21.
![lab_3_graphs](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/lisamsmith/Lab-3/lab_3_graphs.PNG)

Using the equations from before, the frequency range, effective dielectric, phase velocity, and attenuation are calculated.
![lab_3_values](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/lisamsmith/Lab-3/lab_3_values.PNG)

## Conclusion
The measured frequency range matches the calculated frequency range (varying at most by 0.3 GHz.) This implies that the TRL kit was accurate and should do a good job calibrating the network analyzer. 

## Hindsight
IN my experience, I already knew how to design and use a TRL calibration kit on the network analyzer. However, this was a good refresher on the topic and I did learn how I could find certain values based only on the S21 values of magnitude and phase.

## Reflection
Because this lab was just measuring the pre-made TRL kit, it wasn't very challenging. However this lab did give good insight to how the network analyzer operates and why it needs calibration.



