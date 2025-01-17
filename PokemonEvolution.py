#Aarav Moulik
#Period 1
#11/21/24
#Pokemon Evolution

#Global Variable
pokemon_level = 1
pokemon_name = "Piplup"


#Initialize
import random
        
#Functions
def train():
    global pokemon_level
    print("Try helping your pokemon do pushups!")
    print("Input up and down when prompted")
    z = input("Up: ")
    if z == "Up":
          print("Nice! Now input down to make your pokemon go down: ")
          y = input("Down: ")
          if y == "Down":
            pokemon_level = pokemon_level + int(1)
            print("Your pokemon is now level " + str(pokemon_level))
            print("----------------------------------------------------------")
            
def gym_battle():
    global pokemon_level
    print("Which gym would you like to battle: ")
    print("""
    1.Pewter City Gym
    2.Cerulean City Gym
    3.Vermillion City Gym
    4.Celadon City Gym""")
    option= int(input("1-5) Select option: "))
    if option == 1:
        print("You chose the Pewter City Gym!")
        print("You will be fighting Brock's Forretress!")
        b = input("Type Flip: ")
        if b == "Flip":
            outcome = random.randint(1,2)
            if outcome == 1:
                print("PIPLUP BEAT BROCK'S FORRETRESS!!")
                print(":DDDDDDD")
                pokemon_level = pokemon_level + int(1)
                print("Your Piplup leveled up!")
                print("It is now level " + str(pokemon_level))
                print("-------------------------------------------")
            else:
                print("Brock's Forretress beat your Piplup.")
                print(":(")
                print("Help your Piplup back up and get to training!")
                print("-------------------------------------------")
    if option == 2:
        print("You chose the Cerulean City Gym!")
        print("You will be fighting Misty's Satryu!")
        b = input("Type Flip: ")
        if b == "Flip":
            outcome = random.randint(1,2)
            if outcome == 1:
                print("PIPLUP BEAT MISTY'S STARYU!!")
                print(":DDDDDDD")
                pokemon_level = pokemon_level + int(1)
                print("Your Piplup leveled up!")
                print("It is now level " + str(pokemon_level))
                print("-------------------------------------------")
            else:
                print("Misty's Staryu beat your Piplup.")
                print(":(")
                print("Help your Piplup back up and get to training!")
                print("-------------------------------------------")
    if option == 3:
        print("You chose the Vermillion City Gym!")
        print("you will be fighting Lt. Surge's Voltorb!")
        b = input("Type Flip: ")
        if b == "Flip":
            outcome = random.randint(1,2)
            if outcome == 1:
                print("PIPLUP BEAT LT. SURGE'S VOLTORB!!")
                print(":DDDDDDD")
                pokemon_level = pokemon_level + int(1)
                print("Your Piplup leveled up!")
                print("It is now level " + str(pokemon_level))
                print("-------------------------------------------")  
            else:
                print("Lt. Surge's Voltorb beat your Piplup.")
                print(":(")
                print("Help your Piplup back up and get to training!")
                print("-------------------------------------------")
    if option == 4:
        print("You chose the Celadon City Gym!")
        print("You will be fighting Erika's Gloom!")
        b = input("Type Flip: ")
        if b == "Flip":
            outcome = random.randint(1,2)
            if outcome == 1:
                print("PIPLUP BEAT ERIKA'S GLOOM!!")
                print(":DDDDDDD")
                pokemon_level = pokemon_level + int(1)
                print("Your Piplup leveled up!")
                print("It is now level " + str(pokemon_level))
                print("-------------------------------------------")
            else:
                print("Erika's Gloom beat your Piplup.")
                print(":(")
                print("Help your Piplup back up and get to training!")
                print("-------------------------------------------")

def rest():
    print("")
    print("Your Piplup is resting.")
    print("Your piplup is in its first evolution!")
    print("Your" + pokemon_name +  "is currently level " + str(pokemon_level))
    print("----------------------------------------------------")
        


#Main

print("Welcome to Pokemon Evolution!")
print("Your " + str(pokemon_name) + " is waiting for you!")
while True: 
    print("Choose today's activity: ")
    print("""1.Train
    2.Gym Battle
    3.Rest(Display info)
    4.Quit""")
    option= int(input("1-5) Select option: "))
    if option == 1:
        train()
    if option == 2:
        gym_battle()
    if option == 3:
        rest()
    if option == 4:
        break
