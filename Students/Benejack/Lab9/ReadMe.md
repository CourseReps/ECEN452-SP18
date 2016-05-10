# Lab 9 Report
Benjamin Jack

## Background
The microstrip patch antenna is a simple and cheap antenna which is useful in many different applications such as cell phone towers. The patch antenna is useful for a broad radiation width and shorter distances.

## Design
We use the equations below to calculate the width and length of the patch antenna for our design.
We have the following parameters: f = 3GHz, Er = 4.1, h = 1.5748mm and Z0 = 50 ohms. From this we calculate W = 31.3mm and L = 24.4mm.
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Benejack/Lab9/PatchEquations.PNG)<br>

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Benejack/Lab9/Patch.PNG)<br>

We used a single stub tuning network to impedance match our antenna. We measured our impedance at a 15mm reference plane to be 73 + j54 ohms.
This gives a normalized load impedance of 1.46 + j1.08. We plotted this on the smith chart and drew the VSWR circle around 2.5 and then converted our
impedance to an admittance y = .44 - j.32. Rotating toward the load, we moved from .441 to .339 lambda, giving us a differnce of .102lambda, which is equivalent
to moving in 5.727mm from our reference plane. Our normalized admittance at this location was approximately -.95j. By plotting a stub with admittance .95j on the Smith 
chart and then rotating from the open circuit admittance on the left hand side of the chart, we calculated a stub length of .121lambda or 6.793mm
All of your calculations go here. Include relevant dimensions and/or diagrams. Comment on any modifications you had to make to your original design after simulation and include you rationale for making these modifications.

## Procedure
In labe we performed the calculations above to calculate our patch antenna dimensions. After the calculations we cut the antenna out of copper tape and then used the network analyzer
to measure the input impedance to the patch at a 15mm reference plane. After this measurement, we used a Smith chart to calculate the stub length and placement to impedance match the antenna.
We remeasured the VSWR of the resulting matched network and ended up with a VSWR around 1.07.

## Results and Discussion
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Benejack/Lab9/Unmatched.png)<br>
The first plot shows the VSWR of our copper tape patch antenna across the entire bandwidth. The VSWR is a minimum around 3.1 GHz and has a value of 2.59. This is a reasonable value for a patch antenna which has not been matched to the line yet.

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Benejack/Lab9/Match.png)<br>
The second and third images show the impedance matched antennas for both the HFSS design and the copper tape antenna. The resonant frequency for the tape antenna was a bit high because the length of the patch antenna was too long. When designing the antenna, reducing the length of the patch
increases the resonant frequency. After impedance matching, both the measured and simulated patches had a VSWR of 1.11 at the minimum. For the HFSS design, moving the position of the coaxial feed closer to the edge of the antenna rotated the impedance match clockwise on the Smith chart.
In HFSS, the patch antenna dimensions were: L = 23.7mm, W = 31.3mm and probe feed 5.9mm from center (along the length axis).

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Benejack/Lab9/VSWRZoom.png)<br>

## Conclusion
The equations we used for our patch antenna depend on the theoretical calculations for our patch antenna as well as some 'error' terms which are used to account for fringing and other effects at the border of the patch antenna, so it is important to take these factors into account when
designing the patch antenna. Other than that, the design is pretty straight forward other than remembering we have a 15mm reference plane when placing the stub and remembering to rotate toward the load instead of toward the generator on the Smith chart measurements.

## Hindsight
There were not any complications in this lab, but the most complicated part is understanding the error calculations when designing the antenna, but the details are not critical for the patch antenna design here.

## Reflection
The most challenging part of this lab was using the Smith chart to calculate the stub lengths and distance from the reference plane, although it was not complicated because we have done it many many times before. It was slightly different to see the physical circuit constructed and
calculate from that rather than just from a schematic diagram. Getting an impedance matched antenna was the most rewarding part of the lab, because we could see the theoretical side come into play in a very tangible way and see the before and after of our patch antenna design.
