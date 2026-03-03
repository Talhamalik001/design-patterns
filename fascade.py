"""
iska use tb hoa jab hane complex system ko simple interface ke zariye access krna ho
"""
# Subsystem 1 (TV)
class TV:
    def on(self):
        print("TV is ON")

    def off(self):
        print("TV is OFF")


# Subsystem 2 (DVD Player)
class DVDPlayer:
    def on(self):
        print("DVD Player is ON")

    def off(self):
        print("DVD Player is OFF")


# Facade (Home Theater)
class HomeTheaterFacade:
    def __init__(self):
        self.tv = TV()
        self.dvd = DVDPlayer()

    def watch_movie(self):
        self.tv.on()
        self.dvd.on()
        print("Movie is playing")

    def stop_movie(self):
        self.dvd.off()
        self.tv.off()


# Client Code
home_theater = HomeTheaterFacade()
home_theater.watch_movie()
home_theater.stop_movie()