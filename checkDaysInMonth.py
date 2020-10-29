def isYearLeap(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0 and year % 400 != 0:
        return False
    elif year % 4 == 0:
        return True
    else: 
        return False

def daysInMonth(year, month):
    dayInMonthList = [0, 31, 0, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month == 2:
        if isYearLeap(year):
            return 29
        else:
            return 28
    return dayInMonthList[month]

testYears = [1900, 2000, 2016, 1987]
testMonths = [2, 2, 1, 11]
testResults = [28, 29, 31, 30]
for i in range(len(testYears)):
	yr = testYears[i]
	mo = testMonths[i]
	print(yr, mo, "->", end="")
	result = daysInMonth(yr, mo)
	if result == testResults[i]:
		print("OK")
	else:
		print("Failed")
