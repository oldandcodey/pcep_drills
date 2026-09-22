# Ansi Color Setup

RESET = "\033[0m"
RED_BG = "\033[41m"
YELLOW_BG = "\033[43m"
GREEN_BG = "\033[42m"
WHITE = "\033[97m"
BLACK = "\033[30m"

print("Navarre Resilience Check Entry")
user = input("operator name: ")
print("Logged in as", user, sep=": ")
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

# Day 6 Dicts, Tuples and List

category = (
    "POWER",
    "WATER",
    "COMMS",
    "MED",
)

# Day 4 Menu Loop Build
# FIX: items must be a list; `item = ''` is a string and cannot collect rows
kit_items = []

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
        #items.append(input("Item to add: "))
        # Day 6 Create dict row and add to list 
        name = input("Add item name: ")
        qty = int(input("Add item qty: "))
        ok = input(f"Is {name} OK? (y/n): ").strip().lower() == "y"
        row = {"name":name,"qty":qty,"ok":ok}
        kit_items.append(row)
    elif done == 2:
        if not kit_items:
            print("No items yet.")
        else:
            for kit_item in kit_items:
                line = ""
                for key, value in kit_item.items():
                    line = line + key + ": " + str(value) + "  "
                print(line)
    elif done == 3:
        if not kit_items:
            print("No items to remove")
        else:
            toRemove = int(input("Enter item to remove (x): ")) - 1
            del kit_items[toRemove]
    elif done == 5:
        pass
    else:
        continue  # FIX: invalid choice — skip the rest and show the menu again

# print("NAVARRE RESILIENCE CHECK")
# print("Prepared by", user, "on", date)
# print(" | ".join(category))
#

header = f"""Navarre Resilience Check Report
Prepared by {user} on {date}
Categories: {" | ".join(category)}"""
print(header)

print(f"Fuel on hand: {gallons_on_hand}, minimum need: {gallons_required}, Shortfall: {gallon_shortfall}")
if kit_items:
    print("Kit items:")
    for kit_item in kit_items:
    #     line = ""
    #     for key, value in kit_item.items():
    #         line = line + key + ": " + str(value) + "  "
    #     print(line)
    #
        item_name = kit_item["name"].strip().title()
        item_qty = kit_item["qty"]
        item_ok = kit_item["ok"]
        print(f"{item_name}, {item_qty} is {item_ok}")
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

# # Day 5 Additions for extra Credit
recommended = ["5 Gallons Water","Handpump","Easy Prep Food","Can Opener","Butane Stove"]
print("Extra Credit")
print("the last 3 items in recommended : ", recommended[-3:])
b = sorted(recommended)
print(b)
b = recommended[:]
b.append("hurricane Snacks")
print(b)
