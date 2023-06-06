from pkmn import Pokemon
from backend.classes.stats import Stats
from backend.classes.move import Move

def printStats(stats: Stats):
    print(f'\tHP: {stats.hp}')
    print(f'\tAttack: {stats.attack}')
    print(f'\tDefence: {stats.defence}')
    print(f'\tSpecial Attack: {stats.special_attack}')
    print(f'\tSpecial Defence: {stats.special_defence}')

def printMove(move:Move):
    print(f'\t\tName: {move.name}')
    print(f'\t\tType: {move.type}')
    print(f'\t\tPower: {move.power}')
    print(f'\t\tCategory: {move.category}')
    print(f'\t\tAccuracy: {move.accuracy}')


def printPkmn(pkmn:Pokemon):
    print(f'Pokemon: {pkmn.pokemon}')
    print(f'Nickname: {pkmn.nickname}')
    print(f'Trainer: {pkmn.trainer}')
    print(f'Dex Number: {pkmn.number}')
    print(f'Type: {", ".join(pkmn.types)}')
    print(f'Stats:')
    printStats(pkmn.stats)
    print(f'Moves:')
    for i, move in enumerate(pkmn.moves, 1):
        print(f"\tMove {i}:")
        printMove(move)
