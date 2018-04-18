import urllib2 #for connecting to web addresses
def main():
    #open connection to url
    webUrl = urllib2.urlopen('http://google.com')
    #get result code and print it
    print('result code: ', str(webUrl.getcode()))
    
    #read daata from url and print it
    data = webUrl.read()
    print(data)
if __name__ == "__main__": 
    main()
