class animal:
    def speak(self):
        print("animal speaks")

class dog(animal):
    def bark(self):
        print("dog bark")

d=dog()
d.speak()
d.bark()            