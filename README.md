# Nanopore Direct RNA-Seq Toolkit
A collection of scripts for analysis of nanopore direct 
RNA-Seq data. Still in development.

## Hardware and Software Requirments
  * 64 bit Linux or Mac OS X
  * Python 3.6 or higher
  
## Setting up a virtual environment (Optional)
It is recommended to create a virtual environment before setting
the toolkit to avoid errors with dependencies.

```bash
# Creating venv with the name 'npdr-tlk' using anaconda
conda create -n npdr-tlk python=3.6

# Activate venv
conda activate npdr-tlk
```
  
## Download and Installation

```bash
# Download the latest release of toolkit using git
git clone https://github.com/warif2/npd-rnaseq-tlk.git

# Install python packages dependencies using
pip install -r /npd-rnaseq-tlk/requirements.txt
```

Finally, run setup.py to obtain the license key needed to run the tools. It also provides the
option of adding the directory to your PATH variable which allows calling the tool
from any directory.
```bash
# Run setup.py
cd npd-rnaseq-tlk/
python setup.py

Note: After setup, refresh terminal for PATH update to take effect.
If npdr-tools is still not callable, you might need to modify permissions of npdr-tools.

# Change npdr-tools permission to allow system-wide execution.
chmod 755 npdr-tools
```

## Quick Command Line Usage
Currently, only scripts for analyzing nanopolish polya output 
has been developed. With time additional scripts will become 
available. 
```bash
# To see available mode for npr-rnaseq-tlk
~/npdr-tools -h
```

Check out the [Wiki](https://github.com/warif2/npd-rnaseq-tlk/wiki) page for more detailed guides on how to use the various tools.