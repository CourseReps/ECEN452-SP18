# Double Stub Tuning Tutorial

This tutorial demonstrates how to design a double stub matching network that matches a load impedance <b>Z<sub>L</sub> = 25 - j100</b> ohms to a transmission line with characteristic impedance <b>Z<sub>0</sub> = 50</b> ohms. The main design parameters that you need to determine are <b>d<sub>1</sub></b> (distance from load to first stub), <b>d<sub>2</sub></b> (distance from first stub to second stub), <b>l<sub>1</sub></b> (length of first stub), and <b>l<sub>2</sub></b> (length of second stub). In this example all transmission lines will have <b>Z<sub>0</sub> = 50</b> ohms. If you want to use a different characteristic impedance for the stubs, you must pay careful attention when normalizing and unnormalizing impedances/admittances for the different steps. Lastly, this turtorial only considers <b>open-circuit stubs</b> due to their simplicity of fabrication in microstrip circuits.  

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Resources/DoubleStubTuning/DoubleStubTuning_Diagram.png)

## Step 1: Plot Normalized Impedance/Admittance and Rotate Distance d<sub>1</sub> Towards the Generator
The first step is to plot the normalized impedance on the Smith chart. In this example, <b>z<sub>L</sub> = 0.5 - j2</b> which gives us an admittance <b>y<sub>L</sub> = 0.12 + j0.47</b>. You have the freedom to choose the distance <b>d<sub>1</sub></b> between the load and the first stub that best fits your design goals. For simplicity, I have chosen <b>d<sub>1</sub> = 0.5 wavelengths</b> which corresponds to one full rotation on the Smith chart.

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Resources/DoubleStubTuning/DoubleStubTuning_Step1.png)

## Step 2: Draw a Rotated 1 + jb Circle and Determine Susceptance b<sub>1</sub> Required to Move to Point on the Circle
This step is perhaps the most conceptually difficult part. The idea behind this step is that we rotate the entire 1 + jb circle some distance <b>d<sub>2</sub></b> <i>towards the load</i> (this is the distance between the two stubs). Thus, if we can get to a point on that circle, then we would rotate <i>towards the generator</i> by <b>d<sub>2</sub></b> and end up on the 1 + jb circle. 

You have the freedom to choose the distance <b>d<sub>2</sub></b> between the two stubs that best fits your design goals. In this example, I have chosen <b>d<sub>2</sub> = 0.125 wavelengths</b>. You will need to draw the 1 + jb circle rotated by 0.125 wavelengths toward the load which can be done by setting your compass to the size of the 1 + jb circle and drawing a circle centered in the top half of the Smith chart. 

Now you need to find a point on that circle that has the same conductance as the admittance found in step 1, which was <b>y = 0.12 + j0.47</b>. There are two points, and thus two solutions, which are <b>y<sub>1</sub> = 0.12 + j0.525</b> and <b>y<sub>1</sub>' = 0.12 + j1.49</b>. From this we can calculate the susceptance required to move to the circle which is <b>jb<sub>1</sub> = j0.055</b> for the first solution and <b>jb<sub>1</sub>' = j1.02</b> for the second solution. We will use these values to determine the length of the first stub later. <i>(Note that these values are normalized to 50 ohms)</i>

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Resources/DoubleStubTuning/DoubleStubTuning_Step2.png)

## Step 3: Rotate the Distance d<sub>2</sub> Towards the Generator
In this step we simply rotate from our point on the circle from step 2 until it intersects the 1 + jb circle. The distance rotated should be equal to <b>d<sub>2</sub></b> if you drew your rotated circle correctly.

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Resources/DoubleStubTuning/DoubleStubTuning_Step3.png)

## Step 4: Find the Negative of jb on the 1 + jb Circle
Now we need to cancel out the jb term which will be accomplished by the second stub. Simply read the jb value at this point and take the negative of that. In this example, this would be <b>jb<sub>2</sub> = -j3</b> for the first solution and <b>jb<sub>2</sub>' = j4.85</b> for the second solution.

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Resources/DoubleStubTuning/DoubleStubTuning_Step4.png)

## Step 5: Determine the Length of the First Stub
At this point we have all we need to find the lengths of the stubs. In step 2, we found that <b>jb<sub>1</sub> = j0.055</b> for the first solution, so we plot this on the Smith chart and find the number of wavelengths <i>toward the generator</i> required to rotate from the admittance of an open-circuit to this point. This gives the length of the first stub <b>l<sub>1</sub> = 0.009 wavelengths</b>. We do the same for the second solution (<b>jb<sub>1</sub> = j1.02</b>) and find the length of the first stub <b>l<sub>1</sub>' = 0.127 wavelengths</b> for the second solution. <i>(If you use a different characteristic impedance for the stubs, you need to unnormalize and renormalize the values of <b>jb<sub>1</sub></b> and <b>jb<sub>1</sub>'</b> to the stub characteristic admittance before this step)</i>

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Resources/DoubleStubTuning/DoubleStubTuning_Step5.png)

## Step 6: Determine the Length of the Second Stub
This step is similar to step 5, except we will plot the values obtained from step 4 to find the length of the second stub. For the first solution we need a susceptance of <b>jb<sub>2</sub> = -j3</b> which gives us <b>l<sub>2</sub> = 0.301 wavelengths</b> for the first solution. For the second solution we need a susceptance of <b>jb<sub>2</sub>' = 4.85</b> which gives us <b>l<sub>2</sub>' = 0.218 wavelengths</b> for the second solution. <i>(If you use a different characteristic impedance for the stubs, you need to unnormalize and renormalize the values of <b>jb<sub>2</sub></b> and <b>jb<sub>2</sub>'</b> to the stub characteristic admittance before this step)</i>

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Resources/DoubleStubTuning/DoubleStubTuning_Step6.png)

## Summary
The design parameters for this example are:

1st Solution: <br>
d<sub>1</sub> = 0.5 wavelengths <br>
l<sub>1</sub> = 0.009 wavelengths <br>
d<sub>2</sub> = 0.125 wavelengths <br>
l<sub>2</sub> = 0.301 wavelengths <br>

2nd Solution: <br>
d<sub>1</sub>' = 0.5 wavelengths <br>
l<sub>1</sub>' = 0.127 wavelengths <br>
d<sub>2</sub>' = 0.125 wavelengths <br>
l<sub>2</sub>' = 0.218 wavelengths <br>

<b><i>*Remember to use the effective wavelength of the transmission line to translate these values into physical lengths!</b></i>
