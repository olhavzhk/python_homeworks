class Animal:
    def talk(self):
        pass


class Dog(Animal):

    def talk(self):
        print("woof woof")


class Cat(Animal):
    def talk(self):
        print("meow")


def animal_talk(animal_instance):
    return animal_instance.talk()


kitty = Cat()
puppy = Dog()

kitty.talk()
puppy.talk()

animal_talk(kitty)
animal_talk(puppy)
