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

def toBinary(x):
    br = []
    
    while x >= 1:
        y = x
        x = x / 2
        # Prepend
        #br.insert(0, math.floor(y % 2))
        # We need to append
        br.append(math.floor(y % 2))
    
    return br



a = 5
k = 117
n = 19
b = 1
i = 0
c = 0
binar = toBinary(k)

#for num in binar:
#    print(num)

# To finish
# https://cs.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/fast-modular-exponentiation


for item in binar:
    if item == 1:
        c = c + 2**i
    
    i = i + 1

print(c)
