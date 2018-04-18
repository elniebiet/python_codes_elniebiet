from datetime import datetime

def main():
    now = datetime.now()
    print(now.strftime('%Y'), ' ', now.strftime('%y'))
    print(now.strftime('%a' ', ' '%d ' '%B ' '%y'))
    #local time
    print(now.strftime('%c'))
    print(now.strftime('%x'))
    print(now.strftime('%X'))
    
    #time formating
    print(now.strftime('%I:' '%M' ':%S' ' %p')) #12 hr format
    print(now.strftime('%H' ':%M')) #24 hr format
    
if __name__ == "__main__":
    main()