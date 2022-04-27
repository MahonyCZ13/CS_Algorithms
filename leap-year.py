import os

class Color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

print(f"\n{Color.BOLD}---------------------------------{Color.END}")
print(f"{Color.YELLOW}Leap year calculation{Color.END}")
print(f"{Color.BOLD}---------------------------------{Color.END}\n")
    
print("Is the year a leap year?")

year = int(input("Input a year: "))

if year % 400 == 0 or (year % 100 != 0 and year % 4 == 0):
    print("This is a leap year!")
else:
    print("Not a leap year...")

