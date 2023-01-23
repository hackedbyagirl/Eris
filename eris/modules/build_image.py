#!/usr/bin/env python3

import os

class Builder():
    
    @staticmethod
    def build(images):
        from ..config import Config
        from ..tools.packer import Packer
        pkr_path = Config.pkr_path
        for img in images:
            path = ''.join([pkr_path, img])
         
            p = Packer(pwd=path)

