import random

from backend.formulas import speedCalc, attHits, attPowerCalc, attEffectiveness
from backend.classes.move import Move
from pkmn import Pokemon



# Move selector for Player and CPU
def chooseMove(pkmn:Pokemon) -> Move:
    print('Choose one of your moves:')
    for i, move in enumerate(pkmn.moves, 1):
        print(f'{i}. {move.name} [{move.type}]')
        print(f'\tdmg: {move.power}, acc: {move.accuracy}, cat: {move.category}')
    i = input()
    if i not in ['1', '2', '3', '4']:
        print(f'\nINVALID INPUT: {i} please try again\n')
        return chooseMove(pkmn)
    else:
        return pkmn.moves[int(i) - 1]

def randMove(pkmn:Pokemon) -> Move:
    return pkmn.moves[random.randint(0, 3)]



# Pokemon does attack
def attack(attacker:Pokemon, defender:Pokemon, move:Move):
    if attHits(move):
        print(f'{attacker.nickname} used {move.name}')
        defender.takeDmg(attPowerCalc(attacker, defender, move))
        mult = attEffectiveness(move, defender)
        if mult > 1:
            print('It\'s super effective!')
        elif mult == 0:
            print(f'It doesn\'t effect {defender.nickname}')
        elif mult < 1:
            print('It\'s not very effective...')
    else:
        print(f'{attacker.nickname}\'s attack missed')
    input()


def testGameOver(my_pkmn:Pokemon, op_pkmn:Pokemon):
    if op_pkmn.curr_hp <= 0:
        print('Congratulations - You Won')
        exit(0)
    elif my_pkmn.curr_hp <= 0:
        print('You Lost')
        exit(0)



def turn(my_pkmn:Pokemon, op_pkmn:Pokemon, my_move:Move, op_move:Move):
    if speedCalc(my_pkmn, op_pkmn):
        attack(my_pkmn, op_pkmn, my_move)
        testGameOver(my_pkmn, op_pkmn)
        attack(op_pkmn, my_pkmn, op_move)
        testGameOver(my_pkmn, op_pkmn)
    else:
        attack(op_pkmn, my_pkmn, op_move)
        testGameOver(my_pkmn, op_pkmn)
        attack(my_pkmn, op_pkmn, my_move)
        testGameOver(my_pkmn, op_pkmn)


def pkmnBattle(my_pkmn:Pokemon, op_pkmn:Pokemon):

    print(f'{my_pkmn.trainer}\'s {my_pkmn.nickname} vs. {op_pkmn.trainer}\'s {op_pkmn.nickname}')
    print()

    while not my_pkmn.curr_hp <= 0 and not op_pkmn.curr_hp <= 0:


        print(f'{my_pkmn.nickname} HP: {my_pkmn.curr_hp}')
        print(f'{op_pkmn.nickname} HP: {op_pkmn.curr_hp}')

        print()

        my_move = chooseMove(my_pkmn)
        op_move = randMove(op_pkmn)
        

        
        turn(my_pkmn, op_pkmn, my_move, op_move)

