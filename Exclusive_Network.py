# Exclusive Network
# Demostrates logical operators conditions
# Joseph Griecci - 05/14/2011

print "\tExclusive Computer  Network"
print "\t\tMembers only!\n"

username = ""

while not username:
    username = raw_input("Username: ")

password = ""
while not password:
    password = raw_input("Password: ")

if username == "M.Dawson" and password == "secret":
    print "Hi, Mike."
    security = 5
elif username == "S.Meier" and password == "civilization":
    print "Hey, Sid."
    security = 3
elif username == "S.Miyamoto" and  password == "mariobros":
    print "What's up, Shigeru?"
    security = 3
elif username == "W.Wright" and passord == "thesims":
    print "How goes it, Will?"
    security = 3
elif username == "guest" or password == "guest":
    print "Welcome, guest."
    security = 1
else:
    print "Login failed.  You're not so exclusive.\n"

raw_input("\n\nPress the enter key to exit.")

    
