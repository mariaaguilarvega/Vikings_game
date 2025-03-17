import random
import threading




class Soldier():
    def __init__(self, health, strength):
        # your code here
        self.health = health
        self.strength = strength
    
    def attack(self):
        # your code here
        return self.strength

    def receiveDamage(self, damage):
        # your code here
        self.health -= damage
    

# Viking

class Viking(Soldier):
    def __init__(self, name, health, strength):
        # your code here
        super().__init__(health, strength)
        self.name = name

    def battleCry(self):
        # your code here
        return f"Odin Owns You All!"

    def receiveDamage(self, damage):
        # your code here
        self.health -= damage
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"

# Saxon

class Saxon(Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health, strength)
        self.name = name

    def receiveDamage(self, damage):
        # your code here
        self.health -= damage
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return f"A Saxon has died in combat"

# WAAAAAAAAAGH

class War():

    def __init__(self):
        # your code here
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, viking):
        self.vikingArmy.append(viking)
        
    
    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)
    
    def vikingAttack(self):
        # your code here
        if self.saxonArmy:
            saxon = random.choice(self.saxonArmy)
            viking = random.choice(self.vikingArmy)
            result = saxon.receiveDamage(viking.strength)      #or attack?
            if saxon.health <= 0:
                self.saxonArmy.remove(saxon)
            return result
    
    def saxonAttack(self):
        if self.vikingArmy:
            viking = random.choice(self.vikingArmy)
            saxon = random.choice(self.saxonArmy)
            result = viking.receiveDamage(saxon.strength)     #or attack?
            if viking.health <=0:
                self.vikingArmy.remove(viking)
            return result

    def showStatus(self):
        # your code here
        if not self.saxonArmy:
            return "Vikings have won the war of the century!"
        elif not self.vikingArmy:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."

    pass


class Event:
    def trigger(self):
        pass

class HealthBoostEvent(Event):
    def __init__(self, player1, player2, vikingArmy, saxonArmy):
        self.player1 = player1
        self.player2 = player2
        self.vikingArmy = vikingArmy
        self.saxonArmy = saxonArmy

    def trigger(self):
        print("\n!!! Special Event: Health Boost Challenge !!!")
        print(f"{self.player1}, press 'x' | {self.player2}, press 'm'")

        pressed_key = None
        key_received = False  # variable to check if key is received

        def wait_for_keypress():
            nonlocal pressed_key, key_received
            pressed_key = input("Press your key quickly: ").strip()
            key_received = True  #if a key is pressed then true

        # new thread to handle user input
        thread = threading.Thread(target=wait_for_keypress)
        thread.start()
        thread.join(timeout=5)  #Wait for 5 seconds to get the input

        if not key_received:
            # No one pressed the key
            print("No one pressed the key on time!")
            return  # Get out from the event

        # Handle pressed key to check if it comes from player1 or 2 and if it is valid
        if pressed_key == "x" and self.vikingArmy:
            chosen_viking = random.choice(self.vikingArmy)
            chosen_viking.health += 10
            print(f"{self.player1} wins the event! {chosen_viking.name} gains 10 health!")
        elif pressed_key == "m" and self.saxonArmy:
            chosen_saxon = random.choice(self.saxonArmy)
            chosen_saxon.health += 10
            print(f"{self.player2} wins the event! {chosen_saxon.name} gains 10 health!")
        else:
            print("Invalid key pressed or no warriors available!")