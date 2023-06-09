TYPES = [
    'normal',
    'fire',
    'water',
    'grass',
    'electric',
    'ice',
    'fighting',
    'poison',
    'ground',
    'flying',
    'psychic',
    'bug',
    'rock',
    'ghost',
    'dragon',
    'dark',
    'steel',
    'fairy'
]

EFFECTIVENESS = [
    [  1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1, 0.5,   0,   1,   1, 0.5,   1], # Normal
    [  1, 0.5, 0.5,   2,   1,   2,   1,   1,   1,   1,   1,   2, 0.5,   1, 0.5,   1,   2,   1], # Fire
    [  1,   2, 0.5, 0.5,   1,   1,   1,   1,   2,   1,   1,   1,   2,   1, 0.5,   1,   1,   1], # Water
    [  1, 0.5,   2, 0.5,   1,   1,   1, 0.5,   2, 0.5,   1, 0.5,   2,   1, 0.5,   1, 0.5,   1], # Grass
    [  1,   1,   2, 0.5, 0.5,   1,   1,   1,   0,   2,   1,   1,   1,   1, 0.5,   1,   0,   1], # Electric
    [  1, 0.5, 0.5,   2,   1, 0.5,   1,   1,   2,   2,   1,   1,   1,   1,   2,   1, 0.5,   1], # Ice
    [  2,   1,   1,   1,   1,   2,   1, 0.5,   1, 0.5, 0.5, 0.5,   2,   0,   1,   2,   2, 0.5], # Fighting
    [  1,   1,   1,   2,   1,   1,   1, 0.5, 0.5,   1,   1,   1, 0.5, 0.5,   1,   1,   0,   2], # Poison
    [  1,   2,   1, 0.5,   2,   1,   1,   2,   1,   0,   1, 0.5,   2,   1,   1,   1,   2,   1], # Ground
    [  1,   1,   1,   2, 0.5,   1,   2,   1,   1,   1,   1,   2, 0.5,   1,   1,   1, 0.5,   1], # Flying
    [  1,   1,   1,   1,   1,   1,   2,   2,   1,   1, 0.5,   1,   1,   1,   1,   0, 0.5,   1], # Psychic
    [  1, 0.5,   1,   2,   1,   1, 0.5, 0.5,   1, 0.5,   2,   1,   1, 0.5,   1,   2, 0.5, 0.5], # Bug
    [  1,   2,   1,   1,   1,   2, 0.5,   1, 0.5,   2,   1,   2,   1,   1,   1,   1, 0.5,   1], # Rock
    [  0,   1,   1,   1,   1,   1,   1,   1,   1,   1,   2,   1,   1,   2,   1, 0.5,   1,   1], # Ghost
    [  1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   2,   1, 0.5,   0], # Dragon
    [  1,   1,   1,   1,   1,   1, 0.5,   1,   1,   1,   2,   1,   1,   2,   1, 0.5,   1, 0.5], # Dark
    [  1, 0.5, 0.5,   1, 0.5,   2,   1,   1,   1,   1,   1,   1,   2,   1,   1,   1, 0.5,   2], # Steel
    [  1, 0.5,   1,   1,   1,   1,   2, 0.5,   1,   1,   1,   1,   1,   1,   2,   2, 0.5,   1]  # Fairy
]

def typeEnum(pkmn_type:str) -> int:
    return TYPES.index(pkmn_type.lower())

def typeMultiplier(attack:str, defence:str) -> int:
    return EFFECTIVENESS[typeEnum(attack)][typeEnum(defence)]
