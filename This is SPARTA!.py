import random
AK47DAM = random.randint(5,10)
M16DAM = random.randint(1,5)
playeronehealth = 100
playertwohealth = 100
Loop = True
print("Welcome to this shooting game\nYou will enter two names")
playerone=(input("Enter first name: "))
playertwo=(input("Enter second name: "))
gunone = (input("Pick your gun player one: "))
if gunone == 'M16':
    print("You chose a M16")
elif gunone == 'AK47':
    print("You chose an AK47")
guntwo=(input("Pick your gun player two: "))
if guntwo =='M16':
    print("You chose a M16")
elif guntwo =='AK47':
    print("You chose an AK47")
while Loop:
    AK47 = random.randint(1,4)
    M16 = random.randint(1,2)
    if playertwohealth <=0:
        Loop = False
    if playeronehealth <=0:
        Loop = False
    if gunone == 'AK47':
        if AK47 == 1:
            playertwohealth = playertwohealth - random.randint(5,10)
            print(playertwo, (playertwohealth))
    elif gunone == 'M16':
        if M16 == 1:
            playertwohealth = playertwohealth - random.randint(1,5)
            print(playertwo, (playertwohealth))
    if guntwo == 'AK47':
        if AK47 == 1:
            playeronehealth = playeronehealth - random.randint(5,10)
            print(playerone, (playeronehealth))
    elif guntwo == 'M16':
        if M16 == 1:
            playeronehealth = playeronehealth - random.randint(1,5)
            print(playerone, (playeronehealth))
    if playeronehealth <=0:
        print((playerone, "died!"))
    elif playertwohealth <=0:
        print((playertwo, "died!"))
       