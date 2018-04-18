from HTMLParser import HTMLParser

class MyHTMLParser(HTMLParser):
    #function to handle the procesing of html comments
    def handle_comment(self, data):
        print('Encountered comment: ', data)
        pos = self.getpos()
        print('At line: '. pos[0], ' Position ', pos[1])
def main():
    #instantiate parser and feed it html
    parser = MyHTMLParser()
    
    #open the sample html file and read it
    f = open("samplehtml.html")
    if f.mode == 'r':
        contents = f.read() #read the entire file
        parser.feed(contents)
        
if __name__ == "__main__":
    main()
