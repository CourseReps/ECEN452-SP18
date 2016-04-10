# Lab Report 9
Thomas Darden

## Background
For this lab we will be designing and building a patch antenna and a patch antenna with a QWT. Our design will have the design parameters of 3GHz frequency, 50ohm feed line, and 62mil FR4 board. We will design these antennas and test them with the network anaylzer to see if they work. Then we will use the antenna design we create and use it in an HFSS file. This HFSS file will have a probe feed. We will find the correct length of the antenna and position of the feed probe to find the best response for the antenna.

## Design
A patch antenna can be descibed in the following diagram:
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/td2016/Lab9/PatchAntenna.PNG)<br>
For our design, our feed line will actually be 45mm long. This will allow us enough room to add the QWT later. 
To design this patch antenna, we must use the following equations:
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/td2016/Lab9/Equations.PNG)<br>

From these equations we can find our parameters.

W = (3*10^8/(2*3*10^9)) * sqrt(2/5.1) = 31.3mm

Eff = 5.1/2 + (3.1/2)*sqrt(1 + 12(1.5748/31.3)) = 3.774

deltaL = 0.412 * (1.5748*10^-3) * ((3.774 + 0.3)(31.3/1.5748 + 0.264))/((3.774 - 0.258)(31.3/1.5748 + 0.3)) = .732mm

L = (3*10^8)/(2*3*10^9*sqrt(3.774)) - 2 * .732*10^-3 = 24.3mm

Knowing the impedance of the feed line, we find the length of the feed line to be 3.11mm.

This gives us all of the parameters we need to construct the patch antenna.

After we test the antenna with the network analyzer, we now alter the antenna to include a QWT. This is illustrated in the following graphic:
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/td2016/Lab9/PatchAntennaQWT.PNG)<br>
The results from the test of the patch antenna gave us a real impedance of 61.8ohms and an imaginary impedance -63.7ohms at 3GHz. When normalized, this gives us an impedance of 1.236-j1.274. When we rotate this value clockwise to the generator we find the distance to be .324*wavelength and an impedance of .345. From this information we must find the impedance of the transform. 

Z = .345 * 50 = 17.25ohms

Z_quarterwave = sqrt(50*17.25) = 29.368ohms

From this impedance, we find the width to be 6.76mm and the length to be 13.5mm. 

The means the distance from the 15mm reference plane must be .324*(13.5*4) = 17.496mm. 

After the QWT has been attached we must measure the patch antenna with the network analyzer.

## Procedure
Measure and cut the copper tape to the design parameters found in the previous section. Attach the cutout to the substrate and solder on the coax connector. Measure the results with the network analyzer and make sure the design works as intended.

Add the QWT to the antenna with the design parameters detailed in the previous section. Measure the results.

Modify the HFSS file to the design parameters found for the patch antenna. Alter the length of the patch antenna and the probe distance until the response of the antenna is as required. 

## Results and Discussion
From the unmatched patch antenna we designed, we got the following data from the network analyzer:
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/td2016/Lab9/PA_Impedance.png)<br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/td2016/Lab9/PA_VSWR.png)<br>
This shows that our antenna does indeed work but is not matched.

From the QWT we designed, we measured the following graphs:
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/td2016/Lab9/QWT_Impedance.png)<br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/td2016/Lab9/QWT_VSWR.png)<br>
From these graphs we see that our antenna is indeed matched and we have a minimum at 3GHz in the VSWR, which we want. 

From the HFSS design files we created, I found that the length of 23.7mm and a probe distance of 5.55mm gave us a good matched response from the antenna. I determined this from the following Smith chart and VSWR graph given from HFSS:
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/td2016/Lab9/SmithBackup.PNG)<br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/td2016/Lab9/VSWR.PNG)<br>
The VSWR graph can be expanded to show the full range as shown below:
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/td2016/Lab9/VSWRFull.png)<br>
From this data, we can see from the minima in the VSWR around 3GHz and the close to perfect matching on the Smith chart, that our design and probe location is correct.

## Conclusion
From this lab I was able to see how to design a patch antenna and modify the response of the antenna with a QWT. I was also able to see from the HFSS file how to a feed probe can modify the response of the antenna so greatly and how it can eliminate the need for a transform. 

## Hindsight
After performing this lab, I think it would have been easier to solve the HFSS file if we have any idea of where the probe is supposed to be. A random inital guess is not very comforting to do, though it does allow us to find (albeit slowly).

## Reflections
Overall, this lab was fun and I was able to learn how to build a patch antenna. My favorite part was the construction of the antenna, however, the burnt substrates were rather annoying. My least favorite part was, again, the random guess and check method of determining the accurate probe location.
