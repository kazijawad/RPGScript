import os
import re

from classes.character import Character
from classes.inventory import Item
from classes.magic import Spell


terminal_size = os.get_terminal_size().columns

# Black Magic
bm_cruciatus = Spell("Cruciatus Curse", 70, 70, "black")
bm_stinging = Spell("Stinging Jinx", 20, 20, "black")
bm_oppugno = Spell("Oppugno Jinx", 15, 15, "black")
bm_knockback = Spell("Knockback Jinx", 10, 10, "black")
bm_toenail = Spell("Toenail-Growing Hex", 5, 5, "black")

# White Magic
wm_expelliarmus = Spell("Expelliarmus", 25, 25, "white")

# Potions
pt_emerald = Item("Drink of Despair", "potion", "A mysterious potion which induces fear, delirium, and extreme thirst.", 40)

# Player Characters
pc_harry    = Character("Harry Potter    ", 50, 50, [wm_expelliarmus], [])
pc_ron      = Character("Hermione Granger", 30, 70, [], [])
pc_hermione = Character("Ron Weasley     ", 60, 40, [], [])

# Enemy Characters
ec_voldemort = Character("Lord Voldemort     ", 50, 50, [bm_cruciatus, bm_stinging, bm_oppugno, bm_knockback, bm_toenail], [pt_emerald])
ec_bellatrix = Character("Bellatrix Lestrange", 70, 30, [bm_stinging, bm_oppugno, bm_knockback, bm_toenail], [])
ec_severus   = Character("Severus Snape      ", 40, 60, [bm_stinging, bm_oppugno, bm_knockback, bm_toenail], [pt_emerald])

players = [pc_harry, pc_ron, pc_hermione]
enemies = [ec_voldemort, ec_bellatrix, ec_severus]
running = True

def display_info():
    print("\n")
    print("╔═══════════════╗          ╔══════════════════╗          ╔════════════════╗")
    print("║     Names     ║          ║      Health      ║          ║      Mana      ║")
    print("╚═══════════════╝          ╚══════════════════╝          ╚════════════════╝")
    for player in players:
        print(player.name + "           " + str(player.health) + "                           " + str(player.mana))
    print("\n")
    for enemy in enemies:
        print(enemy.name + "        " + str(enemy.health) + "                           " + str(enemy.mana))
    print("\n")

print("\n")
print("╔══════════════════════════════════════════════╗")
print("║            Dark Wizards Approach!            ║")
print("╚══════════════════════════════════════════════╝")

while running:
    display_info()
    choice = input("What would you like to do? Attack|Magic|Item: ")
    choice_regex = re.compile("attack|magic|item")
    choice_result = re.search(choice_regex, choice)

    if choice_result == None:
        print("\n\nInvalid Choice!\n")
        running = False
        break

    if choice_result.group() == "attack":
        player_choice = int(input("\nWhich character should attack? ")) - 1
        enemy_choice = int(input("\nWhich enemy should be targetted? ")) - 1
        damage = players[player_choice].generate_damage()
        enemies[enemy_choice].take_damage(damage)
        print("\n" + players[player_choice].name.strip(), "attacks", enemies[enemy_choice].name.strip(), "for", str(damage) + "hp.")
        continue

    running = False
