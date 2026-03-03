# Subject Interface
class Subject:
    def register(self, observer):
        pass

    def unregister(self, observer):
        pass

    def notify(self):
        pass


# Observer Interface
class Observer:
    def update(self, message):
        pass


# Concrete Subject
class NewsPublisher(Subject):
    def __init__(self):
        self.observers = []
        self.news = ""

    def register(self, observer):
        self.observers.append(observer)

    def unregister(self, observer):
        self.observers.remove(observer)

    def notify(self):
        for observer in self.observers:
            observer.update(self.news)

    def set_news(self, news):
        self.news = news
        self.notify()


# Concrete Observer
class Subscriber(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, news):
        print(f"{self.name} received news: {news}")


# Client Code
publisher = NewsPublisher()

subscriber1 = Subscriber("Subscriber 1")
subscriber2 = Subscriber("Subscriber 2")

publisher.register(subscriber1)
publisher.register(subscriber2)

publisher.set_news("Breaking news: Design Patterns in Python!")