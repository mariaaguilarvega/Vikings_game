import random
import time
import keyboard


#
# Soldier
#
class Soldier():
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    
    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.health -= damage
    

#
# Viking
#
class Viking(Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health, strength)
        self.name = name

    def battleCry(self):
        return f"Odin Owns You All!"

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"


#
# Saxon
#
class Saxon(Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health, strength)
        self.name = name

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return f"A Saxon has died in combat"


#
# War
#
class War():
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, viking):
        self.vikingArmy.append(viking)
        
    
    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)
    
    def vikingAttack(self):
        return self.armyAttack(self.vikingArmy, self.saxonArmy)

    def saxonAttack(self):
        return self.armyAttack(self.saxonArmy, self.vikingArmy)

    def armyAttack(self, attacking_army, defending_army):
        """
        implements a generic attack 
        (a random soldier from the attacking army attacks a random soldier from the defending army)
        """
        attacker = random.choice(attacking_army)
        defender = random.choice(defending_army)

        strength = attacker.attack()
        result = defender.receiveDamage(strength)

        if defender.health <= 0:
            defending_army.remove(defender)

        return result

    def showStatus(self):
        if not self.saxonArmy:
            return "Vikings have won the war of the century!"
        elif not self.vikingArmy:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."


#
# Event
#
class Event:
    def trigger(self):
        pass


#
# HealthBoostEvent
#
class HealthBoostEvent():

    def __init__(self, player1, player2, vikingArmy, saxonArmy):
        self.player1 = player1
        self.player2 = player2
        self.vikingArmy = vikingArmy
        self.saxonArmy = saxonArmy
    def trigger(self):
        print("\nSpecial Event: Health Boost Challenge !!!")
        print(f"{self.player1}, press 'x' | {self.player2}, press 'm'")

        start_time = time.time()

        while time.time() - start_time < 3:
            if keyboard.is_pressed('x') and self.vikingArmy:
                chosen_viking = random.choice(self.vikingArmy)
                chosen_viking.health += 10
                print(f"\n{self.player1} wins the event! {chosen_viking.name} gains 10 health!")
                time.sleep(3)
                return
            elif keyboard.is_pressed('m') and self.saxonArmy:
                chosen_saxon = random.choice(self.saxonArmy)
                chosen_saxon.health += 10
                print(f"\n{self.player2} wins the event! {chosen_saxon.name} gains 10 health!")
                time.sleep(3)
                return
            else:
                pass

        print("\nNo one pressed the key in time! The event is skipped.")
        time.sleep(3)
        return

