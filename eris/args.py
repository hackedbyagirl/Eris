#!/usr/bin/env python3

from .utils.colors import Color

import argparse, sys

class Arguments(object):
    ''' Holds arguments used by Eris '''

    def __init__(self, configuration):
        self.verbose = '-v' in sys.argv or '-hv' in sys.argv or '-vh' in sys.argv
        self.config = configuration
        self.args = self.get_arguments()

    def _verbose(self, msg):
        if self.verbose:
            return Color.s(msg)
        else:
            return argparse.SUPPRESS

    def get_arguments(self):
        ''' Returns parser.args() containing all program arguments '''

        parser = argparse.ArgumentParser(usage=argparse.SUPPRESS,
                formatter_class=lambda prog: argparse.HelpFormatter(
                    prog, max_help_position=80, width=130))
        
        parser.add_argument('-v',
            '--verbose',
            action='count',
            default=0,
            dest='verbose',
            help=Color.set('Shows more options','wh'))
        
        # Subparser
        subparse = parser.add_subparsers(dest='module', help="Choose a module to run")
        
        # Subparser for Create Module
        create_parser = subparse.add_parser('create', help='Create pre-configured machine images')
        create_parser.add_argument('image', action='store', choices=['kali', 'terraformer', 'teamserver', 'phishingserver'], nargs='*', type=str, help='Machine Image you would like to create')
        
        # deploy subparser
        deploy_parser = subparse.add_parser('deploy', help='Deploy Operation Offensive Security Infrastructure')
        deploy_parser.add_argument('infrastructure', action='store', choices=['external-base', 'phishing'], nargs='*', type=str, help='Image you would like to create')

        return parser.parse_args()
    
if __name__ == '__main__':
    from .utils.colors import Color
    from .config import Config
    Config.init(False)
    a = Arguments(Config)
    args = a.args
    for (key,value) in sorted(args.__dict__.items()):
        Color.pl('{C}%s: {G}%s{W}' % (key.ljust(21),value))
    
