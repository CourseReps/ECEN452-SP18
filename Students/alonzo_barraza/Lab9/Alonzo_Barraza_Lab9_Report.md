# Lab 9 Report
Alonzo Barraza 

## Background
Lab 9 consisted of studying a simple patch antenna and how to use different techniques to impedance match the patch and a feed line. The lab required the calculation for the dimensions for the patch antenna and implementing those values into a copper tape design similar to previous labs.    

## Design
There was only one design that had to be done before the measurement part of the lab. The parameters for the this particular patch antenna were an operating frequency of 3GHz, dielectric constant of 4.1 (FR4), height of 1.5748mm (62mil), and characteristic impedance of 50ohms (Z0). With these parameters the values for the width and the length of the patch antenna could be calculated with the given equations in the lab handout. In order to find the length, the effective dielectric and the length due capacitance had to be taken into account. This is because the microstrip patch antenna adds additional length to the overall physical length. Once the width (31.3mm), effective dielectric (3.77), and the change of length (.7323mm) were found the length was calculated to be 24.3mm.  

## Procedure
With the patch antenna dimensions calculated the design could be built with copper tape. The first design consited of only the patch antenna with a 40mm 50ohm feed line. The width for the feed line was calculated at 3GHz (3.09mm) instead of the previous labs which the width was for 2.5GHz. Though this was a small change it is important to always calculate for the operating frequency. When the copper tape design was constructed, the patch antenna was connected to the network analyzer where the VSWR and the impedance were measured. For this particular patch antenna the VSWR was 2.4 and the impedance was 100+j34 ohms. Typically a good VSWR is below 2, so in order to not achieve this but to also match the feed line and the patch antenna, a single-stub tuner was implemented.

The design process for the stub required the use of the Smith Chart. First the impedance was normalized to 50ohms, making the complex impedance equal to 2+j0.68 ohms. Once located on the Smith Chart, the point was rotated by a quarter-wavelength in order to get the admittance (Y_A = 0.45-j0.17 S) which is neccessary for stub-matching. The length from the generator was found by moving from Y_A towards the load until the constant reactance circle 1 was crossed. The distance traveled was 0.133*effective_wavelength (7.48mm) and the stub length came out to be 0.1145*effective_wavlength (6.4mm). With these two values, the stub could be implemnted to the feed line. Once added on the design was connected to the network anaylzer agin. The result this time showed a VSWR of 1.13 at 3.015GHz, therefore a succesful matching network was implemented.

Using a quarter-wave transform is another viable matching technique that could have used for this lab.

## Results and Discussion


## Conclusion
The matching network for a patch antenna is a straight foward design and can be easily implemented. This is useful because a patch antenna is an effective antenna that is widely used and it is important to have impedance matching. So the easy implemenetation of matching furthers the value of a patch antenna. 

## Hindsight
It would have been beneficial to have known how to use the quarter-wave transformer matching network so that I would have gotten more experince with a matching techinque that I have had little exposure to.

## Reflection
This lab did a great job of showing how simple a patch antenna can be to work with for beginners with antenna. It also provived an effective way of understanding just how important a good matching network can make a difference to a system. 
