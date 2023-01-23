#!/usr/bin/env python3

import sys

class Config(object):
    ''' Stores configuration variables and functions for Eris '''
    initialized = False
    os_mode = None
    verbose = 0

    
    @classmethod
    def init(cls, get_os=True):
        '''
            Sets up default initial configuration values.
            Also sets config values based on command-line arguments.
        '''
        if cls.initialized:
            return
        cls.initialized = True

        cls.verbose = 0
        
        # Data Paths
        cls.pkr_path = "./packer/" 

        # Executables Variables
        cls.packer_executable = None
        cls.ansible_executable = None
        cls.terraform_executable = None 
       
        # Commands
        cls.module = None
        cls.create = []
        cls.deploy = []

        if get_os:
            cls.set_os()

        # Will overwrite provided args    
        cls.load_args()

############################################
    @classmethod
    def set_os(cls):
        if cls.os_mode is None:
            if sys.platform == 'darwin':
                cls.os_mode = 'mac'
            elif sys.platform == 'win32':
                cls.os_mode = 'win'
            else:
                cls.os_mode = 'linux'
        cls.set_executable_paths()

    @classmethod
    def set_executable_paths(cls):
        if cls.os_mode == 'mac' or cls.os_mode == 'linux':
            cls.packer_executable = 'packer'
            cls.ansible_executable = 'ansible-playbook'
            cls.terraform_executable = 'terraform'
        else:
            print('You have windows, sorry :/')    
            cls.exit()
    
    @classmethod
    def load_args(cls):
        ''' Sets configuration values based on Argument.args object '''
        from .args import Arguments
        
        args = Arguments(cls).args
        cls.module = args.module
        
        #get options
        cls.load_ops(args)
    
    @classmethod
    def load_ops(cls, args):
        if cls.module == 'create':
            cls.create = args.image
        
        if cls.module == 'deploy':
            cls.deploy = args.infrastructure
    
    @classmethod
    def exists(cls):
        from .utils.cmds import Command
        return Command.program_exists(cls.dep_name)


    @classmethod
    def exit(cls, code=0):
        print('Stopping program')

        exit(code)

###############################################################

if __name__ == '__main__':
    Config.init(False)
