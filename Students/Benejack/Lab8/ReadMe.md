# Lab 8 Report
Benjamin Jack

## Background
The 3dB hybrid coupler is used to provide two outputs which are 90 degrees out of phase and have an equal (3dB) power split between the two output ports. The fourth port is isolated and should not have an output.
The 180 degree rat-race coupler has similar purpose to the hybrid coupler, but the rat race coupler provides two outputs which are 90 degrees out of phase with the input but in opposite directions. The fourth port
is once again the isolation port and has no output.

## Design
For the hybrid coupler, the feed line was a 50 ohm line and the operating frequency was 2.5GHz so the line widths of the vertical sections and feed lines were 3.09mm. The vertical sections were a quarter wavelength, or 16.9mm long.
The horizontal sections of the hybrid coupler had a characteristic impedance of Z0/sqrt(2) which gives 35.5 ohms and a line width of 5.25mm. The quarter wavelengths were 16.5mm. 

*Hybrid Coupler
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Benejack/Lab8/HC.png)<br>

For the hybrid coupler, I modified the length of the 35.5 ohm sections to lower the operating frequency of the circuit. When I first put my design into HFSS, the operating frequency was too low. When I changed the length of the 35.5 ohm
section to 20mm, I ended up with the correct operating frequency around 2.5GHz. I added length to this section because if we increase the length of this section, we are increasing what should be a quarter wavelength and theoretically
increasing the wavelength and thus decreasing the associated frequency of our operating point. I think this discrepancy is just from the nature of microstrip with the different ways corners can be cut and spurious coupling effects.

*Rat-Race Coupler
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Benejack/Lab8/RR.png)<br>

I did not have to make any changes to the rat-race coupler design in HFSS.

## Procedure
*No lab this week

## Results and Discussion
For the hybrid coupler magnitude output, we see almost exactly what we would hope for. There aren't any notable differences between the measured and simulated data. Ports S21 and S31 sit right around a 3.5dB loss, which is slightly worse than
the desired 3dB. However, the power split is approximately even, as desired. The S11 and S41 parameters show that, at 2.5GHz, there is no reflection to port one and port four is isolated from the input signal.
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Benejack/Lab8/HCOutputMag.png)<br>

The phase difference between S21 and S31 is right around 90 degrees, as we should expect, at 2.5GHz. However, as the frequency increases, the simulated and measured data do not follow closely. One reason for this might be how I modified the length
of the 35.5 ohm sections of my coupler. I believe it also may have affected the phase difference here as I did not change both the horizontal and vertical sections of my coupler to get my desired operating frequency. This also may have attributed to
some port mismatch and why our signals at S21 and S31 had a little over 3dB loss.
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Benejack/Lab8/HC_Phase_Difference.png)<br>

For the rat-race coupler, we see almost the same behavior as with the hybrid coupler and the HFSS results match the milled results even more closely. The exception is the HFSS file has a slight curve in the S11 plot at 2.5GHz which gives it a slightly
wider bandwidth than the milled circuit. I don't know why this would happen in HFSS alone except maybe the milled result is not as precise. However, that hardly explains much here and it is a minor difference. As we expected from the design, ports four
and one are drastically attenuated at the design frequency of 2.5GHz, while ports two and three have an even power split - around 3dB loss from the input signal.
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Benejack/Lab8/OutputMag.png)<br>

## Conclusion
It is important to put matched loads on the ports we are not measuring during these measurements so that none of the input signal is reflected back out of these ports. For example, if we are measuring port three with an input signal at port one, we need
to match ports two and four so that it doesn't appear that a small input signal is coming from port two/four from reflections. The hybrid coupler is better for applications which are lower than 40 GHz. The rat-race coupler has been used up to higher frequencies,
but the rat-race coupler is better for designs which do not require a bandwidth over 20-30%.
The main points of each design is the distance between the different ports. The quarter wavelength segments allow for the different phase shifts at the design frequency and also allow us to isolate port four. The ninety degree increments get the simple phase
shifts we want at each port, and our line impedances are matched by using quarter wave transformer concepts, just with multiple ports. 
