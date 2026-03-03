



"""
Factory design pattern is design pattern that
provides an interface for creating objects in a
superclass , but allows subclasses to alter the 
type of objects that will be created.
it is used when we want to create objects without exposing the creation logic to the client and refer to
the newly created object using a common interface. 
"""







class Car:

    def drive(self): 
        raise NotImplementedError("this method should be implemented by subclasses")
    

class sportsCar(Car):

    def drive(self):
        return "driving a sports car"
    
class SadanCar(Car):
    def drive(self):
        return "Driving a sedan car"
        


class CarFactory:
    @staticmethod
    def get_Car(car_type):
        if car_type =="sports":
            return sportsCar()
        elif car_type =="sadan":
            return SadanCar()
        else:
            raise ValueError("invalid car type")
        
if __name__ == "__main__":

    car1 = CarFactory.get_Car("sports")
    print(car1.drive())

    car2 = CarFactory.get_Car("sadan")
    print(car2.drive()) 


    try:
        car3 = CarFactory.get_Car("truck")  # Invalid type
    except Exception as e:
        print(e) 


print("/")
class Payment:
    def process_payment(self):
        raise NotImplementedError("This method should be overridden by subclasses")


# Concrete classes for different payment methods
class CreditCardPayment(Payment):
    def process_payment(self):
        return "Processing Credit Card payment"

class PayPalPayment(Payment):
    def process_payment(self):
        return "Processing PayPal payment"

class BitcoinPayment(Payment):
    def process_payment(self):
        return "Processing Bitcoin payment"


# Factory Class to create payment methods
class PaymentFactory:
    @staticmethod
    def create_payment(payment_type):
        if payment_type == "credit_card":
            return CreditCardPayment()
        elif payment_type == "paypal":
            return PayPalPayment()
        elif payment_type == "bitcoin":
            return BitcoinPayment()
        else:
            raise ValueError("Invalid payment type")


# Client Code
if __name__ == "__main__":
    payment1 = PaymentFactory.create_payment("credit_card")
    print(payment1.process_payment())  # Output: Processing Credit Card payment

    payment2 = PaymentFactory.create_payment("paypal")
    print(payment2.process_payment())  # Output: Processing PayPal payment

    payment3 = PaymentFactory.create_payment("bitcoin")
    print(payment3.process_payment())  # Output: Processing Bitcoin payment

    try:
        payment4 = PaymentFactory.create_payment("bank_transfer")  # Invalid payment type
    except Exception as e:
        print(e)  # Output: Invalid payment type