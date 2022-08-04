# create an Animal class
# syntax class Name:

class Animal:

    # __init__ to declare class attributes
    def __init__(self): # self refers current class
        self.alive = True
        self.spine = True

    def sleep(self):
        return "8 hours sleep is advised.."

    def eat(self):
        return "eat if you like to stay alive... and eat healthy "

# create an object of the class before using it
cat = Animal() # ensure it's the name of the class not file

#print(cat.eat()) # abstracted how was eat created or what info is available


