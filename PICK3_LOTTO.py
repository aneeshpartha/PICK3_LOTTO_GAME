from datetime import datetime
import random
import sys

# Global variables
value1 = 0 # User input 1
value2 = 0 # user input 2
value3 = 0 # user input 3
randomnum = [] # Random number variable
fireball = "N/A" # fireball value
fboption = "N/A" # fireball option
attempts = 2 # Attempts to user
total = 0 # Total prize money

print("\t\t\tWelcome to pick 3 Lotto game")
print("\t\t\t****************************")

# Main function which invokes the entire game
def main():


    global attempts
    getuserdata() # Call to user input function
    if(attempts == 2):
        genrandomnum_fb() # Call to generate random sequence
    result,fbresult = checker() # Call to check randomly generated sequence with user input
    #Conditions based on match with random sequence and fireball number
    if(result == True and fbresult == "wofb"):
        print("Congratulations!!! You have won the pick 3 lotto without using Fireball... A $" +str(total)+ " cash prize is on your way")
        summary("Win")
    elif(result == True and fbresult == "wfbwin"):
        print("Congratulations!!! You have won both pick 3 lotto and fireball...A $"+ str(total)+ "cash prize is on your way")
        summary("win")
    elif(result == True and fbresult == "wfblose"):
        print("Congratulations!!! Though you lost fireball You have won the pick 3 lotto... A $" + str(total) + " cash prize is on your way.")
        summary("win")
    elif(result == False and fbresult == "wfbwin"):
        print("Congratulations !!! Though you lost in pick 3 lotto  You have won using fireball...A $"+str(total)+ " cash prize is on your way")
        summary("Win")
    elif(attempts != 0):
        print("Sorry you have lost the game. You have " + str(attempts) + " attempt(s) left")
        attempts -= 1
        replay = input("\nDo you want to play again ?")
        if ( replay == "y" or replay == "Y"):
            main()
        elif(replay == "n" or replay == "N"):
            summary("lost")
            sys.exit()
            
    else:
        print("Sorry you have lost the game. Nice try !!! Better luck next time")
        summary("lost")

# Function to generate 3 random numbers
def genrandomnum_fb():
    global randomnum
    randomnum = sorted(random.sample(range(0,10),3)) #Usage of random.sample function

# Function to get user input and also to check user interest to play fireball

def getuserdata():
    global value1,value2,value3
    enteredvalue = 0
    # loop to iterate in case of any errors
    while (enteredvalue != 1):
        try:
            # User inputs integer value
            value1 = int(input("\nPlease enter first number :"))
            value2 = int(input("Please enter second number :"))
            value3 = int(input("Please enter third number : "))

            # Condition to check if the value is greater than or equal to 0 and less than 10
            if ( value1 < 0 or value2 < 0 or value3 < 0 or value1 > 9 or value2 > 9 or value3 > 9):
                print("Entered value is not valid. Please re-enter")
                continue

            global fboption
            # Loop to check user interest to play fireball
            while(fboption != "y" and fboption != "Y" and fboption != "n" and fboption != "N"):
                fboption = input("\nDo you want to play pick three with fireball option?(Y/N) :")
                if(fboption != "y" and fboption != "Y" and fboption != "n" and fboption != "N"):
                    print("Entered option is invalid. Please re-enter")

            print("\nUser entered sequence:" + "[" +str(value1) + "," + str(value2)+ "," + str(value3) + "]")
            enteredvalue = 1
        except ValueError:
            print("Sorry !!! The entered value is not valid.Please re-enter ")
            enteredvalue = 0

# Function to check if user entered input matches the randomly generated sequence
def checker():
    global fboption,total
    if(randomnum == [value1,value2,value3]):
        total = 100 # Prize amount without fireball play
        if(fboption == "y" or fboption == "Y"):
            return (True , checkfireball()) # Calling fireball function
        else:
            return (True, "wofb")
    else:
       if(fboption == "y" or fboption == "Y"):
           return (False,checkfireball())
       else:
           return False,"wfbno"

# Function which randomly generates a fireball number and checks with the user sequence
def checkfireball():
    global fireball,total
    status = "wfblose"
    if(attempts == 2 ):
        fireball = random.randint(1, 9)
    #print("FB:" + str(fireball))
    if([fireball,value2,value3] == randomnum) :
        total += 50 # for each fireball match user gets $50
        status = "wfbwin"
    if([value1,fireball,value3] == randomnum):
        total+= 50
        status = "wfbwin"
    if([value1,value2,fireball] == randomnum):
        total+= 50
        status = "wfbwin"
    return status

# This function prints the summary of the game at the end
def summary(decision):
    print("\nBelow is the summary of the game")
    print("User entered input :"+ "[" +str(value1) + "," + str(value2)+ "," + str(value3) + "]")
    print("Gen:" + str(randomnum) + " " + "FB:" + str(fireball))
    print("Result:" + decision)
    print("Total prize = $"+str(total))

# main function is invoked
main()



