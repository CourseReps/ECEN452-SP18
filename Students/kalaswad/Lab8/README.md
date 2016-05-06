# Lab 8 Report
Matias Kalaswad

## Background
In this lab we worked with the ratrace coupler and the hybrid coupler. Ratrace couplers are used in planar technologies like microstrips and waveguides. It consists of a ring-shaped structure, with four ports, each a quarter wavelength from each other around and impedance factor of sqrt(2) compared to the port’s impedance.  The hybrid coupler is a passive device that is often used in radio and telecommunications. It is a directional coupler with the input power divided equally between two output ports.

## Design
Both couplers were to simulated in HFSS before lab. A screenshot of the hybrid coupler design and the parameters used for simulation are shown below.

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/kalaswad/Lab8/Lab8HybridHFSS.png)

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/kalaswad/Lab8/Lab8HybridParameters.png)

A screenshot of the ratrace coupler design and the parameters used for simulation are shown below.

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/kalaswad/Lab8/Lab8_RatRace_HFSS.png)

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/kalaswad/Lab8/Lab8_RatRace_Parameters.png)

## Procedure
The in-lab portion for this lab was fairly straight-forward. David performed measurements on milled versions of the hybrid and ratrace couplers. We put matched loads on the ports while measuring S-parameters so that reflections from other ports wouldn't interfere. 

## Results and Discussion
The results for this lab matched up very well with the simulated data. This could have been because the couplers were milled instead of put together using less exact methods, such as cutting copper tape. The plots show that the devices worked at the design frequency of 2.5GHz.

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/kalaswad/Lab8/Hybrid_Coupler_Magnitude2.png)

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/kalaswad/Lab8/Hybrid_Coupler_Phase2.png)

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/kalaswad/Lab8/RatRace_Magnitude2.png)

## Conclusion
By the end of this lab we had learned more about the hybrid and ratrace couplers.  David took measurements in lab and gave us the results to compare to HFSS. The results were almost the same.

## Hindsight
This results of this lab helped us realize that the greatest source of error in previous labs was probably coming from inexact measuremnts using the copper tape. 

## Reflection
At this point, HFSS was beginning to get a little easier to work with and understand. I was also glad we didn't have to build our own couplers. 
