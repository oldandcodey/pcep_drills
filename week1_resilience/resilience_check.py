# Ansi Color Setup

RESET = "\033[0m"
RED_BG = "\033[41m"
YELLOW_BG = "\033[43m"
GREEN_BG = "\033[42m"
WHITE = "\033[97m"
BLACK = "\033[30m"

print("Navarre Resilience Check Entry", end="\n")
name = input("operator name: ")
print("Logged in as",name, sep=": ")
date = input("todays date: ")
month = int(input("what is the month (m): "))
gallons_on_hand = input("how many gallons of gas do you have? ")
gallons_required = 5
gallon_shortfall = gallons_required - int(gallons_on_hand)
kit_complete = input("Is your kit complete? (y/n): ")

# Day 4 Menu Loop Build
done = 1

print("1. Add Item")
print("2. List Item")
print("3. Quit")

while (done > 0) & (done < 3):
    done = int(input("Enter choice: "))

print("NAVARRE RESILIENCE CHECK", end="\n")
print("Prepared by", name, "on", date)

print("gallons of gas on hand ", gallons_on_hand, "Gallons Required: ", gallons_required, "Shortfall: ", gallon_shortfall)
if (kit_complete == "y") & (int(gallon_shortfall) < 1):
    line = GREEN_BG + WHITE + "You are ready for hurricane seaoson. Good Job" + RESET
elif (kit_complete == "y") & (int(gallons_on_hand) > 0):
    line = YELLOW_BG + BLACK + "You are almost ready for hurricane seaoson. Get some more gas"+ RESET
else:
    line = RED_BG + BLACK + "You are not ready, get at it!" + RESET
    if (month > 5) & (month < 12):
        line = line + RED_BG + WHITE + " You better get on it! Its hurricane season" + RESET
print(line)
