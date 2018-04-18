from datetime import date
from datetime import time #time class
from datetime import datetime

def main():
    #using date objects
    today = date.today()
    print('today is ', today)
    #date compnents
    print('date components: ', today.day, today.month, today.year)
    #print weekday
    print('weekday of today: ', today.weekday())
    
    #using datetime objects
    today = datetime.now() #also uses time class
    print('date time now is ', today)
    
    #time now 
    t = datetime.time(datetime.now())
    print('the time  now is: ', t)
    
    #use weekday
    wd = date.weekday(today)
    dn = ["Mon", "Tue", "Wed", "Thurs", "Fri", "Sat", 'Sun']
    print("Today is the ", wd+1, ' day of the week, which is a ',dn[wd])
    
    
    
if __name__ == "__main__":
    main()