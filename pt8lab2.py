def box(height, width):
    for i in range(height):
        for j in range(width):
            print("*", end = " ")
        print()


box(7,5)
print()
box(3,2)
print()
box(3,10)