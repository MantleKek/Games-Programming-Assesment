import plain


plain.start()
print(plain.player_data)

plain.input_parse(input('Test: '))

world_data = {
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

def fedhq():
    valid_targets = None
    valid_warps = (2)

def business():
    valid_targets = 'davey'
    valid_warps = (1,3)

def sec1_solarflare():
    #-20 health and warp them back.

def sec1_fedscout1():
    valid_targets = None
    valid_warps = (2,3,6)
    if 'id' in plain.player_data['inventory']:
        plain.player_data['inventory'].remove('id')
        #First encounter
    else:
        #Coming back

def sec1_distress1():
    valid_targets = None
    valid_warps = (6,7)

def sec1_fedscout2():
    if  plain.sec1_data['rebel_scout_defeated']:
        valid_targets = None
        valid_warps = (5, 8)
        #Already defeated
    else:
        valid_targets = 'rebel'
        valid_warps = (0)
        #Fight encounter
        #Reset valid warps at combat end

def sec1_distress2():
    valid_targets = 'wrecked ship'
    valid_warps = (5)
    #Stupid minigame to save person -30 health if you dont

def sec1_goods():
    valid_targets = 'shopkeeper'
    valid_warps = (6,9,10)
    #Buy stuff and tell you about the shop next door

def sec1_repair():
    valid_targets = 'mechanic'
    valid_warps = (8)
    #Fix your ship for money

def sec1_boss():
    if plain.sec1_data['boss_defeated']:
        valid_targets = None
        valid_warps = (8,11)
    else:
        valid_targets = 'cruiser'
        valid_warps = (0)
        #Bossfight encounter
        #Reset valid warps at combat end

def exit_beacon():
    valid_targets = None
    valid_warps = 10



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