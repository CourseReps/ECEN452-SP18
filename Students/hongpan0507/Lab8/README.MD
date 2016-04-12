# Lab X Report
Hong Pan

## Background
1. Hybrid Coupler is a 4 port symmetric device that splits power equally with 90 degree of phase shift.
![Hybrid](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/hongpan0507/Lab8/plotting/hybrid.jpg)
2. Rat-race Coupler has 2 operation mode
  + power split: 
      + divide input power from port 1 equally with 180 degree of phase shifte between port 2 and port 3. Port 4 is isolated.
      + divide input power from port 2 equally with 0 degree of phase shifte between port 1 and port 4. Port 3 is isolated.
  + combine input signal from port 1 and 4
      + summed output is at port 2
      + substracted output is at port 3
![rat race](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/hongpan0507/Lab8/plotting/rat_race.jpg)      
  
## Design
### Hybrid Coupler
#### Specification: operating frequency = 2.5GHz; Z0 = 50ohms

### Rat-race Coupler
#### Specification: operating frequency = 2.5GHz; Z0 = 50ohms

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
