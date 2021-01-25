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
    global current_targets
    current_targets = []
    test_command = user_input.lower().split()[0]
    try:
        valid_functions[valid_command(test_command)]()
    except:
        pass
    valid_target(user_input.lower().split()[1:])
    print(current_targets)

def valid_target(test_targets):
    for words in test_targets:
        if words in all_targets:
            current_targets.append(words)

def valid_command(test_command):
    for command in valid_commands:
        for counter in range(len(valid_commands[command])):
            if test_command == valid_commands[command][counter]:
                return command
    print('Sorry I do not understand what '+test_command+' is, please try again.')


def fire_weapon_check():
    print('shoot')

def fire_laser():
    print('laser')

def fire_rocket():
    print('rocket')

def sector_jump():
    print('warp')

def talk():
    print('talk')

def power_management():
    print('power')

def status_check():
    print('status check')

all_targets = {
    'id': None,
    'davey': ('talk')
    'rebel': ('shoot'),
    'mechanic': ('talk'),
    'shopkeeper': ('talk')
    'cruiser': ('talk','shoot')
}


valid_functions = {
    'shoot': fire_weapon_check,
    'warp': sector_jump,
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
    'ship_health': 100
    'credits': 30
    'fuel': 10
    'inventory': ['id']
}
sec1_data = {
    'rebel_scout_defeated': False
    'boss_defeated': False
}
