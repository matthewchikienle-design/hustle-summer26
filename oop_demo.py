class Animal:
    def __init__(self, legs, fur, colors, lifespan, eyes, habitat, size,):
        self.legs = legs
        self.fur = fur
        self.colors = colors
        self.lifespan = lifespan
        self.eyes = eyes
        self. habitat = habitat
        self.size = size
    def move(self):
        if self.legs >=2:
            print("ZOOOOOOOOOM")
        elif self.legs == 1:
            print("The animal is hopping along")
        else:
            print("The animal did not move.")
dog = Animal(4, True, "brown", 15, 2, "house", "medium")

dog.move