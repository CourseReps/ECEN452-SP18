from matplotlib import pyplot as plot
from matplotlib import cm
import numpy as np


# data format = [[freq], [e1'], [e2']...]
def meas_rect_plot(file_name, data, save_name):
    fig = plot.figure(1, figsize=(12, 6), dpi=80, facecolor='w', edgecolor='k')
    ax0 = plot.subplot(111)
    color = iter(cm.rainbow(np.linspace(0, 1, len(data))))
    for i in range(1, len(data)):
        ax0.plot(data[0], data[i], color=next(color), label=file_name[i-1])
    # ax0.axis([0.2, 5, -50, 5])     # [xmin, xmax, ymin, ymax]

    plot.xlabel('Frequency (GHz)')
    plot.ylabel('Dielectric Constant')
    plot.title('Dielectric Probe Measurement')
    plot.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)  # loc=4 => bottom right corner
    plot.subplots_adjust(left=0.1, right=0.7, top=0.9, bottom=0.1, hspace=0, wspace=0)
    plot.savefig('plotting/' + save_name, dpi=200, facecolor='w', edgecolor='k')
    plot.show()

