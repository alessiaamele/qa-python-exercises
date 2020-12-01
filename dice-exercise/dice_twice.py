import dice

def throwDiceTwice():
    valueOne = dice.genRandomNumber()
    valueTwo = dice.genRandomNumber()
    sumValues = valueOne + valueTwo
    return sumValues

print(throwDiceTwice())