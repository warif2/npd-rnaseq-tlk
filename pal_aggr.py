# Import modules
import sys
import os
import argparse
import license
import csv
import logging
import datetime
import version
import pickle

if __name__ == '__main__':
    # Check license
    license.check_status()

    # Setup of argparse for script arguments
    class licenseAction(argparse.Action):
        def __call__(self, parser, namespace, values, option_string=None):
            print("License status: %s" % license.message())
            sys.exit()


    parser = argparse.ArgumentParser(description="Post-processing of 'nanopolish polya' output file with "
                                                 "annotation-based data aggregation and downstream analysis.",
                                     prog="pal_aggr.py")
    optional = parser._action_groups.pop()
    required = parser.add_argument_group('required arguments')
    required.add_argument("-fl", type=str, default=None, metavar="path_file",
                          help="text file of sample name and nanopolish polya output paths", required=True)
    optional.add_argument("-t", type=int, default=1, metavar='num_threads',
                          help='specify number of threads to use, default = 1')
    optional.add_argument("-qc_filter", action='store_true', help='process only reads with qc_tag = PASS')
    optional.add_argument("--silent", action='store_true', help='run script without terminal outputs')
    optional.add_argument("-l", "--license", action=licenseAction, metavar="", nargs=0,
                          help='show license status and exit')
    parser._action_groups.append(optional)
    args = parser.parse_args()

    # Preparing logging console for __main__
    time_stamp = str(datetime.datetime.now())
    numeric_level = getattr(logging, 'INFO', None)
    logging.basicConfig(filename='npd-rnaseq-tlk.' + time_stamp.replace(" ", "_") + '.log',
                        level=logging.DEBUG,
                        format='%(asctime)s\t%(name)-12s\t%(message)s',
                        filemode='w')
    logger = logging.getLogger('nanopolish_polya_aggr')
    logger.debug('nanopolish_polya_aggregate.py version: %s' % version.__version__)
    logger.debug('Input command: python nanopolish_polya_aggregate ' + " ".join(sys.argv))

    # Defining Handler to write messages to sys.stdout
    if args.silent:
        sys.stdout = open(os.devnull, 'w')
    console = logging.StreamHandler(sys.stdout)
    console.setLevel(numeric_level)
    formatter = logging.Formatter('[%(asctime)s] %(message)s', datefmt='%y-%m-%d %H:%M:%S')
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)
    logger.info('Begin aggregation of nanopolish polyA data with npd-rnaseq-tlk ver=%s' % version.__version__)
    logger.info('Number of threads: %i' % args.t)

    for run in csv.reader(open(args.fl, 'r'), delimiter='\t'):
        if run[0][0] == '#':
            continue
        sample = run[0]
        path = run[1]
        logger.info('Creating directory for sample: %s' % sample)
        if not os.path.isdir(sample):
            os.mkdir(sample)
        logger.info('Starting run...')
        tx_pd, tx_aggr, gn_pd, gn_aggr = license.np_polya_aggr(path, args.t, args.qc_filter, args.silent)
        # Saving results
        logger.info('Saving results...')
        tx_pd.to_csv(sample + '/' + 'tx_polyA.csv', index=False)
        gn_pd.to_csv(sample + '/' + 'gn_polyA.csv', index=False)

        # Store data (serialize)
        with open(sample + '/' + 'tx.pickle', 'wb') as handle:
            pickle.dump(tx_aggr, handle, protocol=pickle.HIGHEST_PROTOCOL)
        with open(sample + '/' + 'gn.pickle', 'wb') as handle:
            pickle.dump(gn_aggr, handle, protocol=pickle.HIGHEST_PROTOCOL)

    logger.info('All runs are complete!')
