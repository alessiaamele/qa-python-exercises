
def near(first_word, second_word):
    isFound = False
    wordOne = list(first_word)
    wordTwo = list(second_word)
    for i in range (0,len(wordOne)):
        wordOne_temp = list(wordOne)
        wordOne_temp.pop(i)
        if wordOne_temp == wordTwo:
            isFound = True
            break
        else:
            isFound = False
    print(isFound)

near("Alessia","Alssia")
near("reset", "rest")
near("dragoon", "dragon")
near("eave", "leave")
near("sleet", "lets")