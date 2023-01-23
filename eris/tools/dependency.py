#!/usr/bin/env python3

import sys
from ..config import Config

class Dependency(object):
    required_attrs = ['dep_name', 'dep_required']

    def __init_subclass__(cls):
        for attr in cls.required_attrs:
            if not attr in cls.__dict__:
                raise NotImplementedError(
                    'Attribute "{}" has not been overridden in class "{}"' \
                    .format(attr, cls.__name__)
                )

    @classmethod
    def exists(cls):
        from ..utils.cmds import Command
        return Command.program_exists(cls.dep_name)

    @classmethod
    def dependency_check(cls):
        from ..utils.colors import Color
        from .packer import Packer
        apps = [Packer]
     

        missing_required = any([app.fails_check() for app in apps])

        if missing_required:
            Color.print('{!} {O}At least 1 Required app is missing. Eris need required Apps to run.{W}')
            import sys
            sys.exit(-1)

    @classmethod
    def fails_check(cls):
        from ..utils.colors import Color
        from ..utils.cmds import Command

        if Command.program_exists(cls.dep_name):
            Color.print('{G} You have the correct tool installed')
            return False

        if cls.dep_req:
            Color.print('{!} {O}Error: Required app {R}%s{O} was not found' % cls.dep_name)
            return True

        else:
            Color.p('{!} {O}Warning: Recommended app {R}%s{O} was not found' % cls.dep_name) 
