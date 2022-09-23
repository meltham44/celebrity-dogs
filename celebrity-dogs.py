import random
import time

def menu():
    print ('Type play to play game or type quit to quit game and press enter.')
    menuchoice = input()
    if menuchoice == 'play':
        start()
    elif menuchoice == 'quit':
        raise SystemExit
    elif menuchoice != 'play' or 'quit':
        print ('This is not an option.')
        menu()
        

def start():
    global playerlist
    global cpulist
    global global_cardID
    global NoofCards
    global doglist
    print('Please enter number of cards you would like in the pack.')
    print('Remember this needs to be between 4 and 30.')
    NoofCards = input()
    IntegerTest = NoofCards.isnumeric()
    if IntegerTest == True:
        NoofCards = int(NoofCards)
        if NoofCards >= 4 and NoofCards <= 30 and NoofCards != int and NoofCards %2==0:
          with open('dogs.txt','r') as doglist:
            doglist = doglist.read().splitlines()
            doglist = [line.split(",") for line in doglist]
            playerlist = NoofCards / 2
            cpulist = NoofCards / 2
            gameplay()
        else:
            print ('Incorrect value')
            start()
    else:
        print ('Incorrect value')
        start()

def gameplay():
    global playerlist
    global cpulist
    global global_cardID
    global NoofCards
    global doglist
    global PCategoryChoice
    global PExerciseValue
    global PIntelligenceValue
    global PFriendlinessValue
    global PDroolValue
    global CPUExerciseValue
    global CPUIntelligenceValue
    global CPUFriendlinessValue
    global CPUDroolValue

    CPUExerciseValue = random.randint(1,5)
    CPUIntelligenceValue = random.randint(1,100)
    CPUFriendlinessValue = random.randint(1,10)
    CPUDroolValue = random.randint(1,10)
    PExerciseValue = random.randint(1,5)
    PIntelligenceValue = random.randint(1,100)
    PFriendlinessValue = random.randint(1,10)
    PDroolValue = random.randint(1,10)
    
    print("------------Celebrity Dogs---------------")
    print("You have:",playerlist, "cards out of",NoofCards)
    time.sleep(1)
    print("Computer has:",cpulist, "cards out of",NoofCards)
    time.sleep(1)
    print("-----------------------------------------")
    print("Your dog is:")
    print(random.choice(doglist))
    time.sleep(1)
    print("Exercise:", PExerciseValue, "out of 5.")
    time.sleep(1)
    print("Intelligence:", PIntelligenceValue, "out of 100.")
    time.sleep(1)
    print("Friendliness:", PFriendlinessValue, "out of 10.")
    time.sleep(1)
    print("Drool:", PDroolValue, "out of 10.")
    print("Please enter the number of the category you would like to challenge.")
    print ("Enter 1 for exercise, 2 for intelligence, 3 for friendliness or 4 for drool.")
    choice()
    
def choice():
    global PCategoryChoice
    global PExerciseValue
    global PIntelligenceValue
    global PFriendlinessValue
    global PDroolValue
    global CPUExerciseValue
    global CPUIntelligenceValue
    global CPUFriendlinessValue
    global CPUDroolValue
    global cpulist
    global playerlist

    PCategoryChoice = input()
    IntegerTest = PCategoryChoice.isnumeric()
    if IntegerTest == True:
        PCategoryChoice = int(PCategoryChoice)
        if PCategoryChoice == 1 or PCategoryChoice == 2 or PCategoryChoice == 3 or PCategoryChoice == 4: 
            print("Computer's dog is:")
            print(random.choice(doglist))
            time.sleep(1)
            print("Exercise:", CPUExerciseValue, "out of 5.")
            time.sleep(1)
            print("Intelligence:", CPUIntelligenceValue, "out of 100.")
            time.sleep(1)
            print("Friendliness:", CPUFriendlinessValue, "out of 10.")
            time.sleep(1)
            print("Drool:", CPUDroolValue, "out of 10.")
            playerchoice()
        if PCategoryChoice != 1 or PCategoryChoice != 2 or PCategoryChoice != 3 or PCategoryChoice != 4:
            print("Please enter a valid choice")
            choice()
    else:
        print("Please enter a numerical value")
        choice()

def playerchoice():
    global PCategoryChoice
    global PExerciseValue
    global PIntelligenceValue
    global PFriendlinessValue
    global PDroolValue
    global CPUExerciseValue
    global CPUIntelligenceValue
    global CPUFriendlinessValue
    global CPUDroolValue
    global cpulist
    global playerlist
    
    if PCategoryChoice == 1:
        if CPUExerciseValue > PExerciseValue:
            print("Computer Wins")
            time.sleep(1)
            cpulist = cpulist + 1
            playerlist = playerlist - 1
            wincheck()
        if CPUExerciseValue <= PExerciseValue:
            print("You Win!")
            time.sleep(1)
            cpulist = cpulist - 1
            playerlist = playerlist + 1
            wincheck()

    if PCategoryChoice == 2:
        if CPUIntelligenceValue > PIntelligenceValue:
            print("Computer Wins")
            time.sleep(1)
            cpulist = cpulist + 1
            playerlist = playerlist - 1
            wincheck()
        if CPUIntelligenceValue <= PIntelligenceValue:
            print("You Win!")
            time.sleep(1)
            cpulist = cpulist - 1
            playerlist = playerlist + 1
            wincheck()

    if PCategoryChoice == 3:
        if CPUFriendlinessValue > PFriendlinessValue:
            print("Computer Wins")
            time.sleep(1)
            cpulist = cpulist + 1
            playerlist = playerlist - 1
            wincheck()
        if CPUFriendlinessValue <= PFriendlinessValue:
            print("You Win!")
            time.sleep(1)
            cpulist = cpulist - 1
            playerlist = playerlist + 1
            wincheck()

    if PCategoryChoice == 4:
        if CPUDroolValue < PDroolValue:
            print("Computer Wins")
            time.sleep(1)
            cpulist = cpulist + 1
            playerlist = playerlist - 1
            wincheck()
        if CPUDroolValue >= PDroolValue:
            print("You Win!")
            time.sleep(1)
            cpulist = cpulist - 1
            playerlist = playerlist + 1
            wincheck()
        
def wincheck():
    global playerlist
    global cpulist
    global regamechoice
    
    if cpulist == 0:
        print ('------------And the winner is...---------------')
        time.sleep(1)
        print ('You!')
        print ('Would you like to play again?')
        print ('Type yes or no depending on your choice.')
        print ('-----------------------------------------------')
        replaychoice()
    if playerlist == 0:
        print ('------------And the winner is...---------------')
        time.sleep(1)
        print ('The Computer!')
        print ('Better luck next time!')
        print ('Would you like to play again?')
        print ('Type yes or no depending on your choice.')
        print ('-----------------------------------------------')
        replaychoice()
    else:
        gameplay()

def replaychoice():
    regamechoice = input()
    if regamechoice == "yes":
        start()
    if regamechoice == "no":
        raise SystemExit
    if regamechoice != "yes or no":
        print ("Please enter a valid choice.")
        replaychoice()

menu()


