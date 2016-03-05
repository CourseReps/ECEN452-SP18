# Lab 5 Report
Mazin M Mustafa 

## Background

TRL: 
TRL calibration is a very useful calibration technique. TRL allows us to move the reference planes into the test fixture. This is important in order to cancel the effect of the transmission lines and coaxial connectors.

RF PIN Diode:
The second part is about PIN diode switch design. The purpose of this circuit is to design an RF switch controlled by DC bias. The key point in this design is to isolate the RF circuit from the DC circuit using a bias T. This simply achieved by introducing a high impedance quarter wave-length stub that can produce an open-circuit for RF signal. For the DC signal the circuit will be a short circuit, but also open-circuit from the RF transmission line because because of blocking capacitors.

## Design

TRL:
The calibration kit design for 50 ohm transmission line. The calculations for 50 ohm microstrip is based on the follwoing parameters:

Z0 = 50 ohm
h = 62 mil FR4
Dielectric constant = 4.1
tand = 0.01
fL = 1 GHz
fH = 5 GHz
Refrence plane = 15 mm

fo = (fL+fH)/2 = 3 GHz

Using microstrio equations : 
w = 3.175 mm
Effective dielectric constant = 3.14
Quarter wave-length = 11.36 mm

Based on the discussion in lab 3, the dimension of Line = 41.36 mm. The dimesnion of Thru = 30 mm. The dimension of Refl = 15 mm.

The circuit diagram:
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Mazin-M-Mustafa/Lab5/TRL.png) <br>

RF PIN Diode switch:

The frequency of this design is fo = 2.5 GHz. 

for Z0 = 50 ohm
w = 3.175 mm
Effective dielectric constant = 3.14
Quarter wave-length = 16.94 mm

for Z0 = 100 ohm
w = 3.175 mm
Effective dielectric constant = 3.14
Quarter wave-length = 17.71 mm

The circuit diagram: Source David M. Pozar 
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Mazin-M-Mustafa/Lab5/Circuit.png) <br>

## Procedure
Provide a step-by-step decription of the activities you performed during the lab.

## Results and Discussion
Include measured/simulated Plots here. All plots are to be made in Python by modifying the csv plotter code. Explain how you can tell the device is working by examining the data (S-parameters). Comment on any differences between the measured and simulated results and sources of error.

To embed graphs or diagrams in your README.md file, commit and push the graphs to your LabX folder (I prefer to save them as .png files) and then get the URL link to the file on github. Then use: <br>
`![Plot_Name](https://link_to_image_on_github)` <br>

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Mazin-M-Mustafa/Lab5/Capacitance.png) <br>

See the raw text of the tutorials for an example.

## Conclusion
Summarize the key points in the design and results. Also mention unexpected challenges (if any) in the design and how you overcame them. 

## Hindsight
Comment on anything you know now, having completed the lab, that you wish you knew at the beginning of the lab.

## Reflection
Breifly describe the most challenging parts of the lab and the most rewarding parts of the lab.
