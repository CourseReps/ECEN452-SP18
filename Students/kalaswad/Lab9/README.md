# Lab 9 Report
Matias Kalaswad

## Background
This lab was meant to teach us about the design of a patch antenna. They are frequently used in mobile devices because they are relatively cheap and easy to manufacture. We were expected to calculate the dimensions of the patch and then make it in the lab.

## Design
We designed two different networks in this lab.  The first was the general patch antenna with an operating frequency at 3 GHz, then we added a stub in order to have a quarter wave matching network. In the lab manual we were given that the patch antenna should have a dielectric constant of 4.1, a characteristic impedance of 50 ohms, and a height of 62 mil.  With these values we used the very large equations from the lab manual to calculate the following dimensions:
	width = 31.3 mm
	ε_eff = 3.774
	△L = 0.73 mm
	L = 24.2 mm

## Procedure
In lab we built the general patch antenna with just a 50 ohm feed line out of copper tape and then had David test it with network analyzer to show the operating frequency and impedance of the antenna. David then told us to implement the single stub tuner using the smith chart to calculate the dimensions of the stub. Our antenna’s impedance was 57.75-j52Ω which we normalized with 50 ohms and plotted on the Smith chart.  Then the point was rotated a quarter wavelength in order to match the network.  To find the length, we rotated the point until we hit the VSWR = 1 circle. We also used the equation Z_0= √(Z_OT*Z_L )= √(50*20)=31.62Ω. Get stub length and effective wavelengthand VSWR  from Matias. When David ran our circuit through the network analyzer again, we were able to see that the operating frequency was 3.066 GHz.

## Results and Discussion
Below is the graph from HFSS of the patch antenna.

## Conclusion
The main point of this lab was to show us the design process of building a patch antenna

## Hindsight
We realized that it would have been helpful to review concepts from ECEN 322 like how to use a Smith chart to match a quarter wave network.  We spent quite a bit of lab time working through that process because we had to remind ourselves of all the steps.

## Reflection
The most challenging part of this lab was using the large equations to calculate the initial values for the patch antenna and also utilizing the Smith chart to match the network.

The most rewarding part of the lab was getting to refresh 322 skills and learning how relatively simple it is to design a patch antenna.  This helped explain why it is so popular in the cell phone industry.
