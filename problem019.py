countSundays = 0
def isLeapyear(year):
    if (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):
        return True
    return False

day = 365 + isLeapyear(1990)
months = [31,(28,29),31,30,31,30,31,31,30,31,30,31]
year = 1900
month = 0
dayOfMonth = 0

while year <= 2000:
    if day % 8 == 7 and dayOfMonth == 0:
        countSundays += 1
    day += 1
    if month != 1:
        dayOfMonth = (dayOfMonth + 1) % months[month]
    else:
        dayOfMonth = (dayOfMonth + 1) % months[1][isLeapyear(year)]
    if dayOfMonth == 0:
        month = (month + 1) % 12
    if month == 0 and dayOfMonth == 0:
        year += 1

print countSundays
