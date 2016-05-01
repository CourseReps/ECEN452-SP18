# Lab 3 Report
Lisa Smith

## Background
The TRL calibration uses three standards (thru, reflect, and line,) to solve for the error coefficient when using a network analyzer. The TRL calibration accounts for transition effects due to the coax-microstrip connection and allows you to set a reference plane some distance along the feed line. The reference plane is the reflect standard and the thru standard is twice this lenght. The Line standard then has an extra lenght added that allows it to operate at frequencies from -20 degress to -160 degress from the center frequency.  

## Design
`![lab_3_eq](https://link_to_image_on_github)` <br>

## Procedure
In lab, a TRL calibration kit was already designed. Students learned how to calibrate the network analyzer using the TRL kit. Each standard was attached and the magnitude and phase of the S-parameters was measured. The S21 data for the line standard was then used to find the operational frequency range, effective dielectric, phase velocity, and attenuation.

## Results and Discussion
Include measured/simulated Plots here. All plots are to be made in Python by modifying the csv plotter code. Explain how you can tell the device is working by examining the data (S-parameters). Comment on any differences between the measured and simulated results and sources of error.

To embed graphs or diagrams in your README.md file, commit and push the graphs to your LabX folder (I prefer to save them as .png files) and then get the URL link to the file on github. Then use: <br>
`![lab_3_eq](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/lisamsmith/Lab-3/lab_3_eq.PNG)` <br>
See the raw text of the tutorials for an example.

## Conclusion
Summarize the key points in the design and results. Also mention unexpected challenges (if any) in the design and how you overcame them. 

## Hindsight
Comment on anything you know now, having completed the lab, that you wish you knew at the beginning of the lab.

## Reflection
Breifly describe the most challenging parts of the lab and the most rewarding parts of the lab.
ECEN452-Spring2016/Students/lisamsmith/Lab-3/lab_3_eq.PNG

frequency=f 
speed of light=c=3*10^8 m/s
effective dielectric=eff
theta=t 
wavelenght effective=Xg
wavelenght=Xo=.1 m
lenght of Thru=l=.00644 m
propagation velocity=Vp
attenuation=a

f=c/(l*sqrt(eff))(t/360)
Xg=2*pi*l/t
Xg=Xo/sqrt(eff)
Vp=c/sqrt(eff)
a=S21/l