# Abstraction (Remote Control)
class RemoteControl:
    def __init__(self, device):
        self.device = device

    def turn_on(self):
        self.device.turn_on()

    def turn_off(self):
        self.device.turn_off()


# Implementor (Device Interface)
class Device:
    def turn_on(self):
        pass

    def turn_off(self):
        pass


# Concrete Implementor (TV)
class TV(Device):
    def turn_on(self):
        print("TV is now ON.")

    def turn_off(self):
        print("TV is now OFF.")


# Concrete Implementor (Fan)
class Fan(Device):
    def turn_on(self):
        print("Fan is now ON.")

    def turn_off(self):
        
        print("Fan is now OFF.")


# Client Code
tv = TV()
remote = RemoteControl(tv)
remote.turn_on()  # Output: TV is now ON.

fan = Fan()
remote.device = fan
remote.turn_on()  # Output: Fan is now ON.