import os
import sys
import time

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'     
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

if len(sys.argv) > 1:
    FOLDER = sys.argv[1]
else:
    FOLDER = ''


if len(FOLDER) != 0 and os.path.exists(FOLDER):
    files = os.listdir(FOLDER)
else:
    print('Path is not defined or folder py this path name is not existing.\n Browsing by the path \'\': ')
    files = os.listdir()

for f in files:
    if os.path.isdir(FOLDER + '/' + f):
        print(bcolors.OKBLUE, f, bcolors.ENDC)
    else:
        print(bcolors.OKCYAN, f, bcolors.ENDC)
