class Mammal:
    def walk(self):
        print("walk")


class Dog (Mammal):
    def bark(self):
        print("bark")

dog1 = Dog()
dog1.bark()

class Cat(Mammal):
    def purr(self):
        print('purr')

cat1 = Cat()
cat1.purr()