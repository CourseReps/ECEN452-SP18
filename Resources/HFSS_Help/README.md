# HFSS Help

Each lab requires you to simulate designs in HFSS. For the first few labs, you will be given pre-made HFSS files that will already have the core design, simulation setup, and result graphs that you need. For these pre-made files, you will need to input your calculated dimensions into the design parameters, run the simulation, and export the data as a .csv file. This document will provide some basic tips for running your simulation and getting the data you need for the lab reports. 

## Navigating the Model Space
Rotate: Hold Alt -> click and drag <br>
Pan: Hold Shift -> click and drag <br>
Zoom: Hold Alt+Shift -> click and drag OR use scroll wheel <br>
Zoom Fit: Hold Alt+Shift -> double-click <br>
Snap to View: Hold Alt -> double-click near edge of design window <br>

## Modify Design Parameters
First double-click on a design in the Project Manager window to make it the active design. Single-clicking the design name will bring up the parameter list in the Properties window below. Here you must enter the values for the physical dimensions of your design (e.g. widths and lengths of transmission lines). You should only modify parameters that pertain to your specific design, changing the substrate parameters can lead to errors in the simulation. When you have entered all of your design parameters and are ready to simulate, click on the green exclamation point ('Analyze All') to begin the simulation. 

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Resources/HFSS_Help/HFSS_Help_Slide1.png)

## View/Export Results
The pre-made HFSS files already have the graphs set up for the data that you need. To view the graphs, expand the design in the Project Manager window and expand the Results section. Here you will find the graphs of the data that you will need for the report (typically S parameters in dB). Double click on the graph names to view them. Right-click on the graph and click "Export...", then choose the file path and click OK. You will need to combine this data with calculations and z0lver data into one .csv file, then use the python program to plot the data. You will need to modify the python code to produce the required plots for a particular lab report.

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Resources/HFSS_Help/HFSS_Help_Slide2.png)
