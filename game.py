"""
Boo Boo

Author: Danilo Valle

"""


import time
import random
import itertools


def all_foe_data() -> tuple:
    """
    Return a tuple of various foes and their information.

    :return: a tuple of various foes and their information

    >>> foe_data = all_foe_data()
    >>> foe_data[1]['Name']
    'An apprentice girlie'
    >>> foe_data[1]['Required Level']
    1
    """
    return ({'Name': "An auditionee girlie", 'Damage': 6, 'Current HP': 25, 'XP worth': 5, 'Required Level': 1,
             'Accuracy': 10},
            {'Name': "An apprentice girlie", 'Damage': 9, 'Current HP': 30, 'XP worth': 5, 'Required Level': 1,
             'Accuracy': 20},
            {'Name': "A corps girlie", 'Damage': 12, 'Current HP': 40, 'XP worth': 10, 'Required Level': 2,
             'Accuracy': 30},
            {'Name': "A soloist girlie, careful this one's a lot stronger than the others...", 'Damage': 15,
             'Current HP': 60, 'XP worth': 20, 'Required Level': 3, 'Accuracy': 50})


def all_class_data() -> dict:
    """
    Return a dictionary containing class information for the game.

    :return: a dictionary containing information on all the classes in the game

    >>> class_list = all_class_data()
    >>> 'Name' in class_list["1"]
    True
    >>> 'Max HP' in class_list["2"]
    True
    """
    return {"1": {'Name': 'JUMPER', 'Damage': 70, 'Max HP': 50, 'XP Cap': 20, 'Accuracy': 30,
                  'Description': 'Very light on your feet. A lot of power goes into making those jumps look '
                                 '\neffortless!',
                  'Attack Name': 'SHOOTING GRAND JETE - You leap into a stunning split midair, gliding '
                                 '\nforward and impaling your pointed foot right into the opponent!'},
            "2": {'Name': 'TURNER', 'Damage': 50, 'Max HP': 100, 'XP Cap': 25, 'Accuracy': 50,
                  'Description': 'You spin like a top. ',
                  'Attack Name': 'TORNADO PIROUETTES - You rotate so fast that you produce a tornado headed '
                                 '\nright for the opponent!'},
            "3": {'Name': 'BENDER', 'Damage': 25, 'Max HP': 160, 'XP Cap': 25, 'Accuracy': 40,
                  'Description': 'Legs for days, honey. You got the lines that ballet enthusiasts gush over.',
                  'Attack Name': 'GRAND BATTEMENT SLAM - You kick your leg forward tapping your shoulder, '
                                 '\nand then slamming it back down into the opponent!'},
            "4": {'Name': 'EXPRESSER', 'Damage': 10, 'Max HP': 300, 'XP Cap': 10, 'Accuracy': 90,
                  'Description': 'You don\'t have strong technical abilities like the other classes, but you sell '
                                 '\nit in the face. You give the drama.',
                  'Attack Name': 'HEART TOUCHING EMOTION - You perform a cute little act. Your opponent so '
                                 '\ntransfixed that they question their own performance abilities in comparison!'}
            }


def make_boss() -> dict:
    """
    Create a boss.

    :return: a dictionary of final boss information

    >>> some_boss = make_boss()
    >>> some_boss['Name']
    'Principal dancer, Miss Prima'

    >>> some_boss['Attack 2']['Damage']
    20
    """
    return {'Name': "Principal dancer, Miss Prima", 'X-position': 24, 'Y-position': 24, 'Current HP': 300,
            'Accuracy': 90,
            'Attack 1': {'Damage': 30,
                         'Name': "THOUSAND POINTE SHOES - She throws several pairs of her old ballet pointe "
                                 "\nshoes at you! They may be worn out from all her performances, but they "
                                 "\nstill pack a punch!"},
            'Attack 2': {'Damage': 20,
                         'Name': "FOAM ROLL CRUSHER - She chases you down with her foam roller!"}
            }


def game_exposition() -> None:
    """
    Print a brief background of the game's story.
    """
    time.sleep(1)
    print("You got the job to be a ballerina at the BooBoo Ballet Company.")
    time.sleep(1.5)
    print("\nYour job is to be the best girlie in the company.")
    time.sleep(1.5)
    print("\nThat is done by battling the veteran girlies and eventually defeat...")
    time.sleep(1.5)
    print("\n...Miss Prima, BooBoo's Principal Ballerina.")
    time.sleep(2)
    print("\n\n\n******************************************")
    print("\t\t BOOBOO")
    print("******************************************\n\n\n")


def unsuccessful_ending_text() -> None:
    """
    Print a text message indicating an unsuccessful play-through.
    """
    print("\n\t GAME OVER")
    print("\n \t \t \t End.")


def successful_ending_text() -> None:
    """
    Print a text message indicating a successful play-through.
    """
    print("\n\t CONGRATULATIONS YOU HAVE DEFEATED THE GAME!")
    print("\n \t \t \t End.")


def make_board(rows: int, columns: int) -> dict:
    """
    Create a game board of specified rows and columns.

    :param rows: an int
    :param columns: an int
    :precondition: rows must be an integer greater than or equal to 2
    :precondition: columns must be an integer greater than or equal to 2
    :postcondition: return a board of specified rows and columns inclusive
    :return: a dictionary with keys of coordinate tuples and strings randomly assigned from a list as values to each
             tuple

    >>> some_board = make_board(2, 2)
    >>> list(some_board.keys())
    [(0, 0), (0, 1), (1, 0), (1, 1)]

    >>> "You enter the grand foyer of BunBun Ballet Academy." in some_board[(0, 0)]
    True
    """
    room_descriptions = ["a hallway. The walls decorated with framed images of the girlies "
                         "\nin Swan Lake, Don Quixote, Romeo & Juliet... they've got them all!",
                         "a studio. Ew, it's a lot smaller than you're used to and the lighting "
                         "\nis horrendous. Having class in here must be awful, but it gets the job "
                         "\ndone, you suppose.",
                         "(surprise, surprise) a dance studio. Nice high ceilings, springy flooring, "
                         "\nplenty of ballet barre space, and windows to the outside. It's a cute room.",
                         "a studio. This one is huge! And at the top: a glass domed ceiling, sunlight "
                         "\nilluminating the space. It's gorgeous in here!",
                         "a theatre stage. You vividly imagine playing Odette from Swan Lake, or "
                         "\nJuliet in Romeo & Juliet. You feel more determined than ever to become "
                         "\nthe next prima ballerina girlie.",
                         "a lobby area. Nice and spacious."]
    board = {(column, row): "\nYou enter " + random.choice(room_descriptions)
             for column in range(columns) for row in range(rows)}
    board[(0, 0)] = "\nYou enter the grand foyer of BunBun Ballet Academy. It's mesmerizing, what " \
                    "\nyou've always dreamed of."
    return board


def choose_name() -> str:
    """
    Return the name entered by the user.

    :return: a string containing anywhere between 2 and 10 alphabetical characters
    """
    print("\nPlease enter a character name below to begin. A valid name must contain "
          "\nonly letters, and is between 2 and 10 characters")
    name = input('\nYour name: ')
    while not (2 <= len(name) <= 10 and name.isalpha()):
        print("\nThat's not allowed!")
        print("Please enter a character name below to begin. A valid name must contain "
              "\nonly letters, and is between 2 and 10 characters")
        name = input("\nYour name: ")
    return name


def choose_class() -> dict:
    """
    Return the class selected by the user.

    :return: a dictionary of the information for the class selected by the user
    """
    class_list = all_class_data()
    print("\nPlease enter the number corresponding to your desired class below\n")
    for option, some_class in class_list.items():
        print(f"{option}: {some_class['Name']} - {some_class['Description']}")
    response = input("\nYour selected class: ")
    while response not in class_list.keys():
        print("\nThat's not allowed!")
        print("Please enter a number corresponding to your desired class below\n")
        for option, some_class in class_list.items():
            print(f"{option}: {some_class['Name']} - {some_class['Description']}")
        response = input("\nYour selected class: ")
    return class_list[response]


def make_character() -> dict:
    """
    Create a character with set attributes.

    :return: a dictionary of character information
    """
    chosen_name = choose_name()
    chosen_class = choose_class()
    return {'Name': chosen_name, 'X-position': 0, 'Y-position': 0, 'Level': 1, 'Current XP': 0,
            'Current HP': chosen_class['Max HP'], 'Class': chosen_class}


def display_map(board: dict, character: dict, boss: dict) -> None:
    """
    Display the character's current surrounding areas.

    :param board: a dictionary
    :param character: a dictionary
    :param boss: a dictionary
    :precondition: board must be a dictionary created by the make_board function
    :precondition: character must be a dictionary created by the make_character function
    :precondition: boss must be a dictionary created by the make_boss function
    :postcondition: board, character and boss are unchanged
    :postcondition: outputs a 5 by 5 map of the character's current surrounding grid points

    """
    visual_map = ""
    for y_coordinate in range(character['Y-position'] - 2, character['Y-position'] + 3):
        visual_map += "\n\n"
        for x_coordinate in range(character['X-position'] - 2, character['X-position'] + 3):
            if (x_coordinate, y_coordinate) == (character['X-position'], character['Y-position']):
                visual_map += " [#] "
            elif (x_coordinate, y_coordinate) == (boss['X-position'], boss['Y-position']):
                visual_map += " [!] "
            else:
                visual_map += "  ®  " * ((x_coordinate, y_coordinate) not in board.keys())
                visual_map += " [ ] " * ((x_coordinate, y_coordinate) in board.keys())
    print(visual_map)


def describe_current_location(board: dict, character: dict) -> None:
    """
    Describe the character's current position on the board.

    :param board: a dictionary
    :param character: a dictionary
    :precondition: board must be a dictionary created by the make_board function
    :precondition: character must be a dictionary created by the make_character function
    :postcondition: board and character are unchanged
    :postcondition: outputs a description of the character's current position on the board

    """
    current_location = board[(character["X-position"], character["Y-position"])]
    print(f"\n{current_location}")


def display_options(all_options: dict) -> None:
    """
    Display each key value pair of a dictionary on a new line.

    :param all_options: a dictionary
    :precondition: all_options must be a non-empty dictionary
    :postcondition: all_options is unchanged
    :postcondition: print each key value pair separated by a colon on a new line
    """
    print(f"\nEnter the number corresponding to a direction below to make a move.")
    for key, value in all_options.items():
        print(f"{key}: {value}")
    print("\nOr, if you'd like to quit the game instead, just type quit \n")


def get_user_choice() -> str:
    """
    Obtain a player's next movement choice.

    Prompt the user to input a selection from a list of options. If the user wants to quit however, they can also type
    "quit" at this prompt to end the game.

    :return: "NORTH", "SOUTH", "WEST", or "EAST" if the user inputs 1, 2, 3, or 4 respectively or "quit" if the user
             inputs the word quit
    """
    all_options = {"1": "NORTH", "2": "SOUTH", "3": "WEST", "4": "EAST"}
    display_options(all_options)
    response = input("Your choice: ")
    while response not in all_options.keys() and response != "quit":
        print("\nStop playing around!")
        display_options(all_options)
        response = input("Your choice: ")
    if response == "quit":
        return response
    else:
        return all_options[response]


def validate_move(board: dict, character: dict, direction: str) -> bool:
    """
    Check to see if a character's movement selection is within the bounds of the game board.

    :param board: a dictionary
    :param character: a dictionary
    :param direction: a string
    :precondition: board must be a dictionary created by the make_board function
    :precondition: character must be a dictionary created by the make_character function
    :precondition: direction must be a string returned by the get_user_choice function
    :postcondition: board and character are unchanged
    :postcondition: checks if a character's movement choice is possible or not
    :return: True if a character's new desired position exists in the game board or False if otherwise

    >>> game_board = {(0, 0): 'Empty', (0, 1): 'Empty', (1, 0): 'Empty', (1, 1): 'Empty'}
    >>> player = {'X-position': 0, 'Y-position': 0, 'Current HP': 5}
    >>> validate_move(game_board, player, 'NORTH')
    False

    >>> validate_move(game_board, player, 'SOUTH')
    True
    """
    x_destination = character["X-position"] + (direction == "EAST") - (direction == "WEST")
    y_destination = character["Y-position"] + (direction == "SOUTH") - (direction == "NORTH")
    return (x_destination, y_destination) in board


def move_character(character: dict, direction: str) -> None:
    """
    Update a character's X and Y position according to a selected direction.

    :param character: a dictionary
    :param direction: a dictionary
    :precondition: character must be a dictionary created by the make_character function
    :precondition: direction must be a dictionary created by the get_user_choice function
    :postcondition: change the character's X and Y values based on a movement selection

    >>> player = {'X-position': 0, 'Y-position': 0, 'Current HP': 5}
    >>> move_character(player, "EAST")
    >>> player
    {'X-position': 1, 'Y-position': 0, 'Current HP': 5}
    """
    character["X-position"] += (direction == "EAST") - (direction == "WEST")
    character["Y-position"] += (direction == "SOUTH") - (direction == "NORTH")


def check_for_foes() -> bool:
    """
    Return True if a foe is encountered and False if otherwise.

    :return: True if a randomly selected integer falls between 1 inclusive and 20 inclusive and False if otherwise
    """
    return 1 <= random.randint(1, 100) <= 20


def opponent_below_level_three(opponent: dict) -> bool:
    """
    Indicate whether an opponent's required level is below level 3.

    :param opponent: a dictionary
    :precondition: opponent must be a dictionary within the tuple of the all_foe_data function
    :postcondition: opponent is unchanged
    :postcondition: indicates if a foe's required level is below level 3
    :return: True if the 'Required Level' attribute of a foe is below level 3, and False otherwise

    >>> opponent_below_level_three({'Name': 'A', 'Required Level': 2})
    True
    >>> opponent_below_level_three({'Name': 'A', 'Required Level': 3})
    False
    """
    return opponent['Required Level'] <= 2


def generate_foe(character: dict) -> dict:
    """
    Return a randomly selected foe.

    :param character: a dictionary
    :precondition: character must be a dictionary made by the make_character function
    :postcondition: character is unchanged
    :postcondition: randomly generate an opponent based on level
    :return: a dictionary representing a type of foe and their information
    """
    all_foes = all_foe_data()
    if character['Level'] <= 2:
        foe_pool = list(filter(opponent_below_level_three, all_foes))  # opponent_below_level_three defined right above
    else:
        foe_pool = all_foes
    return random.choice(foe_pool)


def level_up_character(character: dict) -> None:
    """
    Increase the character's current level.

    :param character: a dictionary
    :precondition: character must be a dictionary created by the make_character function
    :postcondition: increases the character's current level by 1, max HP by 20, next level's XP cap by 10, and attack
                    damage by 10. Also resets the current XP meter and grants a full heal

    >>> player = {'Level': 1, 'Current HP': 25, 'Current XP': 3, 'Class': {'XP Cap': 10, 'Max HP': 40, 'Damage': 50}}
    >>> level_up_character(player)
    <BLANKLINE>
    Congratulations! You are now at level 2! Your Max HP has increased to 60 and your attack damage has increased to 60.
    >>> player['Current HP']
    60
    """
    character['Level'] += 1
    character['Class']['XP Cap'] += 10
    character['Class']['Max HP'] += 20
    character['Class']['Damage'] += 10
    character['Current XP'] = 0
    character['Current HP'] = character['Class']['Max HP']
    time.sleep(2)
    print(f"\nCongratulations! You are now at level {character['Level']}! "
          f"Your Max HP has increased to {character['Class']['Max HP']} and your attack damage has increased to "
          f"{character['Class']['Damage']}.")
    time.sleep(2)


def gain_xp(character: dict, opponent: dict) -> None:
    """
    Increase the character's XP after defeating an opponent.

    :param character: a dictionary
    :param opponent: a dictionary
    :precondition: character must be a dictionary created by the make_character function
    :precondition: opponent must be a dictionary created by the generate_foe function
    :postcondition: opponent is unchanged
    :postcondition: increase the character's XP by the XP value of a foe

    >>> player = {'Level': 1, 'Current HP': 25, 'Current XP': 3, "Class": {'XP Cap': 10, 'Max HP': 40, 'Damage': 50}}
    >>> some_foe = {'Current HP': 0, 'XP worth': 10}
    >>> gain_xp(player, some_foe)
    <BLANKLINE>
    You gained 10XP!
    <BLANKLINE>
    Congratulations! You are now at level 2! Your Max HP has increased to 60 and your attack damage has increased to 60.
    <BLANKLINE>
    You are now at a current XP of 0.
    """
    print(f'\nYou gained {opponent["XP worth"]}XP!')
    character['Current XP'] += opponent['XP worth']
    if character['Current XP'] >= character['Class']['XP Cap']:
        level_up_character(character)
    time.sleep(1.5)
    print(f"\nYou are now at a current XP of {character['Current XP']}.")
    time.sleep(2)


def combat_your_turn(character: dict, opponent: dict) -> None:
    """
    Attack a foe.

    :param character: a dictionary
    :param opponent: a dictionary
    :precondition: character must be a dictionary created by the make_character function
    :precondition: opponent must be a dictionary created by the generate_foe function
    :postcondition: character is unchanged
    :postcondition: inflict damage on opponent if a randomly generated integer falls between 1 and an upper bound
                    equal to character['Class']['Accuracy']
    """
    time.sleep(1)
    print(f"\nYou attack with: {character['Class']['Attack Name']}")
    time.sleep(2)
    if 1 <= random.randint(1, 100) <= character['Class']['Accuracy']:
        opponent['Current HP'] -= character['Class']['Damage']
        opponent['Current HP'] *= opponent['Current HP'] > 0
        print(f"\nDirect Hit! You deal {character['Class']['Damage']} damage! \nThat brings her down to "
              f"{opponent['Current HP']}HP.")
    else:
        print("\nDarn, she dodged your attack!")


def combat_opponent_turn(character: dict, opponent: dict) -> None:
    """
    Experience an attack from an opponent.

    :param character: a dictionary
    :param opponent: a dictionary
    :precondition: character must be a dictionary created by the make_character function
    :precondition: opponent must be a dictionary created by the generate_foe function
    :postcondition: opponent is unchanged
    :postcondition: opponent will inflict damage on a player if a randomly generated integer falls between 1 and an
                    upper bound equal to opponent['Accuracy']
    """
    print("\nIt's her turn!")
    time.sleep(2)
    if 1 <= random.randint(1, 100) <= opponent['Accuracy']:
        character['Current HP'] -= opponent['Damage']
        character['Current HP'] *= character['Current HP'] > 0
        print(f"\nShe got ya gal! You lose {opponent['Damage']}HP bringing you down "
              f"to {character['Current HP']}HP.")
    else:
        print("\nYou managed to dodge her attack!")


def combat_round(character: dict, opponent: dict) -> bool:
    """
    Drive an entire round of combat with a foe.

    :param character: a dictionary
    :param opponent: a dictionary
    :precondition: character must be a dictionary created by the make_character function
    :precondition: opponent must be a dictionary created by the generate_foe function
    :postcondition: determine if the opponent or the character has been defeated
    :return: True if both character and opponent have current HP's greater than or equal to 1, and False otherwise.
    """
    combat_your_turn(character, opponent)
    character_is_alive = character['Current HP'] > 0
    opponent_is_alive = opponent['Current HP'] > 0
    if opponent_is_alive:
        combat_opponent_turn(character, opponent)
        character_is_alive *= (character['Current HP'] > 0)
    else:
        print("\nYou successfully defeated her!")
    return character_is_alive and opponent_is_alive


def get_continue_combat_or_flee_choice() -> str:
    """
    Request the user to continue to a new round of combat or flee.

    :return: 1 if YES is selected and 2 if NO is selected
    """
    print("\nEnter the number corresponding to an option below: ")
    for number, option in enumerate(["YES", "NO"], 1):
        print(f"{number}: {option}")
    response = input('\nYour selection: ')
    while response not in ("1", "2"):
        print("\nInvalid selection!")
        print("\nEnter the number corresponding to an option below: ")
        for number, option in enumerate(["YES", "NO"], 1):
            print(f"{number}: {option}")
        response = input('\nYour selection: ')
    return response


def combat(character: dict, opponent: dict) -> bool:
    """
    Initialize a potential combat scene with with an opponent.

    :param character: a dictionary
    :param opponent: a dictionary
    :precondition: character must be a dictionary created by the make_character function
    :precondition: opponent must be a dictionary created by the generate_foe function
    :postcondition: begin and continue combat or refuse based on user input
    :postcondition: returns True if character has defeated opponent and is still alive, and False otherwise
    :return: True if character has defeated opponent and is still alive, and False otherwise
    """
    opponent['isScared'] = False
    print(f"\n{opponent['Name']} challenges you along the way! "
          f"\n\"Bring it, bitch!\", she shouts. Do you accept the challenge?")
    response = get_continue_combat_or_flee_choice()
    there_can_be_a_next_round = True
    while response == "1" and there_can_be_a_next_round:
        there_can_be_a_next_round = combat_round(character, opponent)
        if there_can_be_a_next_round:
            print("\nDo you want to continue battling?")
            response = get_continue_combat_or_flee_choice()
            opponent['isScared'] = (1 <= random.randint(1, 100) <= 20)
            there_can_be_a_next_round = not opponent['isScared']
    return (character['Current HP'] > 0) and (opponent['Current HP'] < 1)


def flee_early(character: dict, opponent: dict) -> None:
    """
    Accept a 20% chance that the opponent hits your character if combat is left early.

    :param character: a dictionary
    :param opponent: a dictionary
    :precondition: character must be a dictionary created by the make_character function
    :precondition: opponent must be a dictionary created by the generate_foe function
    :postcondition: opponent is unchanged
    :postcondition: there will be a 20% chance that the opponent hits the character
    """
    if 1 <= random.randint(1, 100) <= 20:
        character['Current HP'] -= opponent['Damage']
        character['Current HP'] *= character['Current HP'] > 0
        time.sleep(2)
        print(f"\nOuch! She got in one more hit before you could leave! You're down to {character['Current HP']}HP.")
    else:
        print("\nYou flee the scene...")


def foe_encounter(character: dict, opponent: dict) -> None:
    """
    Drive the entire encounter with a foe.

    :param character: a dictionary
    :param opponent: a dictionary
    :precondition: character must be a dictionary created by the make_character function
    :precondition: opponent must be a dictionary created by the generate_foe function
    :postcondition: go through all user-requested rounds of combat, gain the XP worth of the opponent,
                    or flee from the opponent
    """
    character_is_victorious = combat(character, opponent)
    character_is_alive = character['Current HP'] > 0
    opponent_is_alive = opponent['Current HP'] > 0
    if character_is_victorious:
        gain_xp(character, opponent)
        print("\n")
    elif opponent['isScared']:
        time.sleep(1.5)
        print("\nWell, you actually can't attack her anymore 'cause she vanished. You didn't defeat her but at least "
              "she's outta the way!")
        time.sleep(1)
    elif character_is_alive and opponent_is_alive:
        flee_early(character, opponent)


def combat_boss_turn(character: dict, boss: dict, boss_attack: dict) -> None:
    """
    Experience an attack from the final boss.

    :param character: a dictionary
    :param boss: a dictionary
    :param boss_attack: a dictionary
    :precondition: character must be a dictionary created by the make_character function
    :precondition: boss must be a dictionary created by the make_boss function
    :precondition: boss_attack must be a dictionary equal to boss['Attack 1'] or boss['Attack 2']
    :postcondition: boss and current_attack are unchanged
    :postcondition: boss will inflict damage on a player if a randomly generated integer falls between 1 and an
                    upper bound equal to boss['Accuracy']
    """
    print("\nIt's her turn!")
    time.sleep(1)
    print(f"She attacks with: {boss_attack['Name']}")
    time.sleep(1.5)
    if 1 <= random.randint(1, 100) <= boss['Accuracy']:
        character['Current HP'] -= boss_attack['Damage']
        character['Current HP'] *= character['Current HP'] > 0
        print(f"\nShe got ya gal! OOF! You lose {boss_attack['Damage']}HP bringing you down "
              f"to {character['Current HP']}HP.")
    else:
        print("\nWoah you dodged her attack! Something tells you that's rare...")


def boss_round(character: dict, boss: dict, boss_attack: dict) -> bool:
    """
    Drive an entire round of combat with the final boss.

    :param character: a dictionary
    :param boss: a dictionary
    :param boss_attack: a dictionary
    :precondition: character must be a dictionary created by the make_character function
    :precondition: boss must be a dictionary created by the make_boss function
    :precondition: boss_attack must be a dictionary equal to boss['Attack 1'] or boss['Attack 2']
    :postcondition: boss_attack is unchanged
    :postcondition: determine if the boss or the character has been defeated
    :return: True if both character and boss have current HP's greater than or equal to 1, and False otherwise.
    """
    combat_your_turn(character, boss)
    character_is_alive = character['Current HP'] > 0
    boss_is_alive = boss['Current HP'] > 0
    if boss_is_alive:
        combat_boss_turn(character, boss, boss_attack)
        character_is_alive *= (character['Current HP'] > 0)
    else:
        print("\nYou successfully defeated her!")
    return character_is_alive and boss_is_alive


def boss_intro_text(boss: dict) -> None:
    """
    Print the boss's introductory scene.

    :param boss: a dictionary
    :precondition: boss must be a dictionary from the make_boss function
    :postcondition: boss is unchanged
    :postcondition: prints the boss's intro scene
    """
    print("\nIs that?")
    time.sleep(1.5)
    print("IT IS...")
    time.sleep(1.5)
    print(f"\nIt's {boss['Name']}. \"HOW DARE YOU THINK YOU'RE WORTHY OF APPROACHING ME, YOU'RE GONNA REGRET THIS!\", "
          f"she shouts.")
    time.sleep(1)


def boss_combat(character: dict, boss: dict) -> bool:
    """
    Initialize a potential combat scene with with the final boss.

    :param character: a dictionary
    :param boss: a dictionary
    :precondition: character must be a dictionary created by the make_character function
    :precondition: boss must be a dictionary created by the make_boss function
    :postcondition: returns True if character has defeated boss and is still alive, and False otherwise
    :return: True if character has defeated boss and is still alive, and False otherwise
    """
    boss_intro_text(boss)
    print("\nDo you want to attack the final boss?")
    response = get_continue_combat_or_flee_choice()
    there_can_be_a_next_round = True
    boss_attack_generator = itertools.cycle([boss['Attack 1'], boss['Attack 2']])
    while response == "1" and there_can_be_a_next_round:
        current_attack = next(boss_attack_generator)
        there_can_be_a_next_round = boss_round(character, boss, current_attack)
        if there_can_be_a_next_round:
            print("\nDo you want to continue battling?")
            response = get_continue_combat_or_flee_choice()
    return (character['Current HP'] > 0) and (boss['Current HP'] < 1)


def flee_from_boss(character: dict, boss: dict) -> None:
    """
    Accept a 20% chance that the final boss hits your character if combat is left early.

    :param character: a dictionary
    :param boss: a dictionary
    :precondition: character must be a dictionary created by the make_character function
    :precondition: boss must be a dictionary created by the make_boss function
    :postcondition: boss is unchanged
    :postcondition: there will be a 20% chance that the opponent hits the character
    """
    if 1 <= random.randint(1, 100) <= 20:
        character['Current HP'] -= random.choice([boss['Attack 1']['Damage'], boss['Attack 2']['Damage']])
        character['Current HP'] *= character['Current HP'] > 0
        time.sleep(2)
        print(f"\nOuch! She got in one more hit before you could leave! You're down to {character['Current HP']}HP.")
    else:
        print("\nYou finally flee the scene...")


def boss_encounter(character: dict, boss: dict) -> None:
    """
    Drive the entire encounter with the final boss.

    :param character: a dictionary
    :param boss: a dictionary
    :precondition: character must be a dictionary created by the make_character function
    :precondition: boss must be a dictionary created by the make_boss function
    :postcondition: go through all user-requested rounds of combat with the boss or flee from the boss
    """
    character_is_victorious = boss_combat(character, boss)
    character_is_alive = character['Current HP'] > 0
    boss_is_alive = boss['Current HP'] > 0
    if character_is_victorious:
        print("\nYou've ruined Miss Prima's career... it's over for her!")
        print("\nBOSS DEFEATED!")
    elif character_is_alive and boss_is_alive:
        flee_from_boss(character, boss)


def game():
    """
    Set the main game function.
    """
    board = make_board(25, 25)
    game_exposition()
    character = make_character()
    character_is_alive = character['Current HP'] > 0
    boss = make_boss()
    boss_is_alive = boss['Current HP'] > 0
    selection = None
    while boss_is_alive and character_is_alive:
        display_map(board, character, boss)
        describe_current_location(board, character)
        selection = get_user_choice()
        if selection == "quit":
            unsuccessful_ending_text()
            return None
        valid_move = validate_move(board, character, selection)
        if valid_move:
            move_character(character, selection)
            if (character['X-position'], character['Y-position']) == (boss['X-position'], boss['Y-position']):
                boss_encounter(character, boss)
            else:
                there_is_a_foe = check_for_foes()
                if there_is_a_foe:
                    time.sleep(2)
                    foe = generate_foe(character)
                    foe_encounter(character, foe)
            character_is_alive *= character['Current HP'] > 0
            boss_is_alive *= boss['Current HP'] > 0
        else:
            print("\nSorry, you do not have access to that area!")

    if character_is_alive and selection != 'quit':
        successful_ending_text()
    elif not character_is_alive:
        print("\nYOU'VE RUN OUT OF HEALTH!")
        unsuccessful_ending_text()


def main():
    """
    Drive the program.
    """
    game()


if __name__ == "__main__":
    main()
