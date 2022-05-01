print("Bubble Sort")

myArray = [2, 76, 1, 56, 3, 33, 2222, 34]
sortedArray = ""

n = len(myArray)

for i in range(n - 1):
    for j in range(0, n - i - 1):
        if myArray[j] > myArray[j + 1]:
            tmp = myArray[j]
            myArray[j] = myArray[j + 1]
            myArray[j + 1] = tmp

# Print sorted array 
for item in myArray:
    sortedArray += str(item)
    if item != myArray[-1]:
        sortedArray += ", "

print(sortedArray)
