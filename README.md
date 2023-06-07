# Live Code Smell Detection of Data Clumps in an Integrated Development Environment

[![Scientific Paper](https://img.shields.io/badge/Scientific-Paper-blue)](https://www.scitepress.org/Link.aspx?doi=10.5220/0011727500003464)

This repository presents the research work and tool for live detection and semi-automatic refactoring of data clumps in Java. This work has been implemented as an IntelliJ integrated development environment application plugin.

https://www.scitepress.org/Link.aspx?doi=10.5220/0011727500003464

## Abstract

Code smells pose significant maintenance and extension challenges in software systems. Although numerous tools exist for detecting code smells, a scarcity remains in the number offering refactoring suggestions, let alone live detection in an integrated development environment. Our tool targets this gap, specifically focusing on data clumps, a common type of code smell.

By examining projects and their corresponding abstract syntax trees, and analyzing variable types, our research endeavors to detect data clumps and generate proactive suggestions to mitigate them. In our analysis of the ArgoUML software project, live detection consistently achieved a median of less than 0.5 seconds.

Our methodology was compared to the Code Bad Smell Detector (CBSD), yielding consistent results. Out of over 1500 investigated files, our approach detected 125 files with data clumps, while CBSD detected 97. In both cases, 92 of the detected files were common.

Furthermore, we integrated manual refactoring steps into the tool, leading to a semi-automatic system that facilitates the elimination of data clumps.

## Test Cases

You can find the test cases in the following directory: `Source Code/src/test/testData/dataclumps`.

## Usage

Open `Source Code` in IntelliJ IDEA 2022.2.3 or similar version.
 
## License

MIT

## Contact

See E-mails in the paper