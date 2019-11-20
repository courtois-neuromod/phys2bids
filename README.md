[![Join the chat at https://gitter.im/ME-ICA/tedana](https://badges.gitter.im/phys2bids/community.svg)](https://gitter.im/phys2bids/community?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
[![DOI](https://zenodo.org/badge/208861898.svg)](https://zenodo.org/badge/latestdoi/208861898)


phys2bids
=========
Phys2bids is a python3 library meant to format physiological files in BIDS.
It was born for Acqknowledge files (BIOPAC), and at the moment it supports
``.acq`` files as well as ``.txt`` files obtained by labchart
(ADInstruments).
It doesn't support physiological files recorded with the MRI, as you can find a software for it [here](https://github.com/tarrlab/physio2bids).

It requires python 3.6 or above, as well as the modules:
- `numpy >= 1.9.3`
- `pandas >= 0.10`
- `matplotlib >= 3.1.1`

In order to process ``.acq`` files, it needs [`bioread`](https://github.com/uwmadison-chm/bioread), an excellent module
that can be found at [this link](https://github.com/uwmadison-chm/bioread).

### Linux and mac installation
Donwload the package as zip from github and uncompress or if you have ``git`` use the command:

`` git clone https://github.com/smoia/phys2bids.git``

open a terminal in the phy2bids folder and execute the command:

``sudo pip3 install -e .``

type the command:

``phys2bids -v ``

if your output is: ``phys2bids 0.4.0`` or similar, phys2bids is ready to be used.

**The project is currently under development**.
Any suggestion/bug report is welcome! Feel free to open an issue.

At the very moment, it assumes all the extracted channels from a file
have the same sampling freq.
