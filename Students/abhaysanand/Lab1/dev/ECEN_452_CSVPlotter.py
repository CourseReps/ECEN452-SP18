import matplotlib.pyplot as plt
import csv

# Note: In order to use this code, all of the columns in the .csv file must have the same length. If your columns have
# different lengths, simply repeat the last value in each of the shorter columns until they are all the same size.

# Initialize arrays for x, y1, y2, y3
x = []
y1 = []
y2 = []
y3 = []

# Read .csv data file
# replace quoted text below with filepath to your .csv file
with open('ECEN_452_PlottingTestData.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # items in '' below need to exactly match the entry in the first row of the columns in the .csv file
        # edit/add additional lines as needed for each column of data
        x.append(float(row['x']))
        y1.append(float(row['y1']))
        y2.append(float(row['y2']))
        y3.append(float(row['y3']))

# Plotting
plt.figure(1)  # initialize plot1
ax1 = plt.subplot(111)  # create axes handle for plot1
ax1.plot(x, y1, '-b', label="y1 Data")  # plot y1 vs. x, solid-blue, add label for legend
ax1.plot(x, y2, '-r', label="y2 Data")  # plot y2 vs. x, solid-red, add label for legend
ax1.plot(x, y3, '--r', label="y3 Data")  # plot y3 vs. x, dashed-red, add label for legend
ax1.set_xlim(min(x), max(x))  # set x-axis limits
ax1.legend(loc=4)  # add legend at location #4 (bottom-right corner)
plt.grid(b=True, which='both', color='0.65', linestyle='-')  # add solid grey grid-lines
plt.title('Python Test Plot')  # add plot title
plt.xlabel('x-axis [units]')  # add x-axis title
plt.ylabel('y-axis [units]')  # add y-axis title

plt.show()  # required to display plots
