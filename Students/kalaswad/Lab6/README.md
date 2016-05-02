# Lab 6 Report
Matias Kalaswad

## Background
This lab introduced us two types of filters: low-pass and band-pass. Two types of low-pass filters were made; one was a maximally flat T-line filter while the other was tapped. We were tasked with designing the filters in HFSS and then building the circuits in lab with copper tape. These filters are commonly used and we’ve learned about them in a lot of other ECEN classes so it was interesting to design them in this lab.

## Design
There were three different designs for this lab.  The first was the low-pass filter with 2.5 GHz cut-off frequency and attenuation of 10 dB at 3.25 GHz. We knew it was a fifth order filter and obtained the coefficients from the charts and graphs given in the lab manual.  The lab manual also had very clear step-by-step instructions for using Richard’s transformation to get the open circuit shunt values from the capacitor and the short circuit values from the inductors. Finally, we obtained the widths of each stub to be:
•	8.37 mm
•	3.94 mm
•	3.11 mm
•	1.74 mm
•	0.52 mm
•	0.07 mm

## Procedure
In lab David showed us a milled version of a band-pass filter so that we had an idea of how to construct them.  We used our calculated values to find the lengths and widths of each segment and then carefully cut them out and placed them on the board in precise increments. Our values were as followed:
•	50 ohm lines were 3.11 mm wide
•	75 ohm lines were 1.478 mm wide
•	104 ohm lines were 0.667 mm wide
•	Each stub was 14.75 mm long
•	The space between each stub was a quarter wavelength or about 16.88 mm

Once the stubs were soldered into place, David hooked up the circuit to the network analyzer and it showed that the cut-off frequency was around 2.5 GHz as expected.

## Results and Discussion


## Conclusion
The main point of this lab was to teach us about designing different types of filters. While we only built one, we were able to go through design process of several and see how each type of filter simulated in Z0lver and HFSS.  Clearly the milled version was the most accurate of the filters but our design was still fairly accurate.

## Hindsight
The only thing we wished we had known prior to this lab was how to solder with the hot air torch.  It took some of the lab time in order to get used to soldering this way and we had to start over a couple of times because the copper tape curled up from too much heat.

## Reflection
The most challenging and also the most rewarding part of this lab was learning how to use the hot air soldering torch. Soldering is a very important skill for engineers to have so it was extremely beneficial to get to learn about a different way than traditional soldering irons. Unfortunately, the copper tape is very hard to solder and wouldn’t stick to the board very well.
