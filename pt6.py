for i in range(10):
    # print(i)
    for j in range(10):
        # print((j+1)*(i+1), end =" ")
        if ((j+1)*(i+1))<10:
            print(" ", end="")
        # else:
        print((j + 1) * (i + 1), end=" ")

    print()