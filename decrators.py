#iska use tab hota jab ham ne aik basic strucre banae ke bad usko enahnce karna ho ad mian 
class Coffee:
    def cost(self):
        return 5


# Decorator (Milk)
class MilkDecorator:
    def __init__(self, coffee):
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost() + 2


# Decorator (Sugar)
class SugarDecorator:
    def __init__(self, coffee):
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost() + 1


# Client Code
coffee = Coffee()
print(f"Basic Coffee: ${coffee.cost()}")

milk_coffee = MilkDecorator(coffee)
print(f"Coffee with Milk: ${milk_coffee.cost()}")

milk_sugar_coffee = SugarDecorator(milk_coffee)
print(f"Coffee with Milk and Sugar: ${milk_sugar_coffee.cost()}")