# Fraunhofer-pattern

Use a Matplotlib gridspec to plot the Fraunhofer pattern of a 2 rectangle aperture.


<p align="center">
<img src="https://github.com/artmenlope/Fraunhofer-pattern/blob/master/drawing.png" width="20%">
</p>


The used solution is

<!-- Note: For Latex formulas in Github's Markdown see https://gist.github.com/a-rodin/fef3f543412d6e1ec5b6cf55bf197d7b and the app at https://alexanderrodin.com/github-latex-markdown/ -->

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=u_z(x_z%2Cy_z)%20%3D%20e%5E%7Bj%5Cfrac%7B%5Cpi%7D%7B%5Clambda%20Z%7D(x_z%5E2%2By_z%5E2)%7D%20%5C%2C%204%20h%20w%20%5C%3B%5Csinc%7B%5Cleft(%202%20%5Cfrac%7Bx_z%7D%7B%5Clambda%20Z%7D%20w%20%5Cright)%7D%20%5C%3B%20%5Ccos%7B%5Cleft(%202%20%5Cpi%20%5Cfrac%7Bx_z%7D%7B%5Clambda%20Z%7D%20d%20%5Cright)%7D%20%5C%3B%20%5Csinc%7B%5Cleft(%20%20%5Cfrac%7By_z%7D%7B%5Clambda%20Z%7D%20h%20%5Cright)%7D">,
</p>

where ![x_z](https://render.githubusercontent.com/render/math?math=x_z) and ![y_z](https://render.githubusercontent.com/render/math?math=y_z) are the coordinates on the screen, ![Z](https://render.githubusercontent.com/render/math?math=Z) is the distance from the object to the screen and ![\lambda](https://render.githubusercontent.com/render/math?math=%5Clambda) is the wavelength of the light.

The plotted pattern will be given by

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=I_z(x_z%2Cy_z)%20%3D%20%7Cu_z(x_z%2Cy_z)%7C%5E2">
</p>

When executed, the Python 3 script [_Fraunhofer-difraction.py_](https://github.com/artmenlope/Fraunhofer-pattern/blob/master/Fraunhofer-difraction.py) will produce the following output:



<p align="center">
<img src="https://github.com/artmenlope/Fraunhofer-pattern/blob/master/fraunhofer-difraction-output.png" width="90%">
</p>

