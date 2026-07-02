class car:
    def __init__(self,model,speed):
        self.model=model
        self.speed=speed

    def start(self):
        print("the car model is: ",self.model)

    def acculrate(self):
        self.speed +=100
        print("the speed is: ",self.speed)

c1=car("Tesla",0)
c1.start()
c1.acculrate()                