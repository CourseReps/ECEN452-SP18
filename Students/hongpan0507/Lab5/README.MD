# Lab 5 Report
Hong Pan

## Background
TRL is a calibration kit that performs VNA calibration which is unique to the transmission line implemented on a device.
It has the advantage of shifting the reference plane to any kind of transmission line that the device is attached.

Pin diode is DC voltage controlled RF switch.

## Design  
   + Design Parameter 
     + Z0 = 50ohms 
     + FR4 substrate height = 62mil
     + dielectric constant = 4.1
     + Frequency Range = 1GHz to 5Ghz
     + referecen plane = 15mm beyond SMA probe end launch
   + Calculation
     + Microstrip width = 3.07mm; [microstrip line calculator](http://www1.sphere.ne.jp/i-lab/ilab/tool/ms_line_e.htm)
     + Center Frequency = 3GHz
       + effective dielectric constant = 3.2
       + quarter wavelength = 14mm
     + Reflect length = 15mm; Reflect provides high reflectivity required by the VNA TRL calibration
     + Through length = 30mm; Through sets the reference plane
     + Line length = through length + quarter wavelength @ 3GHz = 44mm; Line implements transmission line characteristic impedance
     
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
