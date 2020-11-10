class Animals:
    def __init__(self, legs=4, eyes=2):
        self.legs = legs
        self.eyes = eyes


class wild_animals(Animals):
    def place(self):
        print("Jungle")

class carnivores(wild_animals):
    def food(self):
        print("Meat")
    
        
class tiger(carnivores):
    def speak(self):
        print("Roar")
    def colour(self):
        print("Orange")
        
class lion(carnivores):
    def speak(self):
        print("Roar")
    def colour(self):
        print("Yellow")
        
class hyena(carnivores):
    def speak(self):
        print("laugh")
    def colour(self):
        print("Grey")
