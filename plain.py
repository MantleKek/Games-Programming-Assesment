"""
NEED:
Input parsing (command and identifier)
Map support
World floors/sectors
Basic NPC conversations

WANT:
Map random generation

"""

valid_commands = {
    'shoot': ('shoot', 'fire', 'gun'),
    'laser': ('laser','zap'),
    'missile': ('missile','explode'),
    'warp': ('warp','jump'),
    'power': ('power','management','redirect','divert','reroute')
}

player_data = {
    'name': '',
    'race': ''
}

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
    test_command = user_input.lower().split()[0]
    print(valid_command(test_command))

def valid_command(test_command):
    for command in valid_commands:
        for counter in range(len(valid_commands[command])):
            if test_command == valid_commands[command][counter]:
                return command
    print('Sorry I do not understand what '+test_command+' is, please try again.')


def fire_weapon_check():
    print('weapon check')

def fire_laser():
    print('laser')

def fire_missile():
    print('missile')

def sector_jump():
    print('warp')

def power_management():
    print('power')

valid_functions = {
    'shoot': fire_weapon_check,
    'laser': fire_laser,
    'missile': fire_missile,
    'warp': sector_jump,
    'power': power_management
}