Lab 11:  Free Space Measurement of Material Properties

Background:

Free Space measurement is a method of obtaining the electrical properties of materials.  This method uses the transmission and reflection of electromagnetic waves through a material in order to determine it's relative permeability and permittivity.  The system is first calibrated using a GRL (Gated-Reflect-Line) calibration scheme.  Two antennas are set up and aligned with each other, then measurements are taken with no material between the probes and with a reflective material (usually metal) between the probes.  Then a time gate process is used to isolate the response due to reflection from the metal sheet.  This data is used to calibrate the network analyzer.  Next, sheets of the material to be measured are inserted between the two antennas, and the antennas measure the transmission and reflection of of a test signal.  Throuugh mathematical analysis, these values are used to calculate the material properties.

To apply the time gate, the recieved signal is transformed into the time domain.  In this case, the magnitude of the signal relative to time elapsed after transmission is plotted, rather than a magnitude versus frequency plot.  In this case, the S11 data corresponds to reflection as a function of time; a spike is seen when the reflection from the metal sheet arrives, and the signal is gated around this point to eliminate unnecessary noise not associated with the reflected signal from the material.  The reflect is used to located this reflected signal in time.

Applications:

The free space measurement is most suited to measuring materials with large surface area and uniform composition, thickness, and surface.  The material has to present a large and regular cross section in order to capture as much of the field as possible.  These requirements make this measurement more applicable to solids and composite materials, rather than liquids or gasses.  The material properties obtained from this analysis are particularly useful in calculating wave behavior incident upon material surfaces or propagating through a material.

Results:

![Pre-Cal Measurements](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/derekjanak/Lab11/Pre_Calibration_Measurements.png)
This plot shows the calibration measurements taken in order to prepare the system for use.  Time gating was applied in order to isolate the reflected signal from the metal from ambient noise resulting from incident waves and scattering from other locations.

![Permeability Measurements](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/derekjanak/Lab11/Permeabillity_Measurements.png)
These measurements show the real and imaginary components of the permeabilities of Air, Cardboard, and Plexiglass.  As might be expected from a selection of non-magnetic materials, the permeabilities are all approximately 1.

![Permittivity Measurements](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/derekjanak/Lab11/Permittivity_Measurements.png)
These measurements show the permittivities of the same materials.  The permittivities are real, and Air has the lowest relative permittivity, almost equal to 1, as the permittivity of air approaches the permittivity of free space.  Predictably, cardboard has a higher relative permittivity than plexiglass.  This agrees well with expected values.

Conclusion:

In this lab, the students were able to see a real material measurement demonstration.  The enormous take-away from this lab was knowledge of actual real-world measurement techniques and the opportunity to see the practical application of theoretical knowledge.  The challenges faced in lab were minimal and primarily centered on a lack of material with a cross section sufficient for precise measurement.  However, the lab demonstration effectively obtained measurements and was able to provide insight into the process.

In practice, the calibration could be improved by calibrating using a larger reflect surface and taking measurements using a larger segment of material to capture more of the emitted signal, as well as by using a more focused antenna that doesn't disperse the signal so widely.  Additionally, the test could be conducted in the anechoic chamber in order to reduce/eliminate ambient noise.  This would increase the accuracy and precision of the results.

Hindsight:

There was no further knowledge needed on my part before the lab.  However, I do wish that I had been able to participate more in the actual measurement process.

Reflection:

The greatest challenge of this lab was grasping the conceptual framework presented in class; the greatest reward was seeing theory in practice.
