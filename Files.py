def main():
    
    #write to file 'a+' to append
#     f = open('pytextfile.txt', 'w+') #w for write only is exist
#     
#     for i in range(10):
#         f.write('this is a new line %d\r\n' %(i+1))
#     f.close()
#     i = 19
#     print('python confusing print function %d' %i) #test line
    
    #read text file
#     f = open('pytextfile.txt', 'r')
#     if f.mode == 'r':
#         contents = f.read()  #read everything
#     print(contents)
    
    #read line by line
    f = open('pytextfile.txt', 'r')
    if f.mode == 'r':
        fl = f.readlines()
    for x in fl:
        print(x)
    
if __name__ == "__main__":
    main()