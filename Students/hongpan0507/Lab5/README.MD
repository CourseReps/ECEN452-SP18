# Lab 5 Report
Hong Pan

## Background
TRL is a calibration kit that performs VNA calibration which is unique to the transmission line implemented on a device.
It has the advantage of shifting the reference plane to any kind of transmission line that the device is attached.

Pin diode is DC voltage controlled RF switch.

## Design  
### TRL Design
   + Design Parameter 
     + Z0 = 50ohms 
     + FR4 substrate height = 62mil
     + dielectric constant = 4.1
     + Frequency Range = 1GHz to 5Ghz
     + referecen plane = 15mm beyond SMA probe end launch
   + Calculation
     + Center Frequency = 3GHz
       + 50ohms microstrip width = 3.07mm; [microstrip line calculator](http://www1.sphere.ne.jp/i-lab/ilab/tool/ms_line_e.htm)
         + effective dielectric constant = 3.2
         + quarter wavelength = 14mm
     + Reflect length = 15mm; Reflect provides high reflectivity required by the VNA TRL calibration
     + Through length = 30mm; Through sets the reference plane
     + Line length = through length + quarter wavelength @ 3GHz = 44mm; Line implements transmission line characteristic impedance

### RF Switch Design
   + Design Parameter
     + Z0 = 50ohms 
     + FR4 substrate height = 62mil
     + dielectric constant = 4.1
     + Center Frequency = 2.5GHz
     + referecen plane = 15mm beyond SMA probe end launch
   + Calculation
     + Center Frequency = 2.5GHz
       + 50 ohms microstrip width = 3.09mm; [microstrip line calculator](http://www1.sphere.ne.jp/i-lab/ilab/tool/ms_line_e.htm)
         + effective dielectric constant = 3.1
         + quarter wavelength = 17mm
       + 100 ohms microstrip width = 0.71mm; [microstrip line calculator](http://www1.sphere.ne.jp/i-lab/ilab/tool/ms_line_e.htm)
         + effective dielectric constant = 2.8
         + quarter wavelength = 17.9mm
         
## Procedure
### TRL Procedure
1. Through standard is simulated and tuned such that the Z0->50ohms (changing the width of the microstrip line); the length is set to 30mm.
2. De-embedding is set in order to get  0degree s21 phase and 0dB s21 magnitude for the through  
3. Reflect standard has same line width and half of the line length compared to the through. After simulating the reflect, port 1 de-embedding is turned on and the de-embed length is the same as line length.
4. Imaginary part of the reflect port 1 impedance is exported as csv file to extract the coefficient of the 3rd order polynomial equation required by the VNA.
5. Effective dielectric constant and effective wavelength is recorded from the reflect simulation.
6. The length of the line standard is set to line length from the calculation above before its simulation is performed.
7. Port 1 and port 2 is de-embedded by the same length as the half of the through line length.
8. After checking s21 phase is close to 90 degree for line standard, the delay is recorded.
9. A Python program is written to perform the polynomial fit for the data exported in step 4 and output the 3rd order polynomial coefficients required by the VNA
  + The code is named as lab5_TRL.py under the same folder as this README.MD

### RF Switch Procedure
1. Two microstripe lines are simulated and tuned by changing the width of the line until their characteristic impedances of 50ohms and 100ohms are reached.
2. The width of the main transmission line from all the .hfss designs is changed to the width of the 50ohms microstrip line based on step 1.
2. A 100ohms quater-wave stub is simulated in "SCGroundStub.hfss" based on the parameters extracted from the simulation from step 1. At the center operating frequency, S11 magnitude of -60dB sugguests that the quater-wave stub is transparent to the main 50ohms line.
3. A 100ohms quater-wave stub is simulated in "SCBiasStub.hfss" based on the parameters extracted from the simulation from step 1. At the center operating frequency, S11 magnitude of -40dB sugguests that the biasing circuit is transparent to the main 50ohms line.
4. The microstrip line parameters from step 2 and step 4 are inserted into "PINSeriesSwitch.hfss". Both "on" and "off" states are simulated.


## Results and Discussion
### TRL
![TRL Reflect z img](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/hongpan0507/Lab5/figures/TRL_reflect_z_img.png)
![TRL Thru S21 mag and phase](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/hongpan0507/Lab5/figures/TRL_thru_s21_mag_phase.png)
![TRL Line S21 mag and phase](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/hongpan0507/Lab5/figures/TRL_line_s21_mag_phase.png)

#### Observations:
1. Polynomial coefficients have a good representation of the simulated capacitance at the end of the transmission line of the reflect standard
2. The measured TRL S parameters is very close to the simulation.
3. The measured s21 has magnitude greater than 0dB at center freuencies; the error could come from the process of constructing the TRL kit.

### RF Switch
![PIN diode s parameter](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/hongpan0507/Lab5/figures/PIN_diode.png)

#### Observations:
1. The measured data has good agreement with the simulated data.
2. For off state, s21 isolation is only -10dB
3. For s21, a dip appears at 4.8GHz. It's most likely because of the quater-wave stub at 2.5GHz looks like a half-wave stub at 5GHz. By accouting for the non-linear relationship between frequency and effective dielectric constant, it's reasonable that it shows up at 4.8GHz

## Conclusion
### TRL
1. It's important to understand the function of each TRL standard when designing TRL
2. PIN diode s21 isolation is not as good as expected

## Hindsight
1. It was very helpful to go through the process of deriving the TRL calibration equations in the class.
2. 

## Reflection
1. I feel much more comfortable using TRL calibration
