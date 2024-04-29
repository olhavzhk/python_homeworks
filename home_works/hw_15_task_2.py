class Dog:
    age_factor = 7

    def __init__(self, age):
        self.age = age

    def human_age(self):
        return Dog.age_factor * self.age


molly = Dog(age=2)

print(molly.human_age())
