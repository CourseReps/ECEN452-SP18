# Lab 8 Report
Joshua Ruff

## Background
The Hybrid coupler and Rat Rase couplers are four port divices in which the power input into one port is divided between two output ports and isolated from the fourth. The Hybrid coupler provides 90 degrees of phase shift in the out of phase port, while the Rat Race coupler provides 180 degrees in the out of phase port. The phase difference on the rat-race allows it to be used to output the sum and difference of input signals. 

## Design
###Hybrid Coupler
All interconnections of the hybrid coupler are quarter-wave. In the diagram, the vertical strips match the feedline impedance (50-Ohms), while the horizontal strips are scaled down to 35-Ohms. A microstrip line calculator was used to determine the physical lengths and widths. The 50 Ohm lines had a width of 3.13 mm and a length of 16.88 mm. The 35 Ohm lines had a width of 5.27 mm and a physical length of 16.47 mm. 


###Rat-Race Coupler
To achieve an equal power split, the interconnections in the Rat-Race coupler are all equally set to root 2 times the feed line impedance, or 71 Ohms. The three smaller interconnections are all quarter wave in length, while the longer interconnection is three-quarters of a wavelength long. Using the microstrip calculator, the feedline is determined ot have a width of 1.71 mm, and a length of 17.7 mm. The feedline had a width of 3.13 mm. 

## Procedure
These devices were designed and simulated in HFSS, and optimized as necessary. Afterwards they were compared to versions of the devices which were fabricated by a milling machine. When measuring S-parameters, matched loads were placed on each port to prevent signal from being reflected back into the device by unused ports. Such a reflection would prevent lead to an innacurate measurement. 

## Results and Discussion
###Hybrid Coupler
![Hybrid-S](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/joshruff/Lab8/Data/Hybrid-S.png)<br>
![Phase_Diff](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/joshruff/Lab8/Data/Phase_Diff.png)<br>
###RatRace Coupler
![RatRace-S](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/joshruff/Lab8/Data/RatRace-S.png)<br>
## Conclusion
Summarize the key points in the design and results. Also mention unexpected challenges (if any) in the design and how you overcame them. 

