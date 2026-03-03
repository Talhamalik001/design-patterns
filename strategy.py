"""
Strategy Design Pattern aik design pattern hai
jo aik family of algorithms ko define karta hai,
unko alag classes me rakhta hai (encapsulate karta hai),
aur unko interchangeable bana deta hai.

Is pattern ka faida yeh hai ke hum algorithm ko
asani se change (swap) kar sakte hain bina client
code ko change kiye.
"""





class SortingStrategy:
    def sort(self , data):
        pass



class Bubblesort(SortingStrategy):

    def sort(self , data):
        print("sorting using bubble sort")
        return sorted(data)
    

class QuickSortStrategy(SortingStrategy):
    def sort(self , data):
        print("sorting using quick sort")
        return sorted(data, reverse=True)


class Sorter:

    def __init__(self , strategy : SortingStrategy):
        self.strategy = strategy

    def set_strategy(self , strategy : SortingStrategy):
        self.strategy = strategy

    def sort(self ,data):
        return self.strategy.sort(data)
    

data = [ 4 ,3 , 5 ,6,8 ,1 ,2 ,7]

sorter = Sorter(Bubblesort())
print(sorter.sort(data))

sorter.set_strategy(QuickSortStrategy())
print(sorter.sort(data))