import calendar  #calendar object

def main():
    #create a plain text calendar
    c = calendar.TextCalendar(calendar.SUNDAY)
    str = c.formatmonth(2013, 1, 0, 0)
    print(str)
if __name__ == "__main__":
    main()
