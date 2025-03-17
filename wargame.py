# With a correction already implemented: dont forget to initialize an instance of Class "War"

from vikingsClasses import Soldier, Viking, Saxon, War, Event, HealthBoostEvent
import random
import threading
import time
import os

def choose_warrior(army, player_name):
    while True:
        try:
            print(f"\n{player_name}, it's time to choose your warrior!")
            print("Here are your available warriors:")
            for i, warrior in enumerate(army):
                print(f"{i}: {type(warrior).__name__} with {warrior.health} health and {warrior.strength} strength")
            # Ask te user to enter warriors name. Maybe here is worth to implement selection with arrows as done in previos project
            choice = int(input(f"{player_name}, enter the number of the warrior you choose: "))
            if 0 <= choice < len(army):
                return army[choice]
            else:
                print("Invalid choice. The number must match a warrior in the list. Try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def clear_screen():
    # Clear the command window based on the operating system
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    player1 = input("Player 1, write your name (Vikingos' leader): ")
    player2 = input("Player 2, (Saxons leader): ")

    great_war = War()

    for i in range(1):
        great_war.addViking(Viking(f"Viking-{i+1}", 100, random.randint(50, 100)))
        great_war.addSaxon(Saxon(f"Saxon-{i+1}", 100, random.randint(50, 100)))

    round = 1
    while great_war.showStatus() == "Vikings and Saxons are still in the thick of battle.":
        print(f"\n--- Ronda {round} ---")
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
        viking = choose_warrior(great_war.vikingArmy, player1)
        saxon = choose_warrior(great_war.saxonArmy, player2)
        attack_damage = viking.attack()
        print(attack_damage)
        print(saxon.receiveDamage(attack_damage))
        if saxon.health <= 0:
            great_war.saxonArmy.remove(saxon)

        # Check if Saxons are dead
        if not great_war.saxonArmy:
            print(f"{player1} and the Vikings army win the war!")
            break

        # Player 2 turn (Saxons)
        print(f"\n{player2}'s turn")
        saxon = choose_warrior(great_war.saxonArmy, player2)
        viking = choose_warrior(great_war.vikingArmy, player1)
        attack_damage = saxon.attack()
        print(attack_damage)
        print(viking.receiveDamage(attack_damage))
        if viking.health <= 0:
            great_war.vikingArmy.remove(viking)

        # Check if Vikings are dead
        if not great_war.vikingArmy:
            print(f"{player2} and the Saxon army win the war!")
            break

        round += 1
        clear_screen()

if __name__ == "__main__":
    main()