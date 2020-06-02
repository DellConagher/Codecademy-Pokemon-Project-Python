class Pokemon:
    def __init__(self, name, level, type, is_knocked_out=False):
        self.name = name
        self.level = level
        if level > 100:
            self.level = 100
        self.max_health = level * 5
        self.health = self.max_health
        self.type = type
        self.is_knocked_out = is_knocked_out

    def knock_out(self):
        if self.health <= 0:
            self.is_knocked_out = True
            print("{name} has been knocked out!".format(name=self.name))
        else:
            self.is_knocked_out = False
            print("not dead")                                                                           #remove this when finished testing
        

    def revive(self):
        if self.is_knocked_out == True:
            self.health = self.max_health / 2
            self.is_knocked_out = False
            print("{name} has been revived with 50% health!".format(name=self.name))
        else:
            print("{name} is not knocked out".format(name=self.name))



    def lose_health(self, health_lost):
        health_remaining = self.health - health_lost
        self.health = health_remaining
        lose_h = "{name} lost {health_lost} health. {name} now has {health} health".format(name=self.name, health=self.health, health_lost=health_lost)
        print(lose_h)
        if self.health <= 0:
            self.health = 0
            self.knock_out()
        


    def gain_health(self, health_gained):
        if self.health + health_gained > self.max_health:
            self.health = self.max_health
        else:
            self.health += health_gained

        gain_h = "{name} gained {health_gained}. {name} now has {health} health".format(name=self.name, health=self.health, health_gained=health_gained)
        print(gain_h)

    
    def attack(self, other_pokemon):
        types = ["grass", "fire", "water"]
        damage = 0
        if self.type is types[0] and other_pokemon.type is types[1]:
            damage = self.level / 2
            print(f"{self.name} attacks {other_pokemon.name} for {damage} damage!")
            print("It wasn't very effective.")
        elif self.type is types[0] and other_pokemon.type is types[2]:
            damage = self.level * 2
            print(f"{self.name} attacks {other_pokemon.name} for {damage} damage!")
            print("It was super effective!")
        elif self.type is types[1] and other_pokemon.type is types[0]:
            damage = self.level * 2
            print(f"{self.name} attacks {other_pokemon.name} for {damage} damage!")
            print("It was super effective!")
        elif self.type is types[1] and other_pokemon.type is types[2]:
            damage = self.level / 2
            print(f"{self.name} attacks {other_pokemon.name} for {damage} damage!")
            print("It wasn't very effective.")
        elif self.type is types[2] and other_pokemon.type is types[0]:
            damage = self.level / 2
            print(f"{self.name} attacks {other_pokemon.name} for {damage} damage!")
            print("It wasn't very effective.")
        elif self.type is types[2] and other_pokemon.type is types[1]:
            damage = self.level * 2
            print(f"{self.name} attacks {other_pokemon.name} for {damage} damage!")
            print("It was super effective!")
        else:
            damage = self.level
            print(f"{self.name} attacks {other_pokemon.name} for {damage} damage!")
        other_pokemon.lose_health(damage)
        

    def printStats(self):
        print(f"Name: {self.name}, Level: {self.level}, Max Health: {self.max_health}, Current Health: {self.health}.")

    def __repr__(self):
        return f"{self.name}"

    def test(self):
        print("Hello this is test")


class Trainer:
    def __init__(self, name, numPotions, numRevives, pokeTeam):
        self.name = name
        self.numPotions = numPotions
        self.numRevives = numRevives
        self.pokeTeam = pokeTeam
        self.current_pokemon = 0

    def usePotion(self):
        if self.numPotions > 0:
            print(f"{self.name} used a Potion!")
            self.pokeTeam[self.current_pokemon].gain_health(20)
        else:
            print(f"{self.name} doesn't have any potions left!")

    def useRevive(self):
        if self.numRevives > 0:
            print(f"{self.name} used a Revive!")
            self.pokeTeam[self.current_pokemon].revive()

    def attack_other_trainer(self, other_trainer):
        self.pokeTeam[self.current_pokemon].attack(other_trainer.pokeTeam[other_trainer.current_pokemon])



a = Pokemon("Bulbasaur", 5, "grass")
b = Pokemon("Charmander", 5, "fire")
c = Pokemon("Squirtle", 5, "water")


trainer_one = Trainer("Red", 3, 1, [a, b, c])
trainer_two = Trainer("Blue", 3, 1, [c, b, a])


trainer_one.attack_other_trainer(trainer_two)

trainer_one.attack_other_trainer(trainer_two)

trainer_one.attack_other_trainer(trainer_two)

trainer_one.attack_other_trainer(trainer_two)

trainer_one.attack_other_trainer(trainer_two)

trainer_two.useRevive()