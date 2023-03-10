import math
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
print(f"{Color.YELLOW}Extended Euclides{Color.END}")
print(f"{Color.BOLD}---------------------------------{Color.END}\n")
    
def euclideExt(a, b):
 
    if b == 0 : 
        d = a
        x = 1
        y = 0
    x2 = 1
    x1 = 0
    y1 = 1
    y2 = 0
    while b > 0:
        q = math.floor(a/b)
        r = a - q * b
        x = x2 - q * x1
        y = y2 - q * y1
        a = b
        b = r
        x2 = x1
        x1 = x
        y2 = y1
        y1 = y

    d = a
    x = x2
    y = y2

    return d, x, y

a = input("Enter value for 'a': ")
b = input("Enter value for 'b': ")

d, x, y = euclideExt(int(a), int(b))
print(f"\n{Color.GREEN}NSD =", d, f"{Color.CYAN} The Inverse element for 'a' is x =", x, "The Inverse element for 'b' is y =", y,f"{Color.END}\n")
