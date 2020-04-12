class InsufficientException(Exception):
    pass

class MobileInventory:
    def __init__(self, inventory = 'None'):
        if inventory == 'None':
            self.balance_inventory = {}
        elif type(inventory) != dict:
            raise TypeError("Input inventory must be a dictionary")
        else:
            self.balance_inventory = inventory
            for item in self.balance_inventory.items():
                if type(item[0]) != str:
                    raise ValueError("Mobile model name must be a string")
                if type(item[1]) != int or item[1]<=0:
                    raise ValueError("No. of mobiles must be a positive integer")

    def add_stock(self, new_stock):
        if type(new_stock) != dict:
            raise TypeError("Input stock must be a dictionary")
        else:
            for item in new_stock.items():
                if type(item[0]) != str:
                    raise ValueError("Mobile model name must be a string")
                if type(item[1]) != int or item[1]<=0:
                    raise ValueError("No. of mobiles must be a positive integer")
                if item[0] in self.balance_inventory.keys():
                    self.balance_inventory[item[0]] += item[1]
                else:
                    self.balance_inventory[item[0]] = item[1]

    def sell_stock(self, requested_stock):
        if type(requested_stock) != dict:
            raise TypeError("Requested stock must be a dictionary")
        else:
            for item in requested_stock.items():
                if type(item[0]) != str:
                    raise ValueError("Mobile model name must be a string")
                if type(item[1]) != int or item[1]<=0:
                    raise ValueError("No. of mobiles must be a positive integer")
                if item[0] not in self.balance_inventory.keys():
                    raise InsufficientException("No Stock. New Model Request")
                if item[1] > self.balance_inventory[item[0]]:
                    raise InsufficientException("Insufficient Stock")

                self.balance_inventory[item[0]] -= item[1]


m = MobileInventory({'iPhone Model X':100, 'Xiaomi Model Y': 1000, 'Nokia Model Z':25})
m.add_stock({'iPhone Model X':100, 'Xiaomi Model Z': 100, 'Nokia Model Z':25})
m.sell_stock({'iPhone Model X':100, 'Xiaomi Model Z': 25, 'Nokia Model Z':50})
print(m.balance_inventory)
