from collections import defaultdict

class store:
    def __init__(self, items):
        self.items = items
        self.lenddict = defaultdict()
        self.buyList = defaultdict()

    def stock_available(self):
        for i in self.items.keys():
            print(f"{i} : {self.items[i][0] , self.items[i][1]}")

    def Buy(self, item_name, quantity):
        if (self.items[item_name][0]-quantity) < 0:
            print("Required quanity is not available")
        else:
            self.items[item_name][0] += -quantity
            self.buyList[item_name] = [
                quantity, quantity*self.items[item_name][1]]

    def sales(self):
        for i in self.buyList:
            print(f"{i} : {self.buyList[i][0] , self.buyList[i][1]}")

    def add(self, name, quantity, price):
        if name in self.items.keys():
            self.items[name][0] += quantity
            self.items[name][1] = price
        else:
            self.items[name] = [quantity, price]

    def lend(self, name, item_name, quantity):
        if name in self.lenddict.keys():
            print("Credit for Required stock cannot be Given as there is still a pending Due")   
        elif (self.items[item_name][0]-quantity) < 0:
            print("Required quanity is not available")
        else:
            self.items[item_name][0] += -quantity
            self.buyList[item_name] = [
                quantity, quantity*self.items[item_name][1]]
            self.lenddict[name] = [item_name, quantity,
                                   quantity*self.items[item_name][1]]

    def repay(self, name):
        if name in self.lenddict.keys():
            self.lenddict.pop(name)
        else:
            print("All dues Cleared")

    def lendlist(self):
        if len(self.lenddict.keys()) == 0:
            print("currentlty no pending dues:")
        else:
            for i in self.lenddict.keys():
                print(
                    f"{i}--> Brand:{self.lenddict[i][0]}, Quantity:{self.lenddict[i][1]} Amount:{self.lenddict[i][2]}")


database = store({"Hydrocodon": [928, 83], "paracetamol": [
                 2964, 7], "Losartan": [652, 76]})
