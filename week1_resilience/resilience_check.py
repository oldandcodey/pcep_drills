print("Navarre Resilience Check Entry", end="\n")
name = input("operator name: ")
print("Logged in as",name, sep=": ")
date = input("todays date: ")
gallons_on_hand = input("how many gallons of gas do you have? ")
gallons_required = 5
gallon_shortfall = gallons_required - int(gallons_on_hand)

print("NAVARRE RESILIENCE CHECK", end="\n")
print("Prepared by", name, "on", date)
print("gallons of gas on hand ", gallons_on_hand, "Gallons Required: ", gallons_required, "Shortfall: ", gallon_shortfall)
