import subprocess
import re
import os
from typing import List, Union

class PylintErrorCustomizer:
    def __init__(self, base_dir="."):
        self._base_dir = base_dir

    def __find_py_files(self, path=None):
        if path is None:
            path = self._base_dir
        self._py_files = [file_ for file_ in os.listdir(path)
                          if file_.endswith(".py")]
        return self._py_files

    def find_pylint_errors(py_files: Union(str, List[str])=None) -> str:
        if py_files is None:
            py_files = self._py_files
        elif isinstance(py_files, str):
            if py_files.endswith(".py"):
                py_files = list(py_files)
            else:
                py_files = self.__find_py_files(py_files)
        elif not isinstance(py_files, list):
            raise TypeError("Invalid type given")
        try:
            fp = open('py_files.txt', 'r')
            fp1 = open('pylint_errors.txt', 'a')
            files = fp.readlines()
            #files_a = files[0:1]
            for file_name in files:
                out = subprocess.Popen(["pylint3", file_name[:-1]], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                stdout, stderr = out.communicate()
                op = stdout.decode("utf-8").splitlines()
                for k in op:
                    fp1.write(k+'\n')
                fp1.write('\n')
        finally:
            fp.close()
            fp1.close()

#def filter_pylint_errors():
#    patterns = ['Exactly one space required after comma']
#    try:
#        fp = open('pylint_errors.txt', 'r')
#        for line in fp.readlines():
#            match = re.matches("", line)
#            print(match)
#    finally:
#        fp.close()

