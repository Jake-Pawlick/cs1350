
# Unit 1.1 
# Beginner 
my_info = {"Name": "Jacob", "Age": 19, "Major": "Cybersecurity"}
# Intermediate 
menu = {"Hot Dog": 4, "Cheeseburger": 6, "Chicken Sandwhich": 6.50, "Vanilla Ice Cream": 5}
course_credits = {"CS1350": 3, "NET2300": 3, "IS2180": 3, "CJ2500": 3}
# Advanced 
weekly_temps = dict(Sunday=70, Monday=74, Tuesday=72, Wednesday=65, Thursday=68, Friday=78, Saturday=74)

# Unit 1.2
# Beginner
pet = {"name": "Buddy", "type": "dog", "age": 3}
print(pet["name"])
print(pet["age"])
# Intermediate
print(pet.get("color", "Unknown"))
grades = {"Alice": 85, "Bob": 45, "Charlie": 70}
print("Passed" if grades.get("Alice", 0) >= 60 else "Failed")
# Advanced 
products = {"laptop": 999.99, "mouse": 29.99, "keyboard": 79.99}
print(products.get("laptop", "Product not available"))
print(products.get("headphones", "Product not available"))

# Unit 1.3
# Beginner 
inventory = {}
inventory["apples"] = 10
inventory["bananas"] = 15
inventory["oranges"] = 20
# Intermediate 
scores = {"Team A": 45, "Team B": 38}
scores["Team B"] = 52
scores["Team C"] = 41
removed = scores.pop("Team A")
print(removed)
# Advanced 
cart = {}
print(cart)
cart["Laptop"] = 599.99
cart["USB Mouse"] = 6.99
cart["Pens"] = 4.99
cart["USB Mouse"] = 5.99
cart_removed_item = "Laptop"
removed_price = cart.pop(cart_removed_item)
print("Your removed item was:", cart_removed_item, removed_price)
print(cart)




# Unit 2.1
# Beginner
print("a) valid - strings are immutable and hashable")
print("b) invalid - lists are mutable and unhashable")
print("c) valid - integers are immutable and hashable")
print("d) valid - tuples are immutable and hashable")
print("e) invalid - dictionaries are mutable and unhashable")
print("f) valid - frozensets are immutable and hashable")
# Intermediate
locations = {(40.7, -74.0): "New York", (34.0, -118.2): "Los Angeles"}
print(locations)
data = {"a": 1, "b": 2, "a": 3, "b": 4}
print(data)
print(len(data))
print("Hash of my name:", hash("Jacob"))
print("Hash of 100:", hash(100))
# Advanced
game_scores = {
    ("Jacob", "Minecraft"): 9500,
    ("Alice", "Fortnite"): 8750,
    ("Bob", "Terraria"): 10200
}
print(game_scores[("Jacob", "Minecraft")])
import time
big_list = list(range(100000))
big_dict = {i: i for i in range(100000)}
start = time.time()
result = 99999 in big_list
list_time = time.time() - start
start = time.time()
result = 99999 in big_dict
dict_time = time.time() - start
print("List search time:", list_time)
print("Dictionary search time:", dict_time)
if list_time < dict_time:
    print("List is faster by", dict_time / list_time, "times")
else:
    print("Dictionary is faster by", list_time / dict_time, "times")
# Unit 2.2
# Beginner
temps = {"Monday": 72, "Tuesday": 75, "Wednesday": 68}
print(temps.keys())
print(temps.values())
print(len(temps))
# Intermediate
print("Highest temperature:", max(temps.values()))
print("Lowest temperature:", min(temps.values()))
if "Friday" in temps:
    print("Friday is in the dictionary.")
else:
    print("Friday is not in the dictionary.")
temps.setdefault("Thursday", 70)
print(temps)
keys_view = temps.keys()
print("Before adding Friday:", keys_view)
temps["Friday"] = 76
print("After adding Friday:", keys_view)
# Advanced
prices = {"laptop": 999, "phone": 699, "tablet": 449, "watch": 299}
total_value = sum(prices.values())
average_price = total_value / len(prices)
print("Total value:", total_value)
print("Average price:", average_price)
most_expensive = max(prices.items(), key=lambda item: item[1])
least_expensive = min(prices.items(), key=lambda item: item[1])
print("Most expensive:", most_expensive[0], most_expensive[1])
print("Least expensive:", least_expensive[0], least_expensive[1])
import sys
keys_view = prices.keys()
keys_list = list(prices.keys())
print("Memory used by keys view:", sys.getsizeof(keys_view), "bytes")
print("Memory used by keys list:", sys.getsizeof(keys_list), "bytes")
prices.update({
    "headphones": 149,
    "keyboard": 89,
    "mouse": 39
})
print("All products:")
for product, price in prices.items():
    print(product, price)

# Unit 2.3
# Beginner
colors = {"apple": "red", "banana": "yellow", "grape": "purple"}
for fruit, color in colors.items():
    print(f"The {fruit} is {color}")
print(list(colors.items()))
# Intermediate
prices = {"coffee": 4.50, "tea": 3.00, "juice": 5.25}
for item, price in prices.items():
    tax = price * 0.10
    total = price + tax
    print(f"{item}: ${price:.2f} + tax = ${total:.2f}")
count = 0
for item, price in prices.items():
    if price > 4.00:
        count += 1
print("Items costing more than $4.00:", count)
x = 10
y = 20
x, y = y, x
print("x:", x)
print("y:", y)
numbers = [1, 2, 3, 4, 5]
first, *middle, last = numbers
print("First:", first)
print("Middle:", middle)
print("Last:", last)
# Advanced
scores = {
    "Alice": 88,
    "Bob": 65,
    "Carol": 92,
    "Dave": 71,
    "Eve": 58
}
best_student, best_score = max(scores.items(), key=lambda item: item[1])
print("Highest scoring student:", best_student)
print("Highest score:", best_score)
passed = {}
failed = {}
for student, grade in scores.items():
    if grade >= 70:
        passed[student] = grade
    else:
        failed[student] = grade
print("Passed:", passed)
print("Failed:", failed)
average = sum(scores.values()) / len(scores)
deviations = {}
for student, grade in scores.items():
    deviations[student] = grade - average
print("Class average:", average)
print("Deviations:", deviations)
import time
big_dict = {i: i * 2 for i in range(50000)}
start = time.time()
for key, value in big_dict.items():
    result = key + value
items_time = time.time() - start
start = time.time()
for key in big_dict.keys():
    value = big_dict[key]
    result = key + value
keys_time = time.time() - start
print("items() time:", items_time)
print("keys() + lookup time:", keys_time)
if items_time < keys_time:
    print("items() is faster.")
    print("Difference:", keys_time - items_time, "seconds")
else:
    print("keys() + lookup is faster.")
    print("Difference:", items_time - keys_time, "seconds")