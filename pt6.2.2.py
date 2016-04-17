n = int(input("How many eggs?:"))
print("E.g. n: ",n)
# n = 8
for i in range(n):
    for j in range(n*2):
        if i in (0 , n-1) or j in (0, 2*n-1):
            print("o", end = "")
        else:
            print(" ", end = "")
    print()
