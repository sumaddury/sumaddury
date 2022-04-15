"""
____________________________________________________________________________________________________________________________________________________________________________________
Filename:      Lab4ItP.py

Author:        Sucheer Maddury

Date:          2021.07.12

Modifications: Sucheer Maddury – 2021.07.13
               Sucheer Maddury - 2021.07.14

Description:   This program demonstrates the use of functions to:
               1) take user input and determine which cake and size they desire
               2) calculate how much of each ingredient is needed
               3) convert these to the appropriate unit
____________________________________________________________________________________________________________________________________________________________________________________
"""
def chocolate_cake_calculator(weight):
    ingredient_a=round((float(weight)*0.158)*16,3)
    ingredient_b=round((float(weight)*0.245)*16,3)
    ingredient_c=round((float(weight)*0.056)*16,3)
    ingredient_d=round((float(weight)*0.541)*16,3)
    print(str(weight)+" Lb","Chocolate Cake Ingredient list:")
    print("Ingredient A:  "+str(ingredient_a)+" Oz")
    print("Ingredient B:  "+str(ingredient_b)+" Oz")
    print("Ingredient C:  "+str(ingredient_c)+" Oz")
    print("Ingredient D:  "+str(ingredient_d)+" Oz")
"""
____________________________________________________________________________________________________________________________________________________________________________________
Function:      chocolate_cake_calculator(weight)

Parameters:    weight - the weight of the desired cake size in pounds (lbs)

Inputs:        None

Outputs:       Prints the cake type and cake size in addition to the amount of each ingredient needed in ounces (oz)

Returns:       None

Author:        Sucheer Maddury

Date:          2021.07.12

Modifications: None

Description:   This function prints the ounce values for 4 different ingredients for the chocolate cake recipe
____________________________________________________________________________________________________________________________________________________________________________________
"""
def red_velvet_cake_calculator(weight):
    ingredient_a=round((float(weight)*0.224)*16,3)
    ingredient_b=round((float(weight)*0.224)*16,3)
    ingredient_c=round((float(weight)*0.240)*16,3)
    ingredient_d=round((float(weight)*0.179)*16,3)
    ingredient_e=round((float(weight)*0.133)*16,3)
    print(str(weight)+" Lb","Red Velvet Cake Ingredient list:")
    print("Ingredient A:  "+str(ingredient_a)+" Oz")
    print("Ingredient B:  "+str(ingredient_b)+" Oz")
    print("Ingredient C:  "+str(ingredient_c)+" Oz")
    print("Ingredient D:  "+str(ingredient_d)+" Oz")
    print("Ingredient E:  "+str(ingredient_d)+" Oz")
"""
____________________________________________________________________________________________________________________________________________________________________________________
Function:      red_velvet_cake_calculator(weight)

Parameters:    weight - the weight of the desired cake size in pounds (lbs)

Inputs:        None

Outputs:       Prints the cake type and cake size in addition to the amount of each ingredient needed in ounces (oz)

Returns:       None

Author:        Sucheer Maddury

Date:          2021.07.13

Modifications: None

Description:   This function prints the ounce values for 5 different ingredients for the red velvet cake recipe
____________________________________________________________________________________________________________________________________________________________________________________
"""
def lemon_cake_calculator(weight):
    ingredient_a=round((float(weight)*0.385)*16,3)
    ingredient_b=round((float(weight)*0.358)*16,3)
    ingredient_c=round((float(weight)*0.257)*16,3)
    print(str(weight)+" Lb","Lemon Cake Ingredient list:")
    print("Ingredient A:  "+str(ingredient_a)+" Oz")
    print("Ingredient B:  "+str(ingredient_b)+" Oz")
    print("Ingredient C:  "+str(ingredient_c)+" Oz")
"""
____________________________________________________________________________________________________________________________________________________________________________________
Function:      lemon_cake_calculator(weight)

Parameters:    weight - the weight of the desired cake size in pounds (lbs)

Inputs:        None

Outputs:       Prints the cake type and cake size in addition to the amount of each ingredient needed in ounces (oz)

Returns:       None

Author:        Sucheer Maddury

Date:          2021.07.13

Modifications: Sucheer Maddury - 2021.07.14

Description:   This function prints the ounce values for 3 different ingredients for the lemon cake recipe
____________________________________________________________________________________________________________________________________________________________________________________
"""
cake_type=input("Please select cake type; Enter 1 for Chocolate, 2 for Red Velvet and 3 for Lemon: ")
cake_size=input("Please select cake size; Enter L for large, R for regular: ")

if cake_type=="1":
    if cake_size=="R":
        chocolate_cake_calculator(4)
    elif cake_size=="L":
        chocolate_cake_calculator(7)
    else:
        print("Invalid Cake Size")

elif cake_type=="2":
    if cake_size=="R":
        red_velvet_cake_calculator(4)
    elif cake_size=="L":
        red_velvet_cake_calculator(7)
    else:
        print("Invalid Cake Size")

elif cake_type=="3":
    if cake_size=="R":
        lemon_cake_calculator(4)
    elif cake_size=="L":
        lemon_cake_calculator(7)
    else:
        print("Invalid Cake Size")

else:
    print("Invalid Cake Type")
"""
RESULTS:
Large Chocolate
____________________________________________________________________________________________________________________________________________________________________________________
====================== RESTART: C:/Users/sumad/Lab4ItP.py ======================
Please select cake type; Enter 1 for Chocolate, 2 for Red Velvet and 3 for Lemon: 1
Please select cake size; Enter L for large, R for regular: L
7 Lb Chocolate Cake Ingredient list:
Ingredient A:  17.696 Oz
Ingredient B:  27.44 Oz
Ingredient C:  6.272 Oz
Ingredient D:  60.592 Oz
____________________________________________________________________________________________________________________________________________________________________________________
Regular Lemon
____________________________________________________________________________________________________________________________________________________________________________________
============================= RESTART: C:/Users/sumad/Lab4ItP.py ============================
Please select cake type; Enter 1 for Chocolate, 2 for Red Velvet and 3 for Lemon: 3
Please select cake size; Enter L for large, R for regular: R
4 Lb Lemon Cake Ingredient list:
Ingredient A:  24.64 Oz
Ingredient B:  22.912 Oz
Ingredient C:  16.448 Oz
____________________________________________________________________________________________________________________________________________________________________________________
Large Red Velvet 
____________________________________________________________________________________________________________________________________________________________________________________
============================= RESTART: C:/Users/sumad/Lab4ItP.py ============================
Please select cake type; Enter 1 for Chocolate, 2 for Red Velvet and 3 for Lemon: 2
Please select cake size; Enter L for large, R for regular: L
7 Lb Red Velvet Cake Ingredient list:
Ingredient A:  25.088 Oz
Ingredient B:  25.088 Oz
Ingredient C:  26.88 Oz
Ingredient D:  20.048 Oz
Ingredient E:  20.048 Oz
____________________________________________________________________________________________________________________________________________________________________________________
"""