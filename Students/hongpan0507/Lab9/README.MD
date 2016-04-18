# Lab 9 Report
Hong Pan

## Background
Patch antenna is a low profile antenna that is easily built on a flat surface.  
![patch](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/hongpan0507/Lab9/plotting/patch.png)

## Design
#### Specification: operating frequency = 3GHz; Z0 = 50ohms; substrate = FR4 (e_r = 4.1); substrate height = 62 mil
1. [microstrip line calculator](http://www1.sphere.ne.jp/i-lab/ilab/tool/ms_line_e.htm) is used to calculated the characteristic impedance of input microstrip line and quater-wave transformer
2. The length and width of the patch is calculated accoording to the formula below.
![patch formula](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/hongpan0507/Lab9/plotting/patch_formula.png)

## Procedure
#### Lab activity
1. An unmatched patch with 50ohms feed-line is constructed on the substrate.
2. input impedance at 15mm into the feed-line of the patch is measured and recorded.
3. From the measurement of input impedance at 15mm into the feed-line, the input impedance at the design frequency is rotated towards the load on smith chart for at lease one quater-wave length long and until the impedance is purely real.
4. The real impedance is transformed into 50ohms using an quarter-wave transformer is constructed

#### HFSS simulation
1. A patch with length and width from the design above is simulated and tuned to 3GHz
2. The position of the probe is adjusted until the patch is matched to 50ohms

## Results and Discussion
### edge-fed impedance matching using quater-wave transformer
From the smith chart below, it is obvious that the quater-wave transformer is implemented correctly, and it matched the 50ohms line to the patch. The reflect is significantly reduced in s11 magnitude plot.
![smith chart 1](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/hongpan0507/Lab9/plotting/smith_chart1.png)
![s11 mag 1](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/hongpan0507/Lab9/plotting/s11_mag1.png)

### edge-fed vs probe-fed
From the plots below, the probe-fed patch is just as good edge-fed in terms of input impedance matching
![smith chart 2](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/hongpan0507/Lab9/plotting/smith_chart2.png)
![s11 mag 2](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/hongpan0507/Lab9/plotting/s11_mag2.png)

## Conclusion
The patch formula is very useful during the lab activity. No tuning was required to get the patch to resonate at the design frequency. The quater-wave transformer works well for the input impedance matching. 
