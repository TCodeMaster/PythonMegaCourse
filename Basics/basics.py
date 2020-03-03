class Dog():
    dogtype = "loving"

    def __init__(self, breed):
        self.breed = breed

myref = Dog("yes i have edited")
print(myref.breed)
print(Dog.dogtype)
