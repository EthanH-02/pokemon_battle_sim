import json

from backend.classes.stats import Stats
from backend.classes.move import Move

class Pokemon():

    # Allows the Pokemon to take damage
    def takeDmg(self, dmg:int):
        self.curr_hp = max(0, self.curr_hp - int(dmg))

    # Initialises the Pokemon class from a json file
    def __init__(self, pkmnInfo: json) -> None:

        # Pokemon can have at most 2 types and 4 moves
        assert(len(pkmnInfo['types']) <= 2)
        assert(len(pkmnInfo['moves']) <= 4)

        # Sets the elements from the JSON file
        self.pokemon = pkmnInfo['pokemon']
        self.nickname = pkmnInfo['nickname']
        self.trainer = pkmnInfo['trainer']
        self.types = pkmnInfo['types']
        self.number = pkmnInfo['dex num']

        # Needs to access a nested JSON element
        self.curr_hp = pkmnInfo['stats']['hp']

        # Call the constructor from stats
        self.stats = Stats(pkmnInfo['stats'])

        # Initialise a list of moves
        self.moves = []
        # For each move in the JSON file use the JSON to form a move object and append it in
        for move_json in pkmnInfo['moves']:
            move = Move(move_json)
            self.moves.append(move)
    
