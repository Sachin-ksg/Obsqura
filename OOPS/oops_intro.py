#It is a pgmng approach in which we organise our code using classes and objects.
#Real world ex:
#A CAR category has properties (Brand name, color, speed, model) and behaviours (start, stop, accelerate, brake)
#Each Car objects (different car brands Swift,XUV, Hyundai etc) under the category can have its own properties and behaviours.
#In real OOPs pgmng properties are represented using Attributes
#Behaviours are represented using Methods (functions inside OOPs class)
#Objects are instances of Class.
#Class is the blue print of Objects.
#Terms in OOPs- Class, Objetcs, Attributes, Methods
#Adv:1.Code resusability
#2.Code maintainability
#3.Encapsulating data and methods.
#4.Organising entire code scripts

class CarClass:
    color="Black"
    model="Electric"

#Methods
    def start(self): #self refers to the current object using which we invoked the method
        print("Engine Started")

    def stop(self,distance):
        self.distance=distance #instance variable is created, to use in other methods inside the class
        print(f"Car stopped at {distance}")

    def detail(self):
        print(f"The car started and stopped at {self.distance} kms")

car1=CarClass() #Creating objects
#print(color) #Cannont be access variables inside class directly
print(car1.color)
car2=CarClass()
print(car2.model)
car1.speed="100Kmph"
car2.speed="80Kmph"
print(car1.speed)
print(car2.speed)
car1.start()
car2.start()
car1.stop(10)
#car2.stop(20)
car1.detail()
car2.stop(50)
car2.detail()
#In this case the value 10 is reused inside detail method, this is possible because both stop and detail are invoked using same object(car1)





