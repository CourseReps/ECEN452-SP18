import skrf as rf
import os
from matplotlib import pyplot as plot
from mod_snp import s1p

# convert from csv file to touchstone file (.snp; n = 1, 2, 3...)

rf_n1 = s1p('HP_JP_QWT.csv')
rf_n2 = s1p('HP_JP_Unmatched.csv')

fig = plot.figure(1, figsize=(8, 6), dpi=80, facecolor='w')
fig.suptitle("Patch Antenna s11", fontsize=15, y=0.95)
rf_n1.plot_s_smith(label='QWT s11', color='r')
rf_n2.plot_s_smith(label='unmatched s11', color='b')
plot.subplots_adjust(left=0, right=1, top=0.9, bottom=0, hspace=0, wspace=0)
plot.legend(bbox_to_anchor=(1, 1))  # adjust box location
plot.savefig('smith_chart', dpi=200, facecolor='w', edgecolor='k')

fig = plot.figure(2, figsize=(8, 6), dpi=80, facecolor='w')
fig.suptitle("Patch Antenna |s11|", fontsize=15, y=0.95)
rf_n1.plot_s_db(label='QWT |s11|', color='r')
rf_n2.plot_s_db(label='unmatched |s11|', color='b')
plot.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1, hspace=0, wspace=0)
plot.legend(bbox_to_anchor=(1, 0.2))  # adjust box location
plot.savefig('s11_mag', dpi=200, facecolor='w', edgecolor='k')

plot.show()
