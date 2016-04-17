# Program Function:
#   1. plots the s21 measured_phase and magnitude from the measurement data (.csv) of a TRL line standard
#   2. poly curve fit the data and use the equation to extrapolate the data

# Notes:
#   1. poly fit example: http://stackoverflow.com/questions/19165259/python-numpy-scipy-curve-fitting
#   2. poly fit reference: http://docs.scipy.org/doc/numpy-1.10.0/reference/generated/numpy.polyfit.html
#   3. p = np.poly1d(z) import poly fit result to create the poly equation, p(x) can be used as the poly equation

import csv
from matplotlib import pyplot as plot

file1 = open('lab8_hybrid_coupler_port_matching.csv', 'rb')  # open the file
hybrid_port_match = csv.reader(file1, delimiter=',')   # convert cvs file to python list
file1 = open('lab8_hybrid_coupler_transmission.csv', 'rb')  # open the file
hybrid_trans_mag = csv.reader(file1, delimiter=',')   # convert cvs file to python list
file1 = open('lab8_hybrid_coupler_transmission_phase.csv', 'rb')  # open the file
hybrid_trans_phase = csv.reader(file1, delimiter=',')   # convert cvs file to python list
file1 = open('lab8_hybrid_coupler_port_isolation.csv', 'rb')  # open the file
hybrid_port_iso = csv.reader(file1, delimiter=',')   # convert cvs file to python list

file1 = open('lab8_rat_race_coupler_port_matching.csv', 'rb')  # open the file
rat_race_port_match = csv.reader(file1, delimiter=',')   # convert cvs file to python list
file1 = open('lab8_rat_race_coupler_transmission.csv', 'rb')  # open the file
rat_race_trans_mag = csv.reader(file1, delimiter=',')   # convert cvs file to python list
file1 = open('lab8_rat_race_coupler_transmission_phase.csv', 'rb')  # open the file
rat_race_trans_phase = csv.reader(file1, delimiter=',')   # convert cvs file to python list
file1 = open('lab8_rat_race_coupler_port_isolation.csv', 'rb')  # open the file
rat_race_port_iso = csv.reader(file1, delimiter=',')   # convert cvs file to python list

file1 = open('Milled_Hybrid_S11.csv', 'rb')  # open the file
csv_hybrid_s11 = csv.reader(file1, delimiter=',')   # convert cvs file to python list
file1 = open('Milled_Hybrid_S21.csv', 'rb')  # open the file
csv_hybrid_s21 = csv.reader(file1, delimiter=',')   # convert cvs file to python list
file1 = open('Milled_Hybrid_S22.csv', 'rb')  # open the file
csv_hybrid_s22 = csv.reader(file1, delimiter=',')   # convert cvs file to python list
file1 = open('Milled_Hybrid_S31.csv', 'rb')  # open the file
csv_hybrid_s31 = csv.reader(file1, delimiter=',')   # convert cvs file to python list
file1 = open('Milled_Hybrid_S32.csv', 'rb')  # open the file
csv_hybrid_s32 = csv.reader(file1, delimiter=',')   # convert cvs file to python list
file1 = open('Milled_Hybrid_S33.csv', 'rb')  # open the file
csv_hybrid_s33 = csv.reader(file1, delimiter=',')   # convert cvs file to python list
file1 = open('Milled_Hybrid_S41.csv', 'rb')  # open the file
csv_hybrid_s41 = csv.reader(file1, delimiter=',')   # convert cvs file to python list
file1 = open('Milled_Hybrid_S42.csv', 'rb')  # open the file
csv_hybrid_s42 = csv.reader(file1, delimiter=',')   # convert cvs file to python list
file1 = open('Milled_Hybrid_S43.csv', 'rb')  # open the file
csv_hybrid_s43 = csv.reader(file1, delimiter=',')   # convert cvs file to python list
file1 = open('Milled_Hybrid_S44.csv', 'rb')  # open the file
csv_hybrid_s44 = csv.reader(file1, delimiter=',')   # convert cvs file to python list

file1 = open('Milled_RatRace_S11.csv', 'rb')  # open the file
csv_rat_race_s11 = csv.reader(file1, delimiter=',')   # convert cvs file to python list
file1 = open('Milled_RatRace_S21.csv', 'rb')  # open the file
csv_rat_race_s21 = csv.reader(file1, delimiter=',')   # convert cvs file to python list
file1 = open('Milled_RatRace_S22.csv', 'rb')  # open the file
csv_rat_race_s22 = csv.reader(file1, delimiter=',')   # convert cvs file to python list
file1 = open('Milled_RatRace_S31.csv', 'rb')  # open the file
csv_rat_race_s31 = csv.reader(file1, delimiter=',')   # convert cvs file to python list
file1 = open('Milled_RatRace_S23.csv', 'rb')  # open the file
csv_rat_race_s23 = csv.reader(file1, delimiter=',')   # convert cvs file to python list
file1 = open('Milled_RatRace_S33.csv', 'rb')  # open the file
csv_rat_race_s33 = csv.reader(file1, delimiter=',')   # convert cvs file to python list
file1 = open('Milled_RatRace_S41.csv', 'rb')  # open the file
csv_rat_race_s41 = csv.reader(file1, delimiter=',')   # convert cvs file to python list
file1 = open('Milled_RatRace_S42.csv', 'rb')  # open the file
csv_rat_race_s42 = csv.reader(file1, delimiter=',')   # convert cvs file to python list
file1 = open('Milled_RatRace_S43.csv', 'rb')  # open the file
csv_rat_race_s43 = csv.reader(file1, delimiter=',')   # convert cvs file to python list
file1 = open('Milled_RatRace_S44.csv', 'rb')  # open the file
csv_rat_race_s44 = csv.reader(file1, delimiter=',')   # convert cvs file to python list

# extract information from csv and store in the following lists for plotting and processing
freq = []
hybrid_meas_s11_mag = []
hybrid_meas_s22_mag = []
hybrid_meas_s33_mag = []
hybrid_meas_s44_mag = []
hybrid_meas_s21_mag = []
hybrid_meas_s31_mag = []
hybrid_meas_s41_mag = []
hybrid_meas_s32_mag = []
hybrid_meas_s42_mag = []
hybrid_meas_s43_mag = []

hybrid_meas_s21_phase = []
hybrid_meas_s31_phase = []

hybrid_hfss_s11_mag = []
hybrid_hfss_s22_mag = []
hybrid_hfss_s33_mag = []
hybrid_hfss_s44_mag = []
hybrid_hfss_s21_mag = []
hybrid_hfss_s31_mag = []
hybrid_hfss_s41_mag = []
hybrid_hfss_s32_mag = []
hybrid_hfss_s42_mag = []
hybrid_hfss_s43_mag = []

hybrid_hfss_s21_phase = []
hybrid_hfss_s31_phase = []

rat_race_meas_s11_mag = []
rat_race_meas_s22_mag = []
rat_race_meas_s33_mag = []
rat_race_meas_s44_mag = []
rat_race_meas_s21_mag = []
rat_race_meas_s31_mag = []
rat_race_meas_s41_mag = []
rat_race_meas_s32_mag = []
rat_race_meas_s42_mag = []
rat_race_meas_s43_mag = []

rat_race_meas_s21_phase = []
rat_race_meas_s31_phase = []

rat_race_hfss_s11_mag = []
rat_race_hfss_s22_mag = []
rat_race_hfss_s33_mag = []
rat_race_hfss_s44_mag = []
rat_race_hfss_s21_mag = []
rat_race_hfss_s31_mag = []
rat_race_hfss_s41_mag = []
rat_race_hfss_s32_mag = []
rat_race_hfss_s42_mag = []
rat_race_hfss_s43_mag = []

rat_race_hfss_s21_phase = []
rat_race_hfss_s31_phase = []

freq_marker = []
meas_s21_marker = []
meas_s31_marker = []
hfss_sim_s21_marker = []
hfss_sim_s31_marker = []
z0lver_sim_s21_marker = []
meas_s31_marker = []
hfss_sim_s31_marker = []
z0lver_sim_s31_marker = []
marker1 = 2.5

for row in hybrid_port_match:   # row contains the row data
    if hybrid_port_match.line_num > 1:    # ignore the first line
        if row[0] == 'END':     # check if row reaches the last one
            break
        freq.append(float(row[0]))   # convert from Hz to GHz
        hybrid_hfss_s11_mag.append(float(row[1]))
        hybrid_hfss_s22_mag.append(float(row[2]))
        hybrid_hfss_s33_mag.append(float(row[3]))
        hybrid_hfss_s44_mag.append(float(row[4]))

for row in hybrid_trans_mag:   # row contains the row data
    if hybrid_trans_mag.line_num > 1:    # ignore the first line
        if row[0] == 'END':     # check if row reaches the last one
            break
        hybrid_hfss_s21_mag.append(float(row[2]))
        hybrid_hfss_s31_mag.append(float(row[3]))
        hybrid_hfss_s41_mag.append(float(row[4]))
        if float(row[0]) == 2.5:
            hfss_sim_s21_marker.append(float(row[2]))
            hfss_sim_s31_marker = [float(row[3])]

print hfss_sim_s21_marker
print hfss_sim_s31_marker

for row in hybrid_trans_phase:   # row contains the row data
    if hybrid_trans_phase.line_num > 1:    # ignore the first line
        if row[0] == 'END':     # check if row reaches the last one
            break
        hybrid_hfss_s21_phase.append(float(row[1]))
        hybrid_hfss_s31_phase.append(float(row[2]))

for row in hybrid_port_iso:   # row contains the row data
    if hybrid_port_iso.line_num > 1:    # ignore the first line
        if row[0] == 'END':     # check if row reaches the last one
            break
        hybrid_hfss_s32_mag.append(float(row[1]))
        hybrid_hfss_s42_mag.append(float(row[2]))
        hybrid_hfss_s43_mag.append(float(row[3]))

for row in csv_hybrid_s11:   # row contains the row data
    if csv_hybrid_s11.line_num > 8:    # ignore the first line
        if row[0] == 'END':     # check if row reaches the last one
            break
        hybrid_meas_s11_mag.append(float(row[1]))

for row in csv_hybrid_s22:   # row contains the row data
    if csv_hybrid_s22.line_num > 8:    # ignore the first line
        if row[0] == 'END':     # check if row reaches the last one
            break
        hybrid_meas_s22_mag.append(float(row[1]))

for row in csv_hybrid_s33:   # row contains the row data
    if csv_hybrid_s33.line_num > 8:    # ignore the first line
        if row[0] == 'END':     # check if row reaches the last one
            break
        hybrid_meas_s33_mag.append(float(row[1]))

for row in csv_hybrid_s44:   # row contains the row data
    if csv_hybrid_s44.line_num > 8:    # ignore the first line
        if row[0] == 'END':     # check if row reaches the last one
            break
        hybrid_meas_s44_mag.append(float(row[1]))

for row in csv_hybrid_s21:   # row contains the row data
    if csv_hybrid_s21.line_num > 8:    # ignore the first line
        if row[0] == 'END':     # check if row reaches the last one
            break
        hybrid_meas_s21_mag.append(float(row[1]))
        hybrid_meas_s21_phase.append(float(row[2]))

for row in csv_hybrid_s31:   # row contains the row data
    if csv_hybrid_s31.line_num > 8:    # ignore the first line
        if row[0] == 'END':     # check if row reaches the last one
            break
        hybrid_meas_s31_mag.append(float(row[1]))
        hybrid_meas_s31_phase.append(float(row[2]))

for row in csv_hybrid_s41:   # row contains the row data
    if csv_hybrid_s41.line_num > 8:    # ignore the first line
        if row[0] == 'END':     # check if row reaches the last one
            break
        hybrid_meas_s41_mag.append(float(row[1]))

for row in csv_hybrid_s32:   # row contains the row data
    if csv_hybrid_s32.line_num > 8:    # ignore the first line
        if row[0] == 'END':     # check if row reaches the last one
            break
        hybrid_meas_s32_mag.append(float(row[1]))

for row in csv_hybrid_s42:   # row contains the row data
    if csv_hybrid_s42.line_num > 8:    # ignore the first line
        if row[0] == 'END':     # check if row reaches the last one
            break
        hybrid_meas_s42_mag.append(float(row[1]))

for row in csv_hybrid_s43:   # row contains the row data
    if csv_hybrid_s43.line_num > 8:    # ignore the first line
        if row[0] == 'END':     # check if row reaches the last one
            break
        hybrid_meas_s43_mag.append(float(row[1]))

for row in rat_race_port_match:   # row contains the row data
    if rat_race_port_match.line_num > 1:    # ignore the first line
        if row[0] == 'END':     # check if row reaches the last one
            break
        rat_race_hfss_s11_mag.append(float(row[1]))
        rat_race_hfss_s22_mag.append(float(row[2]))
        rat_race_hfss_s33_mag.append(float(row[3]))
        rat_race_hfss_s44_mag.append(float(row[4]))

for row in rat_race_trans_mag:   # row contains the row data
    if rat_race_trans_mag.line_num > 1:    # ignore the first line
        if row[0] == 'END':     # check if row reaches the last one
            break
        rat_race_hfss_s21_mag.append(float(row[2]))
        rat_race_hfss_s31_mag.append(float(row[3]))
        rat_race_hfss_s41_mag.append(float(row[4]))

for row in rat_race_trans_phase:   # row contains the row data
    if rat_race_trans_phase.line_num > 1:    # ignore the first line
        if row[0] == 'END':     # check if row reaches the last one
            break
        rat_race_hfss_s21_phase.append(float(row[1]))
        rat_race_hfss_s31_phase.append(float(row[2]))

for row in rat_race_port_iso:   # row contains the row data
    if rat_race_port_iso.line_num > 1:    # ignore the first line
        if row[0] == 'END':     # check if row reaches the last one
            break
        rat_race_hfss_s32_mag.append(float(row[1]))
        rat_race_hfss_s42_mag.append(float(row[2]))
        rat_race_hfss_s43_mag.append(float(row[3]))

for row in csv_rat_race_s11:   # row contains the row data
    if csv_rat_race_s11.line_num > 8:    # ignore the first line
        if row[0] == 'END':     # check if row reaches the last one
            break
        rat_race_meas_s11_mag.append(float(row[1]))

for row in csv_rat_race_s22:   # row contains the row data
    if csv_rat_race_s22.line_num > 8:    # ignore the first line
        if row[0] == 'END':     # check if row reaches the last one
            break
        rat_race_meas_s22_mag.append(float(row[1]))

for row in csv_rat_race_s33:   # row contains the row data
    if csv_rat_race_s33.line_num > 8:    # ignore the first line
        if row[0] == 'END':     # check if row reaches the last one
            break
        rat_race_meas_s33_mag.append(float(row[1]))

for row in csv_rat_race_s44:   # row contains the row data
    if csv_rat_race_s44.line_num > 8:    # ignore the first line
        if row[0] == 'END':     # check if row reaches the last one
            break
        rat_race_meas_s44_mag.append(float(row[1]))

for row in csv_rat_race_s21:   # row contains the row data
    if csv_rat_race_s21.line_num > 8:    # ignore the first line
        if row[0] == 'END':     # check if row reaches the last one
            break
        rat_race_meas_s21_mag.append(float(row[1]))
        rat_race_meas_s21_phase.append(float(row[2]))

for row in csv_rat_race_s31:   # row contains the row data
    if csv_rat_race_s31.line_num > 8:    # ignore the first line
        if row[0] == 'END':     # check if row reaches the last one
            break
        rat_race_meas_s31_mag.append(float(row[1]))
        rat_race_meas_s31_phase.append(float(row[2]))

for row in csv_rat_race_s41:   # row contains the row data
    if csv_rat_race_s41.line_num > 8:    # ignore the first line
        if row[0] == 'END':     # check if row reaches the last one
            break
        rat_race_meas_s41_mag.append(float(row[1]))

for row in csv_rat_race_s23:   # row contains the row data
    if csv_rat_race_s23.line_num > 8:    # ignore the first line
        if row[0] == 'END':     # check if row reaches the last one
            break
        rat_race_meas_s32_mag.append(float(row[1]))

for row in csv_rat_race_s42:   # row contains the row data
    if csv_rat_race_s42.line_num > 8:    # ignore the first line
        if row[0] == 'END':     # check if row reaches the last one
            break
        rat_race_meas_s42_mag.append(float(row[1]))

for row in csv_rat_race_s43:   # row contains the row data
    if csv_rat_race_s43.line_num > 8:    # ignore the first line
        if row[0] == 'END':     # check if row reaches the last one
            break
        rat_race_meas_s43_mag.append(float(row[1]))

n = 0
n += 1
plot.figure(n)
ax0 = plot.subplot(111)
ax0.plot(freq, hybrid_meas_s11_mag, 'r-', label="measured |s11|")
ax0.plot(freq, hybrid_meas_s22_mag, 'b-', label="measured |s22|")
ax0.plot(freq, hybrid_meas_s33_mag, 'g-', label="measured |s33|")
ax0.plot(freq, hybrid_meas_s44_mag, 'k-', label="measured |s44|")
ax0.plot(freq, hybrid_hfss_s11_mag, 'r--', label="simulated |s11|")
ax0.plot(freq, hybrid_hfss_s22_mag, 'b--', label="simulated |s22|")
ax0.plot(freq, hybrid_hfss_s33_mag, 'g--', label="simulated |s33|")
ax0.plot(freq, hybrid_hfss_s44_mag, 'k--', label="simulated |s44|")
ax0.axis([1, 5, -45, 0])     # [xmin, xmax, ymin, ymax]
plot.xlabel('Frequency (GHz)')
plot.ylabel('|s| (dB)')
plot.title('Hybrid Coupler Port matching')
plot.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)  # loc=4 => bottom right corner
plot.tight_layout(pad=0.15, w_pad=0, h_pad=0)
plot.subplots_adjust(left=0.1, right=0.7, top=0.9, bottom=0.1, hspace=0, wspace=0)

n += 1
plot.figure(n)
ax0 = plot.subplot(111)
ax0.plot(freq, hybrid_meas_s21_mag, 'r-', label="measured |s21|")
ax0.plot(freq, hybrid_meas_s31_mag, 'b-', label="measured |s31|")
ax0.plot(freq, hybrid_meas_s41_mag, 'g-', label="measured |s41|")
ax0.plot(freq, hybrid_hfss_s21_mag, 'r--', label="simulated |s21|")
ax0.plot(freq, hybrid_hfss_s31_mag, 'b--', label="simulated |s31|")
ax0.plot(freq, hybrid_hfss_s41_mag, 'g--', label="simulated |s41|")
ax0.axis([1, 5, -45, 0])     # [xmin, xmax, ymin, ymax]
plot.xlabel('Frequency (GHz)')
plot.ylabel('|s| (dB)')
plot.title('Hybrid Coupler Port transmission')
plot.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)  # loc=4 => bottom right corner
plot.tight_layout(pad=0.15, w_pad=0, h_pad=0)
plot.subplots_adjust(left=0.1, right=0.7, top=0.9, bottom=0.1, hspace=0, wspace=0)

n += 1
plot.figure(n)
ax0 = plot.subplot(111)
ax0.plot(freq, hybrid_meas_s21_phase, 'r-', label="measured s21 phase")
ax0.plot(freq, hybrid_meas_s31_phase, 'b-', label="measured s31 phase")
ax0.plot(freq, hybrid_hfss_s21_phase, 'r--', label="simulated s21 phase")
ax0.plot(freq, hybrid_hfss_s31_phase, 'b--', label="simulated s31 phase")
# ax0.axis([1, 5, -45, 0])     # [xmin, xmax, ymin, ymax]
plot.xlabel('Frequency (GHz)')
plot.ylabel('Phase (deg)')
plot.title('Hybrid Coupler Port transmission Phase')
plot.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)  # loc=4 => bottom right corner
plot.tight_layout(pad=0.15, w_pad=0, h_pad=0)
plot.subplots_adjust(left=0.1, right=0.7, top=0.9, bottom=0.1, hspace=0, wspace=0)

n += 1
plot.figure(n)
ax0 = plot.subplot(111)
ax0.plot(freq, hybrid_meas_s32_mag, 'r-', label="measured |s32|")
ax0.plot(freq, hybrid_meas_s42_mag, 'b-', label="measured |s42|")
ax0.plot(freq, hybrid_meas_s43_mag, 'g-', label="measured |s43|")
ax0.plot(freq, hybrid_hfss_s32_mag, 'r--', label="simulated |s32|")
ax0.plot(freq, hybrid_hfss_s42_mag, 'b--', label="simulated |s42|")
ax0.plot(freq, hybrid_hfss_s43_mag, 'g--', label="simulated |s43|")
ax0.axis([1, 5, -45, 0])     # [xmin, xmax, ymin, ymax]
plot.xlabel('Frequency (GHz)')
plot.ylabel('|s| (dB)')
plot.title('Hybrid Coupler Port Isolation')
plot.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)  # loc=4 => bottom right corner
plot.tight_layout(pad=0.15, w_pad=0, h_pad=0)
plot.subplots_adjust(left=0.1, right=0.7, top=0.9, bottom=0.1, hspace=0, wspace=0)

n += 1
plot.figure(n)
ax0 = plot.subplot(111)
ax0.plot(freq, rat_race_meas_s11_mag, 'r-', label="measured |s11|")
ax0.plot(freq, rat_race_meas_s22_mag, 'b-', label="measured |s22|")
ax0.plot(freq, rat_race_meas_s33_mag, 'g-', label="measured |s33|")
ax0.plot(freq, rat_race_meas_s44_mag, 'k-', label="measured |s44|")
ax0.plot(freq, rat_race_hfss_s11_mag, 'r--', label="simulated |s11|")
ax0.plot(freq, rat_race_hfss_s22_mag, 'b--', label="simulated |s22|")
ax0.plot(freq, rat_race_hfss_s33_mag, 'g--', label="simulated |s33|")
ax0.plot(freq, rat_race_hfss_s44_mag, 'k--', label="simulated |s44|")
ax0.axis([1, 5, -45, 0])     # [xmin, xmax, ymin, ymax]
plot.xlabel('Frequency (GHz)')
plot.ylabel('|s| (dB)')
plot.title('rat_race Coupler Port matching')
plot.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)  # loc=4 => bottom right corner
plot.tight_layout(pad=0.15, w_pad=0, h_pad=0)
plot.subplots_adjust(left=0.1, right=0.7, top=0.9, bottom=0.1, hspace=0, wspace=0)

n += 1
plot.figure(n)
ax0 = plot.subplot(111)
ax0.plot(freq, rat_race_meas_s21_mag, 'r-', label="measured |s21|")
ax0.plot(freq, rat_race_meas_s31_mag, 'b-', label="measured |s31|")
ax0.plot(freq, rat_race_meas_s41_mag, 'g-', label="measured |s41|")
ax0.plot(freq, rat_race_hfss_s21_mag, 'r--', label="simulated |s21|")
ax0.plot(freq, rat_race_hfss_s31_mag, 'b--', label="simulated |s31|")
ax0.plot(freq, rat_race_hfss_s41_mag, 'g--', label="simulated |s41|")
ax0.axis([1, 5, -45, 0])     # [xmin, xmax, ymin, ymax]
plot.xlabel('Frequency (GHz)')
plot.ylabel('|s| (dB)')
plot.title('rat_race Coupler Port transmission')
plot.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)  # loc=4 => bottom right corner
plot.tight_layout(pad=0.15, w_pad=0, h_pad=0)
plot.subplots_adjust(left=0.1, right=0.7, top=0.9, bottom=0.1, hspace=0, wspace=0)

n += 1
plot.figure(n)
ax0 = plot.subplot(111)
ax0.plot(freq, rat_race_meas_s21_phase, 'r-', label="measured s21 phase")
ax0.plot(freq, rat_race_meas_s31_phase, 'b-', label="measured s31 phase")
ax0.plot(freq, rat_race_hfss_s21_phase, 'r--', label="simulated s21 phase")
ax0.plot(freq, rat_race_hfss_s31_phase, 'b--', label="simulated s31 phase")
# ax0.axis([1, 5, -45, 0])     # [xmin, xmax, ymin, ymax]
plot.xlabel('Frequency (GHz)')
plot.ylabel('Phase (deg)')
plot.title('rat_race Coupler Port transmission Phase')
plot.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)  # loc=4 => bottom right corner
plot.tight_layout(pad=0.15, w_pad=0, h_pad=0)
plot.subplots_adjust(left=0.1, right=0.7, top=0.9, bottom=0.1, hspace=0, wspace=0)

n += 1
plot.figure(n)
ax0 = plot.subplot(111)
ax0.plot(freq, rat_race_meas_s32_mag, 'r-', label="measured |s32|")
ax0.plot(freq, rat_race_meas_s42_mag, 'b-', label="measured |s42|")
ax0.plot(freq, rat_race_meas_s43_mag, 'g-', label="measured |s43|")
ax0.plot(freq, rat_race_hfss_s32_mag, 'r--', label="simulated |s32|")
ax0.plot(freq, rat_race_hfss_s42_mag, 'b--', label="simulated |s42|")
ax0.plot(freq, rat_race_hfss_s43_mag, 'g--', label="simulated |s43|")
ax0.axis([1, 5, -45, 0])     # [xmin, xmax, ymin, ymax]
plot.xlabel('Frequency (GHz)')
plot.ylabel('|s| (dB)')
plot.title('rat_race Coupler Port Isolation')
plot.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)  # loc=4 => bottom right corner
plot.tight_layout(pad=0.15, w_pad=0, h_pad=0)
plot.subplots_adjust(left=0.1, right=0.7, top=0.9, bottom=0.1, hspace=0, wspace=0)

plot.show()

file1.close()
