import json

class Move:
    def __init__(self, moveInfo:json):
        self.name = moveInfo['name']
        self.type = moveInfo['type']
        self.power = moveInfo['power']
        self.category = moveInfo['category']
        self.accuracy = moveInfo['accuracy']
