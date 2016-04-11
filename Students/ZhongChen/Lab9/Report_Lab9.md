
#Lab 9 Report

Zhong Chen

## Background

In this lab,I will design and simulate a patch antenna. Furthermore,I will match this antenna to 50 Ohms transmission line on the 62 mil thick FR-4 substrate.<br>

## Design

Use the following equations to calculate the length and width of the patch antenna:<br> 
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/ZhongChen/Lab9/Formula.PNG) <br>

Base on FR-4 Substrate:<br>
er = 4.1 <br>
h = 1.5748 mm <br>
f = 3 GHz <br>

We can obtain:<br>
Length L = 24.27 mm <br>
Width W = 31.31 mm <br>

## Procedure
Task 1: Constructe the patch antenna using copper tape <br>
In this task, I use a single stub to match this antenna. <br>
Step 1: Calculate the length and width of the patch, the width of the 50 ohm transmission line. L = 24.27mm, W = 31.31mm, 50ohm transmisson line width W1 = 3.115 mm <br>
Step 2: Cut and solder the copper tape. <br> 

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/ZhongChen/Lab9/Feedline_copper.PNG) <br>

Step 3: Test the unmatched patch antenna and we can get the input impedance = 73+j54,the normalized impedance is 1.46+j1.08. <br>
Step 4: Use smith chart to obtain the stub length. <br>
Step 5: Cut and solder the copper tape.<br>

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/ZhongChen/Lab9/Singlestub_copper.PNG) <br>

Step 6: Measure the patch antenna. <br>


Task 2: Simulate the probe-fed patch antenna in HFSS.<br>
Step 1: Input the patch_length = 24.27mm , patch_width = 31.31mm and probe_feed_x = 5mm into the HFSS model, then run the simulation <br>
Step 2: Look at the VSWR plot to make sure the patch is resonant at 3 GHz and try to get the VSWR at 3 GHz below 1.2 <br>
Step 3: Based on the simulation and knowledge to determine whether to move the probe closer to center or closer to the edge of the patch, rerun the simulation <br>
Step 4: Repeat the Step 2 and Step 3 until we obtain the suitable result <br>

Note:<br>
1.Probe_feed_x = 6mm. <br>
2.I cannot match the patch antenna at 3 GHz only by tuning feed port location. So I change the length of patch antenna into 23.7mm, then it can fully match at 3 GHz and the value of VSWR is below 1.2.<br>


## Results

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/ZhongChen/Lab9/Unmatch_copper.png) <br>

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/ZhongChen/Lab9/Match_copper.png) <br>

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/ZhongChen/Lab9/VSWR_HFSS.png) <br>

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/ZhongChen/Lab9/Smith_HFSS.png) <br>


## Conclusion
The results of measurement data and simulated data are similiar. However, there may be some results are not matched very well. This problem may be coming from that the microstrip line may not be fabricated as precise as simulated model.

## Reflection
No.



