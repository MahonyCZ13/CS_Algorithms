import os

print("Is the year a leap year?")

year = int(input("Input a year: "))

if year % 400 == 0 or (year % 100 != 0 and year % 4 == 0):
    print("This is a leap year!")
else:
    print("Not a leap year...")

