---
title: 'The Activity Browser – an open source LCA software building on top of the brightway framework'
tags:
  - Python
  - Life Cycle Assessment (LCA)

authors:
  - name: Bernhard Steubing
    orcid: 0000-0002-1307-6376
    affiliation: 1 
  - name: Daniel de Koning  # make ORCID id?
    affiliation: 1
  - name: Adrian Haas
    affiliation: 2
  - name: Chris Mutel  # ORCID id?
    affiliation: 3    
affiliations:
 - name: Institute of Environmental Sciences (CML), Leiden University, 2300, RA Leiden, The Netherlands
   index: 1
 - name: Institute of Environmental Engineering, Swiss Federal Institute of Technology (ETH) Zürich, Schafmattstr. 6, 8093 Zurich, Switzerland
   index: 2
 - name: Paul Scherrer Institute, 5232 Villigen PSI, Switzerland
   index: 3
date: 5 November 2019
bibliography: paper.bib

---

# Summary
The Activity Browser is an open source software for advanced Life Cycle Assessment (LCA) [@ISO]. LCA is a method for 
assessing potential environmental impacts associated with products and services over their life cycle, which is often 
used to inform decision making, for example in designing sustainable technologies or policy making. The Activity Browser 
is a graphical user interface (GUI) to the brightway LCA framework [@mutel], 
and makes common tasks such as managing projects, modeling life cycle inventories, and interpreting LCA results, easier 
and more intuitive. Due to its pluggable design, it can also be extended to include new functionality. One example is a 
modeling environment for modular LCA [@steubing], the impetus for the original development of the Activity Browser. 
Modular LCA has since then been applied in several research applications [@suter, @mehr]. Another example is the recent 
development of support for parameterized inventory datasets, which allow for better model fidelity than classic 
assumptions of purely linear systems. 
The Activity Browser is mainly written in Python, with some Javascript for interactive elements and consists roughly of 
two parts: a GUI part and an interface with brightway. Brightway and the Activity Browser can together be seen as two 
complementary layers to enhance productivity and innovation in life cycle assessment by enabling practitioners to work 
both at the python level (through brightway) and at the GUI level (through the Activity Browser). 

# Acknowledgements
We kindly acknowledge funding from the EIT Raw Materials (project number 18231). We would also like to thank all the 
people who have made smaller contributions to the Activity Browser and have stimulated our development through raising 
issues and feature requests. Finally, we thank the editor and the two anonymous reviewers for their work. 

# References