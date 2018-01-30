# import sys
# sys.path.insert(0, 'D:\Github\Programming\Python\pycharm')

import csv
import matplotlib.pyplot as plot

# Reading CSV file
hfss_file1 = open('hfss_ECEN_452_Lab1a_s_para.csv', 'rb')   # open csv file
hfss_file2 = open('hfss_ECEN_452_Lab1b_s_para.csv', 'rb')   # open csv file
z0lver_file1 = open('z0lver_ECEN_452_Lab1a.csv', 'rb')   # open csv file
z0lver_file2 = open('z0lver_ECEN_452_Lab1b.csv', 'rb')   # open csv file
hfss_a_s_para = csv.DictReader(hfss_file1, delimiter=',')   # convert csv file to python DictReader object
hfss_b_s_para = csv.DictReader(hfss_file2, delimiter=',')   # convert csv file to python DictReader object
z0lver_a_s_para = csv.DictReader(z0lver_file1, delimiter=',')   # convert csv file to python DictReader object
z0lver_b_s_para = csv.DictReader(z0lver_file2, delimiter=',')   # convert csv file to python DictReader object

# array to hold all the data
# a = with de-embedding
# b = without de-embedding
hfss_a_freq = []
hfss_a_s11 = []
hfss_a_s12 = []
hfss_a_s21 = []
hfss_a_s22 = []

hfss_b_freq = []
hfss_b_s11 = []
hfss_b_s12 = []
hfss_b_s21 = []
hfss_b_s22 = []

z0lver_a_freq = []
z0lver_a_s11 = []
z0lver_a_s12 = []
z0lver_a_s21 = []
z0lver_a_s22 = []

z0lver_b_freq = []
z0lver_b_s11 = []
z0lver_b_s12 = []
z0lver_b_s21 = []
z0lver_b_s22 = []

# parse the data and store in the list
for a_s_row in hfss_a_s_para:  # row is a python list that contains the data
    # read the column that matches the name 'Freq [GHz]' from a_s_row list
    # then convert to float and store in a array for future processing
    hfss_a_freq.append(float(a_s_row['Freq [GHz]']))
    hfss_a_s11.append(float(a_s_row['dB(S(1,1)) []']))
    hfss_a_s12.append(float(a_s_row['dB(S(1,2)) []']))
    hfss_a_s21.append(float(a_s_row['dB(S(2,1)) []']))
    hfss_a_s22.append(float(a_s_row['dB(S(2,2)) []']))

for b_s_row in hfss_b_s_para:  # row is a python list that contains the data
    # read the column that matches the name 'Freq [GHz]' from a_s_row list
    # then convert to float and store in a array for future processing
    hfss_b_freq.append(float(b_s_row['Freq [GHz]']))
    hfss_b_s11.append(float(b_s_row['dB(S(1,1)) []']))
    hfss_b_s12.append(float(b_s_row['dB(S(1,2)) []']))
    hfss_b_s21.append(float(b_s_row['dB(S(2,1)) []']))
    hfss_b_s22.append(float(b_s_row['dB(S(2,2)) []']))

for a_s_row in z0lver_a_s_para:  # row is a python list that contains the data
    # read the column that matches the name 'frequency' from a_s_row list
    # then convert to float and store in a array for future processing
    z0lver_a_freq.append(round(float(a_s_row['frequency'])/1e9, 3))
    z0lver_a_s11.append(float(a_s_row[' S11']))
    z0lver_a_s12.append(float(a_s_row[' S12']))
    z0lver_a_s21.append(float(a_s_row[' S21']))
    z0lver_a_s22.append(float(a_s_row[' S22']))

for b_s_row in z0lver_b_s_para:  # row is a python list that contains the data
    # read the column that matches the name 'frequency' from a_s_row list
    # then convert to float and store in a array for future processing
    z0lver_b_freq.append(round(float(b_s_row['frequency'])/1e9, 3))
    z0lver_b_s11.append(float(b_s_row[' S11']))
    z0lver_b_s12.append(float(b_s_row[' S12']))
    z0lver_b_s21.append(float(b_s_row[' S21']))
    z0lver_b_s22.append(float(b_s_row[' S22']))

ana_reslt_a_s11 = []
ana_reslt_a_s21 = []
for i in xrange(0, len(z0lver_a_freq)):
    ana_reslt_a_s11.append(-12.4)    # from calculation
    ana_reslt_a_s21.append(-1.05)    # from calculation

ana_reslt_a_s22 = ana_reslt_a_s11     # symmetric circuit
ana_reslt_a_s12 = ana_reslt_a_s21     # symmetric circuit
ana_reslt_b_s11 = ana_reslt_a_s11   # shift reference plane; magnitude doesn't change
ana_reslt_b_s12 = ana_reslt_a_s12   # shift reference plane; magnitude doesn't change
ana_reslt_b_s21 = ana_reslt_a_s21   # shift reference plane; magnitude doesn't change
ana_reslt_b_s22 = ana_reslt_a_s22   # shift reference plane; magnitude doesn't change

# plotting
plot.figure(1)  # create empty figure
ax1 = plot.subplot(221)     # create axes handle for figure 1
ax1.plot(hfss_a_freq, hfss_a_s11, 'r--', label="hfss_a_s11")
ax1.plot(z0lver_a_freq, z0lver_a_s11, 'b-', label="z0lver_a_s11")
ax1.plot(z0lver_a_freq, ana_reslt_a_s11, 'g:', label="analytical_a_s11")
plot.axis([2, 3, -15, -10])     # [xmin, xmax, ymin, ymax]
plot.legend(loc=1)  # loc=4 => bottom right corner
plot.xlabel('Frequency (GHz)')
plot.ylabel('Magnitude (dB)')
plot.title('s-parameter (reference plane not shifted)')
ax2 = plot.subplot(222)     # create axes handle for figure 1
ax2.plot(hfss_a_freq, hfss_a_s12, 'r--', label="hfss_a_s12")
ax2.plot(z0lver_a_freq, z0lver_a_s12, 'b-', label="z0lver_a_s12")
ax2.plot(z0lver_a_freq, ana_reslt_a_s12, 'g:', label="analytical_a_s12")
plot.axis([2, 3, -2, -1])     # [xmin, xmax, ymin, ymax]
plot.legend(loc=4)  # loc=4 => bottom right corner
plot.xlabel('Frequency (GHz)')
plot.ylabel('Magnitude (dB)')
plot.title('s-parameter (reference plane not shifted)')
ax3 = plot.subplot(223)     # create axes handle for figure 1
ax3.plot(hfss_a_freq, hfss_a_s21, 'r--', label="hfss_a_s21")
ax3.plot(z0lver_a_freq, z0lver_a_s21, 'b-', label="z0lver_a_s21")
ax3.plot(z0lver_a_freq, ana_reslt_a_s21, 'g:', label="analytical_a_s21")
plot.axis([2, 3, -2, -1])     # [xmin, xmax, ymin, ymax]
plot.legend(loc=4)  # loc=4 => bottom right corner
plot.xlabel('Frequency (GHz)')
plot.ylabel('Magnitude (dB)')
plot.title('s-parameter (reference plane not shifted)')
ax4 = plot.subplot(224)     # create axes handle for figure 1
ax4.plot(hfss_a_freq, hfss_a_s22, 'r--', label="hfss_a_s22")
ax4.plot(z0lver_a_freq, z0lver_a_s22, 'b-', label="z0lver_a_s22")
ax4.plot(z0lver_a_freq, ana_reslt_a_s22, 'g:', label="analytical_a_s22")
plot.axis([2, 3, -15, -10])     # [xmin, xmax, ymin, ymax]
plot.legend(loc=1)  # loc=4 => bottom right corner
plot.xlabel('Frequency (GHz)')
plot.ylabel('Magnitude (dB)')
plot.title('s-parameter (reference plane not shifted)')

plot.figure(2)  # create empty figure
ax1 = plot.subplot(221)     # create axes handle for figure 1
ax1.plot(hfss_b_freq, hfss_b_s11, 'r--', label="hfss_b_s11")
ax1.plot(z0lver_b_freq, z0lver_b_s11, 'b-', label="z0lver_b_s11")
ax1.plot(z0lver_a_freq, ana_reslt_b_s11, 'g:', label="analytical_b_s11")
plot.axis([2, 3, -15, -10])     # [xmin, xmax, ymin, ymax]
plot.legend(loc=1)  # loc=4 => bottom right corner
plot.xlabel('Frequency (GHz)')
plot.ylabel('Magnitude (dB)')
plot.title('s-parameter (reference plane shifted)')
ax2 = plot.subplot(222)     # create axes handle for figure 1
ax2.plot(hfss_b_freq, hfss_b_s12, 'r--', label="hfss_b_s12")
ax2.plot(z0lver_b_freq, z0lver_b_s12, 'b-', label="z0lver_b_s12")
ax2.plot(z0lver_a_freq, ana_reslt_b_s12, 'g:', label="analytical_b_s12")
plot.axis([2, 3, -2, -1])     # [xmin, xmax, ymin, ymax]
plot.legend(loc=4)  # loc=4 => bottom right corner
plot.xlabel('Frequency (GHz)')
plot.ylabel('Magnitude (dB)')
plot.title('s-parameter (reference plane shifted)')
ax3 = plot.subplot(223)     # create axes handle for figure 1
ax3.plot(hfss_b_freq, hfss_b_s21, 'r--', label="hfss_b_s21")
ax3.plot(z0lver_b_freq, z0lver_b_s21, 'b-', label="z0lver_b_s21")
ax3.plot(z0lver_a_freq, ana_reslt_b_s21, 'g:', label="analytical_b_s21")
plot.axis([2, 3, -2, -1])     # [xmin, xmax, ymin, ymax]
plot.legend(loc=4)  # loc=4 => bottom right corner
plot.xlabel('Frequency (GHz)')
plot.ylabel('Magnitude (dB)')
plot.title('s-parameter (reference plane shifted)')
ax4 = plot.subplot(224)     # create axes handle for figure 1
ax4.plot(hfss_b_freq, hfss_b_s22, 'r--', label="hfss_b_s22")
ax4.plot(z0lver_b_freq, z0lver_b_s22, 'b-', label="z0lver_b_s22")
ax4.plot(z0lver_a_freq, ana_reslt_b_s22, 'g:', label="analytical_b_s22")
plot.axis([2, 3, -15, -10])     # [xmin, xmax, ymin, ymax]
plot.legend(loc=1)  # loc=4 => bottom right corner
plot.xlabel('Frequency (GHz)')
plot.ylabel('Magnitude (dB)')
plot.title('s-parameter (reference plane shifted)')
plot.show()
