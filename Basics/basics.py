class Dog():
    dogtype = "loving"

    def __init__(self, breed):
        self.breed = breed

myref = Dog("jungly")
print(myref.breed)
print(Dog.dogtype)