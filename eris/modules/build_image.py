#!/usr/bin/env python3

import os
from ..utils.colors import Color

class Builder():
    '''
    Class for Builds Packer Images
    '''

###############################################################################
#                              Helper Methods
###############################################################################
    @staticmethod
    def build_kali():
        intro = "{G}Task: Building Kali AMI for Offensive Operations\n"
        desc = "{P}Description: {W}This AMI will build a Kali EC2 Instance that can be deployed for External Penetration Testing Operations.\n"
        time = "{Y}Estimated Time: {W}~20-30 minuets\n\n{Y}Sit back and relax while Eris does the work for you.\n\n"

        Builder.helper_msg(intro, desc, time)

    @staticmethod
    def build_terraformer():
        intro = "{G}Task: Building Base Operations Server AMI (terraformer) for Offensive Operations\n"
        desc = "{P}Description: {W}This AMI will be build as the main EC2 Instance that will host Camelot's code for using terraform to deplay images\n"
        time = "{Y}Estimated Time: {W}~10-15 minuets.\n\n"

        Builder.helper_msg(intro, desc, time)

    @staticmethod
    def build_phisingsvr():
        intro = "{G}Task: Building Base Phishing Server AMI for Offensive Operations\n"
        desc = "{P}Description: {W}This AMI will build an EC2 Server that will host a long-standing phishing server. The phishing server is the base for all phishing campaigns.\n"
        time = "{Y}Estimated Time: {W}To be determined.\n\n"

        Builder.helper_msg(intro, desc, time)

    @staticmethod
    def build_teamserver():
        info = "{G}Building Base Teamserver for Offensive Operations\n"
        desc = "{P}Description: {W}Main C2 Server for Command and Control Operations\n"
        time = "{Y}Estimated Time: {W}To be determiend... \n\n"

        Builder.helper_msg(intro, desc, time)

    @staticmethod
    def helper_msg(intro, description, time):
        Color.print(intro)
        Color.print(description)
        Color.print(time)

###############################################################################
#                         Main Build Functionality
###############################################################################
    @staticmethod
    def build(images):
        from ..config import Config
        from ..tools.packer import Packer
        pkr_path = Config.pkr_path
        for img in images:
            if img == "kali":
                Builder.build_kali()
            if img == "terraformer":
                Builder.build_terraformer()
            if img == "phishing-ami":
                Builder.build_phisingsvr()
            if img == "teamserver-ami":
                Builder.build_teamserver()

            path = ''.join([pkr_path, img])

            p = Packer(pwd=path)
