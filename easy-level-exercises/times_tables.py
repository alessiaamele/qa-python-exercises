max_range = int(input("Input a number"))
listOfValues = []

# create a list
for i in range(1, max_range + 1):
    listOfValues.append(i)

# function to multiply all values in a list
def multiplyList(myList, multiplier):
    for x in myList:
        x = x * multiplier
    return myList

print(multiplyList(listOfValues, 3))
#for num in listOfValues:
#    print(multiplyList(listOfValues, num))