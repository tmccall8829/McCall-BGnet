from matplotlib import pyplot
from pylab import *
import numpy as np

marker_size = 0.5
ncell = 50
global_gidoffset = input("What is the global GID offset (probs either 0 or 4000)? ")
global_gidoffset = float(global_gidoffset)

def plotSpikes(*files):
	"Takes a spikes.txt file as input, then processes and plots the data"
	fig, axarr = pyplot.subplots(2)
	fig.set_tight_layout(True)
	for f in files:
		data = loadtxt(f, unpack=True)
		data = data.T

		stn = np.array([row for row in data if 0 <= (row[1]-global_gidoffset) < (ncell/5)])
		gpe = np.array([row for row in data if ncell/5 <= (row[1]-global_gidoffset) < (ncell/5 * 4)])
		gpi = np.array([row for row in data if (ncell/5 * 4) <= (row[1]-global_gidoffset) < ncell])


		axarr[files.index(f)].plot(stn[:, 0], stn[:, 1], 'r.', markersize=marker_size)
		axarr[files.index(f)].plot(gpe[:, 0], gpe[:, 1], 'g.', markersize=marker_size)
		axarr[files.index(f)].plot(gpi[:, 0], gpi[:, 1], 'b.', markersize=marker_size)
		axarr[files.index(f)].set_title(f)
		# axarr[files.index(f)].set_xlim([250,500])
		# pyplot.xticks(np.arange(0, 1000, 50))
		pyplot.yticks(np.arange(0, ncell, ncell/5))
		pyplot.tick_params(labelsize=4)

	savefig('figure.png', dpi=500)

plotSpikes("mptp_spikes000_16.txt", "normal_spikes000_16.txt")
