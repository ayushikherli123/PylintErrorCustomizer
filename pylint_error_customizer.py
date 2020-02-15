"""
Description : This module is used to customize pylint errors
Author : Ayushi Jain
Date : 15 Feb 2020
"""

import os
import subprocess

OUTPUT_FILE = 'pylint_errors.txt'

class PylintErrorCustomizer:
    """
    This module is used to customize pylint errors
    """
    def __init__(self, base_dir="."):
        if not isinstance(base_dir, str):
            raise TypeError("Invalid type, must be str")
        if not os.path.exists(base_dir):
            raise FileNotFoundError("Invalid path, no such file or directory")
        self.__base_dir = base_dir
        self.__py_files = self.__find_py_files(base_dir)

    def __find_py_files(self, path):
        self.__py_files = tuple([file_ for file_ in os.listdir(path) if file_.endswith(".py")])
        return self.__py_files

    def __validate_files(self, py_files):
        if py_files is None:
            py_files = self.__py_files
        elif isinstance(py_files, str):
            if py_files.endswith(".py"):
                py_files = tuple(py_files)
            else:
                py_files = self.__find_py_files(py_files)
        elif isinstance(py_files, list):
            py_files = tuple(py_files)
        elif isinstance(py_files, tuple):
            pass
        else:
            raise TypeError("Invalid type, must be str, list or tuple")
        return py_files

    def find_pylint_errors(self, py_files=None):
        """
        Method is used to return pylint errors in a text file
        """
        py_files = self.__validate_files(py_files)
        with open(OUTPUT_FILE, 'w') as out_file:
            for file_name in py_files:
                out = subprocess.Popen(["pylint3", file_name],
                                       stdout=subprocess.PIPE,
                                       stderr=subprocess.PIPE)
                stdout, stderr = out.communicate()
                output_ = stdout.decode("utf-8").splitlines()
                for line_ in output_:
                    out_file.write(line_+'\n')
                out_file.write('\n')

    def filter_pylint_errors(self, pattern):
        """ Functionality will be added soon """
        pass
