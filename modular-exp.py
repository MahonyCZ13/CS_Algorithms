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
print(f"{Color.YELLOW}RMSA{Color.END}")
print(f"{Color.BOLD}---------------------------------{Color.END}\n")

# Convert decimal number to binary
def toBinary(x):
    br = []
    
    while x >= 1:
        y = x
        x = x / 2
        # Prepend is useful for true binary represenatation
        #br.insert(0, math.floor(y % 2))

        # We need to append because of the RMSA requirement to start
        # from the right when checking the binary number represenatation
        br.append(math.floor(y % 2))
    
    return br

def modularExp(binArray):

    total = 1
    b = 1
    c = 1
    i = 0
    for item in binar:
        # print("Item: " + str(item))
        if item == 1:
            # Exponent
            if i == 0:
                c = 1
            else:
                c = 2**i
            # print(str(b) + " * (" + str(base) + "^" + str(c) + ") mod " + str(modular))
            b = (int(base)**c) % int(modular)
            # print(str(total) + " * " + str(b))
            total = total * b
        # print("Total = " + str(total))
        i = i + 1
    return total

# Variables
base = input("Enter value for base number: ")
expo = input("Enter exponent: ")
modular = input("Enter modulo: ")
binar = toBinary(int(expo))
total = modularExp(binar) % int(modular)

print(f"{Color.BOLD}{Color.CYAN}Result:{Color.END}\n{Color.BOLD}{Color.YELLOW} " + str(base) + "^" +
        str(expo) + " mod " + str(modular) + f" = {Color.BOLD}{Color.GREEN}" + str(total) + f"{Color.END}")

