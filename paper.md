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

 The Activity Browser is an open source software for Life Cycle Assessment (LCA) [@ISO]. 
 It builds on top of the brightway framework [@mutel], which consists of a number of python packages [@brightway2, @bw2calc,  @bw2data, @bw2io, @bw2parameters, @statsarrays]  
 that enable fast and flexible LCA calculations and analyses. The purpose of the Activity Browser is twofold: 
 A) it can act as a graphical user interface (GUI) to brightway and thus greatly increase the productivity of 
 working with brightway - e.g. managing projects and databases, modeling life cycle inventories, and analyzing 
 LCA results. B) it is meant to be an open, community driven software, so that anyone can modify or extend the 
 GUI to meet specific requirements and enable new modeling approaches for LCA. The latter was the original purpose 
 for the development of the Activity Browser, and it has since been used to implement a number of innovative modeling 
 approaches, e.g. as a modeling environment for modular LCA [@steubing, @suter, @mehr]. The Activity Browser is mainly 
 written in Python (but also makes use of JavaScript) and consists roughly of two parts: a GUI part and an interface 
 with brightway. The GUI part deals with user interface elements such as panels, tabs, tables, and wizards. The other 
 part deals with the interface to brightway, but also includes code that extends or introduces new functionality on 
 top of brightway. A central design principle is to focus within the Activity Browser on the user interface, while 
 relying on and introducing new functionality within the brightway framework, wherever possible. Brightway and the 
 Activity Browser can together be seen as two complementary layers to enhance productivity and innovation in life 
 cycle assessment by enabling practitioners to work both at the python layer (through brightway) and through the 
 GUI (Activity Browser). 

# References