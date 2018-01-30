import skrf as rf
import os
from matplotlib import pyplot as plot
from mod_snp import s1p

# convert from csv file to touchstone file (.snp; n = 1, 2, 3...)

rf_n1 = s1p('HP_JP_QWT.csv')
rf_n2 = s1p('HP_JP_Unmatched.csv')

fig = plot.figure(1, figsize=(8, 6), dpi=80, facecolor='w', edgecolor='k')
fig.suptitle("Patch s11", fontsize=15, y=0.95)
rf_n1.plot_s_smith(label='QWT s11', color='r')
rf_n2.plot_s_smith(label='unmatched s11', color='b')
plot.subplots_adjust(left=0, right=1, top=0.85, bottom=0.15, hspace=0, wspace=0)
plot.legend(bbox_to_anchor=(1, 1))  # adjust box location
plot.show()

# ts_file = os.path.join(rf.data.pwd, 'ring slot.s2p')
# ring_slot = rf.Network(ts_file)
# print "ring slot: "
# print ring_slot
# ring_slot.plot_s_smith(m=0, n=0)
# plot.show()
