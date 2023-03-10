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
print(f"{Color.YELLOW}Easter calculation{Color.END}")
print(f"{Color.BOLD}---------------------------------{Color.END}\n")
    
year = int(input("Input a year: "))

a = int(year % 19)
b = int(year % 4)
c = int(year % 7)

## Constants for 20. and 21. century
m = int(24)
n = int(5)

d = (19 * a + m) % 30
e = (n + 2 * b + 4 * c + 6 * d) % 7

day = d + e - 9

if day == 25 and d == 28 and e == 6 and a > 10:
    day = 18 + 1
    month = 4
elif day >= 1 and day <= 25:
    day = day + 1
    month = 4
elif day > 25:
    day = day - 6
    month = 4
else:
    day = 22 + d + e 
    month = 3

print("Easter monday this year is on " + str(day) + "." + str(month) + "." + str(year)) 
