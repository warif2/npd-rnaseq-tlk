"""
Handles commands from CLI and initiates scripts. Kind of like the middle man.
"""

# Modules
import sys
import pal_aggr
import pal_diff

help_text = """npd-rnaseq-tlk v1.0
A collection of tool to aid in the analysis of nanopore direct rnaseq data.

usage: npdr-tools <mode> [options] [-h]

modes:
pal_aggr    aggregate nanopolish polya output data at transcript and gene level
pal_diff    perform differential polyA length analysis between conditions

Note: Further [options] for mode can be obtained by <mode> --help."""

if __name__ == '__main__':

    try:
        # Shifting sys.argv
        mode = sys.argv[1]
        sys.argv = sys.argv[1:]

        # Run pal_aggr
        if mode == 'pal_aggr':
            pal_aggr.main()

        # Run pal_diff
        elif mode == 'pal_diff':
            pal_diff.main()

        # Run help
        elif mode == '-h' or mode == '--help':
            print(help_text)

        # Run Error
        else:
            print('usage: npdr-tools <mode> [options] [-h] ')
            print("npdr-tools: error: unrecognized command '%s'" % sys.argv[1])
            print('Please refer to --help for usage and options.')

    except IndexError:
        print(help_text)
