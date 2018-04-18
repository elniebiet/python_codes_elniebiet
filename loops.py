def main():
    #while loop
    x = 0
    while (x < 10):
        print(x)
        x = x + 1
    #for loop
    print()
    for value in range(5,10):
        print(value)
    #use for loop over collection
    days = ("mon", "tue","wed", "thu", "fri", "sat", "sun")
    for d in days:
        print(d)
        if(d == "thu"):
            break #see continue
    #enumerate
    for i, d in enumerate(days):
        print(i,'. ', d)
    for letter in '\nletters':
        print(letter)
    letters = '\nletters'
    for letter in range(len(letters)):
        print(letters[letter])
def func():
    print('func')
        
if __name__ == "__main__":
    func() #test
    main()