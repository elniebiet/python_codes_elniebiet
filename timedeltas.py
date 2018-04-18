from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta
def main():
    print(timedelta(days = 365, hours = 5, minutes = 1))
    print('today is ', datetime.now())
    print('one year from now will be ', str(datetime.now() + timedelta(days=365)))
    print('in two weeks and three days it will be ', str(datetime.now() + timedelta(weeks=2, days=3)))
    
if __name__ == "__main__":
    main()