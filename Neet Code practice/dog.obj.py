class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age
        self.energy = 10

    def bark(self):
        if self.energy > 0:
            print(f"{self.name} is barking!")
            self.energy -= 1
        else:
            print(f"{self.name} is too tired to bark.")

    def eat(self, food_amount):
        print(f"{self.name} is eating {food_amount} units of food.")
        self.energy += food_amount // 2

    def sleep(self, hours):
        print(f"{self.name} is sleeping for {hours} hours.")
        self.energy += hours

    def play(self):
        if self.energy >= 3:
            print(f"{self.name} is playing!")
            self.energy -= 3
        else:
            print(f"{self.name} is too tired to play.")

    def get_info(self):
        print(f"Name: {self.name}, Breed: {self.breed}, Age: {self.age}, Energy: {self.energy}")



terry = Dog("terry", "german shepard", 2)
terry.get_info()

for i in range(5):
    terry.bark()

for i in range(2):
    terry.eat(1)

terry.get_info

for i in range(3):
    terry.play()

for i in range(5):
    terry.sleep(5)

for i in range(3):
    terry.play()
    
terry.get_info()

