############################################################
################ Utilitary functions and variables #########
############################################################


# Imports

# To support both python 2 and python 3
from __future__ import division, print_function, unicode_literals

import numpy as np
import os



# To plot pretty figures

import matplotlib
import matplotlib.pyplot as plt
#plt.rcParams['axes.labelsize'] = 14
#plt.rcParams['xtick.labelsize'] = 12
#plt.rcParams['ytick.labelsize'] = 12




# Variables



# Where to save the figures
PROJECT_ROOT_DIR = "."
FIGURE_FOLDER = "Figures"
figsize = (10,6)


# Function


def save_fig(fig_id, save, figsize=figsize,  tight_layout=True):
    #plt.figure(figsize=figsize)
	if save:
		path = os.path.join(PROJECT_ROOT_DIR, FIGURE_FOLDER, fig_id + ".png")
		print("Saving figure", fig_id)
		if tight_layout:
			plt.tight_layout()
		plt.savefig(path, format='png', dpi=300)