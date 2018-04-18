import os
import shutil
from os import path
from shutil import make_archive
from zipfile import ZipFile
def main():
    #make duplicate of an existing file
    if(path.exists('pynewfile.txt')):
        #get path to file in current directory'
        src = path.realpath('pynewfile.txt')
        #seperate path from filename
#         head, tail = path.split(src)
#         print('path: ', head)
#         print('file: ', tail)
        
        #make a backup copy by appending bak to the name
#         dst = src + '.bak'
        #use the shell to maake a copy of the file
#         shutil.copy(src, dst)

        #copy alongside permissiions, mod time and other info
#         shutil.copystat(src, dst)

        #rename the original file
#         os.rename('pytextfile.txt', 'pynewfile.txt')

        #put things in a zip file
#         root_dir, tail = path.split(src)
#         shutil.make_archive('archive', 'zip', root_dir)
        
        #more control over zip files
        with ZipFile('testzip.zip','w') as newzip:
            newzip.write('pynewfile.txt')
            newzip.write('pytextfile.txt.bak')
        
        
if __name__ == "__main__":
    main()
