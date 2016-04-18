import skrf as rf
import csv

# reference:
# 1. create Network object from arrays: http://scikit-rf.readthedocs.org/en/latest/reference/generated/skrf.network.Network.__init__.html#skrf.network.Network.__init__
# 2. plotting: http://scikit-rf.readthedocs.org/en/latest/reference/generated/skrf.network.Network.html#skrf.network.Network

# function:
# convert from csv file to touchstone file (.snp; n = 1, 2, 3...)


def s1p(file_name):
    file_r = open(file_name, 'rb')  # open the file
    csv_data = csv.reader(file_r, delimiter=',')   # convert cvs file to python list

    freq = []   # cell to hold data
    s11 = []    # cell to hold data
    z0 = [50]   # port impedance = 50ohms

    for row in csv_data:   # row contains the row data
        if csv_data.line_num > 8:    # ignore the first 8 line
            if row[0] == 'END':     # check if row reaches the last one
                break
            f = float(row[0])/1e9
            if f >= 2 and f <= 4:   # only plot data from 2 to 3 GHz
                freq.append(f)   # convert from Hz to GHz
                zin_norm = (float(row[1])+1j*float(row[2]))/z0[0]     # normalized input impedance
                s11.append((zin_norm-1.0)/(zin_norm+1.0))    # convert to complex s-parameter

    rf_n = rf.Network(f=freq, s=s11, z0=z0)

    return rf_n

