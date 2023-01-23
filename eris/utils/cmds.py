#!/usr/bin/env python3

import subprocess as s

from ..config import Config
from .colors import Color


class CmdTest:
    def __init__(self):
        pass

    def execute_cmd(self, cmd, cwd=None):
        cmd_str = " ".join(cmd)
        msg = "{G} Executing: {C} " + cmd_str

        try:
            Color.print(msg)
            output = s.check_output(cmd, cwd=cwd, shell=False)
            return output.decode()
        except s.CalledProcessError as e:
            return e.output.decode()


class Command:
    @staticmethod
    def devnull():
        """Helper method for opening devnull"""
        return open("/dev/null", "w")

    @staticmethod
    def packer(cmd, pwd):

        if type(stdout) is bytes:
            stdout = stdout.decode("utf-8")
        if type(stderr) is bytes:
            stderr = stderr.decode("utf-8")

        if Config.verbose > 1 and stdout is not None and stdout.strip() != "":
            Color.pe(
                "{P} [stdout] %s{W}" % "\n [stdout] ".join(stdout.strip().split("\n"))
            )
        if Config.verbose > 1 and stderr is not None and stderr.strip() != "":
            Color.pe(
                "{P} [stderr] %s{W}" % "\n [stderr] ".join(stderr.strip().split("\n"))
            )

        return (stdout, stderr)

    @staticmethod
    def program_exists(program):
        """Checks if program is installed on this system"""
        command = ["which", program]

        proc = Command(command)

        stdout = proc.stdout().strip()
        stderr = proc.stderr().strip()

        if stdout == "" and stderr == "":
            return False

        return True

    def launch(self, path, stdout=s.PIPE, stderr=s.PIPE):
        """Launch a tool from a specific directory"""
        print("Launching command")
        proc = s.Popen(self.cmd, cwd=path, stdin=s.PIPE, stdout=stdout, stderr=stderr)
        out, err = proc.communicate(path)
        return (out, err)

    def __init__(
        self,
        cmd="",
        devnull=False,
        stdout=s.PIPE,
        stderr=s.PIPE,
        cwd=None,
        bufsize=0,
        stdin=s.PIPE,
    ):
        """cmd = command line program with arguments in a list format. Must be in list format to have shell = false"""

        if type(cmd) is str:
            self.cmd = cmd.split()
        else:
            self.cmd = cmd

        self.output = []

    # self.out = None
    # self.err = None

    # if devnull:
    #     std_out = Command.devnull()
    #     std_err = Command.devnull()
    # else:
    #     std_out = stdout
    #     std_err = stderr

    # self.proc = s.Popen(cmd, stdout=std_out, stderr=std_err, stdin=stdin, cwd=cwd, bufsize=bufsize)

    def run(self, shell=False, universal_newlines=True):
        """
        Takes in a command prepopulated with arguments and runs it. The command MUST be in a list format'
        """

        try:
            self.output = s.check_output(
                self.cmd, shell=False, stderr=s.STDOUT, universal_newlines=True
            )

        except s.CalledProcessError as cp:
            return False

        except OSError as e:
            return False

        return self

    def stdout(self):
        """Waits for process to finish, returns stdout output"""
        self.get_output()
        return self.out

    def stderr(self):
        """Waits for process to finish, returns stderr output"""
        self.get_output()
        return self.err

    def get_output(self):
        """Waits for process to finish, sets stdout & stderr"""
        if self.out is None:
            (self.out, self.err) = self.proc.communicate()

        if type(self.out) is bytes:
            self.out = self.out.decode("utf-8")

        if type(self.err) is bytes:
            self.err = self.err.decode("utf-8")

        return (self.out, self.err)
