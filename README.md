
<p align="center">
<img src="radash-logo.png" alt="" /></td>
</p>  
<h2>
<p align="center">
RAdiation DAmage Simulation in High entropy alloys (RADASH) 
</p>
  </h2>

<p>
RADASH is a Python library for evaluation of radiation damage in high entropy and multicomponent complex concentrated alloys.
This makes RADASH independent of the specific platform on which it will be run and only needs a Python interpreter to function.
It is recommended to run RADASH using <a href="https://anaconda.org/" target="_blank">Anaconda</a> Python distribution.
</p>
<p>
Dependencies: RADASH uses Pyhon libraries <a href="https://numpy.org/" target="_blank">Numpy</a> and <a href="https://matplotlib.org/" target="_blank">Matplotlib</a>. These libraries are standard part of the <a href="https://anaconda.org/" target="_blank">Anaconda</a> distribution.
</p>  
<p>
The Radash directory  contains the following files:
<li><b>radash.py</b> - radash code in Python. A new class of objects called <i> Material </i> is created in this library. 
Furthermore, methods for working with objects of the Material class are created in the radash library, which enable the calculation of radiation damage. In particular calculation of NRT dpa and arc dpa damage. 
</li>
<li><b>tutorial.ipyn</b> – Jupiter Notebook containing annotated calculation of radiation damage of Nb<sub>2</sub>TaTi<sub>3</sub>VZr<sub>2</sub> alloy when irradiated with neutrons. The purpose of this file is to explain to the user how to use the RADASH software.</li>
<li>Other files with the txt extension are files containing data that RADASH uses for calculations. E.g. the file arc_dpa_constants.txt contains constants b, c for the survival function of Frenkel pairs. These files are required for RADASH to function properly.</li>
</p>
