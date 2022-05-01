import subprocess
import sys
import os
from zipfile import ZipFile


def main(cmdLine):

    x = os.listdir(cmdLine[1])
    
    pyfiles = [i for i in x if i[-3:] ==".py"]

    os.removedirs(cmdLine[3])
    os.mkdir(cmdLine[3])

    for i in pyfiles:
        subprocess.run(['cp', i, cmdLine[3]])

    with ZipFile(cmdLine[3]+'/archive.zip', 'w') as zf:        
            for file in pyfiles:
                zf.write(file)



main(sys.argv)
