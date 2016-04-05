# Lab 6 Report
Hong Pan

## Background
Filters eliminate or preserve frequency contents based on the filter response.  
There are four types of microwave filters: high pass, low pass, band pass, and band stop.

## Design
The parameter has been provided in the pre-lab document.  
The basic design procedures are:  
1. Select the Nth order of filter based on the specification.  
2. Use look-up table to find the coefficients  
3. Use Richard’s Transformation to convert lumped element to stubs  
4. Use Kuroda’s identities to provide spacing between stubs  

## Procedure
1. Based on the parameters provided by the pre-lab, the length and width for different T lines are determined using microstrip online calculator  
2. T lines are assembled to form a 5th order band stop filter.

## Results and Discussion
By comparing the simulated magtidue data with meausured data, the simulation has slightly higher frequency band than designed frequency band.
s11 magtidue is high over the operating frequency band, and s21 magtidue is very low (-50dB). The device is consistant with band stop 
filter behavior.  
The phase of the filter is very distored in the stop band and relatively linear outside of the stop band.
![s11 mag](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/hongpan0507/Lab6/plotting/s11_mag.png)
![s21 mag](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/hongpan0507/Lab6/plotting/s21_mag.png)
![s11 phase](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/hongpan0507/Lab6/plotting/s11_phase.png)
![s21 phase](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/hongpan0507/Lab6/plotting/s21_phase.png)

## Conclusion
The calculation for the filter design is straight forward, but book keeping must be done right to avoid introducing calculation errors when 
doing the transformation for the stubs and adding space between the stubs. The tuning of the filter becomes harder after the transformation.

## Hindsight
Having successfully built a 5th order band stop filter with copper tape is a very rewarding experience.
