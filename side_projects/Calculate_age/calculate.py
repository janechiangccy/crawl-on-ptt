import time 
from calendar import isleap

# judge the leap year
def judge_leap_year(year):
    if isleap(year):
        return True
    else:
        return False

# returns the number of days in each month
def month_days(month, leap_year):
    if month in (1, 3, 5, 7, 8, 10,12 ):
        return 31
    elif month in(4,6,9, 11):
        return 30
    elif month ==2 and leap_year:
        return 29
    elif month ==2 and (not leap_year):
        return 28

name = input('Input your name: ')
age = input('Input your age: ')
localtime = time.localtime(time.time()) # localtime 為當時的電腦的時間(區域時間)


year = int(age)
month = year * 12 +localtime.tm_mon  #localtime.tm_mon 取當前月份之值, 區間為[0,11]
day = 0

begin_year = int(localtime.tm_year) - year  #localtime.tm_year 取當前年份之值, 其值為實際年份-1900
end_year = begin_year + year

# calculate the days
for y in range(begin_year, end_year):
    if (judge_leap_year(y)):    #若出生年份至今有出現閏年, 則day = day + 366
        day = day + 366
    else:
        day = day + 365

leap_year = judge_leap_year(localtime.tm_year)  #判斷今年是否為閏年
for m in range(1, localtime.tm_mon):
    day = day + month_days(m, leap_year)    #若今年是閏年, 則2月 return 28

day = day + localtime.tm_mday   #tm.mday 一個月中的日期, 區間為[1,31]
print("%s's age is %d years or " %(name, year), end ="")
print("%d month or %d days" % (month, day))





