# Exercise 2.3 (Intermediate): Filter and Sort

words = ["kiwi", "fig", "banana", "plum", "apple"]


# TODO 1: Keep the words with more than 4 letters.
long_words = list(
    filter(lambda word: len(word) > 4, words)
)
print(long_words)  # ['banana', 'apple']


# TODO 2: Order the words by length.
by_length = sorted(
    words,
    key=lambda word: len(word)
)
print(by_length)  # ['fig', 'kiwi', 'plum', 'apple', 'banana']


# Exercise 2.4 (Intermediate): Make an Object Callable


class Adder:
    def __init__(self, amount):
        self.amount = amount

    def __call__(self, value):
        result = value + self.amount
        return result


add_ten = Adder(10)
print(add_ten(5))         # 15
print(callable(add_ten))  # True


# Exercise 3.1 (Beginner): Add the Missing Line


def count_up_to(n):
    """Yield 1, 2, 3, ... up to n."""
    i = 1
    while i <= n:
        yield i
        i += 1


print(list(count_up_to(3)))  # [1, 2, 3]
gen = count_up_to(2)
print(next(gen))  # 1
print(next(gen))  # 2


# Exercise 3.2 (Beginner): From List to Generator


squares = (x * x for x in range(5))
print(next(squares))   # 0
print(next(squares))   # 1
print(list(squares))   # [4, 9, 16] - only what is left


# Exercise 4.1 (Beginner): Any Number of Arguments


def total(*numbers):
    """Return the sum of all the arguments."""
    return sum(numbers)


print(total(1, 2, 3))  # 6
print(total())         # 0

prices = [5, 10, 15]
result = total(*prices)
print(result)          # 30


# Exercise 4.2 (Beginner): Unpack a Dictionary into a Call


def describe(name, age):
    return f"{name} is {age}"

person = {"name": "Ada", "age": 36}

result = describe(**person)
print(result)  # Ada is 36