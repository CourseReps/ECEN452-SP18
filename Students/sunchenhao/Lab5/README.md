# Lab 5

## Task 1
### Step1 ~ Step2

  Line Width of 50 Ohm TL and Length of QuaterWave length was calculated by the online microstrip line calculater. 
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/sunchenhao/Lab5/Task1/T1_S1.png)

### STep3 ~Step4
  After simulation, we find that Thru's phase and loss are basicly 0
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/sunchenhao/Lab5/Task1/T1_S4_Thru_Phase.png)
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/sunchenhao/Lab5/Task1/T1_S4_Thru_Mag.png)

  Then I try my best slightly change Line's length to make it 90Deg Phase at 3GHz. Although failed, but basicly make it 90Deg.
  SO the correct length now can be found.
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/sunchenhao/Lab5/Task1/T1_S4_Line.png)

Then the phase volocity can be calculated
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/sunchenhao/Lab5/Task1/Phase_Volocity.jpg)

For the reflect, I use excel to fit curve
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/sunchenhao/Lab5/Task1/Curve%20Fiting.png)

Finally, here are the comparation between measurement and my simulation data.
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/sunchenhao/Lab5/Task1/Line_dB_Comp.png)
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/sunchenhao/Lab5/Task1/Line_Phase_Comp.png)

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/sunchenhao/Lab5/Task1/Thru_dB_Comp.png)
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/sunchenhao/Lab5/Task1/Thru_Phase_Comp.png)

Well, I think the difference between simulation and measurment is very small so can be tolerated.


## Task 2
### Step1
  50 Ohm TL width is already calculated in task1, so I use the same online calculator to get the width of 100 Ohm, and so as the length of Quaterwave TL
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/sunchenhao/Lab5/task2/Line_Width.png)
  
### Step2
  Based on the width and length I got, I change the simulation files and get the results. Then slightly change the length of SSG and SCB to make the insertion loss is lowest at 2.5GHz
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/sunchenhao/Lab5/task2/T2_LSSG_InsertionLoss.png)
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/sunchenhao/Lab5/task2/T2_Lscb_InerstionLoss.png)
  
### Step3
  So based on the tuned length, we can simulate the final results
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/sunchenhao/Lab5/task2/T2_On.png)
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/sunchenhao/Lab5/task2/T2_off.png)

### Step4
 So here are the comparation between measurement and simulation
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/sunchenhao/Lab5/task2/S11_on_Comp.png)
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/sunchenhao/Lab5/task2/S21_On_Comp.png)
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/sunchenhao/Lab5/task2/S11_Off_Comp.png)
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/sunchenhao/Lab5/task2/S21_Off_Comp.png)

I think the difference between these two is small, so can be tolerated.

#END
