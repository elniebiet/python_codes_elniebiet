import xml.dom.minidom
def main():
     #use the parse function to loaad and parse an xml file
     doc = xml.dom.minidom.parse('samplehtml.html');
     
     #print out the document node aand the name of the first child tag
     print(doc.nodeName)
     print(doc.firstChild.tagName)
     
if __name__ == "__main__":
    main()
