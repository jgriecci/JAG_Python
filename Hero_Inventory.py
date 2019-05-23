# Hero's Inventory 2.0
# Demostrate tuples
# Joseph Griecci - 05/14/2011

# create a tuple with some items and display with a for loop
inventory = ("sword",
             "armor",
             "shield",
             "healing potion")
print "Your items:"
for item in inventory:
    print item

raw_input("\nPress enter key to continue.\n")

# get the length of the tuple
print "You have", len(inventory), "items in you possession."

raw_input("\nPress the enter key to continue.\n")

#  test for membership with in
if "healing potion" in inventory:
    print "You will live to fight another day."

# display one item through an index
boolean = 0
while boolean != 1:
    number = raw_input("\nEnter the index number for an item in inventory: ")
    if number != "":
        index = int(number)
        print "At index", index, "is", inventory[index]
        boolean = 1

# display a slice
boolean = 0
while boolean != 1:
    number = raw_input("\nEnter the index number to begin a slice: ")
    if number != "":
        begin = int(number)
        boolean = 1

boolean = 0
while boolean != 1:
    number = raw_input("Enter the index number to end a slice: ")
    if number != "":
        end = int(number)
        boolean = 1
    
print "inventory[", begin, ":", end, "]\t\t",
print inventory[begin:end]

raw_input("\nPress the enter key to continue.")

