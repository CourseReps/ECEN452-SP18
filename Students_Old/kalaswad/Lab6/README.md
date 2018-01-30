# Lab 6 Report
Matias Kalaswad

In this lab I worked with Chloe Dixon and Matthew Walck. Some of the things that we worked on include parameter calculations, HFSS simulations, lab reports, and plots.

## Background
In this lab we demonstrated two types of microstrip filters: low-pass and band-pass. Two types of low-pass filters were made; one was a maximally flat T-line filter while the other was tapped. Prior to lab we simulated the filters in HFSS and then in lab we built the circuits with copper tape. These filters are commonly used and we’ve learned about them in many other ECEN classes.

## Design
There were three different designs for this lab.  The first was the low-pass filter with 2.5 GHz cut-off frequency and attenuation of 10 dB at 3.25 GHz. We knew it was a fifth order filter and obtained the coefficients from the charts and graphs given in the lab manual.  The lab manual also had very clear step-by-step instructions for using Richard’s transformation to get the open circuit shunt values from the capacitor and the short circuit values from the inductors. We obtained the widths of each stub to be:

    8.37 mm
    3.94 mm
    3.11 mm
    1.74 mm
    0.52 mm
    0.07 mm
    
Screenshots from HFSS simulations are shown below.

Band-stop filter T-line
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/kalaswad/Lab6/BSF_T-Line.PNG)

Low-pass filter T-line
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/kalaswad/Lab6/LPF_T-Line.PNG)

Low-pass filter with tapped stubs
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/kalaswad/Lab6/LPF_tappedStubs.PNG)

## Procedure
In lab David showed us a milled version of a band-pass filter so that we had an idea of how to construct them. We used our calculated values to find the lengths and widths of each segment and then carefully cut them out and placed them on the board. Our values were as follow:

    50 ohm lines were 3.11 mm wide
    75 ohm lines were 1.478 mm wide
    104 ohm lines were 0.667 mm wide
    Each stub was 14.75 mm long
    Quarter wavelength spacing or about 16.88 mm

Once the stubs were soldered into place, David hooked up the circuit to the network analyzer. The cut-off frequency was around 2.5 GHz as expected.

## Results and Discussion
Various plots comparing simulation data and measured data are shown below. For the most part, the simulated and measured data matched up, which was close to our expectations. 

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/kalaswad/Lab6/50ohm_Mag.png)

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/kalaswad/Lab6/50ohm_Phase.png)

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/kalaswad/Lab6/BSF_Mag.png)

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/kalaswad/Lab6/BSF_Phase.png)

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/kalaswad/Lab6/LPF_Mag.png)

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/kalaswad/Lab6/LPF_Phase.png)

## Conclusion
In this lab we learned how to design a couple of different types of microstrip filters. Although we only built one, we were able to go through design process of several and see how each type of filter simulated in Z0lver and HFSS.  Clearly the milled version was the most accurate of the filters but our design was still fairly accurate.

## Hindsight
It would have been good to be more careful while making the copper tape measurements and cuts. However, I think we made the best of it given the materials available.

## Reflection
I had no idea that it was possible to make filters simply using a substrate, copper tape, and SMA connectors. I thought that this was incredible. Using the soldering equipment was a new experience that took some getting used to. 
