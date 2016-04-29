# Lab 8 Report
Deanna Sessions

## Background
This lab is intended to introduce students to the design, simulation, and analysis of two coupler designs. The Hybrid Coupler and the Rat Race Coupler achieve similar goals with different approaches. The Hybrid Coupler divides the input power equally between the two output ports while the Rat Race Coupler splits the input power between ports 2 & 4 and leaves port 3 isolated, the RRC also has the added quality of phase addition at port 2 and phase subtraction at port 4. 

## Design
David, our wonderful TA, very graciously created these designs in HFSS with it pre-parametrized for design implementation. This meant that the only thing left to do was to calculate the lengths and widths of the microstrip lines and input the values in HFSS for simulation.

Hybrid Coupler:
This design includes Z0 = 50 Ohms on an FR4 substrate that is 62 mil thick. 
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/deannasessions/Lab_8/Lab8_Hybrid_Coupler.jpg)<br>

This design yielded the following design parameters:
Feedline Width = 3.13mm
Coupler X Width = 3.13mm
Coupler X Length = 16.88mm
Coupler Y Width = 5.27mm
Coupler Y Length = 16.48mm

Where Coupler X is the set of strips in the X direction and Coupler Y is the set of strips in the Y direction. These numbers had to be shifted slightly in implementation to achieve the proper response.

Rat Race Coupler:
This design includes Z0 = 50 Ohms on an FR4 substrate that is 62 mil thick.
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/deannasessions/Lab_8/Lab8_Rat_Race_Coupler.png)<br>

This design yielded the following design parameters:
Feedline Width (50 ohm)= 3.13mm
Rat Race Circle Width (70.71 ohm) = 1.68mm
Rat Race Circle Circumference (6*lambda/4) = 103.78mm

## Procedure
This lab didn't require much work beyond the design calculations above and the implementation/simulation in HFSS. After initial simulation, the values were slightly tweaked to achieve the desired response, but this ended up still being off from the milled response as seen in the results below. These simulated values were then compared to measured values of the coupler designs that had been milled. The testing of these designs using the network analyzer is achieved by connecting the VNA to the ports under test and placing matched loads on the other two ports to provide isolation and ensure that there is no unwanted feedback.

## Results and Discussion
Below is the comparison between the measured and the simulated results of the hybrid coupler. There is a very distinct shift from the measured to the simulated that can be attributed to not being able to adjust all of the values enough and also I believe the design frequencies varied so it would be expected to have variation in response.
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/deannasessions/Lab_8/Hybrid_Coupler_S_Parameters.png)<br>

Once again, the phase difference is shifted over between the measured and the simulated results which can be attributed to the same reasons listed above.
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/deannasessions/Lab_8/Hybrid_Phase_Difference.png)<br>

Below is the comparison between the measured and the simulated results of the rat race coupler's S-Parameters. These S-Parameters matched up between the measured and the simulated results.
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/deannasessions/Lab_8/RatRace_S_Parameters.png)<br>

## Conclusion
This lab shed some light on coupler design. The first coupler we examined was the Hybrid Coupler which is a passive and directional device used for dividing the input into the two ports. This could be used as a simple power divider which sees applications in telecommunication and radio. The second coupler we examined was the Rat Race Coupler is used to divide the input power while also having the added functionality of adding/subtracting phase at certain ports. This is often used as a coupler or mixer in RF and microwave circuitry. 

## Hindsight
I wish I had more patience to fix the hybrid coupler in HFSS.

## Reflection
This lab was a comprised mostly of HFSS simulations and I had a bit of difficulty adjusting the Hybrid Coupler design to match the milled result. 
