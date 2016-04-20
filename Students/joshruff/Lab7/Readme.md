# Lab X Report
Joshua Ruff

## Background
The Wilkinson Power Divider (WPD) splits all power input to port one between ports two and three. Conversely, any power input to ports two and three is combined and output to port one. Ideally, ports two and three are isolated from one another in this device. 

The phase shifter uses a 50 ohm through as a reference phase, and then uses two longer lines to provide 90 degrees and 180 degrees of phase shift respectively. 

## Design
###Wilkinson Power Divider
The lumped element model for the Wilkinson Power Divider is a simple resistive divider. Transforming these resistors into transmission lines offers better power transfer and isolation. Aditionally, a resistor passed between ports 2 and 3 offers complete isolation between ports 2 and three. The resulting device schematic appears as follows: 

![WPD_Schematic](https://github.com/CourseReps/ECEN452-Spring2016/edit/master/Students/joshruff/Lab7/WPD.jpg)<br>

Zo of the feedlines is 50 Ohms. The characteristic impedance of the quarter wave transformers is 70.1 Ohms. The resistor strung between points two and three is 2*Zo or 100 Ohms. 

To implement this device in microstrip, the phsyical widths of each microstrip line is calculated based on the impeadance. A microstrip line calculator is used to expedite this process. The substrate used is FR4 with a relative permittivity of 4.1 and a height of 62 mil. Thus, the Width of the feedlines comes out to be 3.13 mm. The width of the quarter wave transformers is 1.71 mm, and the length of the quarter wave transformers is 24.4 mm (Later adjusted). 

###Phasse shifter



## Procedure
Provide a step-by-step decription of the activities you performed during the lab.

## Results and Discussion
Include measured/simulated Plots here. All plots are to be made in Python by modifying the csv plotter code. Explain how you can tell the device is working by examining the data (S-parameters). Comment on any differences between the measured and simulated results and sources of error.

To embed graphs or diagrams in your README.md file, commit and push the graphs to your LabX folder (I prefer to save them as .png files) and then get the URL link to the file on github. Then use: <br>
See the raw text of the tutorials for an example.

## Conclusion
Summarize the key points in the design and results. Also mention unexpected challenges (if any) in the design and how you overcame them. 

## Hindsight
Comment on anything you know now, having completed the lab, that you wish you knew at the beginning of the lab.

## Reflection
Breifly describe the most challenging parts of the lab and the most rewarding parts of the lab.
