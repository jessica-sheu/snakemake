#=========================================================================#
# Script: plot-quals.py                                                   #
#-------------------------------------------------------------------------#
# Generates a histogram of the quality scores based on the variant calls  #
# in calls/all.vcf.                                                       #
#=========================================================================#
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pysam import VariantFile

quals = [record.qual for record in VariantFile(snakemake.input[0])]
plt.hist(quals)

plt.savefig(snakemake.output[0])
