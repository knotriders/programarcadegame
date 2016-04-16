import random
head_count = 0
tail_count = 0
for i in range(50):
    coin_resu = random.randrange(0,2)
    if coin_resu == 1:
        print("Head")
        head_count += 1
    else:
        print("tail")
        tail_count += 1
print("Heads:", head_count)
print("Tails:", tail_count)
