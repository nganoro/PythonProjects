class Animal:
    def walk(self):
        print("walk")

class dog(Animal):
    #pass basically avoid the empty method error
    pass

dog1 = dog()
dog1.walk()