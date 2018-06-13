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

# Game Initialization
players = [pc_harry, pc_ron, pc_hermione]
enemies = [ec_voldemort, ec_bellatrix, ec_severus]
running = True

def display_stats():
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

# def display_items():
#     print("\n")
#     print("╔═════════════════════════╗")
#     print("║          Items          ║")
#     print("╚═════════════════════════╝")
#     i = 1
#     for item in players[player].items:
#         print(str(i) + ". " + item.name)
#         i += 1

print("\n")
print("╔══════════════════════════════════════════════╗")
print("║            Dark Wizards Approach!            ║")
print("╚══════════════════════════════════════════════╝")

while running:
    display_stats()
    player = input("Choose a Character: ")

    # Check Player Choice
    if player.isdigit() == False:
        print("\nPlease respond with a number.")
        continue
    elif int(player) > 3 or int(player) < 1:
        print("\nPlease respond with a value between 1-3.")
        continue
    
    # Set the player choice as a parsible integer
    player = int(player) - 1
    players[player].display_actions()
    action = int(input("\nWhich action would you like to take? ")) - 1

    if action == 0:
        enemy = int(input("\nWhich enemy would you like to attack? ")) - 1
        damage = players[player].generate_damage()
        enemies[enemy].take_damage(damage)

        print("\n" + players[player].name.strip(), "attacks", enemies[enemy].name.strip(), "for", str(damage) + "hp.")
    elif action == 1:
        enemy = int(input("\nWhich enemy would you like to attack? ")) - 1
        players[player].display_spells()
        spell = int(input("\nWhich spell would you like to use? ")) - 1

        damage = players[player].magic[spell].generate_damage()
        enemies[enemy].take_damage(damage)

        print("\n" + players[player].name.strip(), "uses", players[player].magic[spell].name, "on", enemies[enemy].name.strip(), "for", str(damage) + "hp.")
    
    # Check Game Status
    for player in players:
        if player.health == 0:
            players.remove(player)
            print("\n" + player.name.strip() + "has died!")

    for enemy in enemies:
        if enemy.health == 0:
            enemies.remove(enemy)
            print("\n" + enemy.name.strip() + "has died!")
    
    if not players:
        print("\nAll your character have died. The Dark Wizards have won!")
        running = False
        continue
    elif not enemies:
        print("\nAll the enemies are dead. You have beat the Dark Wizards!")
        running = False
        continue
