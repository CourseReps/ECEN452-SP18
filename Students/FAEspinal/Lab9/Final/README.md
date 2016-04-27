# Lab 9 Report
Francisco Espinal

## Background
In this lab we created a micro strip patch antenna. A patch antenna is a low profile antenna that is becoming more popular because of its advantages over other antennas. They are lightweight, inexpensive, very easy to fabricate, and can radiate power in certain direction with great efficiency.    

## Design
We used a Z_0 = 50 ohms reference impedance on a 62mil thick FR4 (e_r=4.1, tan d = 0.01) substrate to support a frequency range of 1 GHz to 5 GHz.  For part A we used the following equations to solve for the width and length of the patch. 
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Labs/Lab9/Final/LandW.png) <br>
With these design specification we were able to use an online calculator to find the dimensions needed for the devices. And to find the lengths of stub for part B, I use the following equation. 
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Labs/Lab3/Equation.png) <br>

## Procedure
First, I started off by calculating the lengths and widths of the patch antenna using the equations given above.  With these dimensions, I cut the copper tape and placed the patch on to the FR4 substrate. I then attached a 50-ohm transmission line to get the unmatched measurements. From here we matched our antenna with a stub. The stub was calculated using smith chart techniques. We attached the stub and got our match measurements. Next, I ran simulations on HFSS using the values calculated. I had to adjust the length to get it to resonant at 3GHz. Then I had to adjust the probe until the design was matched at 3GHz.   

## Results and Discussion

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Labs/Lab9/Final/VSWR.png) <br>

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Labs/Lab9/Final/smithchart.jpg) <br>


## Conclusion
Everything ran as expected.  Compare your results to the patch antenna you made during the lab session. Design objective. 

## Hindsight
NA

## Reflection
The lab was straightforward, no changes are recommended. 

