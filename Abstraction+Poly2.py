from abc import ABC, abstractmethod

class Animal(ABC):
    def move(self):
        pass

class Dog(Animal):
    def move(self):
        print("I can run fast and crawl")

class Human(Animal):
    def move(self):
        print("I can run and walk!")

class Snake(Animal):
    def move(self):
        print("I Can crawl!")

class Lion(Animal):
    print("I can leap and smash")

R = Dog()

R.move()

J = Human()

J.move()

E = Snake()

E.move()

L = Lion()

L.move()