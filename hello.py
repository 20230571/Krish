# Python program to check if year is a leap year or not

year =int(input("enter a Year:\n"))

if (year % 400 == 0) and (year % 100 == 0):
    print(year , "is a leap year")

elif (year % 4 ==0) and (year % 100 != 0):
    print(year , "is a leap year")

else:
    print(year , "is not a leap year")