# Author: Santosh Bhandari
# GitHub: https://www.github.com/santoshvandari

# importing the Random Module
import random  
import pyperclip

# Creating the Function that returns Combination of Password
def GeneratePassword(Type,length):    
    PasswordCombination=None
    # Selecting the Different Combination 
    if(Type==1):
        PasswordCombination="abcdefghijklmnopqrstuvwxyz"
    elif(Type==2):
        PasswordCombination="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    elif(Type==3):
        PasswordCombination="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    elif(Type==4):
        PasswordCombination="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890"
    elif(Type==5):
        PasswordCombination="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()<>?;"
    GeneratePassword = ""  
    # Generating the Random Password based upon provided length and Combination using loop  
    for i in range(length):  
        GeneratePassword = GeneratePassword + random.choice(PasswordCombination)  
    return GeneratePassword 

if __name__ == "__main__":  
    while(True):
        # Creating the Welcome Message
        welcomeDisplay='''\n********** Random Password Generator **********
        1. Combination of Lowercase[a-z]
        2. Combination of Uppercase[A-z]
        3. Combination of Lowercase[a-z] & Uppercase[A-Z]
        4. Combination of Lowercase[a-z], Uppercase[A-Z] & Numbers[0-9]
        5. Combination of Lowercase[a-z], Uppercase[A-Z], Numbers[0-9] & Special Character[@#$%^&*()<>?;]
        6. Quit the Password Generator
        '''
        print(welcomeDisplay)
        # Handeling the Errors
        try:
            combinetype=int(input("Enter Your Choice(1,2,3,4,5,6): "))
            if(combinetype in [1,2,3,4,5]):
                len=int(input("Enter a Length of Password: "))
                GeneratedPassword=GeneratePassword(combinetype,len)
                print(f"\nYour Generated Password Password: \n{GeneratedPassword}")
                # Copy the Code in Clipboard
                pyperclip.copy(GeneratedPassword)
                print("The Generated Password Has Been Copied.")
            elif(combinetype==6):
                print("Thank You For Using Password Generator.")
                exit()
            else:
                print("Invalid Option Selected. Please Select Again.")
        except Exception as e:
            print("Invalid Input. Please Select Again. Error: ",e)