# Superhero base class
class Superhero:
    def __init__(self, name, power, level):
        self.name = name
        self.power = power
        self.level = level

    def show_info(self):
        print(f"🦸 Superhero: {self.name}, Power: {self.power}, Level: {self.level}")

    def attack(self):
        print(f"{self.name} attacks with {self.power}!")

# Inherited class (encapsulation + polymorphism)
class FlyingHero(Superhero):
    def __init__(self, name, power, level, flight_speed):
        super().__init__(name, power, level)  # Call parent constructor
        self.__flight_speed = flight_speed  # encapsulated (private attribute)

    def attack(self):
        print(f"{self.name} attacks from the sky at speed {self.__flight_speed} km/h using {self.power}!")

# Usage
hero1 = Superhero("Flash", "Super Speed", 5)
hero2 = FlyingHero("Superman", "Laser Vision", 10, 800)

hero1.show_info()
hero1.attack()

hero2.show_info()
hero2.attack()
