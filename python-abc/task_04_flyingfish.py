#!/usr/bin/python3
"""
python programm
"""
class Fish:
    """
    this is a class
    """
    def swim(self):
        print("The fish is swimming")
    
    def habitat(self):
        print("The fish lives in water")

class Bird:
    def fly(self):
        print("The bird is flying")
    
    def habitat(self):
        print("The bird lives in the sky")

class FlyingFish(Fish, Bird):
    def fly(self):
        print("The flying fish is soaring!")
    
    def swim(self):
        print("The flying fish is swimming!")
    
    def habitat(self):
        print("The flying fish lives both in water and the sky!")


flying_fish = FlyingFish()


flying_fish.fly()
flying_fish.swim()
flying_fish.habitat()

print("\nMethod Resolution Order:")
print(FlyingFish.mro())