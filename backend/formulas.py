# This file is used to contain all the formulas utilised within the program
import random

from pkmn import Pokemon
from backend.classes.move import Move
from backend.pkmn_type import typeMultiplier

# Return true if the user's pokemon goes first
def speedCalc(my_pkmn:Pokemon, op_pkmn:Pokemon) -> bool:
    return random.randrange(100) < (my_pkmn.stats.speed) / (my_pkmn.stats.speed + op_pkmn.stats.speed)

def attHits(move:Move) -> bool:
    return random.randrange(100) < move.accuracy

def attEffectiveness(move:Move, pkmn:Pokemon) -> float:
    eff_mult = 1
    for pkmn_type in pkmn.types:
        eff_mult *= typeMultiplier(move.type, pkmn_type)
    return eff_mult

def attPowerCalc(att_pkmn:Pokemon, def_pkmn:Pokemon, move:Move) -> int:

    pkmn_att_val = 0
    pkmn_def_val = 0
    if move.category.lower() == 'physical':
        pkmn_att_val = att_pkmn.stats.attack
        pkmn_def_val = def_pkmn.stats.defence
    else:
        pkmn_att_val = att_pkmn.stats.special_attack
        pkmn_def_val = att_pkmn.stats.special_defence

    type_bonus = 1
    for pkmn_type in att_pkmn.types:
        if pkmn_type.lower() == move.type.lower():
            type_bonus = 1.5

    eff_mult = attEffectiveness(move, def_pkmn)

    rand = random.randint(217, 255)

    # Power calculation from
    # https://www.math.miami.edu/~jam/azure/compendium/battdam.htm
    power = ((((((((2 * 50/5+2)*pkmn_att_val*move.power)/pkmn_def_val)/50)+2)*type_bonus)*eff_mult/10)*rand)/255

    return power
