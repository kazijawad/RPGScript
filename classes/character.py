import random

from .magic import Spell


class Character:
    def __init__(self, name, attack, defense, magic, items):
        self.name = name
        self.health = 100
        self.health_max = 100
        self.mana = 100
        self.mana_max = 100
        self.attack_low = attack - 5
        self.attack_high = attack + 5
        self.defense = defense
        self.magic = magic
        self.items = items
        self.actions = ['Attack', 'Magic', 'Items']

    def get_health(self):
        return self.health

    def get_max_health(self):
        return self.health_max

    def get_mana(self):
        return self.mana

    def get_max_mana(self):
        return self.mana_max

    def generate_damage(self):
        return random.randrange(self.attack_low, self.attack_high)

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0
        return self.health

    def heal(self, damage):
        self.health += damage
        if self.health > self.health_max:
            self.health = self.health_max

    def reduce_mana(self, cost):
        self.mana -= cost