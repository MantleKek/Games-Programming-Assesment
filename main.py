import plain
from time import time

def fedhq():
    valid_targets = None
    valid_warps = (2)
    print('\nWell this is it, your big job; You have been running parcels for years and finally you are going to get yourself a good payday. '
          "because this isn't just any client, this is the federation. \nUpon seeing the meagre cargo a 4 boxes you are intrigued.\n"
          "'Why spend this much money on just a few boxes?'\nYou know better than to question the federation, even if these suspicious boxes are being delivered "
          "directly into rebel territory, and hey, it's still the best payday you have ever had;\n100,000 credits, and you can even keep "
          "the missile launcher they gave you for protection. An absolute no brainer of a job you think.")
    print("Just before you leave a mantis bureaucrat runs up to you: 'Hey, sorry, I nearly forgot to give you this!' he says as he hands you a federation id pass. You nod in thanks and head on your way.")
    plain.beacon_warp_info()

def business():
    valid_targets = 'davey'
    valid_warps = (1,3)
    print("\nYou warp to the second beacon, just a few seconds from your business, you decide to quickly pop in just before you set off.\nInside you find only Davey, the happy go lucky rockperson.")
    plain.beacon_warp_info()

def sec1_solarflare():
    print('\nYou arrive at the beacon and realise the entire area is engulfed in a solar storm.\nA solar flare strikes your ship and you decide to make a hasty escape (-20 health)')
    plain.player_data['ship_health'] -= 20
    plain.beacon_warp(4)
    plain.beacon_warp_info()
    #-20 health and warp them back.

def sec1_fedscout1():
    valid_targets = None
    valid_warps = (2,3,6)
    if 'id' in plain.player_data['inventory']:
        plain.player_data['inventory'].remove('id')
        print("'You there, halt!' comes the voice over your comms. You look up to see a federation scout.")
        print("You get on the comms to tell him that you are working for the federation and you hand the scout over your id.")
        print("As they are looking it over, a rebel scout comes past at an incredible speed.")
        print("Without second thought the federation scout gives chase to the rebel, still with your id.")
    else:
        print("You recognise this as the site where a federation scout 'stole' your federation id.")
    plain.beacon_warp_info()

def sec1_distress1():
    valid_targets = None
    valid_warps = (6,7)
    print("You arrive in an empty area of space, all you can see is a far off asteroid belt.\n"
          "Your comms system is picking up a feint distress signal.")
    plain.beacon_warp_info()

def sec1_fedscout2():
    if  plain.sec1_data['rebel_scout_defeated']:
        valid_targets = None
        valid_warps = (5, 8)
        #Already defeated
    else:
        valid_targets = 'rebel'
        plain.combat_start('rebel_scout')

    plain.beacon_warp_info()

def sec1_distress2():
    valid_targets = 'wrecked ship'
    valid_warps = (5)
    print("Upon arriving in the asteroid belt you spot a wrecked ship, the source of the distress signal.\n"
          "Approaching the ship you come to realise that someone is still alive in there!"
          "You decide to break into the ship to try to save them.")
    input("Knowing that their time is limited you have to be fast or you may fail (enter to continue) ")
    start_time = time()
    while True:
        if input("Quickly type: Open the door to save the person. ") == 'Open the door to save the person.':
            end_time = time()
            break
    if end_time - start_time < 10:
        print("You manage to open the door and drag out a mantis, gasping for air.\n"
              "She splutters 'Thank you kind stranger. Without you I surely would be dead.\n'"
              "'Here is a token of my appreciation' (+60 credits)")
        plain.player_data['credits'] += 60
    else:
        print("You manage to open the door and inside you see the corpse of a mantis, you were too late.\n"
              "On your way back to your ship you are buffeted by some asteroids (-30 health)")
        plain.player_data['ship_health'] -= 30
    plain.beacon_warp_info()

def sec1_goods():
    valid_targets = 'shopkeeper'
    valid_warps = (6,9,10)
    print("You arrive outside a store, approaching the store you see an elderly? rockperson standing over some barren shelves.")
    plain.beacon_warp_info()

def sec1_repair():
    valid_targets = 'mechanic'
    valid_warps = (8)
    print("You reach Joe's mechanic shop, where there is a mechanic sitting outside reading a magazine.")
    #Fix your ship for money
    plain.beacon_warp_info()

def sec1_boss():
    if plain.sec1_data['boss_defeated']:
        valid_targets = None
        valid_warps = (8,11)
    else:
        valid_targets = 'cruiser'
        valid_warps = (0)
        #Bossfight encounter
        #Reset valid warps at combat end
    plain.beacon_warp_info()

def exit_beacon():
    valid_targets = None
    valid_warps = (10,'sector 2')
    print("You have reached the warp beacon for the sector exit. You may now leave the sector.")
    plain.beacon_warp_info()


sec1_data = {
    '1': fedhq,
    '2': business,
    '3': sec1_solarflare,
    '4': sec1_fedscout1,
    '5': sec1_distress1,
    '6': sec1_fedscout2,
    '7': sec1_distress2,
    '8': sec1_goods,
    '9': sec1_repair,
    '10': sec1_boss,
    '11': exit_beacon
}

#Main Loop
#plain.start()
while True:
    try:
        plain.checkup()
        sec1_data[plain.player_data['beacon']]()
        plain.input_parse(input('\nWhat would you like to do? '))
    except IndexError:
        pass
    except ZeroDivisionError:
        print('Your ship has run out of health and you have died.')
        break
    except IsADirectoryError:
        print('Your ship has run out of fuel and you have died.')
        break

"""

Gameplay outline:
Start at federation base (1) with exposition, tell the player their task and what they have been equipped with.
Have only one warp beacon open which leads to your business (2) where you stop off and talk to an npc (a coworker) who comments on your new weapons and their effectiveness.
3: As you warp to this beacon you are almost immediately made aware of the solar flares there (-20 ship health)
4: A fed scout stops you and interrogates you as to who you are, you show them your id but as they are checking it a rebel scout goes flying past from the way you came, without giving the id back the fed scout gives chase.
5: Empty space but you can see a asteroid belt up ahead and also you are picking up a feint distress signal.
6: You arrive and see the destroyed wreckage of the fed scout, after you arrive the rebel scout turns their attention to you (first fight)
7: Find broken ship, quickly solve puzzle to free trapped crewmate for money, fail and lose health
8: A goods shop, the shopkeeper warns you about federation presence up ahead and tells you about the repair shop around the corner.
9: A small repair shop where you can repair your ship.
10: Fight (fed cruiser) you are asked for your id which was unfortunately destroyed, causing the fed to assume that you are a rebel and a fight ensues.
11: Exit beacon to warp to the next sector
Exit: 


                           |--- 7
                     5 ---- 
       | ---- 3      |
1 ---- 2 ---- 4 ---- 6 ---- 8 ---- 10 ---- 11 (exit)
                            9

"""