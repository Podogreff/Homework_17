class Animal:

    def talk(self):
        return "Animals are speaking"

    def sleep(self):
        pass


class Cat(Animal):
    def talk(self):
        return "woof woof"

    def sleep(self):
        return "cat is sleeping"


class Dog(Animal):
    def talk(self):
        return "meow"

    def sleep(self):
        return "dog is sleeping"


cat = Cat()
dog = Dog()

print(cat.talk())
print(dog.talk())


def animal_sleep(animal):
    print(animal.sleep())


animal_sleep(cat)
animal_sleep(dog)

