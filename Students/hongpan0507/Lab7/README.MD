# Lab 7 Report
Hong Pan

## Background
1. Wilkinson power divider is capable of equally or unequally splitting input power. All ports are matched because of the resistor 
connecting the branch.
2. Phase shifter provides fixed or variable degree of phase shift.

## Design
### Wilkinson Power Divider
#### Specification: operating frequency = 2.5GHz; 2-way equal power split
1. The microstrip width is determined from the substrate height, dielectric constant and characteristic impedance.
  + Input and output T-line characteristic impedance is 50ohms. 
  + The quater-wave T-line characteristic impedance is sqrt(2)*50ohms.
2. The value of the resistor is 100ohms  

### Phase shifter
#### Specification: operating frequency = 2.5GHz; 90deg and 180deg phase shift
1. The microstrip width is determined from the substrate height, dielectric constant and characteristic impedance.
  + All T-line characteristic impedance is 50ohms. 
2. The shortest T-line is used as a reference.
3. The second T-line is 1/4 wave length longer than the shortest T-line to provide 90deg phase shift.
4. The third T-line is 1/2 wave length longer than the shortest T-line to provide 180deg phase shift.

## Procedure
### Wilkinson Power Divider
1. All the parameter is simulated in z0lver
2. The physical width and length is simulated and tuned in HFSS
3. Simulated results are compared to the milled out version

### Phase shifter
1. The shortest T-line is taped down and measured to provide reference phase.
2. The shortest T-line is cut, and additional 1/4 wavelength long T-line is added to the T-line. It's providing 90 degree of phase shift.
3. The 1/2 wavelength long T-line is replaced with a 1/2 wavelength long T-line to provide 180 degree of phase shift.

## Results and Discussion
### Wilkinson Power Divider
1. The data of s11, s22, s33 magnitude shows that all ports are matched because return loss is greater than 10dB at the designed frequency.
  + The z0lver simulated data show that all the port matching can be further tuned to provide better port matching
2. s32 magnitude indicates that port 2 and port 3 are isolated
3. s21 and s31 magnitude have -3dB power split at the design frequency. It is not exactly -3dB power split because of the loss associated with microstrip T-line
![s11](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/hongpan0507/Lab7/plotting/s11.png)
![s22](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/hongpan0507/Lab7/plotting/s22.png)
![s33](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/hongpan0507/Lab7/plotting/s33.png)
![s32](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/hongpan0507/Lab7/plotting/s32.png)
![s21](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/hongpan0507/Lab7/plotting/s21.png)
![s31](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/hongpan0507/Lab7/plotting/s31.png)

### Phase shifter
1. s11 magnitude data shows that both port 1 and port 2 are matched since the device is symmetric
2. s21 magnitude data shows that majority of the power is delivered from port 1 to port 2.
3. s11 phase is not of interest for this design
4. s21 phase is very linear for all 3 phase variation. 0deg reference plane has a different slope compared to 90 and 180deg. It is most likely a measurement error.
![PS_s11_mag](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/hongpan0507/Lab7/plotting/PS_s11_mag.png)
![PS_s21_mag](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/hongpan0507/Lab7/plotting/PS_s21_mag.png)
![PS_s11_phase](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/hongpan0507/Lab7/plotting/PS_s11_phase.png)
![PS_s21_phase](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/hongpan0507/Lab7/plotting/PS_s21_phase.png)

## Conclusion
1. Both designs are straight forward for this lab.

