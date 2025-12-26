import random

print("You are lost underground in a maze of tunnels.")
dangerTunnel = random.randint(1, 2)
# print("Dragon in tunnel", dangerTunnel)

tunnelChoice = 0

while tunnelChoice < 1 or tunnelChoice > 2:
    tunnelChoice = int(input("Choose tunnel 1 or tunnel 2: "))

    if tunnelChoice == dangerTunnel:
        print("You entered a tunnel with a dragon. Watch out! Stand your ground and fight?")
        fightDragon = input("Choose yes or no: ")

        if fightDragon == "yes":
            print("You chose to fight the dragon! You triumph and gain its treasure.")
        elif fightDragon == "no":
            print("Your cowardice provoked the Dragon. You are eaten.")
        else:
            print("You must choose yes or no.")
    else:
        print("You entered an empty tunnel. You are safe for now.")
