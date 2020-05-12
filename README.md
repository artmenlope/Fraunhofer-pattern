# Fraunhofer-pattern

Use a Matplotlib gridspec to plot the Fraunhofer pattern of a 2 rectangle aperture.


<p align="center">
<img src="https://github.com/artmenlope/Fraunhofer-pattern/blob/master/drawing.png" width="20%">
</p>


The used solution is

<img src="https://render.githubusercontent.com/render/math?math= u_z(x_z,y_z) = e^{j\frac{\pi}{\lambda z}(x_z^2+y_z^2)} 4 h w \sinc{\left( 2 \frac{x_z}{\lambda z} w \right)} \cos{\left( 2 \pi \frac{x_z}{\lambda z} d \right)} \sinc{\left(  \frac{y_z}{\lambda z} h \right)}">

When executed, the Python 3 script [_Fraunhofer-difraction.py_](https://github.com/artmenlope/Fraunhofer-pattern/blob/master/Fraunhofer-difraction.py) will produce the following output:



<p align="center">
<img src="https://github.com/artmenlope/Fraunhofer-pattern/blob/master/fraunhofer-difraction-output.png" width="90%">
</p>

