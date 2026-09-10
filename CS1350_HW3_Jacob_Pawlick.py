# Contact records: name -> dictionary of details
contact_book = {
    "Mom": {"phone": "555-1234", "category": "Family", "city": "Fort Wayne"},
    "Dad": {"phone": "555-4321", "category": "Family", "city": "Fort Wayne"},
    "Sister": {"phone": "555-7777", "category": "Family", "city": "Chicago"},
    "Best Friend": {"phone": "555-8888", "category": "Friend", "city": "Indianapolis"},
    "Roommate": {"phone": "555-3141", "category": "Friend", "city": "Fort Wayne"},
    "Boss": {"phone": "555-0000", "category": "Work", "city": "Chicago"},
    "Professor": {"phone": "555-2718", "category": "Work", "city": "Fort Wayne"},
    "Dentist": {"phone": "555-2222", "category": "Business", "city": "Indianapolis"},
}

# Call log: name -> {month -> minutes talked that month}
call_log = {
    "Mom": {"Jan": 120, "Feb": 95, "Mar": 140},
    "Dad": {"Jan": 45, "Feb": 60, "Mar": 30},
    "Sister": {"Jan": 80, "Mar": 70},
    "Best Friend": {"Jan": 200, "Feb": 180, "Mar": 220},
    "Roommate": {"Feb": 15, "Mar": 25},
    "Boss": {"Jan": 60, "Feb": 90, "Mar": 75},
    "Professor": {"Feb": 20, "Mar": 35},
    "Dentist": {"Jan": 10},
}

quick_contacts = {
    "Mom": "555-1234",
    "Dad": "555-5678",
    "Best Friend": "555-8888",
    "Pizza Place": "555-9999",
    "Work": "555-0000"
}

print("=== Phase 1: Quick Contacts ===")
print(quick_contacts)

print("--- Access and Modify ---")
print("Mom's number:", quick_contacts["Mom"])

quick_contacts["Dad"] = "555-4321"
quick_contacts["Dentist"] = "555-2222"

grandma = quick_contacts.get("Grandma")
if grandma is None:
    print("Looking up Grandma: Contact not found")
else:
    print("Looking up Grandma:", grandma)

print("Updated contacts:", quick_contacts)

print("--- Delete and Analyze ---")
del quick_contacts["Pizza Place"]

old_work = quick_contacts.pop("Work")
print("Removed work number:", old_work)

print("Contacts remaining:", len(quick_contacts))
print("Contact names:", list(quick_contacts.keys()))
print("Phone numbers:", list(quick_contacts.values()))


print("\n=== Phase 2: Contact Activity ===")

total_minutes = {}

for name, months in call_log.items():
    total = 0
    busiest_month = ""
    busiest_minutes = 0

    for month, minutes in months.items():
        total += minutes

        if minutes > busiest_minutes:
            busiest_minutes = minutes
            busiest_month = month

    month_count = len(months)
    average = total / month_count
    total_minutes[name] = total

    print(f"{name}: {month_count} month(s), {total} min total, "
          f"avg: {average:.2f}, busiest: {busiest_month} ({busiest_minutes})")


print("\n=== Phase 3: Aggregations ===")

month_stats = {}

for name, months in call_log.items():
    for month, minutes in months.items():
        if month not in month_stats:
            month_stats[month] = {
                "minutes": [],
                "total": 0,
                "avg": 0,
                "contacts": 0
            }

        month_stats[month]["minutes"].append(minutes)
        month_stats[month]["total"] += minutes
        month_stats[month]["contacts"] += 1

for month, stats in month_stats.items():
    stats["avg"] = stats["total"] / stats["contacts"]

print("Monthly summary (sorted by average, highest first):")

sorted_months = sorted(
    month_stats.items(),
    key=lambda item: item[1]["avg"],
    reverse=True
)

for month, stats in sorted_months:
    print(f"{month}: {stats['total']} min total, "
          f"{stats['avg']:.2f} avg ({stats['contacts']} contacts)")

minutes_by_category = {}
minutes_by_city = {}
contacts_per_city = {}

for name, details in contact_book.items():
    category = details["category"]
    city = details["city"]
    minutes = total_minutes[name]

    minutes_by_category[category] = minutes_by_category.get(category, 0) + minutes
    minutes_by_city[city] = minutes_by_city.get(city, 0) + minutes
    contacts_per_city[city] = contacts_per_city.get(city, 0) + 1

print("Minutes by category:", minutes_by_category)
print("Minutes by city:", minutes_by_city)
print("Contacts per city:", contacts_per_city)


print("\n=== Phase 4: Comprehensions ===")

phone_book = {name: details["phone"] for name, details in contact_book.items()}

local_contacts = {name: details["phone"] for name, details in contact_book.items() if details["city"] == "Fort Wayne"}

activity_level = {
    name: "Frequent" if minutes >= 200 else "Occasional"
    for name, minutes in total_minutes.items()
}

print("Phone book:", phone_book)
print("Local contacts (Fort Wayne):", local_contacts)
print("Activity level:", activity_level)


print("\n=== Phase 5: Tier Report ===")

# Returns the contact tier based on total minutes.
def get_tier(minutes):
    if minutes >= 400:
        return "Platinum"
    elif minutes >= 200:
        return "Gold"
    elif minutes >= 100:
        return "Silver"
    elif minutes >= 50:
        return "Bronze"
    else:
        return "Inactive"


for name, minutes in total_minutes.items():
    print(f"{name}: {minutes} min ({get_tier(minutes)})")


print("--- Tier Distribution ---")

tier_counts = {
    "Platinum": 0,
    "Gold": 0,
    "Silver": 0,
    "Bronze": 0,
    "Inactive": 0
}

for name, minutes in total_minutes.items():
    tier = get_tier(minutes)
    tier_counts[tier] += 1

for tier, count in tier_counts.items():
    print(f"{tier}: {count}")


print("--- Top and Bottom ---")

top_name = ""
top_minutes = 0

bottom_name = ""
bottom_minutes = float("inf")

for name, minutes in total_minutes.items():
    if minutes > top_minutes:
        top_minutes = minutes
        top_name = name

    if minutes < bottom_minutes:
        bottom_minutes = minutes
        bottom_name = name

grand_total = sum(total_minutes.values())
average_per_contact = grand_total / len(total_minutes)

print(f"Most contacted: {top_name} ({top_minutes} min)")
print(f"Least contacted: {bottom_name} ({bottom_minutes} min)")
print(f"Total minutes: {grand_total}")
print(f"Average per contact: {average_per_contact:.2f}")

print("--- Above Average Contacts ---")

for name, minutes in total_minutes.items():
    if minutes > average_per_contact:
        print(f"{name}: {minutes}")


print("\n=== Phase 6: Contact Hub Report ===")

print(f"{'Name':<12} {'Category':<10} {'City':<15} {'Minutes':>8} {'Tier':<10}")
print("-" * 59)

sorted_contacts = sorted(
    total_minutes.items(),
    key=lambda item: item[1],
    reverse=True
)

for name, total in sorted_contacts:
    category = contact_book[name]["category"]
    city = contact_book[name]["city"]
    tier = get_tier(total)

    print(f"{name:<12} {category:<10} {city:<15} {total:>8} {tier:<10}")

print("-" * 59)
print(f"{len(total_minutes)} contacts | {grand_total} total minutes | "
      f"{average_per_contact:.2f} average")