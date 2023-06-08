# Encapsulation 
class Human:
    player_count = 0

    def __init__(self, name, health):
        self.name = name
        self.health = health
        Human.player_count += 1

    # Abstraction
    def attack(self, other):
        print(f"{self.name} attacked {other.name}")
        pass

    def take_damage(self, damage):
        self.health -= damage

    def print_stats(self):
        print(f"Name : {self.name}")
        print(f"Health : {self.health}")

    @classmethod
    def print_player_count(cls):
        print(cls.player_count)

    def regenerate_health(self):
        pass

# Inheritance
class Warrior(Human):
    def __init__(self, name, health, strength):
        super().__init__(name, health)
        self.strength = strength

    # Polymorphism
    def attack(self, other):
        super().attack(other)
        damage = self.strength * 0.5
        other.take_damage(damage)


    @classmethod
    def print_player_count(cls):
        print("This is none of your business!")

# Inheritance
class Mage(Human):
    def __init__(self, name, health, magic):
        super().__init__(name, health)
        self.magic = magic

    # Polymorphism
    def attack(self, other):
        super().attack(other)
        damage = self.magic * 0.1
        other.take_damage(damage)

    def regenerate_health(self, health_potion):
        self.health += health_potion


# Inheritance
class Archer(Human):
    def __init__(self, name, health, accuracy):
        super().__init__(name, health)
        self.accuracy = accuracy

    # Polymorphism
    def attack(self, other):
        super().attack(other)
        damage = self.accuracy * 0.8
        other.take_damage(damage)




warrior_1 = Warrior("Warrior 1", 150,50)
warrior_2 = Warrior("Warrior 2", 120,30)
warrior_3 = Warrior("Warrior 3", 130,70)

mage_1 = Mage("Mage 1", 80, 100)
mage_2 = Mage("Mage 2", 50, 200)

archer_1 = Archer("Archer 1", 130, 100)

warrior_1.print_stats()
mage_1.attack(warrior_1)
warrior_1.print_stats()

game_over = False

Human.print_player_count()
Warrior.print_player_count()

# humans_list
# A list of 1000 Warriors and Mages and Archers
# [warrior, mage, warrior]
# for human in human_list:
# human.regenerate_health()
