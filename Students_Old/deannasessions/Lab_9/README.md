# Lab 9 Report
Deanna Sessions

## Background
This lab is an introduction to the patch antenna, a simple, linearly polarized antenna that can be used in many applications. This lab was an exercise in designing and tuning a patch antenna by adjusting the length, width, and feed position based on the desired frequency. The designs were then simulated in HFSS and fabricated using copper tape.

## Design
There are three ways to go about designing this patch. All designs are operating at 3 GHz and are fabricated on a board of FR4 (dielectric constant of 4.1 and height of 62 mil.) The first option is to design a patch with a feed probe feeding the patch directly. This was simulated in HFSS and requires basic calculations based on wavelength for the length and the width, but then the feed position must be adjusted according to the results. Moving the feed closer to the edge of the patch will result in the response tending to the short circuit (left) side of the Smith Chart, while moving the feed closer to the edge of the patch will result in the response tending toward the open circuit (right) side of the Smith Chart. 

The designs that were fabricated during lab were fed by microstrip and there were two options for doing so, quarter wavelength transform and stub matching. Either option would have worked for the purposes of the lab, but the stub matching ended up being the the simplest to implement. This design was calculated using the equations in the lab handout and resulted in a length of 2.43 cm, a width of 3.131 cm, a delta L of 7.523e-4m, and an effective dielectric constant of 3.774. After the patch was fabricated with a 50 ohm microstrip feed line, it was measured using the network analyzer to test for impedance. The measured impedance was Z = 100 + j34 and this was used as the starting impedance for a stub tuning problem using a Smith Chart. The values that resulted from the stub tuning were a stub length of 7.625mm and a distance from the generator of 7.480mm. This design resulted in a measured result of VSWR = 1.13 at a frequency of 3.015 GHz. 

## Procedure
The majority of the lab was in the design portion. The patch length and width were calculated and then the probe position was adjusted within HFSS for simulations and a tuning stub was implemented on the fabricated models. While determining the feed position it came down to a game of trial and error to move the feed closer to the center of the patch for the desired response.

## Results and Discussion
The following graph depicts the VSWR of the three measurements taken of the patch antenna. The blue trace is the fabricated antenna prior to being tuned using a stub matching network. The red trace is the same fabricated patch antenna, but including a stub matching network. The green trace is the VSWR of the simulated patch using a feed probe within the patch area.
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/deannasessions/Lab_9/Lab9_patch.png)<br>

## Conclusion
This lab taught about patch antennas and the simple equations required to design them. Patches are very easy to design and fabricate so it is advantageous to know the theory behind them to implement for many different applications.

## Hindsight
Nothing of note. These patches were fairly straight forward in design and implementation.

## Reflection
This lab was a good introduction to patch antennas and showed the wide range of possibilities for their tuning in fabrication. 
