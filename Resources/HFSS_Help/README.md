# HFSS Help

Each lab requires you to simulate designs in HFSS. For the first few labs, you will be given pre-made HFSS files that will already have the core design, simulation setup, and result graphs that you need. For these pre-made files, you will need to input your calculated dimensions into the design parameters, run the simulation, and export the data as a .csv file. This document will provide some basic tips for running your simulation and getting the data you need for the lab reports.<br>

(Edit 3/11/2016) This document now also serves as a tutorial to model, analyze, and obtain data for original designs.

## Creating a New Design
When you open HFSS you will see a blank project in the Project Manager window. Click the blue icon in the upper left corner to 'Insert HFSS Design' to the project. You can add multiple designs to a single project as needed. Each design will have its own parameters, solutions setups, frequency sweeps, data reports, etc. Double-click on the design name in the Project Manager window to make it the active design. You may also copy and paste designs in the project, which is useful when you want to make variations on a similar design.

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Resources/HFSS_Help/New_Deisgn.png)

## Navigating the Model Space
Rotate: Hold Alt -> click and drag <br>
Pan: Hold Shift -> click and drag <br>
Zoom: Hold Alt+Shift -> click and drag OR use scroll wheel <br>
Zoom Fit: Hold Alt+Shift -> double-click <br>
Snap to View: Hold Alt -> double-click near edge of design window <br>

## Creating Objects
A new HFSS design file consists of an empty model space. HFSS will not solve for fields in the empty space, therefore it can be treated as a perfect electric conductor (PEC) since there are no fields inside it. In order to simulate something, you must model your design using 2- and 3-dimensional objects. Then, you assign materials to the objects such as FR4, Duroid 5880, PEC, Copper, Vacuum etc. This section will walk through the process of creating a microstrip line on a substrate with a region of air above it.

### Step 1: Create Box for Substrate
The substrate is modeled as a 3-D box in HFSS. Click 'Draw box' in the toolbar to enter the drawing mode (note the other 3-D shapes available in the toolbar).  Now click in three different points in the model space to set the dimensions for the box. These points can be completely random, because we will define the exact dimensions next. <br>

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Resources/HFSS_Help/Draw_Box.png)

To the left of the model space you will see a list of all of the objects in your design. Expand the branch for the box you just created and double-click on ‘CreateBox’. This brings up the model position and dimension information for the box. For boxes, the Position refers to the x,y,z coordinates of one corner of the box. The XSize, YSize, and ZSize values are the dimensions in x, y, and z from the corner referenced by Position. <br>

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Resources/HFSS_Help/Create_Box.png)

For this example, we want the substrate centered at the origin with the top surface on the XY-plane. We will use parameters to define all of the dimensions in our design so that we can easily make modifications later. Parameters are automatically created when you enter a string as a value. <br>

First, enter a string as the value for XSize, we will use ‘subx’ in this example which stands for “substrate x dimension”, but you can choose whatever name makes sense to you. When you hit Enter you will be prompted to define your newly created parameter, this value can be changed later from your parameter list. Repeat this process for the YSize and ZSize. <br>

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Resources/HFSS_Help/Create_Box_Parameters.png)

Now you can use your substrate parameters to define the Position of the box. For the Position value, enter “-subx/2,-suby/2,0”, or the equivalent with the parameter names you chose. This sets the reference corner of the box such that it is centered in X and Y. If you set the ZSize to be a negative value of the substrate height, then the box will start at z=0 and extend down from there. If you consistently use parameters to define dimensions and positions then your design will automatically adjust each object if you change the value of a parameter. Click 'OK' to close the CreateBox window and keep your changes. <br>  

Now in the sidebar double-click on the name of the box you created (‘Box1’ by default) to bring up the properties window for the object. In this window you can change the name of the object, adjust the color and transparency, and assign a material to the object. First, change the name to ‘Substrate’ or whatever makes sense to you (this is to help you keep organized when you have several objects in your design). Next, click on the drop-down value for Material and click ‘Edit’. This brings up the HFSS materials library. You can use the search bar to find a particular material, or you can add a material if it is not already in the library.<br>

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Resources/HFSS_Help/Box_Properties.png)

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Resources/HFSS_Help/Assign_Material.png)

<b>The FR4 in the materials library has a relative permittivity of 4.4 which is different from the FR4 we have. To change this, highlight FR4_epoxy in the list and click on ‘View/Edit Materials …’. Then, change the value of the relative permittivity to 4.1 and click ‘OK’.</b> <br>

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Resources/HFSS_Help/Edit_Materials.png)<br>

I typically change the transparency of substrates to 0.8 to make the traces on top easier to see, but that is up to the designer. 

## Modify Design Parameters
First double-click on a design in the Project Manager window to make it the active design. Single-clicking the design name will bring up the parameter list in the Properties window below. Here you must enter the values for the physical dimensions of your design (e.g. widths and lengths of transmission lines). You should only modify parameters that pertain to your specific design, changing the substrate parameters can lead to errors in the simulation. When you have entered all of your design parameters and are ready to simulate, click on the green exclamation point ('Analyze All') to begin the simulation. 

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Resources/HFSS_Help/HFSS_Help_Slide1.png)

## View/Export Results
The pre-made HFSS files already have the graphs set up for the data that you need. To view the graphs, expand the design in the Project Manager window and expand the Results section. Here you will find the graphs of the data that you will need for the report (typically S parameters in dB). Double click on the graph names to view them. Right-click on the graph and click "Export...", then choose the file path and click OK. You will need to combine this data with calculations and z0lver data into one .csv file, then use the python program to plot the data. You will need to modify the python code to produce the required plots for a particular lab report.

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Resources/HFSS_Help/HFSS_Help_Slide2.png)

## Port De-Embedding
Since we will be using a TRL calibration when measuring our devices, it is important to use port de-embedding in our HFSS simulations so that the reference plane is the same for simulated and measured data. To de-embed a port, expand the Excitations section under the design name in the Project Manager window and click on the port number. Then, in the Properties window below, click the "Deembed" checkbox and enter the "Deembed Distance" (TRL reference plane). Repeat this for each port. 

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Resources/HFSS_Help/HFSS_DeEmbedding.png)
