# Lab 10 Report
Abhay Shankar Anand

## Background
Lab 10 consists of Dielectric Measurements of Liquids using open ended Coaxial Probe.

Dielectric measurements use the basic concept of Reflection and Transmission obtained from S-parameters. In this case, it is analyzed using just the reflections (as only a 1 port device is used). Coaxial probes provide reasonable accuracy in measurements and have a broadband response (due to the broadband nature of the probe).

## Design
Fields from the open ended terminal of the probe fringe into the material under test. This fringing of fields causes reflections in the input port and the characteristic impedence of the material is not **Z<sub>0</sub>** of the probe. The reflection data is then analyzed to characterize &#949;' and &#949;''.
After exhaustive calculations, we obtain a relation between &#915;, &#949;' and &#949;''. With calibrations, we are able to remove systematic errors and finally obtain the values of &#949;' and &#949;''.

The calibration process consists of three measurements:
1. Open circuit: reflections caused due to air/vacuum
2. Short circuit: reflections due to a short termination
3. Load: reflections caused due to DI water. The probe is inserted in water and measurements are taken.

The reason for using DI water is that it has the highest dielectric constant for liquids and is a standard used for these measurements.

### Procedure

1. Calibrate the probe for air, short and water using the add-on software package provided by Agilent for use with their VNA.
2. Place the Material Under Test (MUT) under the probe and immerse the open-end of the probe into the liquid and take measurements.
3. Once measurements are obtained, carefully remove the MUT.
4. Clean the probe and run measurements to check dielectric constant of air. If there seems to be a significant error, recalibrate the system (i.e., repeat from step 1).

### Sources of Error

There are three main sources of errors that could affect the measurememts:

1. Cable impurities: It is important to clean the probe before every measurement. To ensure this, it is better to run measurements for air and recalibrate if deviations are noticed.
2. MUT thickness: As the fields fringe due to the open ended probe, we must ensure to minimize the fields that fringe beyond the liquid and into the atmosphere/vacuum. For this, the probe must be sufficiently dipped into the liquid. One must also ensure that it is not too deeply inserted that reflections from the bottom of the MUT holder would affect the measurements.
3. MUT purity: It must be ensured that pure samples of the MUT must be taken before test, including DI water.

### Results
![Dielectric_Liquids](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/abhaysanand/Lab10/results/DielectricConstantsLiquids.png)

Liquids | Measured &#949;' | Expected &#949;'
------- | ---------------- | ----------------
Acetone | 21 | 20.7
Water | 79 | 80.4
Ethylene Glycon | 38 to 8 | 42 to 7

**Dielectric constant of DI Water from 20MHz to 20GHz**
![DIWater_Dielectric](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/abhaysanand/Lab10/results/DielectricConstantsDIWater.png)

The dielectric constant of water is almost linear from 5 GHz to 20 GHz. As per expectation, this is correct.

### Questions
1. **Why do we use DI water as a calibration standard?**<br>
DI water is used as a calibration standard because it is known to have the highest &#949;' for liquids and has an almost linear curve over a wide range of frequency.
2. **What can we do to improve the calibration process?**<br>
To improve the calibration process, we could recalibrate the system after each measurement. And instead of just a probe being dipped into the liquid, a small ground plane could have been added which would also be immersed into the liquid. This would ensure that the fringing fields do not escape the MUT into the air/vacuum.
3. **Can the dielectric probe be used for wideband or only narrowband measurements?**<br>
This measurement technique can be used for broadband measurememts as probes are slightly broadband in nature.
4. **What kind of generalizations can you make based on the type of liquid (oil, alcohol, water-based solutions…) and their measured electrical properties?**<br>
Water and water based liquids have high dielectric constants whereas alcohol based liquids have relatively lower dielectric constants. Oil based liquids have a constant dielectric constant over a large range of frequencies.
5. **Which liquids were considered “watered down” and which one had the highest water content (other than water itself)?**<br>
Pine Sol, Simple Green and Glass cleaner can be considered as "watered down" liquids. From the plot, Glass cleaner is the liquid with highest water content.

## Conclusion
This lab helped me understand the dielectric properties of various almost household liquids and its relation to frequency.

## Hindsight
I believe better measurememts could have been possible by placing a small ground plane near the tip of the coaxial feed as this would reduce the fringe fields that escape the MUT into air/vacuum.
