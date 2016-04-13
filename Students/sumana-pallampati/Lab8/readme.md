# Lab 8 Report
Sumana Pallampati

## Background
In this lab, two types of couplers are studied -
* Quadrature (3 dB) Hybrid Coupler - 
![Plot_Name](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/sumana-pallampati/Lab8/Screen%20Shot%202016-04-13%20at%208.27.12%20AM.png)
Port 1 is input; port 2 is output (0 deg) (3 dB); port 3 is output (-90 deg w.r.t. port 2) (3 dB) and port 4 is isolated. Thus, the signal entering through port 1 is split into two quadrature signals (port 2 and 3). The transmission lines are quarter wavelength long.
* Rat Race Coupler - <br>
![Plot_Name](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/sumana-pallampati/Lab8/Screen%20Shot%202016-04-13%20at%208.28.06%20AM.png) <br>
Port 3 is isolated; port 1 is sum and port 4 is difference. We can use it for in phase and out of phase power division and as a power combiner. For equal power split, the impedance of both the lines is 1.414*Z0. 

## Design
* Quadrature (3 dB) Hybrid Coupler - <br>
The width and length of quarter wavelength for a 35.35 ohms (0.707*Z0) line at 2.5 GHz is 5.25 mm amd 16.5 mm respectively.  The width and length of quarter wavelength for a 50 ohms (Z0) line at 2.5 GHz is 3.1 mm amd 16.9 mm respectively.  To centre the port matching S parameters at 2.5 GHz, the lengths of the quarterwave lines had to be increased to 18.7 mm.
* Rat Race Coupler - <br>
The width of the 70.7 ohm (1.414*Z0) line is 1.65 mm. The length of the line is (3/2)*lambda. Which implies, the circumference of the coupler is calculated to be 101.54 mm. This circumference is increased to 103.5 mm to provide a low attenuation for port matching S parameters at 2.5 GHz. 

## Procedure
The calculated widths and lengths of the couplers were inserted in HFSS design files and simulated. The parameters were tweaked a bit so that the input port S parameters have a low attenuation at 2.5 GHz. The simulated results were compared with the measured data.

## Results and Discussion
* The results for a Quadrature (3 dB) Hybrid Coupler -
![Plot_Name](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/sumana-pallampati/Lab8/Input_Port1_Hybrid.png)
![Plot_Name](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/sumana-pallampati/Lab8/Port_Matching_Hybrid.png)
![Plot_Name](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/sumana-pallampati/Lab8/phase_diff_hybrid.png) <br>
* The results for a Rat Race Coupler -
![Plot_Name](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/sumana-pallampati/Lab8/Input_Port1_RatRace.png)
![Plot_Name](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/sumana-pallampati/Lab8/Port_Matching_RatRace.png) <br>
We observe a 3 dB power split from S31 and S21 at 2.5 GHz for both the couplers. For the hybrid coupler, the measured phase difference is around 100 deg and simulated phase difference is around 89 deg between ports 2 and 3 ( calculated from phase(S21-S31)). Ideally the phase should be 90 deg.

## Conclusion
The deesign of a hybrid coupler and rat race coupler is straightforward. In the case of a rat race coupler, we can get an unequal power split by simply changing the impedances of the quarter wave sections. The only challenge was tweaking the lengths to get the correct response at 2.5 GHz.

## Hindsight
The design was easy and the lab strengthened my understanding on couplers. 

## Reflection
I had an opportunity to witness the milling process with David when he was milling the designs of the couplers. 



