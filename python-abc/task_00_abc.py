#!/usr/bin/python3
"""
this is python program
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """
    this is abstract class
    """
    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    def sound(self):
        return "Bark"


class Cat(Animal):
    def sound(self):
        return "Meow"
