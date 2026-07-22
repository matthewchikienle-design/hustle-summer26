
# ============================================================
# LAB 7  -  MY OWN ORDERING APP
# Week 7  -  Hack the Hood
# ============================================================
# Name: Matthew Le
#
# This is YOUR app. YOU write the code.
# Do the tickets IN ORDER from the Lab 7 sheet.
# Run this file after EVERY ticket to check your work.
#
# My store sells: Games
# ============================================================


# ============================================================
# DAY 1  -  BUILD YOUR ITEMS
# ============================================================

# TICKET 1: My item blueprint
#   A class for your item. Every item has a name and a price.
#   Write your class below.

class Games:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def add(self, item):
        self.items.append(item)

# TICKET 3: The price guard
#   Add a set_price method INSIDE your class above.
#   It should say no to a price below zero.
#   BREAK ON PURPOSE: after you build it, try item1.set_price(-5)
#   PREDICT what happens: Well based off what I read, the "set_price" should make it so the user is unable to buy the games anywhere below 0
#   Paste the message you see here: "Price can't be below zero"
    def set_price(self, amount):
        if amount < 0:
           print("Price can't be below zero")
        else:
             self.price = amount 

# TICKET 4: A second kind of item
#   A new class that copies (inherits from) your first class.
#   Write it below.
class disc(Games):
    def deliver(self):
        print("Sending...")


# TICKET 5: Each item's own action
#   Give each class its own method (deliver, serve, play...).
#   Same method name, different message.
#   EXPLAIN why the same name can do two things: Because each class has it's own version

    def deliver(self):
        print("Downloading...")


# TICKET 2: Make your real items
#   Make 2 or 3 real items with YOUR OWN names and prices.
#   PREDICT what print(item1.name) shows: I predict it will print out the set item in that variable so like item1 would be elden ring

item1 = disc("Elden Ring", 60)
item2 = Games(" Minecraft ", 30)


# ============================================================
# DAY 2  -  BUILD YOUR STORE
# ============================================================

# TICKET 6: My cart
#   A class that holds items in a list and can check out.
#   Write your Cart class below.

class Cart:
    def __init__(self):
        self.items = []
    def add(self, item):
        self.items.append(item)



# TICKET 9: Checkout  (add this method INSIDE your Cart class)
#   Deliver every item and add up the total.
    def checkout(self):
      total = 0
      for item in self.items:
          item.deliver()
          total += item.price
      print("Total: $" + str(total))
    

# TICKET 7: My menu and my cart
#   A dictionary that gives each item a number, and one empty cart.

store = {
    "1": item1,
    "2": item2
}

cart = Cart()


# TICKET 8: Let customers shop
#   Use input() and a loop to keep adding picks until "done".
#   PREDICT what happens when you pick 1: it should choose the game in item 1 

while True:
    choice = input("Pick 1 , 2 , or 'done': ")

    if choice == "done":
        break

    if choice in store:
        cart.add(store[choice])
        print(store[choice].name + "added")
    else:
        print("This Choice does not exist!")


# TICKET 10: Test the whole app
#   Run it start to finish. PREDICT the full output first,
#   then check it against what really prints.

cart.checkout()

# ============================================================
# CHALLENGE: add a THIRD kind of item, or your own feature!
# ============================================================
