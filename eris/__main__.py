#!/usr/bin/python3

# imports
import os
from .config import Config
from .modules.build_image import Builder
from .utils.colors import Color
from eris import cli, __app_name__

try:
    from .config import Config
except (ValueError, ImportError) as e:
    raise Exception('You may need to run wifite from the root directory (which includes README.md)', e)

class Eris(object):
    def __init__(self):
        from .utils.banner import banner
        banner()

        Config.init(get_os=True)
        Color.print('{R}Setting up required configurations...\n')
         
#        from .tools.dependency import Dependency
#        Dependency.dependency_check()
        
    def launch(self):
        self.get_module()
        Builder.build(self.pkr_pkgs)

    def get_module(self):
        if Config.module == 'create':
            self.pkr_pkgs = Config.create
        if Config.module == 'deploy':
            self.pkr_pkgs = Config.deploy    
     
########################################################################
def run():
    eris = Eris()
    eris.launch()
    
if __name__ == "__main__":
    run()
