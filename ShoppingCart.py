class ShoppingCart(object):
  
   def __init__(self):
    self.total = 0
    self.items = {}
    
   def add_item(self, item_name, quantity, price):
    self.total += price*quantity
    self.items.update({item_name: quantity})
      
   def remove_item(self, item_name, quantity, price):
        if quantity >= self.items[item_name]:

            self.total -= (self.items[item_name] * price)
            self.items.pop(item_name, None)
        else:
            self.items[item_name] -= quantity
            self.total -= (quantity * price)
      
   def checkout(self,cash_paid):
        balance = 0
        if cash_paid < self.total:
          return "Cash paid not enough"
        balance = cash_paid - self.total
        return balance
    
class Shop(ShoppingCart):
  
  def __init__(self):
    self.quantity = 100
    
  def remove_item(self):
    self.quantity -= 1
