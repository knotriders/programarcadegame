num1 = float(4)
num2 = float(-2)
num3 = float(0)


inputlist = [num1, num2, num3]

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

print(posi_count)
print(nega_count)
print(zero_count)