
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
The Radash directory  contains the following files:<br>
<ul>  
<li>   
<span style="font-family: Courier New;">radash.py</span>  - radash code in Python. A new class of objects called <span style="font-family: Courier New;"> Material </span> is created in this library. 
Furthermore, methods for working with objects of the Material class are created in the radash library, which enable the calculation of radiation damage. In particular calculation of NRT dpa and arc dpa damage. 
</li>
<li>  
span style="font-family: Courier New;">tutorial.ipyn</span> – Jupiter Notebook containing annotated calculation of radiation damage of Nb2TaTi3VZr2 alloy when irradiated with neutrons. The purpose of this file is to explain to the user how to use the RADASH software.
Other files with the txt extension are files containing data that RADASH uses for calculations. E.g. the file arc_dpa_constants.txt contains constants b, c for the survival function of Frenkel pairs, in relation (3). These files are required for RADASH to function properly.
</li>
</ul>
