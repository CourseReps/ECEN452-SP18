# Lab 9 Report
Jared Pocock

## Background
The device made in this lab is the patch antenna. To help with the design, David supplied us with the design equations needed. In addition to the patch antenna, a quarter wave transformer (QWT) was also made to impedance match the antenna.

## Design
Using the designs given to us at the beginning of the lab, we found the length and width needed to make the patch resonant for the required frequency. The calculations are given in the following photos. 
![Image](image001.jpg)
![Image](image002.jpg) <br>

I can't figure out how to rotate the images.
## Procedure
The first part of the procedure was to simply to solder the connector onto the board. The next step was to add the 50 ohm feed line to the board. After that, using the dimensions that were found using the equations, the patch antenna was added to the board. After measuring what the impedance of the antenna was, the QWT was calculated and placed onto the feed line of the antenna. The system was then measured again to see how well it was impedance matched. 

## Results and Discussion
From the results, the results were pretty close to the mark. Even being unmatched, the VSWR was still at its lowest around the 3 GHz mark. When the antenna was matched, again the VSWR was still at its best at the 3 GHz mark which is what was wanted and expected.
![image](figure_1.png)
![image](figure_2.png)

With the HFSS file, the patch antenna had to be modified slightly to resonate at 3 GHz. The length had to be reduce to 24 mm to get the proper signal.

![image](figure_3.png)
![image](Smith_Chart_Lab9.jpg)

The VSWR is a little high at the marker frequency. Unfortunately, I didn't have much time to tweak the program to perfection.

## Conclusion
The lab was really successful. Using numbers that we calculated, we got really close with the patch antenna and the QWt that we made. No adjustments were really needed in the lab.

## Hindsight
I wish that I was more knowledgeable in making QWT. Hong did most of the calculations.

## Reflection
It always feels great when something works in a lab, but again I wish I was more familiar with QWT calculations.
