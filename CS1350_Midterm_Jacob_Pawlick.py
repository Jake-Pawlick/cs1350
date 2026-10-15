# Problem 1: Library Catalog

'''
class Library:
    def __init__(self):
        self.books = {}  # isbn -> {"title", "author", "copies"}

    def add_book(self, isbn, title, author, copies):
        if isbn in self.books:
            self.books[isbn]["copies"] += copies
        else:
            self.books[isbn] = {"title": title, "author": author, "copies": copies}

    def checkout(self, isbn):
        if isbn not in self.books or self.books[isbn]["copies"] <= 0:
            return False
        self.books[isbn]["copies"] -= 1
        return True

    def by_author(self, author):
        target = author.lower()
        return sorted(
            book["title"]
            for book in self.books.values()
            if book["author"].lower() == target
        )

    def inventory_value(self, prices):
        total = 0
        for isbn, price in prices.items():
            if isbn in self.books:
                total += self.books[isbn]["copies"] * price
        return total

    def low_stock(self, threshold):
        return {
            isbn: book["copies"]
            for isbn, book in self.books.items()
            if book["copies"] < threshold
        }
        
# Test cases
lib = Library()
lib.add_book("111", "Python Basics", "Jane Doe", 2)
lib.add_book("222", "Data Science", "John Roe", 1)
lib.add_book("333", "Advanced Python", "Jane Doe", 3)
lib.add_book("111", "Python Basics", "Jane Doe", 1)   # now 3 copies

print(lib.checkout("222"))                                            # True
print(lib.checkout("222"))                                            # False (none left)
print(lib.checkout("999"))                                            # False (unknown)
print(lib.by_author("jane doe"))                                      # ['Advanced Python', 'Python Basics']
print(lib.inventory_value({"111": 20.0, "333": 30.0, "999": 5.0}))    # 150.0
print(lib.low_stock(3))                                               # {'222': 0}
'''

# Problem 2: Conference Sessions with Sets

'''

class Session:
    def __init__(self, title):
        self.title = title
        self.attendees = set()

    def register(self, name):
        self.attendees.add(name)

    def unregister(self, name):
        self.attendees.discard(name)

    def attendee_count(self):
        return len(self.attendees)


def attended_all(sessions):
    if not sessions:
        return set()
    result = set(sessions[0].attendees)
    for s in sessions[1:]:
        result &= s.attendees
    return result


def attended_exactly_one(sessions):
    counts = {}
    for s in sessions:
        for name in s.attendees:
            counts[name] = counts.get(name, 0) + 1
    return {name for name, c in counts.items() if c == 1}


def no_shows(registered, sessions):
    attended = set()
    for s in sessions:
        attended |= s.attendees
    return set(registered) - attended


def summary(sessions):
    everyone = set()
    for s in sessions:
        print(f"{s.title}: {s.attendee_count()} attendees")
        everyone |= s.attendees
    print(f"Distinct attendees: {len(everyone)}")

# Test cases
keynote = Session("Keynote")
for p in ["Ana", "Ben", "Cruz", "Dee"]:
    keynote.register(p)

workshop = Session("Workshop")
for p in ["Ana", "Cruz", "Eli"]:
    workshop.register(p)

panel = Session("Panel")
for p in ["Ana", "Dee", "Eli", "Fay"]:
    panel.register(p)

workshop.unregister("Eli")
workshop.unregister("Zed")  # no error
print(workshop.attendee_count())  # 2

sessions = [keynote, workshop, panel]
print(attended_all(sessions))                                  # {'Ana'}
print(attended_exactly_one(sessions))                          # {'Ben', 'Eli', 'Fay'}
print(no_shows({"Ana", "Ben", "Fay", "Gus"}, sessions))        # {'Gus'}

summary(sessions)
# Keynote: 4 attendees
# Workshop: 2 attendees
# Panel: 4 attendees
# Distinct attendees: 6
'''

# Problem 4: Hotel Rooms with Inheritence

'''
from abc import ABC, abstractmethod

class Room(ABC):
    def __init__(self, number, nights):
        self.number = number
        self.nights = nights

    @abstractmethod
    def cost(self):
        pass

    def receipt(self):
        return f"Room {self.number} ({self.nights} nights): ${self.cost():.2f}"

    @staticmethod
    def validate_nights(nights):
        if nights <= 0:
            raise ValueError("Nights must be positive")


class StandardRoom(Room):
    def __init__(self, number, nights, rate=100.00):
        super().__init__(number, nights)
        self.rate = rate

    def cost(self):
        return self.nights * self.rate


class DeluxeRoom(StandardRoom):
    def __init__(self, number, nights, rate=100.00, breakfast=15.00):
        super().__init__(number, nights, rate)
        self.breakfast = breakfast

    def cost(self):
        return super().cost() + self.nights * self.breakfast


class Suite(Room):
    def __init__(self, number, nights, rate=250.00, discount_pct=0.10):
        super().__init__(number, nights)
        self.rate = rate
        self.discount_pct = discount_pct

    def cost(self):
        total = self.nights * self.rate
        if self.nights >= 3:
            total *= (1 - self.discount_pct)
        return total


def invoice(rooms):
    total = 0
    for room in rooms:
        print(room.receipt())
        total += room.cost()
    print(f"Total: ${total:.2f}")
    return total


# Test cases
rooms = [
    StandardRoom(101, 2),
    DeluxeRoom(205, 2, rate=120.00),
    Suite(901, 3),
]

total = invoice(rooms)
# Room 101 (2 nights): $200.00
# Room 205 (2 nights): $270.00
# Room 901 (3 nights): $675.00
# Total: $1145.00

try:
    Room.validate_nights(0)
except ValueError as e:
    print("Caught:", e)
# Caught: Nights must be positive
'''