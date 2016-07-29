import getopt
import logger
import processor
import sys

version_number = 1.0

def main(argv):

    if len(argv) == 0:
        help()
        sys.exit()

    cmd = argv[0]
    if cmd == '--help':
        help()
    elif cmd == '--version':
        version()
    elif cmd == '--print':
        execute(processor.PrintCmdProcessor())
    elif cmd == '--auto':
        execute(processor.AutoProcessor())
    else:
        help()

    sys.exit()

def execute(proessor):
    __logger = logger.createLogger(__name__)
    try:
        proessor.process()
    except Exception as e:
        __logger.exception('Processing occur error.')

def help():
    print '--help: Print help message.'
    print '--version: Print script version.'
    print '--print: Print scp command.'
    print '--auto: Auto copy files to remote server.'

def version():
    print 'version=', version_number

if __name__ == '__main__':
    main(sys.argv[1:])   
