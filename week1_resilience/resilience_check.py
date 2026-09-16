# Ansi Color Setup

RESET = "\033[0m"
RED_BG = "\033[41m"
YELLOW_BG = "\033[43m"
GREEN_BG = "\033[42m"
WHITE = "\033[97m"
BLACK = "\033[30m"

print("Navarre Resilience Check Entry")
name = input("operator name: ")
print("Logged in as", name, sep=": ")
date = input("todays date: ")
month = int(input("what is the month (m): "))
# FIX: convert to int at input so later math and checks are not str vs int
gallons_on_hand = int(input("how many gallons of gas do you have? "))
gallons_required = 5
gallon_shortfall = gallons_required - gallons_on_hand
# FIX: "Y" / " y " should count as yes
kit_complete = input("Is your kit complete? (y/n): ").strip().lower()
kit_ok = kit_complete == "y"
fuel_ok = gallons_on_hand >= gallons_required

# Day 4 Menu Loop Build
# FIX: items must be a list; `item = ''` is a string and cannot collect rows
items = []

# FIX: `while True` + `break` on quit. The old `done = 1` flag treated 0/4 as
# quit and never ran Add/List. Reprint the menu each pass.
while True:
    print("1. Add Item")
    print("2. List Item")
    print("3. Remove Item")
    print("4. Quit")
    print("5. Save")
    done = int(input("Enter choice: "))
    if done == 4:
        break
    elif done == 1:
        items.append(input("Item to add: "))
    elif done == 2:
        if not items:
            print("No items yet.")
        else:
            for item in items:
                print("-", item)
    elif done == 3:
        if not items:
            print("No items to remove")
        else:
            toRemove = int(input("Enter item to remove (x): ")) - 1
            del items[toRemove]
    else:
        continue  # FIX: invalid choice — skip the rest and show the menu again

print("NAVARRE RESILIENCE CHECK")
print("Prepared by", name, "on", date)

print("gallons of gas on hand ", gallons_on_hand, "Gallons Required: ", gallons_required, "Shortfall: ", gallon_shortfall)
if items:
    print("Kit items:")
    for item in items:
        print("-", item)

# FIX: Day 3 bands — both → green, either → yellow, neither → red
# FIX: `and` / `or` are boolean; `&` is bitwise
# FIX: typos seaoson → season, Its → It's
if kit_ok and fuel_ok:
    line = GREEN_BG + WHITE + "You are ready for hurricane season. Good Job" + RESET
elif kit_ok or fuel_ok:
    line = YELLOW_BG + BLACK + "You are almost ready for hurricane season. Finish the kit or get more gas" + RESET
else:
    line = RED_BG + BLACK + "You are not ready, get at it!" + RESET
    if month > 5 and month < 12:
        line = line + RED_BG + WHITE + " You better get on it! It's hurricane season" + RESET
print(line)

# Day 5 Additions for extra Credit
print("Extra Credit")
print("the last 3 items in items: ", items[-3:])
b = sorted(items)
print(b)
b = items[:]
print(b)

