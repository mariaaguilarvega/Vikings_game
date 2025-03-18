import random
import time
import os

from ui import UI
from vikingsClasses import Viking, Saxon, War, Event, HealthBoostEvent


def choose_warrior(army, player_name):
    """"Allow the player to select a warrior from their army"""
    message = f"{player_name}, it's time for you to choose a warrior!"
    options = [f"{type(warrior).__name__}: {warrior.name if warrior.name else ''} with {warrior.health} health and {warrior.strength} strength" for warrior in army]
    selected_index = UI.display_user_menu(options, message)
    return army[selected_index]



def main():

    soldier_number = UI.ask_for_int("Enter the number of soldiers: ")

    player1 = input("Player 1, write your name (Vikings' leader): ")
    player2 = input("Player 2, (Saxons' leader): ")

    great_war = War()

    for i in range(1, soldier_number + 1):
        great_war.addViking(Viking(f"Viking-{i}", 100, random.randint(50, 100)))
        great_war.addSaxon(Saxon(f"Saxon-{i}", 100, random.randint(50, 100)))

    round = 1
    while great_war.showStatus() == "Vikings and Saxons are still in the thick of battle.":
        print(f"\n--- Round {round} ---")
        time.sleep(1)
        print("\nActual state of both armies:")
        print(f"{player1}: {len(great_war.vikingArmy)} Vikings alive")
        print(f"{player2}: {len(great_war.saxonArmy)} Saxons alive")
        time.sleep(1)

        # Health boost event (randomly triggered)
        if random.random() < 0.7:  # 70% chance of triggering the event
            event = HealthBoostEvent(player1, player2, great_war.vikingArmy, great_war.saxonArmy)
            event.trigger()

        # Player 1 turn (Vikings)
        print(f"\n{player1}'s turn")
        time.sleep(1)
        viking = choose_warrior(great_war.vikingArmy, player1)
        saxon = choose_warrior(great_war.saxonArmy, player2)
        attack_damage = viking.attack()
        print(saxon.receiveDamage(attack_damage))
        time.sleep(1)
        if saxon.health <= 0:
            great_war.saxonArmy.remove(saxon)

        # Check if Saxons are dead
        if not great_war.saxonArmy:
            UI.display_message(f"{player1} and the Vikings army win the war!")
            break

        # Player 2 turn (Saxons)
        print(f"\n{player2}'s turn")
        time.sleep(1)
        saxon = choose_warrior(great_war.saxonArmy, player2)
        viking = choose_warrior(great_war.vikingArmy, player1)
        attack_damage = saxon.attack()
        print(viking.receiveDamage(attack_damage))
        time.sleep(1)
        if viking.health <= 0:
            great_war.vikingArmy.remove(viking)

        # Check if Vikings are dead
        if not great_war.vikingArmy:
            UI.display_message(f"{player2} and the Saxon army win the war!")
            break

        round += 1
        UI.clear()


if __name__ == "__main__":
    main()

