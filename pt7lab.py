room_list = []
bed2 = ("You are in the bedroom2. north,east door",3,1,None,None)
bed1 = ("You are in the bedroom1. east, south door",None,4,0,None)
n_hall = ("You are in the north hall. north,east,south,west door",6,5,1,3)
s_hall = ("You are in the south hall. northa, east, west door",4,2,None,0)
kitchen = ("You are in the kitchen. west, south door",None,None,2,4)
dining = ("You are in the dining. east north door",5,None,None,1)
balcony = ("You are in the balcony. south door",None,None,4,None)

rooms = [bed2, s_hall, dining, bed1, n_hall, kitchen, balcony]
for room in rooms:
    room_list.append(room)
# print(room_list[0])
current_room = 0


done = False

while not done:
    print(" ")
    print(room_list[current_room][:1][0])
    # print(room_list[current_room][1])
    user_input = input("what are you gonna do?:")
    if user_input == "n":
        next_room = room_list[current_room][1]
        if next_room == None:
            print("You can't go that way")
        else:
            current_room = next_room
    elif user_input == "e":
        next_room = room_list[current_room][2]
        if next_room == None:
            print("You can't go that way")
        else:
            current_room = next_room
    elif user_input == "s":
        next_room = room_list[current_room][3]
        if next_room == None:
            print("You can't go that way")
        else:
            current_room = next_room
    elif user_input == "w":
        next_room = room_list[current_room][4]
        if next_room == None:
            print("You can't go that way")
        else:
            current_room = next_room
    else:
        print("Input correctly n,s,e,w")