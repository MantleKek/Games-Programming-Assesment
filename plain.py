"""
NEED:
Input parsing (command and identifier)
Map support
World floors/sectors
Basic NPC conversations

WANT:
Map random generation

"""
import time

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
    current_targets = []
    test_command = user_input.lower().split()[0]
    try:
        valid_functions[valid_command(test_command)]()
    except:
        pass
    valid_target(user_input.lower().split()[1:])
    if command_on_target(test_command,current_targets):
        valid_functions[test_command](current_targets)


def command_on_target(command,target):
    if command in all_targets[target]:
        return True
    else:
        print('You cannot '+command+' on the '+target+'.')
        return False

def valid_target(test_targets):
    global current_targets
    for words in test_targets:
        if words in all_targets:
            current_targets.append(words)
    if len(current_targets)>1:
        current_targets = []
        print('Please only input one target.')
    else:
        temp = ''
        current_targets = temp.join(current_targets)
        return current_targets

def valid_command(test_command):
    for command in valid_commands:
        for counter in range(len(valid_commands[command])):
            if test_command == valid_commands[command][counter]:
                return command
    print('Sorry I do not understand what '+test_command+' is, please try again.')

def checkup():
    if player_data['ship_health'] <= 0:
        print('Your ship has run out of health and you have died.')
        break
    if player_data['fuel'] <= 0:
        print('Your ship has run out of fuel and you have died.')
        break

def fire_weapon_check():
    print('shoot')

def fire_laser():
    print('laser')

def fire_rocket():
    print('rocket')

def sector_warp(beacon):
    print('bruh')

def talk():
    print('talk')

def power_management():
    print('power')

def status_check():
    print('status check')

all_targets = {
    'id': None,
    'davey': ('talk'),
    'rebel': ('shoot'),
    'mechanic': ('talk'),
    'shopkeeper': ('talk'),
    'cruiser': ('talk','shoot'),
    'exit': ('exit','gate'),
    'wrecked ship': ('wrecked','ship','wreck')
}


valid_functions = {
    'shoot': fire_weapon_check,
    'warp': sector_warp,
    'talk': talk,
    'power': power_management,
    'status': status_check
}
valid_commands = {
    'shoot': ('shoot', 'fire', 'gun'),
    'warp': ('warp','jump'),
    'talk': ('talk','speak','chat'),
    'power': ('power','management','redirect','divert','reroute'),
    'status': ('status','ship')
}

player_data = {
    'name': '',
    'race': '',
    'rockets': 10,
    'ship_health': 100,
    'credits': 30,
    'fuel': 10,
    'inventory': ['id'],
    'beacon': 1,
    'sector': 1,
    'in_combat': False
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
    '1': (2),
    '2': (1,3),
    '3': (2,4),
    '4': (2,3,6),
    '5': (6,7),
    '6': (5,8),
    '7': (5),
    '8': (6,9,10),
    '9': (8),
    '10': (8,11),
    '11': (10,'exit','sector')
}