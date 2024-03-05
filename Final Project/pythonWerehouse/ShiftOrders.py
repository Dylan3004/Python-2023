import random as rd
class ShiftOrders:


    typeOfItem = ["jacket", "coat", "junper", "socks", "trousers", "underwear", "bra", "hat", "gloves"]
    colorOfItem = ["black", "yellow", "gray", "orange", "pink", "blue", "jade", "ametist"]


    def __init__(self,numberOfOrders):
        self.numberOfOrders=numberOfOrders


    # Fuction that generates random order
    def Random_Generator(self):
        #array with numberOfOrders elements with random numbers between 1 and 100 with no duplicates
        typeOfItem = ["jacket","coat","junper","socks","trousers","underwear","bra","hat","gloves"]
        colorOfItem = ["black","yellow","gray","orange","pink","blue","jade","ametist"]
        OrdersArrayList = []
        OrdersArray = {}

        for i in range(self.numberOfOrders):
            for i in range(rd.randint(30, 45)):
                OrdersArray[i] = [colorOfItem[rd.randint(0, len(colorOfItem) - 1)],
                                  typeOfItem[rd.randint(0, len(typeOfItem) - 1)]]
            self.OrdersArray = OrdersArray
        return OrdersArray

    def print(self):
        print(self.numberOfOrders)
        print(self.Random_Generator())
