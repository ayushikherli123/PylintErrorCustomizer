"""
Description : This module is used to customize pylint errors
Author : Ayushi Jain
Date : 15 Feb 2020
"""

import os
import re
import subprocess

OUTPUT_FILE = 'pylint_errors.txt'
FILTER_OUTPUT_FILE = 'filered_pylint_errors.txt'
PYLINT_VERSION = "pylint3"

class PylintErrorCustomizer:
    """
    This module is used to customize pylint errors
    """
    def __init__(self, base_dir="."):
        if not isinstance(base_dir, str):
            raise TypeError("Invalid type, must be str")
        if not os.path.exists(base_dir):
            raise FileNotFoundError("Invalid path, no such file or directory : ", base_dir)
        self.__base_dir = base_dir
        self.__py_files = self.__find_py_files(base_dir)

    def __find_py_files(self, path):
        self.__py_files = tuple([os.path.join(self.__base_dir, file_) \
                                 for file_ in os.listdir(path) \
                                 if file_.endswith(".py")])
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
                if not os.path.exists(file_name):
                    raise FileNotFoundError("Invalid path, no such file or directory : ", file_name) 
                out = subprocess.Popen([PYLINT_VERSION, file_name],
                                       stdout=subprocess.PIPE,
                                       stderr=subprocess.PIPE)
                stdout, stderr = out.communicate()
                output_ = stdout.decode("utf-8").splitlines()
                for line_ in output_:
                    out_file.write(line_+'\n')
                out_file.write('\n')

    def filter_pylint_errors(self, pattern):
        """
        Method is used to return filtered pylint errors in a text file
        """
        if not os.path.exists(OUTPUT_FILE):
            raise FileNotFoundError("`pylint_errors.txt` file does not exist")
        with open(OUTPUT_FILE, 'r') as in_file, open(FILTER_OUTPUT_FILE, 'a') as out_file:
            for line_ in in_file:
               if re.search(pattern, line_):
                   out_file.write(line_+'\n')
