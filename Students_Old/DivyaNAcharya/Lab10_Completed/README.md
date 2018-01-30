# Lab 10: Dielectric Probe Measurements
Divya Acharya 

## Background
A dielectric materials measurement can provide critical design parameter information for many electronics applications. For example, the loss of a cable insulator, the impedance of a substrate, or the frequency of a dielectric resonator can be related to its dielectric properties. <br>The real part of permittivity (er') is a measure of how much energy from an external electric field is stored in a material. The imaginary part of permittivity (er'') is called the loss factor and is a measure of how dissipative or lossy a material is to an external electric field. The imaginary part of permittivity (er") is always greater than zero and is usually much smaller than (er'). The loss factor includes the effects of both dielectric loss and conductivity.
<br>A typical dielectric probe measurement system using a coaxial probe method consists of a network or impedance analyzer, a coaxial probe and software. The material's permittivity/dielectric constant is measured by immersing the probe into a liquid or touching it to the flat face of a solid (or powder) material. The fields at the probe end “fringe" into the material and change as they come into contact with the MUT.The reflected signals (S11) can be measured and related to permittivity.

##Setup
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/DivyaNAcharya/Lab10_Completed/Setup.PNG)

##Procedure
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/DivyaNAcharya/Lab10_Completed/CoAxProbe.PNG)

- Calibrate the coaxial probe by open, short and DI water
- Place the coaxial feed in the MUT and take measurements using special software
- Clean the probe and recalibrate before measuring the next MUT

## Results and Discussion
The plots for various liquids show their variation of permittivity with frequency:
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/DivyaNAcharya/Lab10_Completed/figure_1.png)
<br>"Zoomed-in" view of plots. We can see that the plots for liquids acetone (er=20.7) ethylene glycol(er=37) isopropyl alcohol (er=18.3) closely follow their expected permittiviy values.
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/DivyaNAcharya/Lab10_Completed/figure_2.png)
<br>The DI_Water plot shows that the permittivity of DIwater decreases almost monotonically with frequency from 80 to 40:
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/DivyaNAcharya/Lab10_Completed/DIWater.png)


## Observations
1. Why do we use DI water as a calibration standard?
<br> De-ionized water has a high, stable and easily reproducible dielectric constant and hence is used as a calibration standard
2. What can we do to improve the calibration process?
<br> Random errors due to noise, drift, or the environment (temperature, humidity, pressure) cannot be removed with a measurement calibration. This makes a microwave measurement susceptible to errors from small changes in the measurement system. These errors can be minimized by adopting good measurement practices, such as visually inspecting all connectors for dirt or damage and by minimizing any physical movement of the test port cables after a calibration.
3. Can the dielectric probe be used for wideband or only narrowband measurements?
<br> Dielectric probe is suitable for wideband measurements.
4. What kind of generalizations can you make based on the type of liquid (oil, alcohol, water-based solutions…) and their measured electrical properties?
<br> We see that water based solutions have relatively higher permittivity than alcohol based solutions. Also, as seen from the plot for Silicone fluid, oils have a constant permittivity over wide range of frequencies.
5. Which liquids were considered “watered down” and which one had the highest water content (other than water itself)?
<br> The liquids that show plots most similar to water can be considered "watered down". From the graph it is clear that Glass Cleaner comes the closest followed by Simpe Green and Pine Sol.

##Conclusion
This Lab helped understand the behaviour of different materials (liquids) w.r.t. their dielectric constant accross a wide range of frequencies.

##Hindsight
It would have been interesting to see the results if another liquid was used as a calibration standard other than DI_water

##Reflection
It was interesting to see how a material property could vary with frequency of operation which is something important to consider while building any wideband system/product.

##References
http://www3.imperial.ac.uk/pls/portallive/docs/1/11949698.PDF
<br>
https://www.kabusa.com/Dilectric-Constants.pdf
