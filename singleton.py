class singleton:

    instance = None

"""
singleton class is a design pattern that restricts 
the instantiation of a class to one object and provides
a global point of access to that object.
its mostly used when we want to have a single instance of
a class that can be accessed from anywhere in the code.
"""



def __init__(self ):
        if singleton.instance is None:
            singleton.instance = self
            self.value = 0
        else: 
            raise Exception("this isntance already exists")
        
def increament(self):
        self.value += 1
        
def get_value(self):
        return self.value
    
if __name__ == "__main__":

    s1 = singleton()
    s1.increament()


    print(s1.get_value()) # 1

