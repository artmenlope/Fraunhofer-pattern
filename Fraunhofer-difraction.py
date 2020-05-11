# -*- coding: utf-8 -*-
"""
Created on Sun May 10 20:05:26 2020

@author: artmenlope
"""

import numpy as np
import matplotlib.pyplot as plt


def Fraunhofer_2rect(xz, yz, z, l, w, h, d):
    
    """Fraunhofer pattern of a 2 rectangle aperture."""
    
    head_term = np.exp(1j*np.pi/(l*z)*(xz**2+yz**2))
    tail_term = 4*h*w * np.sinc(2*xz/(l*z)*w) * np.cos(2*np.pi*xz/(l*z)*d) * np.sinc(yz/(l*z)*h)
  
    return head_term * tail_term


# Parameters
w = 0.1e-3 # Width of the rectangles.
h = 5e-3   # Height of the rectangles.
d = 0.7e-3 # Distance between the centers of both rectangles.
l = 500e-9 # Light's wavelength.
N = 5000   # Number of bins on each axis.

xlim = ((2*d+w+20*d)/2) # Modify as desired.
ylim = (h/4)

x , y  = np.linspace(-xlim,xlim,N), np.linspace(-ylim,ylim,N)
xz, yz = np.meshgrid(x, y)
z  = 1

# Calculate the pattern on the plane and on the x and y axis.
I  = np.abs(Fraunhofer_2rect(xz, yz, z, l, w, h, d))**2
Ix = np.abs(Fraunhofer_2rect(x, 0, z, l, w, h, d))**2
Iy = np.abs(Fraunhofer_2rect(0, y, z, l, w, h, d))**2

# Normalized.
In  = I/np.max(I)
Inx = Ix/np.max(Ix)
Iny = Iy/np.max(Iy)


# =============================================================================
# Make the plot.
# =============================================================================

# Set font style to LaTeX.
from matplotlib import rc
rc('font',family="serif")
rc('text', usetex=True)

# Set aspect ratios.
widths  = [5,1]
heights = [1,1.5]

# Create the figure.
fig = plt.figure(figsize=(16,7))
fig.suptitle("Normalized Fraunhofer pattern at $z={}$".format(z), fontsize=20)

# Make the gridspec.
gs = fig.add_gridspec(ncols=2, nrows=2, 
                      width_ratios=widths, 
                      height_ratios=heights, 
                      wspace = 0.05, 
                      hspace = 0.10)

# Create the subplots.
ax_top     = fig.add_subplot(gs[0, 0])
ax_central = fig.add_subplot(gs[1, 0])
ax_right   = fig.add_subplot(gs[1, 1])

# Top subplot texts.
ax_top.set_title("Pattern along the $x_z$ axis", loc="center", fontsize=14)
ax_top.set_ylabel("$|u_z(x_z,0)|^2$ (normalized)", fontsize=14)
ax_top.axes.xaxis.set_ticks([]) # Hide x axis text ticks.

# Central subplot texts.
ax_central.set_xlabel("$x_z$", fontsize=14)
ax_central.set_ylabel("$y_z$", fontsize=14)

# Right subplot texts.
ax_right.set_xlabel("$|u_z(0,y_z)|^2$ (normalized)", fontsize=14)
ax_right.set_ylabel("Pattern along the $y_z$ axis", rotation=-90, labelpad=20, fontsize=14)
ax_right.yaxis.set_label_position("right")
ax_right.axes.yaxis.set_ticks([]) # Hide y axis text ticks.

# Plot the data.
ax_top.plot(x, Inx)
ax_central.contourf(xz, yz, In, levels=100, cmap=plt.cm.gnuplot, vmin=0, vmax=1)
ax_right.plot(Iny, y)

# Show the result.
plt.tight_layout()
plt.show()
