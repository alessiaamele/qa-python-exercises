maths = int(input("Please enter your maths grade between 0 and 100 \n"))
phy = int(input("Please enter your physics grade between 0 and 100 \n"))
chem = int(input("Please enter your chemistry grade between 0 and 100 \n"))
grade = (maths + phy + chem) / 3

if grade < 40:
    print("Fail")
elif grade < 50:
    print("D")
elif grade < 60:
    print("C")
elif grade < 70:
    print("B")
else:
    print("A")