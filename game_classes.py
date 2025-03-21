import random
import time
import keyboard
import threading

from ui import UI


#
# Warrior
#
class Warrior():
    def __init__(self, name, health=None, strength=None):
        self.name = name
        self.health = health or 100
        self.strength = strength or random.randint(50, 100)

    def receive_damage(self, damage):
        self.health -= damage
        if self.health > 0:
            print(f"\n{self.name} has received {damage} points of damage")
            return False
        else:
            print(f"\n{self.name} has died in combat")
            return True


#
# Army
#
class Army():
    def __init__(self, player_name, army_name, warrior_list):
        self.player_name = player_name
        self.army_name = army_name
        self.warriors = []
        self.enlist_warriors(warrior_list)

    def enlist_warriors(self, warrior_list):
        for warrior_data in warrior_list:
            name = warrior_data["name"]
            health = warrior_data.get("health", None)
            strength = warrior_data.get("strength", None)
            new_warrior = Warrior(name, health, strength )
            self.warriors.append(new_warrior)

    def choose_warrior(self):
        message = f"{self.player_name}, it's time for you to choose a warrior!"
        options = [f"{warrior.name} with {warrior.health} health and {warrior.strength} strength" for warrior in self.warriors]
        selected_index = UI.display_user_menu(options, message)
        return self.warriors[selected_index]

    def attack(self):
        attacker = self.choose_warrior()
        return attacker.strength

    def defend(self, damage):
        defender = self.choose_warrior()
        has_died = defender.receive_damage(damage)
        if has_died:
            self.warriors.remove(defender)


#
# War
#
class War():
    def __init__(self, player_1_name, player_2_name, battle_data):
        self.army_1 = Army(player_1_name, battle_data["army_1"]["army_name"], battle_data["army_1"]["warrior_list"])
        self.army_2 = Army(player_2_name, battle_data["army_2"]["army_name"], battle_data["army_2"]["warrior_list"])
        self.battle_data = battle_data
        self.round = 1

    def start(self):
        UI.display_message(self.battle_data["intro_text"], "Let's go!")

        while True:
            UI.clear()
            print("\033[31m" + f"\n--- Round {self.round} ---" + "\033[0m")
            time.sleep(1)

            # Display the current state of the armies
            print("\nActual state of both armies:")
            print(f"- {self.army_1.army_name}: {len(self.army_1.warriors)} warriors alive")
            print(f"- {self.army_2.army_name}: {len(self.army_2.warriors)} warriors alive")
            time.sleep(1)

            # Health boost event (randomly triggered)
            if random.random() < 0.7:  # 70% chance of triggering the event
                event = HealthBoostEvent(self.army_1, self.army_2)
                event.trigger()


            # Player 1 turn
            self.play_turn(self.army_1, self.army_2)
            has_finished = self.check_winner()
            if has_finished:
                return

            # Player 2 turn
            self.play_turn(self.army_2, self.army_1)
            has_finished = self.check_winner()
            if has_finished:
                return

            # Increment the round number
            self.round += 1


    def play_turn(self, attacking_army, defending_army):
        print("\033[32m" + f"\n{attacking_army.player_name}'s turn" + "\033[0m")
        time.sleep(1)

        damage = attacking_army.attack()
        defending_army.defend(damage)
        time.sleep(1)


    def check_winner(self):
        if not self.army_2.warriors:
            UI.display_message(f"{self.army_1.army_name} have won the battle of the century!", "Game Over!")
            return 1
        elif not self.army_1.warriors:
            UI.display_message(f"{self.army_2.army_name} have won the battle of the century!", "Game Over!")
            return 2
        else:
            # print(f"{self.army_1.army_name} and {self.army_2.army_name} are still in the thick of battle.")
            return None
        


#
# HealthBoostEvent
#
class HealthBoostEvent():
    def __init__(self, army_1, army_2):
        self.army_1 = army_1
        self.army_2 = army_2

    def trigger(self):
        print("\033[1;37;41m" + "\n!!! Special Event: Health Boost Challenge !!!" + "\033[0m")
        print(f"{self.army_1.player_name}, press 'x' | {self.army_2.player_name}, press 'm'")

        winner = None
        exit_event = threading.Event()

        
        # Function to listen for key presses
        def listen_for_keypress():
            nonlocal winner
            while not exit_event.is_set():
                if keyboard.is_pressed('x'):
                    winner = 'x'
                    exit_event.set()
                    break
                elif keyboard.is_pressed('m'):
                    winner = 'm'
                    exit_event.set()
                    break

        # Start the key listening thread
        thread = threading.Thread(target=listen_for_keypress, daemon=True)
        thread.start()

        # Wait for 5 seconds, then stop listening if no key was pressed
        thread.join(timeout=5)
        exit_event.set()  # Ensure the thread stops after the timeout

        if not winner:
            print("No one pressed the key in time! The event is skipped.")
            return

        # Handle the key press result
        if winner == "x" and self.army_1.warriors:
            chosen_warrior = random.choice(self.army_1.warriors)
            chosen_warrior.health += 10
            print(f"{self.army_1.player_name} wins the event! {chosen_warrior.name} gains 10 health!")
        elif winner == "m" and self.army_2.warriors:
            chosen_warrior = random.choice(self.army_2.warriors)
            chosen_warrior.health += 10
            print(f"{self.army_2.player_name} wins the event! {chosen_warrior.name} gains 10 health!")
        else:
            print("Invalid key pressed or no warriors available!")
        
        time.sleep(1)

