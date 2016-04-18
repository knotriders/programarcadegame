# import reversed
n = int(input("How many eggs?:"))
print("E.g. n: ",n)
# n = 9
odd_list = list(range(n-1,-1,-1))
com_list = []

for com in odd_list:
    com2 = com*2+1
    com_list.append(com2)
rev_list = com_list[::-1]

print(com_list)
print(rev_list)


for i in range(n):
    for j in range(n-i):
        print(rev_list[j+i], end = " ")
    for j in range(i):
        print(" ", end = " ")
    for j in range(i):
        print(" ", end = " ")
    for j in range(n-i):
        print(com_list[j], end = " ")
    print()
for i in range(n):
    for j in range(i+1):
        print(com_list[i-j], end = " ")
    for j in range(n-i-1):
        print(" ", end = " ")
    for j in range(n-i-1):
        print(" ", end = " ")
    for j in range(i+1):
        print(com_list[j], end = " ")
    print()
