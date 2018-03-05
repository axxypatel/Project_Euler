# You are given the following information, but you may prefer to do some research for yourself.

# 1 Jan 1900 was a Monday.
# Thirty days has September,April, June and November.All the rest have thirty-one,Saving February alone,Which has twenty-eight, rain or shine.And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

Day = 2
Year = 1901
total_sunday = 0

while Year < 2001:
    for Month in range(1, 13):
        if Month == 2:
            if Year % 1000 == 0 and Year % 400 == 0:
                Total_Days = 29
            elif Year % 4 == 0:
                Total_Days = 29
            else:
                Total_Days = 28
        elif Month in (1, 3, 5, 7, 8, 10, 12):
            Total_Days = 31
        else:
            Total_Days = 30

        for Month_Day in range(1, Total_Days+1):
            if Month_Day == 1 and Day % 7 == 0:
                total_sunday += 1
            if Day == 7:
                Day = 0
            Day += 1
    Year += 1

print("Total Sunday:", total_sunday)
