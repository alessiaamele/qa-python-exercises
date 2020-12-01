code = str(input("Please input the ISBN code"))
code_in_numbers = []
check_digit = 0

for i in range(0, 15):
    if code[i]=="-":
        continue
    code_in_numbers.append(code[i])

for j in range(0, 12):
    if j%2==0:
        check_digit = check_digit + int(code_in_numbers[j])
    elif j%2==1:
        check_digit = check_digit + int(code_in_numbers[j]) * 3

check_digit = 10 - (check_digit % 10)

code=code+str(check_digit)
print(code)
        