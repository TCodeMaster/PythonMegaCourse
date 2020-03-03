class Dog():
    dogtype = "loving"

    def __init__(self, breed):
        self.breed = breed

myref = Dog("new code")
print(myref.breed)
print(Dog.dogtype)