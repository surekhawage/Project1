class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} the {self.breed} is barking!")

my_dog = Dog("Fido", "Golden Retriever")
my_dog.bark()