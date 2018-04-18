class class1():
    def method1(self):
        print("method1 in class1")
    def method2(self, string):
        print("method2 in class1 with string: "+ string)
class class2(class1):
    def method1(self): #overriding
        print("method1 in class2")
    def method2(self, string): #overriding
        print("method2 in class2 with string: "+ string)
def main():
    c = class1()
    c.method1()
    c.method2('i am a class one man')
    
    c1 = class2()
    c1.method1()
    c1.method2('i am a class two man')
if __name__ == "__main__":
    main()