#  Assessing Reproducibility and Robustness in Genomic Analyses: A Comparative Study Using Fruit Fly and Mouse Genomes 
# Genomics Analysis Project README

## Overview

This project focuses on exploring the robustness and reproducibility of genomic analysis pipelines, encompassing various steps from initial sequencing reads to the identification of differentially expressed genes. It aims to assess the reliability and consistency of genomic analyses under different input conditions.

## Objectives

1. Assessing Robustness:We investigate the consistency of results when the same analysis method is applied under varying input conditions. Multiple sets of sequencing reads for a chosen genome are generated, and a specific analysis method is applied to each set. The variations in outcomes help determine the robustness of the chosen method.

2. Evaluating Reproducibility: We compare the results of different analysis methods when applied to the same input data. Parallel analyses using distinct techniques enable the evaluation of reproducibility and method compatibility.

3. Quantifying Noise and Variation: Noise and variation are introduced into the data in both objectives. We explore the effects of shuffling reads within the same dataset and introducing sequencing errors into selected reads. This helps us understand how sensitive each analysis method is to data imperfections.

4. Comparing Traditional and Pseudoalignment Methods:We employ two approaches for quantification and differential expression analysis. The first method follows a traditional pipeline involving alignment to a reference genome, gene-level quantification, and differential expression analysis. The second method uses pseudoalignment techniques. By comparing these approaches, we assess their consistency and efficiency.

## Background

This project is rooted in the necessity for a rigorous evaluation of the reliability and reproducibility of genomic analysis pipelines. The genomics field is rapidly evolving, offering numerous tools and methodologies for analysis. However, without a comprehensive understanding of how these methods perform under diverse conditions, making informed decisions about their suitability for specific research questions becomes challenging.

## Dependencies

- use virtual machine and install Ubuntu 18.04.5 (August 2020) is the latest long-term support (LTS) version of the Ubuntu
- operating system that is supported by VirtualBox. You can download this version of Ubuntu here (2 Gb).
- The virtual machine will run as a guest on your host machine. The host (your computer) should have at least 8Gb of RAM and a modern CPU. Ideally, 16Gb of RAM is required.
- You will also need VirtualBox installed on your host machine in order to run the virtual machine.
- You can download VirtualBox here
  - R studio https://posit.co/download/rstudio-desktop/
- python v 3.9 https://www.python.org/downloads/
- virtual machine https://www.virtualbox.org/wiki/Downloads
- in virtual machine use the linux ubutu 64 bit
 -bowtie2 
## Getting Started

- install all the above softwares to get started with the project

## The codes to every software is given in the each code file 



