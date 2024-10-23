"""
Simple recipe generator!!!
Generates recipes depending on what you have at home!!!
(Assuming you have basics like water, oil, salt and pepper)
(These are the most basic version of these recipes- if you're able to, I'd reccomend you try the more complex recipes online!)
"""
###---Import Library---###
import recipes

###---Ask what ingredients you have at home---###
print("Simple Recipe Generator:")
print("(Assuming you have basics like water, oil, salt and pepper)")
print()
eggs = input("Do you have eggs at home? (y/n) ")
flour = input("Do you have flour at home? (y/n) ")
green = input("Do you have chives or green onions at home? (y/n) ")
broth = input("Do you have broth at home? (y/n) ")

###---Calculations---###
eggs_true = eggs == "y" or eggs == "Y" or eggs == "Yes" or eggs == "yes" or eggs == "YES"
flour_true = flour == "y" or flour == "Y" or flour == "Yes" or flour == "yes" or flour == "YES"
green_true = green == "y" or green == "Y" or green == "Yes" or green == "yes" or green == "YES"
broth_true = broth == "y" or broth == "Y" or broth == "Yes" or broth == "yes" or broth == "YES"

###---Recipe output---###
#if you have all ingredients:
if eggs_true and flour_true and green_true and broth_true:
    print("You can make steamed eggs, korean pancakes, sujebi or egg soup:")
    choice = input("Would you like to make steamed eggs (se), korean pancakes (kp), sujebi (s) or eggs soup (es)? ")
    if choice == "SE" or choice == "se" or choice == "Se":
        recipes.steamed_eggs()
    if choice == "KP" or choice == "kp" or choice == "Kp":
        recipes.korean_pancakes()
    if choice == "S" or choice == "s":
        recipes.sujebi()
    if choice == "ES" or choice == "es" or choice == "Es":
        recipes.egg_soup()
#Egg soup (req: broth and eggs)
elif broth_true and eggs_true:
    recipes.egg_soup()
#sujebi (req: flour and broth)
elif flour_true and broth_true:
    recipes.sujebi()
#korean pancakes (req: flour and green)
elif flour_true and green_true:
    recipes.korean_pancakes()
#steamed eggs (req: eggs)
elif eggs_true:
    recipes.steamed_eggs()
else:
    print()
    print("Sorry, we don't have any recipes with the ingredients you have.")
