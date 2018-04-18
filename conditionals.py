def main():
    x, y = 10, 10
    if(x<y) :
        st = "x is less than y"
        print(st)
    elif(x > y):
        print("x is greater than y")
    else:
        print("x is equal to y")
    #conditional statement
    shout = "i am shouting" if(x<y) else "x is greater than or equal to y"
    print(shout)
        
if __name__ == "__main__":
    main()