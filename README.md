# Nanopore Direct RNA-Seq Toolkit
A collection of scripts for analysis of nanopore direct 
RNA-Seq data.

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

## Quick Command Line Usage
Currently, only the scripts for analyzing nanopolish polya output 
has been developed. With time additional scripts will become 
available. 
```bash
# To see available options for nanopolish_polya_aggregate.py
python nanopolish_polya_aggregate.py -h
```

Check out the Wiki page for more detailed guides on how to use the various tools.