#!/usr/bin/env python3

from .dependency import Dependency
from ..config import Config
from ..utils.cmds import Command, CmdTest

class Packer(Dependency):
    dep_name = 'packer'
    dep_required = True
    
    '''
    Packer CLI Wrapper
    - Packer executable is determined in config
    - source is the location of the path where the packer config files are located
    '''

    def __init__(self, packer_executable=None, pwd=None):
        if packer_executable is None:
            self.packer_executable = Config.packer_executable 
        else:
            self.packer_executable = packer_executable

        packer_cmd = [self.packer_executable]
        init_cmd = ['init', '.']
        validate_cmd = ['validate', '.']
        build_cmd = ['build', '.'] 
        self.pwd = pwd

        self.execute(packer_cmd, init_cmd)
        self.execute(packer_cmd, validate_cmd)
        self.execute(packer_cmd, build_cmd)
# ------------------------------------------------------------------------------
#                        Packer Class Methods
# ------------------------------------------------------------------------------
    def execute(self, exececutable, cmd):
        build_command = []
        build_command.extend(exececutable)
        build_command.extend(cmd)

        self.execute_cmd(build_command)
        
    def execute_cmd(self, cmd):
        exe = CmdTest()
        output = exe.execute_cmd(cmd, self.pwd)
        print(output)
