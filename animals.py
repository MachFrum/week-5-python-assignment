class Animal:
    def move(self):
        pass  # Base method to be overridden

class Fish(Animal):
    def move(self):
        print("Swimming 🐟")

class Bird(Animal):
    def move(self):
        print("Flying 🦅")

class Snake(Animal):
    def move(self):
        print("Slithering 🐍")

animals = [Fish(), Bird(), Snake()]

for creature in animals:
    creature.move()