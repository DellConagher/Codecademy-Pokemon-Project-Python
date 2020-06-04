class Pokemon:
    def __init__(self, name, level, type):
        self.name = name
        self.level = level
        if level > 100:
            self.level = 100
        self.max_health = level * 5
        self.health = self.max_health
        self.type = type
        self.is_knocked_out = False


    def knock_out(self):
        if self.health <= 0:
            self.is_knocked_out = True
            print(f"{self.name} has been knocked out!")
        else:
            self.is_knocked_out = False
            print("not knocked out")                                                                           #remove this when finished testing
        

    def revive(self):
        if self.is_knocked_out == True:
            self.health = self.max_health / 2
            self.is_knocked_out = False
            print(f"{self.name} has been revived and has {self.health} health!")
        else:
            print(f"{self.name} is not knocked out")



    def lose_health(self, health_lost):
        health_remaining = self.health - health_lost
        self.health = health_remaining
        if self.health <= 0:
            self.health = 0
        print(f"{self.name} lost {health_lost} health. {self.name} now has {self.health} health")
        if self.health <= 0:
            self.knock_out()        
        

    def gain_health(self, health_gained):
        if self.health + health_gained > self.max_health:
            self.health = self.max_health
        else:
            self.health += health_gained
        print(f"{self.name} gained {health_gained}. {self.name} now has {self.health} health")
        

    
    def attack(self, other_pokemon):
        types = ["grass", "fire", "water"]
        damage = 0
        if other_pokemon.health > 0:
            if (self.type is types[0] and other_pokemon.type is types[1]) or (self.type is types[1] and other_pokemon.type is types[2]) or (self.type is types[2] and other_pokemon.type is types[0]):
                damage = self.level / 2
                print(f"{self.name} attacks {other_pokemon.name} for {damage} damage!")
                print("It wasn't very effective.")
            elif (self.type is types[0] and other_pokemon.type is types[2]) or (self.type is types[1] and other_pokemon.type is types[0]) or (self.type is types[2] and other_pokemon.type is types[1]):
                damage = self.level * 2
                print(f"{self.name} attacks {other_pokemon.name} for {damage} damage!")
                print("It was super effective!")
            else:
                damage = self.level
                print(f"{self.name} attacks {other_pokemon.name} for {damage} damage!")
            other_pokemon.lose_health(damage)
        else:
            print("Can't attack a pokemon that is knocked out!")
        

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
            if self.pokeTeam[self.current_pokemon].health <= 0:
                print(f"{self.name} used a Revive!")
                self.pokeTeam[self.current_pokemon].revive()
            else:
                print("Can't use revive on pokemon that aren't knocked out.")
        else:
            print(f"{self.name} doesn't have any revives left!")

    def attack_other_trainer(self, other_trainer):
        self.pokeTeam[self.current_pokemon].attack(other_trainer.pokeTeam[other_trainer.current_pokemon])

    def switch_Pokemon(self):
        poke_choice = input("Choose the pokemon you would like to switch to: ")
        poke_choice = poke_choice.upper()
        no_health = "You can't send out a pokemon with no health."

        if poke_choice == "BULBASAUR":
            index = self.pokeTeam.index(a)
            if self.pokeTeam[index].health > 0:
                self.current_pokemon = index
                print("You sent out Bulbasaur!")
            else:
                print(no_health)
        elif poke_choice == "CHARMANDER":
            index = self.pokeTeam.index(b)
            if self.pokeTeam[index].health > 0:
                self.current_pokemon = index
                print("You sent out Charmander!")
            else:
                print(no_health)
        elif poke_choice == "SQUIRTLE":
            index = self.pokeTeam.index(c)
            if self.pokeTeam[index].health > 0:
                self.current_pokemon = index
                print("You sent out Squirtle!")
            else:
                print(no_health)
        else:
            print("That's not a vaild Pokemon.")

    def display_current_pokemon(self):
        print(f"Your current Pokemon is {self.pokeTeam[self.current_pokemon].name}.")




a = Pokemon("Bulbasaur", 5, "grass")
b = Pokemon("Charmander", 5, "fire")
c = Pokemon("Squirtle", 5, "water")


trainer_one = Trainer("Red", 3, 1, [a, b, c])
trainer_two = Trainer("Blue", 3, 1, [c, b, a])


trainer_two.switch_Pokemon()
trainer_two.display_current_pokemon()