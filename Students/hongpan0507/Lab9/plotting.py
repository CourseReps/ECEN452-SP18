import skrf as rf
import os
from matplotlib import pyplot as plot
from mod_snp import imp_s1p, s11_s1p

# convert from csv file to touchstone file (.snp; n = 1, 2, 3...)
sim_rf_n1 = s11_s1p('lab9_patch_s11_smith.csv')

meas_rf_n1 = imp_s1p('HP_JP_QWT.csv')
meas_rf_n2 = imp_s1p('HP_JP_Unmatched.csv')

n = 0
n += 1
fig = plot.figure(n, figsize=(10, 6), dpi=80, facecolor='w')
fig.suptitle("Patch Antenna s11", fontsize=15, y=0.95)
meas_rf_n1.plot_s_smith(label='measured QWT s11', color='r')
meas_rf_n2.plot_s_smith(label='measured unmatched s11', color='b')
plot.subplots_adjust(left=0, right=0.8, top=0.9, bottom=0, hspace=0, wspace=0)
plot.legend(bbox_to_anchor=(1.2, 1))  # adjust box location
plot.savefig('smith_chart1', dpi=200, facecolor='w', edgecolor='k')

n += 1
fig = plot.figure(n, figsize=(10, 6), dpi=80, facecolor='w')
fig.suptitle("Patch Antenna |s11|", fontsize=15, y=0.95)
meas_rf_n1.plot_s_db(label='measured QWT |s11|', color='r')
meas_rf_n2.plot_s_db(label='measured unmatched |s11|', color='b')
plot.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1, hspace=0, wspace=0)
plot.legend(bbox_to_anchor=(1, 0.2))  # adjust box location
plot.savefig('s11_mag1', dpi=200, facecolor='w', edgecolor='k')

n += 1
fig = plot.figure(n, figsize=(10, 6), dpi=80, facecolor='w')
fig.suptitle("Patch Antenna s11", fontsize=15, y=0.95)
meas_rf_n1.plot_s_smith(label='measured edge-fed QWT s11', color='r')
sim_rf_n1.plot_s_smith(label='simulated probe-fed s11', color='b')
plot.subplots_adjust(left=0, right=0.8, top=0.9, bottom=0, hspace=0, wspace=0)
plot.legend(bbox_to_anchor=(1.2, 1))  # adjust box location
plot.savefig('smith_chart2', dpi=200, facecolor='w', edgecolor='k')

n += 1
fig = plot.figure(n, figsize=(10, 6), dpi=80, facecolor='w')
fig.suptitle("Patch Antenna |s11|", fontsize=15, y=0.95)
meas_rf_n1.plot_s_db(label='measured edge-fed QWT |s11|', color='r')
sim_rf_n1.plot_s_db(label='simulated probe-fed |s11|', color='b')
plot.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1, hspace=0, wspace=0)
plot.legend(bbox_to_anchor=(1, 0.2))  # adjust box location
plot.savefig('s11_mag2', dpi=200, facecolor='w', edgecolor='k')

plot.show()
