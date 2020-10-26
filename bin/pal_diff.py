# Import modules
import sys
import argparse
import license
import csv
import datetime
import logging
import version
import os


def main():
    # Check license
    license.check_status()

    # Setup of argparse for script arguments
    class LicenseAction(argparse.Action):
        def __call__(self, parser, namespace, values, option_string=None):
            print("License status: %s" %license.message())
            sys.exit()

    parser = argparse.ArgumentParser(description="Performs statistical analysis for differential polyA length"
                                                 "distributions between multiple conditions at the transcript"
                                                 "and gene level.", prog="pal_diff.py")
    optional = parser._action_groups.pop()
    required = parser.add_mutually_exclusive_group()
    required.add_argument("-run", type=str, default=None, metavar="setup_file",
                          help="path to text file specifying comparisons to perform, refer to wiki for formatting")
    required.add_argument("-sf", action='store_true', help='outputs setup_file template')
    optional.add_argument("--silent", action='store_true',
                          help='use with run option, runs script without terminal outputs')
    optional.add_argument("-l", "--license", action=LicenseAction, metavar="", nargs=0,
                          help='show license status and exit')
    parser._action_groups.append(optional)
    args = parser.parse_args()

    if args.sf:
        f = csv.writer(open('pal_diff_setup_file.txt', 'w'), delimiter='\t')
        f.writerow(['#comparison_name', 'condition_1', 'condition_2', 'test_type', 'read_cutoff', 'fdr_cutoff'])
    else:
        # Preparing logging console for __main__
        time_stamp = str(datetime.datetime.now())
        numeric_level = getattr(logging, 'INFO', None)
        logging.basicConfig(filename='npd-rnaseq-tlk.poly_diff.' + time_stamp.replace(" ", "_") + '.log',
                            level=logging.DEBUG,
                            format='%(asctime)s\t%(name)-12s\t%(message)s',
                            filemode='w')
        logger = logging.getLogger('pal_diff')
        logger.debug('pal_diff.py version: %s' % version.__version__)
        logger.debug('Input command: python pal_diff.py ' + " ".join(sys.argv))

        # Defining Handler to write messages to sys.stdout
        if args.silent:
            sys.stdout = open(os.devnull, 'w')
        console = logging.StreamHandler(sys.stdout)
        console.setLevel(numeric_level)
        formatter = logging.Formatter('[%(asctime)s] %(message)s', datefmt='%y-%m-%d %H:%M:%S')
        console.setFormatter(formatter)
        logging.getLogger('').addHandler(console)
        logger.info('pal_diff, %s' % version.__version__)
        logger.info('Begin differential testing of tx and gene polyA length distributions between conditions...')

        # Parse setup file
        runs = dict()
        with open(args.run, 'r') as setup_file:
            read_sf = csv.reader(setup_file, delimiter='\t')
            for line in read_sf:
                if line[0][0] == '#':
                    continue
                runs[line[0]] = {'cond1': line[1].split(','),
                                 'cond2': line[2].split(','),
                                 'test': line[3],
                                 'read_co': int(line[4]),
                                 'fdr_co': float(line[5])}
        # setup and run tests
        license.pal_diff_setnrun(runs)


if __name__ == '__main__':
    main()
