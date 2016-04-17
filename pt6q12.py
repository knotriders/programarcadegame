for i in range(10):

    for j in range(10-i):
        print(" ", end = " ")
    for j in range(i-1):
        print(j+1, end = " ")
    for j in range(i):
        print(i-j, end = " ")
    print()

for i in range(10):
    for j in range(i+2):
        print(" ", end = " ")
    for j in range(8-i):
        print(j+1 , end = " ")

    print()