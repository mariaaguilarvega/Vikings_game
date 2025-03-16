# With a correction already implemented: dont forget to initialize an instance of Class "War"


from vikingsClasses import Soldier, Viking, Saxon, War
import random
import ascii_magic


def choose_warrior(army, player_name):
    while True:
            try:
                print(f"\n{player_name}, choose your warrior:")
                for i, warrior in enumerate(army):
                    print(f"{i}: {type(warrior).__name__} with {warrior.health} health and {warrior.strength} strength")
                choice = int(input("Enter the number of the warrior: "))
                if 0 <= choice < len(army):
                    return army[choice]
                else:
                    print("Invalid choice. Try again.")
            except ValueError:
                print("Please enter a valid number.")




def main():
    
    player1 = input("Player 1, write your name (Vikingos' leader): ")
    player2 = input("Player 2, (Saxons leader): ")

    great_war = War()

    for i in range(1):
        great_war.addViking(Viking(f"Viking-{i+1}", 100, random.randint(50, 100)))
        great_war.addSaxon(Saxon(f"Saxon-{i+1}",100, random.randint(50, 100)))



    round = 1
    while great_war.showStatus() == "Vikings and Saxons are still in the thick of battle.":
        print(f"\n--- Ronda {round} ---")
        print("\nActual state of both armies:")
        print(f"{player1}: {len(great_war.vikingArmy)} Vikings alive")
        print(f"{player2}: {len(great_war.saxonArmy)} Saxons alive")

        
        # Player 1 turn (Vikingos)
        print(f"\n{player1}'s turn")
        viking = choose_warrior(great_war.vikingArmy, player1)
        saxon = choose_warrior(great_war.saxonArmy, player2)
        attack_damage = viking.attack()
        print(attack_damage)
        print(saxon.receiveDamage(attack_damage))
        if saxon.health <= 0:
            great_war.saxonArmy.remove(saxon)

        #check if Saxons dead
        if not great_war.saxonArmy:
            print(f"{player1} and the Vikings army wins the war")
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

        # check if vikings are dead
        if not great_war.vikingArmy:
            print(f"{player2} and the Saxon army wins the war")
            break

        round += 1




if __name__ == "__main__":
    main()



    player1 = input("Player 1, write your name (Vikingos' leader): ")
    player2 = input("Player 2, (Saxons leader): ")

    great_war = War()

    for i in range(1):
        great_war.addViking(Viking(f"Viking-{i+1}", 100, random.randint(50, 100)))
        great_war.addSaxon(Saxon(f"Saxon-{i+1}",100, random.randint(50, 100)))



    round = 1
    while great_war.showStatus() == "Vikings and Saxons are still in the thick of battle.":
        print(f"\n--- Ronda {round} ---")
        print("\nActual state of both armies:")
        print(f"{player1}: {len(great_war.vikingArmy)} Vikings alive")
        print(f"{player2}: {len(great_war.saxonArmy)} Saxons alive")

        
        # Player 1 turn (Vikingos)
        print(f"\n{player1}'s turn")
        viking = choose_warrior(great_war.vikingArmy, player1)
        saxon = choose_warrior(great_war.saxonArmy, player2)
        attack_damage = viking.attack()
        print(attack_damage)
        print(saxon.receiveDamage(attack_damage))
        if saxon.health <= 0:
            great_war.saxonArmy.remove(saxon)

        #check if Saxons dead
        if not great_war.saxonArmy:
            print(f"{player1} and the Vikings army wins the war")
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

        # check if vikings are dead
        if not great_war.vikingArmy:
            print(f"{player2} and the Saxon army wins the war")
            break

        round += 1


