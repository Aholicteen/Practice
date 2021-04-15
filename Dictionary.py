dictionary1 = dict()
dictionary2 = {}

# Both of these are used to declare a dictionary

fruit_basket = {
    "mango": 40,
    "pawpaw": 20,
    "grape": 10,
    "watermelon": [1, 2, 4]
}

dictionary2["key1"] = "value1"
print(dictionary2)

# print("The original fruit basket:", fruit_basket)

# instantiating a dictionary and populating the items in the dictionary
# Dictionaries don't just hold primitive data types, they can hold a list, and also classes.
# A dictionary needs a key and the value the key references. 

# print(isinstance(fruit_basket, dict)) - This gives a true or false answer. 
# It checks if fruit-basket is an instance of a dictionary

mangoes = fruit_basket["mango"]
grapes = fruit_basket["grape"]
banana = fruit_basket.get("banana", None)
# banana = fruit_basket.get("banana", 0) -  it could be this too

# print("I have {} mangoes" .format(mangoes))
# print("I have %s grapes" % grapes)

# using the get function returns none/0 if the value isn't in the dictionary
# print("I have {} mangoes" .format(banana))


all_fruit_keys = fruit_basket.keys()
# print(fruit_basket.keys())
# .keys returns all the keys in the dictionary 

fruit_basket.update({"banana": 40})
# this updates the dictionary

# del fruit_basket["watermelon"]
fruit_basket.pop("watermelon")
# this takes out an item

# fruit_basket.clear()
# clears the fruit basket

# print(fruit_basket)
# print(fruit_basket.items())

# dictionary loop
for fruit, amount in fruit_basket.items():
    print("i have", amount, fruit + "(s) in the basket")

# 'fruit' and 'amount' is the name you're giving to the 'key' and 'value' respectively in the dictionary.
# it can be anything.
