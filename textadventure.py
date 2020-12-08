current_room = 0
key = False
player_data = {
    "name": 'Stephen',
    "pos_x" : 1,
    "pos_y" : 0}
player_inventory = ['none']
usable_commands = ['east','west','north','south',]
all_items = ['none','key']
world_map = [['140','0C0','281']]
room_messages = ["You find yourself in a mysterious room, there is a door to the east and one to the west",
                 "The room is empty apart from a small box in the corner. There is a door the the west",
                 "The door unlocks using the key that you found. \n You have escaped."]

def in_room(a):
#Checks if user is in room with specified room_id value, returns true if in room
    for i in world_map:
        for j in i:
            if a == int(j[0]):
                return True

def room_valid_directions(a):
#Checks what directions the user can go in the current room, returns list of strings for valid directions
    valid_directions = []
    if '1' == str(bin(int(a,16)))[3]:
        valid_directions.append('west')
    if '1' == str(bin(int(a,16)))[2]:
        valid_directions.append('east')
    if '1' == str(bin(int(a,16)))[1]:
        valid_directions.append('south')
    if '1' == str(bin(int(a,16)))[0]:
        valid_directions.append('north')
    return valid_directions

def convert_user_direction(a):
#Takes input of user and converts their direction to hex direction value, returns valid directions hex value.
    j = 0
    input_direction = []
    current_directions_counter = 0
    for i in usable_commands:
        if i in a:
            input_direction.append(i)
        j += 1
    if len(input_direction) > 1:
        print("Please input only one direction. ")
    else:
        for i in input_direction:
            if i == 'north':
                current_directions_counter += 1
            elif i == 'south':
                current_directions_counter += 2
            elif i == 'east':
                current_directions_counter += 4
            elif i == 'west':
                current_directions_counter += 8
    return int(current_directions_counter,16)

def next_room():
    y = 0
    x = 0
    if 'north' in player_input:
        y = 1
    if 'south' in player_input:
        y = -1
    if 'east' in player_input:
        x = 1
    if 'west' in player_input:
        x = -1
    return x,y
#Takes
def room_locked(y,x):
#Checks if specified room can be entered with current items
    print(all_items[int(world_map[y][x][2])])
    if all_items[int(world_map[y][x][2])] in player_inventory:
        return False
    else:
        return True

def change_room():
#Validates that room is in specified direction and that room is unlocked, changes current room.
    if player_input in usable_commands:
        if player_input in room_valid_directions(world_map[player_data['pos_y']][player_data['pos_x']][1]):
            the_next_room = next_room()
            if room_locked(player_data['pos_y']+the_next_room[1],player_data['pos_x']+the_next_room[0]):
                print("This room is locked! \n")
            else:
                player_data['pos_x'] += the_next_room[0]
                player_data['pos_y'] += the_next_room[1]
        else:
            print('You can not head in that direction. ')
    else:
        print("Unrecognized command, usable commands are "+ str(usable_commands)+'\n')

while True:
    print(room_messages[int(world_map[player_data["pos_y"]][player_data["pos_x"]][0])])
    player_input = input("What direction would you like to head? ").lower()
    change_room()


"""
Map info: room_id,valid_directions(hex),required_items

North - 1
South - 2
East - 4
West - 8
"""