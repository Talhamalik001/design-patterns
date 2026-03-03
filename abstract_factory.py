from abc import ABC, abstractmethod

# Abstract Factory
class FurnitureFactory(ABC):
    @abstractmethod
    def create_chair(self):
        pass

    @abstractmethod
    def create_table(self):
        pass


# Concrete Factory 1: Wooden Furniture Factory
class WoodenFurnitureFactory(FurnitureFactory):
    def create_chair(self):
        return WoodenChair()  # Wooden chair object return karega

    def create_table(self):
        return WoodenTable()  # Wooden table object return karega


# Concrete Factory 2: Metal Furniture Factory
class MetalFurnitureFactory(FurnitureFactory):
    def create_chair(self):
        return MetalChair()  # Metal chair object return karega

    def create_table(self):
        return MetalTable()  # Metal table object return karega
    

# Abstract Product 1: Chair
class Chair(ABC):
    @abstractmethod
    def sit_on(self):
        pass


# Abstract Product 2: Table
class Table(ABC):
    @abstractmethod
    def place_items(self):
        pass


# Concrete Product 1: Wooden Chair
class WoodenChair(Chair):
    def sit_on(self):
        return "Sitting on a wooden chair."


# Concrete Product 2: Wooden Table
class WoodenTable(Table):
    def place_items(self):
        return "Placing items on a wooden table."


# Concrete Product 3: Metal Chair
class MetalChair(Chair):
    def sit_on(self):
        return "Sitting on a metal chair."


# Concrete Product 4: Metal Table
class MetalTable(Table):
    def place_items(self):
        return "Placing items on a metal table."
    

# Client Code: Abstract Factory ka use karte hue
def furniture_client(factory: FurnitureFactory):
    chair = factory.create_chair()
    table = factory.create_table()

    print(chair.sit_on())  # Chair par baithne ki action
    print(table.place_items())  # Table par items rakhne ka action


# Creating furniture from different factories
wooden_factory = WoodenFurnitureFactory()
furniture_client(wooden_factory)  # Output: Sitting on a wooden chair. Placing items on a wooden table.

metal_factory = MetalFurnitureFactory()
furniture_client(metal_factory)  # Output: Sitting on a metal chair. Placing items on a metal table.