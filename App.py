
from Monsters import *
from player import *


class App:
    # print(f"The oldest cat, {get_oldest(cat1.name, cat2.name, cat3.name)} is {get_oldest(cat1.age, cat2.age, cat3.age)} years old.")
    for player in all_players:
        if player.gender == 'M':
            gender_call = 'his'
        else:
            gender_call = 'her'
        # print(f"{player.name} is {player.color} {gender_call} age is {player.age} {gender_call} attack power is {player.attack_power}.")


def player_vs_enemy():
    if cat2.hp - player1.attack_power <= 0:
        print(f"{cat2.name} has been killed by {player1.name}")
    else:
        print(f"{player1.name} has been killed by {cat2.name}")


player_move = input('What is your move? ')

if player_move == "kill":
    player1.kill()
elif player_move == "attack":
    player1.attack()
elif player_move == "shout":
    player1.shout()
elif player_move == "run":
    player1.run()
elif player_move == "suicide":
    player1.suicide()
elif player_move == "look for monster":
    cat1.walk()
elif player_move == "cry":
    print(f'I\'m am {player1.name} and I am not ashamed of my tears')
else:
    print('You can\'t do that')




