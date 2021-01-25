"""
NEED:
Input parsing (command and identifier)
Map support
World floors/sectors
Basic NPC conversations

WANT:
Map random generation

"""
from random import randint

def start():
    print('Insert exposition here.')
    while True:
        name = input('\nWhat is your name: ')
        if input('Your name is '+name+' correct? (y/n)').lower()[0] == 'y':
            player_data['name'] = name
            break
    while True:
        race = input('\nWhat race are you? (human, mantis or rockperson) ').lower()[0]
        if race == 'h':
            player_data['race'] = 'human'
            break
        elif race == 'm':
            player_data['race'] = 'mantis'
            break
        elif race == 'r':
            player_data['race'] = 'rockperson'
            break
        else:
            print('That is not a valid selection.')


def input_parse(user_input):
    global current_targets, raw_input
    raw_input = user_input
    current_targets = ''
    test_command = user_input.lower().split()[0]
    if 'help' in raw_input:
        help()
        return None
    try:
        valid_functions[valid_command(test_command)]()
    except:
        pass
    current_targets = valid_target(user_input.lower().split()[1:])
    if current_targets:
        if command_on_target(test_command,current_targets):
            valid_functions[test_command](current_targets)
    else:
        print('You can not do that.')
    checkup()


def command_on_target(command,target):
    if command in all_targets[target]:
        return True
    else:
        print('You can not '+command+' on the '+target+'.')
        return False

def valid_target(test_targets):
    global current_targets
    for word in test_targets:
        if word in all_targets:
            return word

def valid_command(test_command):
    for command in valid_commands:
        for counter in range(len(valid_commands[command])):
            if test_command == valid_commands[command][counter]:
                return command
    print('Sorry I do not understand what '+test_command+' is, please try again.')

def checkup():
    if player_data['ship_health'] <= 0:
        raise ZeroDivisionError
    if player_data['fuel'] <= 0:
        raise IsADirectoryError


def fire_weapon_check():
    if input('Fire a laser shot or a rocket? ').lower()[0] == 'l':
        fire_laser(combat_unit)
    elif input('Fire a laser shot or a rocket? ').lower()[0] == 'r':
        if player_data['rockets'] >= 1:
            fire_rocket(combat_unit)
        else:
            print('No rockets remaining.')
    else:
        fire_weapon_check()

def fire_laser(target):
    laser_base_dmg = 9
    laser_dmg = laser_base_dmg + randint(-2,2)
    target['health'] -= laser_dmg
    print('%s hit for %d damage.'%(target,laser_dmg))

def fire_rocket(target):
    rocket_base_dmg = 18
    rocket_dmg = rocket_base_dmg + randint(-5,5)
    player_data['rockets'] -= 1
    if randint(0,1) == 0:
        target['health'] -= rocket_dmg
        print('%s hit for %d damage.'%(target,rocket_dmg))
    else:
        print('The rocket missed...')

def combat_start(unit):
    global combat_unit
    combat_unit = unit
    combat_unit_health = unit['health']
    player_data['in_combat'] = True

def beacon_warp(beacon):
    if player_data['beacon'] == '11'and beacon == 'exit':
        sector_exit()
        return None
    if player_data['in_combat'] == True:
        print('You can not warp out of combat')
        return None
    try:
        int(beacon)
    except ValueError:
        print('This is not a valid beacon to warp to.')
    if beacon in sec1_warps[str(player_data['beacon'])]:
        player_data['beacon'] = beacon
        player_data['fuel'] -= 1
    else:
        print('You can not warp to that location.')

def beacon_warp_info():
    cur_beacon = player_data['beacon']
    print('You are at beacon '+cur_beacon)
    print('From here you can warp to beacon(s) ',sec1_warps[cur_beacon])

def sector_exit(waffle):
    print('You exit the sector. Ending the game for now.')
    #Endgame text for now

def talk(target):
    print(talk_targets[target])

def repair(amount):
    while True:
        if amount is None:
            amount = input('How much damage would you like to repair (current health: %d'%(player_data['ship_health']))
        else:
            break
        try:
            amount = int(amount)
        except ValueError:
            print('Please give a valid value. ')
    if amount > player_data['credits']:
        print('You cannot afford that, you only have %d credits.'%(player_data['credits']))
    else:
        print('You have fixed %d damage.'%(amount))
        player_data['credits']-=amount
        player_data['ship_health'] += amount

def status_check():
    print('Ship Health: ',player_data['ship_health'])
    print('Credits: ',player_data['credits'])
    print('Fuel: ',player_data['fuel'])
    print('Missiles: ',player_data['rockets'])

def help():
    print('Available commands are: ')
    for fun in valid_functions:
        print(fun)

all_targets = {
    'id': None,
    'davey': ('talk'),
    'rebel': ('shoot'),
    'mechanic': ('talk','repair'),
    'shopkeeper': ('talk'),
    'cruiser': ('talk','shoot'),
    'exit': ('exit','gate','warp'),
    'wrecked ship': ('wrecked','ship','wreck'),
    '1': ('warp'),
    '2': ('warp'),
    '3': ('warp'),
    '4': ('warp'),
    '5': ('warp'),
    '6': ('warp'),
    '7': ('warp'),
    '8': ('warp'),
    '9': ('warp'),
    '10': ('warp'),
    '11': ('warp','sector')
}
valid_functions = {
    'shoot': fire_weapon_check,
    'warp': beacon_warp,
    'talk': talk,
    'help': help,
    'status': status_check,
    'repair': repair,
    'sector': sector_exit
}
valid_commands = {
    'shoot': ('shoot', 'fire', 'gun','attack'),
    'warp': ('warp','jump'),
    'talk': ('talk','speak','chat'),
    'help': ('help'),
    'status': ('status','ship'),
    'repair': ('repair','fix'),
    'sector': ('exit','sector')
}
player_data = {
    'name': 'Default',
    'race': '',
    'rockets': 10,
    'ship_health': 100,
    'credits': 30,
    'fuel': 10,
    'inventory': ['id'],
    'beacon': '1',
    'sector': 1,
    'in_combat': False
}
talk_targets = {
    'davey': "Gee boss, good luck on your next delivery; I'm sure you'll do just great!",
    'mechanic': "'Pleasure to meet ya! The names Jim, whats yours?'\nYou introduce yourself to Jim\n'Well %s do yer need me to work some wonders on that rust bucket there?'"%(player_data['name']),
    'shopkeeper': 'Hello dear and welcome to my humble shop, sadly I have a shortage of supply right now, this bloody war is taking its toll.\n'
                'Your ship looks quite a state! You should bring it over to beacon 9, best mechanic in the galaxy.',
    'cruiser': 'Stop talking and show us your id, or we will open fire.\nUpon realising that you id was lost during your prior meeting with the federation you begin to panic.\nSensing the tension in your voice you hear the captain yell "Enough of this, kill the rebel scum" shortly followed up by a missile that narrowly misses the ship.'
}
sec1_data = {
    'rebel_scout_defeated': False,
    'boss_defeated': False
}
sec1_targets = {
    '1': None,
    '2': 'davey',
    '3': None,
    '4': None,
    '5': None,
    '6': 'rebel',
    '7': 'wrecked ship',
    '8': 'shopkeeper',
    '9': 'mechanic',
    '10': 'cruiser',
    '11': None
}
sec1_warps = {
    '1': ('2'),
    '2': ('1','3','4'),
    '3': ('2','4'),
    '4': ('2','3','6'),
    '5': ('6','7'),
    '6': ('4','5','8'),
    '7': ('5'),
    '8': ('6','9','10'),
    '9': ('8'),
    '10': ('8','11'),
    '11': ('10','sector')
}
sec1_shop = {
    'fuel': 10,
    'missile': 8
}
rebel_scout = {
    'health': 30,
    'base_dmg': 7,
    'var': 2
}
fed_cruiser = {
    'health': 50,
    'base_dmg': 12,
    'var':4
}