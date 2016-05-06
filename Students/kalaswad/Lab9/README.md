# Lab 9 Report
Matias Kalaswad

## Background
In this lab we made and measured the design of a patch antenna. They are frequently used in mobile devices because they are relatively cheap and easy to manufacture.

## Design
We designed two different networks in this lab. The first was the general patch antenna with an operating frequency at 3 GHz, then we added a stub in order to have a quarter wave matching network. We used the following parameters in HFSS and obtained the Smith chart seen below.

	width = 31.3 mm
	ε_eff = 3.774
	△L = 0.73 mm
	L = 24.2 mm

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/kalaswad/Lab9/Patch_Antenna_HFSS.PNG)

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/kalaswad/Lab9/lab9_SmithChart.PNG)

## Procedure
In lab we built the general patch antenna with just a 50 ohm feed line out of copper tape and then had David test it with the network analyzer to show the operating frequency and impedance of the antenna. David then told us to implement the single stub tuner using the Smith chart to calculate the dimensions of the stub. Our antenna’s impedance was 57.75-j52Ω which we normalized with 50 ohms and plotted on the Smith chart. Then the point was rotated a quarter wavelength in order to match the network. To find the length, we rotated the point until we hit the VSWR = 1 circle. We also used the equation Z_0= √(Z_OT*Z_L )= √(50*20)=31.62Ω. When David ran our circuit through the network analyzer again, we were able to see that the operating frequency was 3.066 GHz.

## Results and Discussion
The measured SWR of our matched patch antenna was between the unmatched measurement and the matched simulated data. All three were relatively close to each other, which is good. 

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/kalaswad/Lab9/Patch_Antenna.png)

## Conclusion
The main point of this lab was to show us the design process of building a patch antenna.

## Hindsight
It would have been helpful to review concepts from ECEN 322 such as how to use a Smith chart to match a quarter wave network. 

## Reflection
This lab required more calculations than other labs, especially during the lab itself. We spent a lot of time making sure our values were reasonable. Using the Smith chart again brought back memories of ECEN 322. It was also fun to be able to build a patch antenna. 
