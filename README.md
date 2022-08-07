# Fraunhofer-pattern

## Problem
Use a Matplotlib gridspec to plot the Fraunhofer pattern of a 2 rectangle aperture.


<p align="center">
<img src="https://github.com/artmenlope/Fraunhofer-pattern/blob/master/drawing.png" width="25%">
</p>

## Solution
The used solution is

$$
u_z(x_z, y_z)\propto \exp\left(j\frac{\pi}{\lambda Z}(x_z^2+y_z^2)\right) 4hw \mbox{ sinc}\left(\dfrac{2 x_z w}{\lambda Z} \right) \cos\left(\dfrac{2\pi x_z d}{\lambda Z}\right) \mbox{sinc}\left(\dfrac{y_z h}{\lambda Z} \right)
$$

where $x_z$ and $y_z$ are the coordinates on the screen, $Z$ is the distance from the object to the screen and $\lambda$ is the wavelength of the light.

## Plot
The plotted pattern will be given by

$$
I_z (x_z, y_z) \propto \left| u_z(x_z, y_z) \right|^2
$$


When executed, the Python 3 script [_Fraunhofer-difraction.py_](https://github.com/artmenlope/Fraunhofer-pattern/blob/master/Fraunhofer-difraction.py) will produce the following output:

&nbsp;

<p align="center">
<img src="https://github.com/artmenlope/Fraunhofer-pattern/blob/master/fraunhofer-difraction-output.png" width="100%">
</p>

The parameters used in this case are:

$$
\begin{array}{rcr}
Z&=&1\mbox{ m},\\
w&=&0.1\times 10^{-3}\mbox{ m},\\
h&=&5\times 10^{-3}\mbox{ m},\\
d&=&0.7\times 10^{-3}\mbox{ m},\\
\lambda&=&500\times 10^{-9}\mbox{ m}.\\
\end{array}
$$
