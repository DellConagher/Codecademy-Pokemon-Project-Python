import math

poketypes = {
        "Grass" : {"Grass" : 0.5, "Fire" : 0.5, "Water" : 2},
        "Fire" : {"Grass" : 2, "Fire" : 0.5, "Water" : 0.5},
        "Water" : {"Grass" : 0.5, "Fire" : 2, "Water" : 0.5}        
        }



class Pokemon:
    def __init__(self, name, level, type):
        self.name = name
        self.level = level
        if level > 100:
            self.level = 100
        self.max_health = level * 5
        self.health = self.max_health
        self.type = type
        self.faint_status = False

    def __str__(self):
        return f"{self.name}, {self.level}, {self.type}"

    def print_stats(self):
        print(f"Name: {self.name}, Level: {self.level}, Max Health: {self.max_health}, Current Health: {self.health}.")

    def faint(self):
        if self.health <= 0:
            self.faint_status = True
            print(f"{self.name} has fainted!")
        else:
            self.faint_status = False
            print("Has health.")    #testing purposes only
    
    def lose_health(self, health_lost):
        health_remaining = self.health - health_lost
        self.health = health_remaining
        print(f"{self.name} lost {health_lost} health!  {self.name} has {self.health} health remaining.")
        if self.health <= 0:
            self.health = 0
            self.faint()
    
    def gain_health(self, health_gained):
        if self.health + health_gained > self.max_health:
            self.health = self.max_health
        else:
            self.health += health_gained
        print(f"{self.name} gained {health_gained}. {self.name} now has {self.health} health")

    def revive(self):
        if self.faint_status == True:
            self.health = self.max_health / 2
            self.faint_status = False
            print(f"{self.name} has been revived and has {self.health} health!")
        else:
            print("Can't use that here.")

    def attack(self, other):
        multiplier = poketypes[self.type][other.type]
        attack = math.floor(self.level * multiplier)
        other.health -= attack
        print(f"{self.name} attacked {other.name} for {attack} damage! {other.name} has {other.health} health remaining.")
        if multiplier == 0.5:
            print("It's not very effective.")
        elif multiplier == 2:
            print("It's super effective!")

class GrassType(Pokemon):
    def __init__(self, name, level):
        super().__init__(name, level, "Grass")

class FireType(Pokemon):
    def __init__(self, name, level):
        super().__init__(name, level, "Fire")

class WaterType(Pokemon):
    def __init__(self, name, level):
        super().__init__(name, level, "Water")

class Trainer:
    def __init__(self, name, poke_team, num_potions, num_revives):
        self.name = name
        self.poke_team = poke_team[:6] if len(poke_team) > 6 else poke_team
        self.current_poke = self.poke_team[0]
        self.num_potions = 3
        self.num_revives = 1

    def __repr__(self):
        print(f"{self.name} currently has the following pokemon:")
        for poke in self.poke_team:
            print(poke)
        return f"Current pokemon: {self.current_poke}"

    def attack(self, other):
        if self.current_poke.faint_status == False:
            self.current_poke.attack(other.current_poke)
        else:
            print(f"{self.current_poke.name} has fainted, choose another pokemon, {self.name}.")

    def use_potion(self):
        if self.num_potions > 0:
            print(f"{self.name} used a potion on {self.current_poke}.")
            self.current_poke.gain_health(20)
        else:
            print(f"{self.name} doesn't have any potions left.")

    def use_revive(self):
        if self.num_revives > 0:
            print(f"{self.name} used a revive on {self.current_poke}.")
            self.current_poke.revive()
        else:
            print(f"{self.name} doesn't have any revives left.")

    def switch_poke(self, num):
        if self.poke_team[num] == self.current_poke:
            print(f"{self.name} cannot switch to currently active pokemon.")
        elif self.poke_team[num].faint_status == False:
            print(f"{self.name} switched {self.current_poke} with {self.poke_team[num]}.")
            self.current_poke = self.poke_team[num]
        elif self.poke_team[num].faint_status == True:
            print(f"{self.poke_team[num]} has no health.  Choose another pokemon, {self.name}.")
        else:
            print("Invaild Action")


Bulbasaur = GrassType("Bulbasaur", 5)
Charmander = FireType("Charmander", 5)
Squirtle = WaterType("Squirtle", 5)

Red = Trainer("Red", [Bulbasaur, Charmander, Squirtle], 3, 1)

Blue = Trainer("Blue", [Squirtle, Charmander, Bulbasaur], 3, 1)

#print(Red)
#print(Blue)

Red.attack(Blue)
Blue.attack(Red)
Red.attack(Blue)
Blue.switch_poke(1)
Red.attack(Blue)