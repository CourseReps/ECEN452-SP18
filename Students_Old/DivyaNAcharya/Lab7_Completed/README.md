# Lab 7: Wilkinson Power Divider and Phase Shifter
Divya Acharya 

#Task1: Design of Wilkinson Power Divider

## Background
The Wilkinson power divider is a lossy 3-port network which has all its ports matched and has isolation between each of its output ports. Although power can be split in any arbitrary ratio, we consider the equisplit design implemented in microstrip.
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/DivyaNAcharya/Lab7_Completed/WPD.PNG)

## Design
-Center Frequency= 2.5GHz
-Zo=50ohms
-Characteristic Impedance of divider strips=Z0*sqrt(2)=70.7ohms
-Width of divider strip=1.65mm
-Length of divider strip(lambda/4)=17.36mm
-R=100ohms

##Procedure
- The design values calculated above were simulated in HFSS
- To simulate the design in z0lver file, the 70.7ohms line was split into 2 stubs of 1/8lambda each as per z0lver design given (shown below):

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/DivyaNAcharya/Lab7_Completed/WPDZolver.PNG)
- The Frequency range and steps needed to be changed to 1GHz to 5GHz and 1MHz respectively
- Wilkinson divider fabricated by David was used for lab measurements

## Results and Discussion
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/DivyaNAcharya/Lab7_Completed/S11.png)
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/DivyaNAcharya/Lab7_Completed/S22.png)
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/DivyaNAcharya/Lab7_Completed/S33.png)
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/DivyaNAcharya/Lab7_Completed/S21.png)
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/DivyaNAcharya/Lab7_Completed/S31.png)
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/DivyaNAcharya/Lab7_Completed/PhaseWPD.png)

###Q&A
1. Why do we need the resistor in the power divider design?
<br>A three-port network cannot be simultaneously lossless, reciprocal, and matched at all ports. If any one of these three conditions is relaxed, then a physically realizable device is possible. Hence in case of Wilkinson power divider adding the resistor makes it lossy hence we get ports matched along with isolation between output ports.

2. What modifications did you have to make to the T-line widths/lengths to improve your simulated results?
<br>Acceptable simulation results were obtained using the calculated values so no changes needed to be made.


## Observations
- Plots for S11, S22 and S33 show less than -10 dB at 2.5GHz as required. S22 and S33 plots are almost identical as expected since both the ports are identical.
- Isolation between ports 3 and 2 is apparent from the S32 plot. 
- Magnitude for S21 and S31 is above -5dB
- As expected the phase for S21 and S31 are equal. However, the phase values don't agree for z0lver Measured and HFSS. HFSS phase is "wrapped"

#Task2: Design of Phase shifter

## Background
Altering the value of length of a microstrip line alters the phase of the signal recieved on the other end. By choosing an appropriate length of line, any value of  phase shift can be achieved.

## Design
- Center Frequency= 2.5GHz
- Phase Shift 90deg achieved by additional 1/4 lambda line 
- Phase Shift 180deg achieved by additional 1/2 lambda line

##Procedure
- 50ohm line copper strip was placed and measured for reference and corresponding phase value was noted down
- 1/4 (14mm=>2*7mm vertical strips)lambda line was placed and measured to see phase shift of 90deg w.r.t to reference value
- 1/2 (28mm=>2*14mm vertical strips)lambda line was placed and measured to see phase shift of 180deg w.r.t to reference value

## Results and Discussion
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/DivyaNAcharya/Lab7_Completed/S11PhaseShifter.png)
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/DivyaNAcharya/Lab7_Completed/S11PhaseShifter_Phase.png)
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/DivyaNAcharya/Lab7_Completed/S21PhaseShifter.png)
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/DivyaNAcharya/Lab7_Completed/S21PhaseShifter_Phase.png)

###Q&A
1. How did the presence of the additional microstrip lines affect the Thru measurement (difference between Thru and Thru2)?
<br> Thru with coupling resulted in higher S11 (more loss) but the S21 value was visibly unaffected.

2. How could you improve the performance of your phase shifter if you had time to make a new one?
<br> Our implemented design didn't give acceptable 90deg phase shift. The length of vertical copper strips required to obtain 90deg phase shift was 7mm vertical strip. A small change in this value when implemented could affect the phase shift drastically. a solution to this could be using 3/4 lambda line instead of 1/4 lambda to get a higher length for strip and hence reduce the margin of error while implementation.


## Observations
- For the phase shifter, given the smaller dimension of 1/4 lambda, it is more sensitive to error and hence the phase shift of 90deg was difficult to attain.

## Conclusion
- The labs helped understand the functioning of wilkinson power divider and phase shifter.

##Hindsight
- A more careful placement of copper tapes for 90deg phase shift considering it's sensitivity to slight changes in length might have resulted in better result for 90deg phase shift.
