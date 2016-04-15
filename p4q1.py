number1 = float(input("what is number1:"))
number2 = float(input("what is number2:"))
number3 = float(input("what is number3:"))
number4 = float(input("what is number4:"))
number5 = float(input("what is number5:"))
number6 = float(input("what is number6:"))
number7 = float(input("what is number7:"))
total = number1 + number2 +number3 +number3 +number4 +number5 +number6 +number7
inputlist = [number1,number2,number3,number3,number4 ,number5 ,number6 ,number7]
posi_count = 0
nega_count = 0
zero_count = 0
for i in inputlist:
    if i >0:
        posi_count += 1

    elif i == 0:
        zero_count += 1
    else:
        nega_count += 1

print(total)
print(posi_count)
print(nega_count)
print(zero_count)