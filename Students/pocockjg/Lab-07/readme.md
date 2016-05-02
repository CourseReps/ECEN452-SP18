# Lab 7 Report
Jared Pocock

## Background
The two devices in this lab is the Wilkinson Power Divider and the Delay Line Phase Shifter. The Wilkinson Power Divider, as its name suggests, can split power without the two ports coupling to each other. The Delay Line Phase shifter can shift an incoming signal a certain amount of degrees based on its design.

## Design
Using the usual online microstrip calculator, we know the parameters of the FR4 board and our design frequency (3 GHz) we can determine the QW length as 14.18 mm. We know that a length of lambda/8 gives us a phase shift of 45 degrees and adding a QW length will add 90 degrees of phase shift. Therefore, the phase shifter will be two lengths of 7.09 mm for a 90 phase shift and two lengths of 14.18 for a 180 degree phase shift.

## Procedure
Provide a step-by-step decription of the activities you performed during the lab.

## Results and Discussion
Include measured/simulated Plots here. All plots are to be made in Python by modifying the csv plotter code. Explain how you can tell the device is working by examining the data (S-parameters). Comment on any differences between the measured and simulated results and sources of error.

To embed graphs or diagrams in your README.md file, commit and push the graphs to your LabX folder (I prefer to save them as .png files) and then get the URL link to the file on github. Then use: <br>
`![Plot_Name](https://link_to_image_on_github)` <br>
See the raw text of the tutorials for an example.

## Conclusion
Summarize the key points in the design and results. Also mention unexpected challenges (if any) in the design and how you overcame them. 

## Hindsight
Comment on anything you know now, having completed the lab, that you wish you knew at the beginning of the lab.

## Reflection
Breifly describe the most challenging parts of the lab and the most rewarding parts of the lab.
