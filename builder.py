"""
Builder Design Pattern ka Use Case:

Jab aapko ek object ko multiple steps mein, 
alag-alag configurations ke saath create karna ho.

Jab object banate waqt aapko uske multiple parts 
ko set karna ho, jo ki ek hi waqt mein nahi set
 ho sakte.



"""

from abc import ABC , abstractmethod


class Car:
    def __init__(self):
        self.engine = None
        self.wheels = None
        self.color = None
        self.seats = None

    def __str__(self):
        return f"Car(engine={self.engine}, wheels={self.wheels}, color={self.color}, seats={self.seats})"


class CarBuilder(ABC):
    @abstractmethod
    def set_engine(self):
        pass

    @abstractmethod
    def set_wheels(self):
        pass

    @abstractmethod
    def set_color(self):
        pass

    @abstractmethod
    def set_seats(self):
        pass

    @abstractmethod
    def build(self):
        pass


class ConcreteCarBuilder(CarBuilder):
    def __init__(self):
        self.car = Car()  # Creates a new empty Car object

    def set_engine(self, engine):
        self.car.engine = engine  # Assign the value to self.car.engine

    def set_wheels(self, wheels):
        self.car.wheels = wheels  # Assign the value to self.car.wheels

    def set_color(self, color):
        self.car.color = color  # Assign the value to self.car.color
    
    def set_seats(self, seats):
        self.car.seats = seats  # Assign the value to self.car.seats

    def build(self):
        return self.car  # Return the final constructed car object

class CarDirector:
    def __init__(self , builder : CarBuilder):
        self.builder = builder

    def construct_sports_Car(self):
        self.builder.set_engine("V8 Engine")
        self.builder.set_wheels(4)
        self.builder.set_color("Red")
        self.builder.set_seats(2)

    def construct_family_car(self):
        self.builder.set_engine("V6 Engine")
        self.builder.set_wheels(6)
        self.builder.set_color("blue")
        self.builder.set_seats(5)

    
    
builder = ConcreteCarBuilder()
director = CarDirector(builder)
director.construct_sports_Car()
sports_car  = builder.build()

print(sports_car)

director.construct_family_car()
family_car = builder.build()

print(family_car)