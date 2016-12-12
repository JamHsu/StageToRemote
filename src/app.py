#!/usr/bin/env python

import logger
import processor
import sys
import argparse

version_number = 1.1

def execute(proessor):

    __logger = logger.createLogger(__name__)
    try:
        proessor.process()
    except Exception as e:
        __logger.exception('Processing occur error.')

def version():
    print 'version=', version_number

def paring_arguments():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--version', help='show the version number',
                        action="store_true")
    group.add_argument('--show', help='print the scp command for all stage '
                                       'file', action="store_true")
    group.add_argument('--auto', help='auto process scp command for all '
                                       'stage file, copy files to remote '
                                       'server.', action="store_true")

    parser.add_argument('-s', '-start', dest='start_code', help='start commit '
                                                             'hash code')
    parser.add_argument('-e','-end', dest='end_code', help='end commit hash '
                                                         'code')

    return parser.parse_args()

if __name__ == '__main__':

    arg = paring_arguments()

    print arg

    if arg.version:
        version()
    elif arg.show:
        execute(processor.PrintCmdProcessor(arg.start_code, arg.end_code))
    elif arg.auto:
        execute(processor.AutoProcessor(arg.start_code, arg.end_code))

    sys.exit(0)
