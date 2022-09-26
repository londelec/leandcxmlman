#!/usr/bin/python3

import os
import glob
import fileinput
#import logging


# Process file
def proc_file(filepath):
    #print('File: ', filepath)

    # Carefull inplace=True means source file will be modified!!!
    for line in fileinput.input(filepath, inplace=True):
    #for line in fileinput.input(filepath, inplace=False):
        if '.. _xmlnode-' in line:
            line = line.replace('.. _xmlnode-', '.. _xmlelem-')

        if ':ref:`xmlnode-' in line:
            line = line.replace(':ref:`xmlnode-', ':ref:`xmlelem-')

        print(line, end='')


# Traverse directories
def proc_dirs(rootpath):
    for path in glob.glob(rootpath + '/*'):
        if os.path.isdir(path):
            #print('Dir: ', path)
            proc_dirs(path)
        else:
            print('File: ', path)
            proc_file(path)


# Test on a copy first!
#proc_dirs('./sections')
#proc_file('./uart.rst')
#logging.warning('Test')
#print('DEBUG: hello')

