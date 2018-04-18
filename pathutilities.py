import os
from os import path
import datetime
from datetime import time, date, timedelta
import time
def main():
    print(os.name) #print name of os
    #use path object
    print('path exists? ',str(path.exists('pytextfile.txt')))
    print('item is file? ',str(path.isfile('pytextfile.txt')))
    print('item is directory? ',str(path.isdir('pytextfile.txt')))
    
    print('item path: ', str(path.realpath('pytextfile.txt')))
    #item path and name
    print('item path and name: ', str(path.split(path.realpath('pytextfile.txt'))))
    
    #get modification time of file
    t = time.ctime(path.getmtime('pytextfile.txt'))
    print(t)
    print(datetime.datetime.fromtimestamp(path.getmtime('pytextfile.txt')))
    
if __name__ == "__main__":
    main()