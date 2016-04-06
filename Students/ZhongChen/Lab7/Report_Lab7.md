#Lab 7 Report

Zhong Chen

## Background

In this lab,there were multiple designs that were assigned.Four power dividers were simulated in Z0lver and some were simulated in HFSS.The only design that was constructed for this lab was the time delay shifter which will not be talked in this report.The Wilkinson power divider design is based on the following model and operating frequency is 2.5 GHz.
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/ZhongChen/Lab7/Wilkinson_Power_Divider_Model.png) (br)

## Design

Use Microstrip online calculator, parameters can be easily calculated based on above figure and given substrate information (FR-4). Parameters of power divider are set up as:
Feed line width (50 ohm): 3.1298828125 mm
QW line width (70.71067 ohm): 1.6767578125 mm
QW line length (70.71067 ohm): 17.295580370995644 mm
Resistor 2*Z0 = 100 ohm

##Procedure

Input the value above into the HFSS model and simulate.

## Results

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/ZhongChen/Lab7/Wilkinson_port_matching.png) (br)

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/ZhongChen/Lab7/Wilkinson_S21.png) (br)

The following figures are the results of time delay shifter:

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/ZhongChen/Lab7/thru%2Cs11M.png) (br)

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/ZhongChen/Lab7/thru%2Cs11P.png) (br)

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/ZhongChen/Lab7/thru%2Cs21M.png) (br)

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/ZhongChen/Lab7/thru%2Cs21P.png) (br)


## Conclusion
The results of simulated data and measurement data are close to each other basically. However, there may be some parameters such as S32 are not matched very well. The center frequency shifts about 1.5 GHz. The problems may be coming from the microstrip lines which may not be fabricated as precisely as simulated model.

## Reflection
No.

