import json

class Stats():
    def __init__(self, stats_info:json):
        self.hp = stats_info['hp']
        self.attack = stats_info['attack']
        self.defence = stats_info['defence']
        self.special_attack = stats_info['special attack']
        self.special_defence = stats_info['special defence']
        self.speed = stats_info['speed']