# importing pandas
import pandas as pd

# input file for distribution plot
filename = input('Enter input file name: ')
outfile_prefix = input('Enter output file prefix (without .png): ')

# k-mer distribution
kmerhist = pd.read_csv(filename, header=None, index_col=0, sep=' ')
kmer_dist_plot = kmerhist[1][0:].plot()
kmer_dist = kmer_dist_plot.get_figure()
kmer_dist.savefig(outfile_prefix + '.png')

# the border of the initial peak corresponding to sequence errors at 5
bord = 5
err_5_plot = kmerhist[1][bord:].plot()
err_5 = err_5_plot.get_figure()
err_5.savefig(outfile_prefix + 'err_5.png')

# genome size
import numpy as np
size = round((kmerhist[5:].index * kmerhist[5:][1]).sum() / kmerhist.index[np.argmax(kmerhist[1][bord:]) + bord])
print(size)

