# #lets make a calender
def calender(a,b):
    return f"{b}/{a}"


yy = int(input("Enter the year you want in the calender: "))
mm = int(input("Enter the month of the year you want: "))
#now lets see how my calender gets printed.
print(calender(yy,mm))

# import calendar
# text_calendar = calendar.TextCalendar()
# print(text_calendar.prmonth(2024, 6))