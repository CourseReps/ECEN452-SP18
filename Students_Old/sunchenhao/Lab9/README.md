# Lab 9 Report
Chenhao Sun

## Background
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/sunchenhao/Lab9/patch.jpg) <br>
A patch antenna (also known as a rectangular microstrip antenna) is a type of radio antenna with a low profile, which can be mounted on a flat surface. It consists of a flat rectangular sheet or "patch" of metal, mounted over a larger sheet of metal called a ground plane. They are the original type of microstrip antenna described by Howell in 1972;[1] the two metal sheets together form a resonant piece of microstrip transmission line with a length of approximately one-half wavelength of the radio waves. The radiation mechanism arises from discontinuities at each truncated edge of the microstrip transmission line.[2] The radiation at the edges causes the antenna to act slightly larger electrically than its physical dimensions, so in order for the antenna to be resonant, a length of microstrip transmission line slightly shorter than one-half a wavelength at the frequency is used.[1] <br>

The equation of calculating patch's parameters are showed as follow: 
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/sunchenhao/Lab9/equ.png) <br>

##Design
This assign is still based on FR4(4.1) with 62mil thickness, at 3GHz. <br>
So based on equations in Background, we can calculate basic parameters of this patch. <br>
Length L = 24.27 mm 
Width W = 31.31 mm 

##Procedure
For Patch using QWT matching netwrok: <br>
Firstly, using basic parmaters just calculated, a patch without matching network is built, and baisc structure and VSWR are as followed:<br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/sunchenhao/Lab9/Patch_Picture1.png) <br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/sunchenhao/Lab9/Unmatched.png) <br>
The measured impedance at 3GHz is 20.1+j50.9 Ohm <br>

Then, we need to complete the QWT matching network, baisc structure is showed as follow:
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/sunchenhao/Lab9/Patch_Picture2.png) <br>
We can calculate length and width of QWT in Smith Chart, VSWR after matching is showed as followed:
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/sunchenhao/Lab9/matched.png) <br>

For Patch using probe feed:
Firstly, using same equation to calculate length and width of Patch, and apply them into HFSS simulation file.<br>
Then, tune probe_feed_x and Patch_Lenth to make VSWR is lowest at 3GHz, and below 1.2.

##Results
The structure, VSWR and Impedance on Smith Chart are showed as followed: <br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/sunchenhao/Lab9/Structure.png) <br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/sunchenhao/Lab9/VSWR.png) <br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/sunchenhao/Lab9/Smith%20Chart.png) <br>

##discussion
Well, as we can see, for the patch with QWT matching network, the impedance is not well matched both before and after intalling QWT matching network. I think that is because this QWT is hand-cut and hand-stick in the borad which give this a lot of uncertainty.<br>
For probe_feed patch, simulation work pretty good.<br>

##Conclusion
Patch with QWT work not on the right frequency, which mean it failed. <br>
Patch with probe feed's simulation work good. <br>

##Reference
[1]https://en.wikipedia.org/wiki/Patch_antenna
