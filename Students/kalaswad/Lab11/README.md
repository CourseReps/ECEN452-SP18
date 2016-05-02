# Lab 11 Report
Matias Kalaswad

## Background
This lab introduced us to a calibration technique called the Gated Reflect Line or GRL. It is used for free space calibration on devices like the horn antennas that we used in lab.
	
Transforming into the time domain means to use the Fourier transform to go from frequency domain to time domain. The time domain shows signal changes over time and the frequency domain shows how much signal lies in a certain frequency range. The S11 parameter in time domain can be used to locate discontinuities as a function of time. It can show you where unwanted reflections are occurring so you can filter them with gating. This helps with calibration. Putting the reflect in before performing the calibration gives us a reference point to a sort of “ground” for when we actually do perform the calibration.

The three materials measured were very close to the expectations we had; there were no surprise results. A way to improve the calibration process would be to have more sturdy holders for the materials that we were measuring. David said that it would have been beneficial to have the materials be at exactly 90 degree angles with the horn antennas but he had to make the holders out of PBC pipe at the last minute so they weren’t very reliable.

## Design
There was no design required for this lab since it was a demonstration by David.

## Procedure
In lab David demonstrated how the GRL calibration works. David had set up some PBC pipes to hold sheets of different materials. First David calibrated the cables to the horn antennas. Next he placed a piece of Plexiglas in the holders that was the same thickness as the reflect sheet (5.6mm).  He then substituted the glass for a sheet of metal of the same thickness.  Finally, he placed cardboard in the holders to measure it dielectric constant too.  The data was then put through a time domain Fourier transformation.  David explained that “gating” isolated the signal and the graph showed where the measurements took place in time.

## Results and Discussion
Ideally the thru should have very little attenuation, whereas this graph has a very large slope. In reality this result is actually very close to what it’s supposed to look like. If the y-axis showed more dB values, we would be able to see that the S21 values are extremely close to zero, which is what they should be for low attenuation.
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/kalaswad/Lab11/Free_Space_Measurements.png)

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/kalaswad/Lab11/S11_TD_wReflect_preGRLcal.png)

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/kalaswad/Lab11/S21_Thru_postGRL.png)

## Conclusion
The main point of this lab was to see the GRL calibration and watch how the dielectric constants of solids could be measured.  David explained to us that this setup was far from perfect some there was a margin of error that could be seen but for the most part it was an accurate depiction of the process.

## Hindsight
There was nothing else that we wished we had known before the lab because we discussed GRL calibration in class beforehand.  We could have done a little more research to learn about exactly how it operates with different kinds of antennas other than the horn antennas.

## Reflection
This lab wasn’t particularly challenging because it was just a demonstration by David.  It was extremely interesting to see the calibration process and the different dielectric constants of solids since we had previously seen them for liquids. We learned something new from every single lab and it was a very well thought out lab overall. 
