import os
import re
import random

from classes.character import Character
from classes.inventory import Item
from classes.magic import Spell


terminal_size = os.get_terminal_size().columns

# Black Magic
bm_avada = Spell("Avada Kedavra", 100, 100, "black")
bm_cruciatus = Spell("Cruciatus Curse", 70, 70, "black")
bm_knockback = Spell("Knockback Jinx", 10, 10, "black")
bm_oppugno = Spell("Oppugno Jinx", 15, 15, "black")
bm_sectumsempra = Spell("Sectumsempra", 60, 60, "black")
bm_stinging = Spell("Stinging Jinx", 20, 20, "black")
bm_toenail = Spell("Toenail-Growing Hex", 5, 5, "black")

# White Magic
wm_confundo = Spell("Confundo", 15, 15, "white")
wm_expelliarmus = Spell("Expelliarmus", 25, 25, "white")
wm_finestra = Spell("Finestra", 10, 10, "white")
wm_levicorpus = Spell("Levicorpus", 10, 10, "white")
wm_muffliato = Spell("Muffliato", 15, 15, "white")
wm_petrificus = Spell("Petrificus Totalus", 25, 25, "white")
wm_stupefy = Spell("Stupefy", 20, 20, "white")

# Healing Potions
pt_peace = Item("Draught of Peace", "heal", "The Draught of Peace provides personal comfort, calms anxiety and soothes agitation.", 50, 1)
pt_pepperup = Item("Pepperup Potion", "heal", "A Pepperup Potion is designed to improve health, relieve coughs and colds.", 30, 5)
pt_skele = Item("Skele-Gro", "heal", "Skele-Gro is a medicinal potion that can regrow missing or removed bones, though it tastes terrible and the process is very slow and extremely painful.", 60, 1)

# Attack Potions
pt_confusing = Item("Confusing Concoction", "attack", "A Confusing Concoction will cause the drinker to become confused, distracted and sick.", 15, 10)
pt_death = Item("Draught of Living Death", "attack", "When a person drinks the Draught of Living Death, they go into a deep sleep so strong that they appear to be dead, hence the name.", 40, 3)
pt_emerald = Item("Drink of Despair", "attack", "A mysterious potion which induces fear, delirium, and extreme thirst.", 40, 1)

# Player Characters
pc_harry    = Character("Harry Potter    ", 50, 50, [wm_expelliarmus, wm_levicorpus, wm_stupefy], [pt_confusing, pt_pepperup, pt_skele])
pc_ron      = Character("Hermione Granger", 30, 70, [wm_levicorpus, wm_petrificus], [pt_confusing, pt_pepperup])
pc_hermione = Character("Ron Weasley     ", 60, 40, [wm_confundo, wm_finestra, wm_levicorpus, wm_muffliato], [pt_confusing, pt_peace, pt_pepperup])

# Enemy Characters
ec_voldemort = Character("Lord Voldemort     ", 50, 50, [bm_avada, bm_cruciatus, bm_knockback, bm_oppugno, bm_stinging, bm_toenail], [pt_emerald])
ec_bellatrix = Character("Bellatrix Lestrange", 70, 30, [bm_cruciatus, bm_knockback, bm_oppugno, bm_stinging, bm_toenail], [pt_confusing])
ec_severus   = Character("Severus Snape      ", 40, 60, [bm_knockback, bm_oppugno, bm_sectumsempra, bm_stinging, bm_toenail], [pt_death, pt_emerald])

# Game Initialization
players = [pc_harry, pc_ron, pc_hermione]
enemies = [ec_voldemort, ec_bellatrix, ec_severus]
playerCount = 3
enemyCount = 3
running = True

def check_stats(stat):
    stat = str(stat)
    if len(stat) < 3 and len(stat) > 1:
        stat = stat + " "
    elif len(stat) < 2:
        stat = stat + "  "
    return stat

def display_stats():
    print("\n")
    print("╔═══════════════╗          ╔══════════════════╗          ╔════════════════╗")
    print("║     Names     ║          ║      Health      ║          ║      Mana      ║")
    print("╚═══════════════╝          ╚══════════════════╝          ╚════════════════╝")
    for player in players:
        print(player.name + "           " + check_stats(player.health) + "                           " + check_stats(player.mana))
    print("\n")
    for enemy in enemies:
        print(enemy.name + "        " + check_stats(enemy.health) + "                           " + check_stats(enemy.mana))
    print("\n")

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
    elif int(player) > playerCount or int(player) < 1:
        print("\nPlease respond with a value between 1-" + str(playerCount) + ".")
        continue

    # Set the player choice as a parsible integer
    player = int(player) - 1
    players[player].display_actions()

    # Ask for an Action
    while True:
        action = input("\nWhich action would you like to take? ")
        if action.isdigit() == False:
            print("\nPlease respond with a number.")
            continue
        elif int(action) > 3 or int(action) < 1:
            print("\nPlease respond with a value between 1-3.")
            continue
        break
    action = int(action) - 1

    if action == 0:
        # Check Proper Enemy Selection
        while True:
            enemy = input("\nWhich enemy would you like to attack? ")
            if enemy.isdigit() == False:
                print("\nPlease respond with a number.")
                continue
            elif int(enemy) > enemyCount or int(enemy) < 1:
                print("\nPlease respond with a value between 1-" + str(enemyCount) + ".")
                continue
            break
        enemy = int(enemy) - 1
        damage = players[player].generate_damage()
        enemies[enemy].take_damage(damage)

        print("\n" + players[player].name.strip(), "attacks", enemies[enemy].name.strip(), "for", str(damage) + "hp.")
    elif action == 1:
        if not players[player].mana:
            print("\nThat character has no mana!")
            continue

        enemy = int(input("\nWhich enemy would you like to attack? ")) - 1
        players[player].display_spells()
        spell = int(input("\nWhich spell would you like to use? ")) - 1

        players[player].reduce_mana(players[player].magic[spell].cost)
        damage = players[player].magic[spell].generate_damage()
        enemies[enemy].take_damage(damage)

        print("\n" + players[player].name.strip(), "uses", players[player].magic[spell].name, "on", enemies[enemy].name.strip(), "for", str(damage) + "hp.")
    elif action == 2:
        if not players[player].items:
            print("\nThis character has no items!")
            continue

        players[player].display_items()
        item = int(input("\nWhich item would you like to use? ")) - 1

        if players[player].items[item].type == "attack":
            enemy = int(input("\nWhich enemy would you like to attack? ")) - 1

            damage = players[player].items[item].property
            enemies[enemy].take_damage(damage)

            print("\n" + players[player].name.strip(), "uses", players[player].items[item].name, "on", enemies[enemy].name.strip(), "for", str(damage) + "hp.")
        elif players[player].items[item].type == "heal":
            target = int(input("\nWhich character would you like to heal? ")) - 1

            damage = players[player].items[item].property
            players[target].heal(damage)

            print("\n" + players[player].name.strip(), "heals", players[target].name.strip(), "with", players[player].items[item].name, "for", str(damage) + "hp.")

        # Check Item Amount
        players[player].items[item].amount -= 1
        if players[player].items[item].amount == 0:
            for item in players[player].items:
                players[player].items.remove(item)

    # Enemy Actions
    player = random.choice(players)
    enemy = random.choice(enemies)

    action = enemy.rand_action()
    if action == 0:
        damage = enemy.generate_damage()
        player.take_damage(damage)
        print("\n"+ enemy.name.strip(), "attacks", player.name.strip(), "for", str(damage) + "hp.")
    elif action == 1:
        if not enemy.mana:
            print("\nThe enemy attempted a spell, but had no mana!")
            continue

        spell = enemy.rand_spell()
        enemy.reduce_mana(enemy.magic[spell].cost)
        damage = enemy.magic[spell].generate_damage()
        player.take_damage(damage)

        print("\n" + enemy.name.strip(), "uses", enemy.magic[spell].name, "on", player.name.strip(), "for", str(damage) + "hp.")
    elif action == 2:
        if not enemy.items:
            print("\nThe enemy wanted to use an item, but they had no items left!")
            continue

        item = enemy.rand_item()
        damage = enemy.items[item].property
        player.take_damage(damage)
        print("\n" + enemy.name.strip(), "uses", enemy.items[item].name, "on", player.name.strip(), "for", str(damage) + "hp.")

    # Check Game Status
    for player in players:
        if player.health == 0:
            players.remove(player)
            playerCount -= 1
            print("\n" + player.name.strip() + " died!")

    for enemy in enemies:
        if enemy.health == 0:
            enemies.remove(enemy)
            enemyCount -= 1
            print("\n" + enemy.name.strip() + " died!")

    if not players:
        print("\nAll your character have died. The Dark Wizards have won!")
        running = False
    elif not enemies:
        print("\nAll the enemies are dead. You have beat the Dark Wizards!")
        running = False
