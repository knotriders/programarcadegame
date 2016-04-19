import random

def average_list(list):
    k = 0
    for i in list:
        k += i
    avg = k / len(list)
    return avg

def count_list(list, number):
    count_num = 0
    for i in list:
        if i == number:
            count_num += 1
    return count_num

def create_list(list_size):
    ran_list = []
    for i in range(list_size):
        ran_list.append(random.randrange(1,7))
    return ran_list

def main():
    ten_th = create_list(10000)
    print(len(ten_th))
    for k in range(6):
        count_num  = count_list(ten_th,k+1)
        print("count of %s :" % (k+1),count_num)


    avg_sum = average_list(ten_th)
    print("average :",avg_sum)


main()