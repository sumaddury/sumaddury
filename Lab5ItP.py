"""
____________________________________________________________________________________________________________________________________________________________________________________
Filename:      Lab5ItP.py

Author:        Sucheer Maddury

Date:          2021.07.16

Modifications: None

Description:   This program demonstrates the use of functions to:
               1) take user input and determine which cake and size they desire
               2) calculate how much of each ingredient is needed by calling 1 of 3 functions with the correct parameters
               3) convert these to the appropriate unit
               4) display the results in an organized fashion
               5) build the program around a loop so that the user can get the result for multiple different cakes, and exit the program when they desire
____________________________________________________________________________________________________________________________________________________________________________________
"""
def chocolate_cake_calculator(weight):
    """
    ____________________________________________________________________________________________________________________________________________________________________________________
    Function:      chocolate_cake_calculator(weight)

    Parameters:    weight - the weight of the desired cake size in pounds (lbs)

    Inputs:        None

    Outputs:       Prints the cake type and cake size in addition to the amount of each ingredient needed in ounces (oz), and the total weight in ounces (oz)

    Returns:       None

    Author:        Sucheer Maddury

    Date:          2021.07.16

    Modifications: None

    Description:   This function:
                   1) recieves the weight parameter
                   2) multiples the weight value by the correct percentage for each of the 11 ingredients
                   3) converts the values for each of the 11 ingredients into ounces (oz)
                   4) displays them in an organized fashion
    ____________________________________________________________________________________________________________________________________________________________________________________
    """
    flour=round((float(weight)*0.158)*16,2)
    sugar=round((float(weight)*0.245)*16,2)
    unsweetened_cocoa_powder=round((float(weight)*0.056)*16,2)
    baking_powder=round((float(weight)*0.004)*16,2)
    baking_soda=round((float(weight)*0.006)*16,2)
    salt=round((float(weight)*0.004)*16,2)
    egg=round((float(weight)*0.09)*16,2)
    buttermilk=round((float(weight)*0.18)*16,2)
    canola_oil=round((float(weight)*0.081)*16,2)
    vanilla_extract=round((float(weight)*0.006)*16,2)
    boiling_water=round((float(weight)*0.17)*16,2)
    total=round(flour+sugar+unsweetened_cocoa_powder+baking_powder+baking_soda+salt+egg+buttermilk+canola_oil+vanilla_extract+boiling_water,1)
    flour=(7-len(str(flour)))*" "+str(flour)
    sugar=(7-len(str(sugar)))*" "+str(sugar)
    unsweetened_cocoa_powder=(7-len(str(unsweetened_cocoa_powder)))*" "+str(unsweetened_cocoa_powder)
    baking_powder=(7-len(str(baking_powder)))*" "+str(baking_powder)
    baking_soda=(7-len(str(baking_soda)))*" "+str(baking_soda)
    salt=(7-len(str(salt)))*" "+str(salt)
    egg=(7-len(str(egg)))*" "+str(egg)
    buttermilk=(7-len(str(buttermilk)))*" "+str(buttermilk)
    canola_oil=(7-len(str(canola_oil)))*" "+str(canola_oil)
    vanilla_extract=(7-len(str(vanilla_extract)))*" "+str(vanilla_extract)
    boiling_water=(7-len(str(boiling_water)))*" "+str(boiling_water)
    total=(6-len(str(total)))*" "+str(total)
    print("\n"+str(weight)+" Lb","Chocolate Cake Ingredient list:","\n")
    print("Flour:                   "+flour+" Oz")
    print("Sugar:                   "+sugar+" Oz")
    print("Unsweetened Cocoa Powder:"+unsweetened_cocoa_powder+" Oz")
    print("Baking Powder:           "+baking_powder+" Oz")
    print("Baking Soda:             "+baking_soda+" Oz")
    print("Salt:                    "+salt+" Oz")
    print("Egg:                     "+egg+" Oz")
    print("Buttermilk:              "+buttermilk+" Oz")
    print("Canola Oil:              "+canola_oil+" Oz")
    print("Vanilla Extract:         "+vanilla_extract+" Oz")
    print("Boiling Water:           "+boiling_water+" Oz",)
    print("\n"+"Total:                   "+total+"  Oz","\n","\n")

def red_velvet_cake_calculator(weight):
    """
    ____________________________________________________________________________________________________________________________________________________________________________________
    Function:      red_velvet_cake_calculator(weight)

    Parameters:    weight - the weight of the desired cake size in pounds (lbs)
    
    Inputs:        None

    Outputs:       Prints the cake type and cake size in addition to the amount of each ingredient needed in ounces (oz), and the total weight in ounces (oz)

    Returns:       None

    Author:        Sucheer Maddury

    Date:          2021.07.16

    Modifications: None

    Description:   This function:
                   1) recieves the weight parameter
                   2) multiples the weight value by the correct percentage for each of the 11 ingredients
                   3) converts the values for each of the 11 ingredients into ounces (oz)
                   4) displays them in an organized fashion
    ____________________________________________________________________________________________________________________________________________________________________________________
    """
    flour=round((float(weight)*0.224)*16,2)
    sugar=round((float(weight)*0.224)*16,2)
    unsweetened_cocoa_powder=round((float(weight)*0.004)*16,2)
    baking_soda=round((float(weight)*0.007)*16,2)
    salt=round((float(weight)*0.004)*16,2)
    egg=round((float(weight)*0.09)*16,2)
    buttermilk=round((float(weight)*0.179)*16,2)
    canola_oil=round((float(weight)*0.24)*16,2)
    vanilla_extract=round((float(weight)*0.003)*16,2)
    red_food_coloring=round((float(weight)*0.021)*16,2)
    distilled_vinegar=round((float(weight)*0.004)*16,2)
    total=round(flour+sugar+unsweetened_cocoa_powder+baking_soda+salt+egg+buttermilk+canola_oil+vanilla_extract+red_food_coloring+distilled_vinegar,1)
    flour=(7-len(str(flour)))*" "+str(flour)
    sugar=(7-len(str(sugar)))*" "+str(sugar)
    unsweetened_cocoa_powder=(7-len(str(unsweetened_cocoa_powder)))*" "+str(unsweetened_cocoa_powder)
    baking_soda=(7-len(str(baking_soda)))*" "+str(baking_soda)
    salt=(7-len(str(salt)))*" "+str(salt)
    egg=(7-len(str(egg)))*" "+str(egg)
    buttermilk=(7-len(str(buttermilk)))*" "+str(buttermilk)
    canola_oil=(7-len(str(canola_oil)))*" "+str(canola_oil)
    vanilla_extract=(7-len(str(vanilla_extract)))*" "+str(vanilla_extract)
    red_food_coloring=(7-len(str(red_food_coloring)))*" "+str(red_food_coloring)
    distilled_vinegar=(7-len(str(distilled_vinegar)))*" "+str(distilled_vinegar)
    total=(6-len(str(total)))*" "+str(total)
    print("\n"+str(weight)+" Lb","Red Velvet Cake Ingredient list:","\n")
    print("Flour:                   "+flour+" Oz")
    print("Sugar:                   "+sugar+" Oz")
    print("Baking Soda:             "+baking_soda+" Oz")
    print("Salt:                    "+salt+" Oz")
    print("Unsweetened Cocoa Powder:"+unsweetened_cocoa_powder+" Oz")
    print("Canola Oil:              "+canola_oil+" Oz")
    print("Buttermilk:              "+buttermilk+" Oz")
    print("Egg:                     "+egg+" Oz")
    print("Red Food Coloring:       "+red_food_coloring+" Oz")
    print("Vanilla Extract:         "+vanilla_extract+" Oz")
    print("Distilled Vinegar:       "+distilled_vinegar+" Oz",)
    print("\n"+"Total:                   "+total+"  Oz","\n","\n")

def lemon_cake_calculator(weight):
    """
    ____________________________________________________________________________________________________________________________________________________________________________________
    Function:      lemon_cake_calculator(weight)

    Parameters:    weight - the weight of the desired cake size in pounds (lbs)

    Inputs:        None

    Outputs:       Prints the cake type and cake size in addition to the amount of each ingredient needed in ounces (oz), and the total weight in ounces (oz)

    Returns:       None

    Author:        Sucheer Maddury

    Date:          2021.07.16

    Modifications: None

    Description:   This function:
                   1) recieves the weight parameter
                   2) multiples the weight value by the correct percentage for each of the 6 ingredients and 4 fillings
                   3) converts the values for each of the 6 ingredients and 4 fillings into ounces (oz)
                   4) displays them in an organized fashion
    ____________________________________________________________________________________________________________________________________________________________________________________
    """
    butter=round((float(weight)*0.085)*16,2)
    sifted_self_rising_flour=round((float(weight)*0.156)*16,2)
    sugar=round((float(weight)*0.15)*16,2)
    egg=round((float(weight)*0.09)*16,2)
    buttermilk=round((float(weight)*0.09)*16,2)
    vanilla_extract=round((float(weight)*0.002)*16,2)
    yolk_egg_filling=round((float(weight)*0.179)*16,2)
    filling_sugar=round((float(weight)*0.113)*16,2)
    filling_butter=round((float(weight)*0.021)*16,2)
    lemon_juice_zest_filling=round((float(weight)*0.114)*16,2)
    total=round(butter+sugar+egg+sifted_self_rising_flour+buttermilk+vanilla_extract+yolk_egg_filling+filling_butter+filling_sugar+lemon_juice_zest_filling,1)
    butter=(7-len(str(butter)))*" "+str(butter)
    sifted_self_rising_flour=(7-len(str(sifted_self_rising_flour)))*" "+str(sifted_self_rising_flour)
    sugar=(7-len(str(sugar)))*" "+str(sugar)
    egg=(7-len(str(egg)))*" "+str(egg)
    buttermilk=(7-len(str(buttermilk)))*" "+str(buttermilk)
    vanilla_extract=(7-len(str(vanilla_extract)))*" "+str(vanilla_extract)
    yolk_egg_filling=(7-len(str(yolk_egg_filling)))*" "+str(yolk_egg_filling)
    filling_sugar=(7-len(str(filling_sugar)))*" "+str(filling_sugar)
    filling_butter=(7-len(str(filling_butter)))*" "+str(filling_butter)
    lemon_juice_zest_filling=(7-len(str(lemon_juice_zest_filling)))*" "+str(lemon_juice_zest_filling)
    total=(6-len(str(total)))*" "+str(total)
    print("\n"+str(weight)+" Lb","Lemon Cake Ingredient list:","\n")
    print("Butter:                  "+butter+" Oz")
    print("Sugar:                   "+sugar+" Oz")
    print("Egg:                     "+egg+" Oz")
    print("Sifted Self-Rising Flour:"+sifted_self_rising_flour+" Oz")
    print("Buttermilk:              "+buttermilk+" Oz")
    print("Vanilla Extract:         "+vanilla_extract+" Oz")
    print("\n"+"Fillings:","\n")
    print("Egg Yolk:                "+yolk_egg_filling+" Oz")
    print("Sugar (Filling):         "+filling_sugar+" Oz")
    print("Butter (Filling):        "+filling_butter+" Oz")
    print("Lemon Juice and Zest:    "+lemon_juice_zest_filling+" Oz")
    print("\n"+"Total:                   "+total+"  Oz","\n","\n")

def cake_type_and_size_interpreter():
    """
    ____________________________________________________________________________________________________________________________________________________________________________________
    Function:      cake_type_and_size_interpreter()

    Parameters:    None

    Inputs:        cake_type - the cake flavor (chocolate, red velvet, lemon, or 'q' to exit the program)
                   cake_size - the cake size (L for 7 Lb Large, or R for 4 Lb Regular)

    Outputs:       Calls the appropriate function, which then prints out the correct recipe

    Returns:       cake_type, with the purpose of recognizing when the user has quit (when they enter cake_type as 'q')

    Author:        Sucheer Maddury

    Date:          2021.07.16

    Modifications: None

    Description:   This function:
                   1) prompts the user for the cake type and size
                   2) calls the approriate cake type function with the appropriate weight as the parameter
                   3) repeats this process of input and output until the user inputs 'q'/'Q' as the cake type
                   4) exits the program when the user inputs 'q'/'Q'
    ____________________________________________________________________________________________________________________________________________________________________________________
    """
    cake_type=input("Please Select Cake Type; Enter 1 for Chocolate, 2 for Red Velvet, 3 for Lemon, q to quit: ")
    if not (cake_type=="q" or cake_type=="Q"):
        cake_size=input("Please Select Cake Size; Enter L for large, R for regular: ")

        if cake_type=="1":
            if cake_size=="R":
                chocolate_cake_calculator(4)
            elif cake_size=="L":
                chocolate_cake_calculator(7)
            else:
                print("Invalid Cake Type and/or Size")

        elif cake_type=="2":
            if cake_size=="R":
                red_velvet_cake_calculator(4)
            elif cake_size=="L":
                red_velvet_cake_calculator(7)
            else:
                print("Invalid Cake Type and/or Size")

        elif cake_type=="3":
            if cake_size=="R":
                lemon_cake_calculator(4)
            elif cake_size=="L":
                lemon_cake_calculator(7)
            else:
                print("Invalid Cake Type and/or Size")

        else:
            print("Invalid Cake Type and/or Size")
    else:
        print("Bye!")
    return cake_type

"""
____________________________________________________________________________________________________________________________________________________________________________________
                                                                                PROGRAM STARTS HERE
____________________________________________________________________________________________________________________________________________________________________________________
"""

sentinel=cake_type_and_size_interpreter()
while not (sentinel=="q" or sentinel=="Q"):
    sentinel=cake_type_and_size_interpreter()

"""
RESULTS:
____________________________________________________________________________________________________________________________________________________________________________________
====================== RESTART: C:/Users/sumad/Lab5ItP.py ======================
Please Select Cake Type; Enter 1 for Chocolate, 2 for Red Velvet, 3 for Lemon, q to quit: 2
Please Select Cake Size; Enter L for large, R for regular: L

7 Lb Red Velvet Cake Ingredient list: 

Flour:                     25.09 Oz
Sugar:                     25.09 Oz
Baking Soda:                0.78 Oz
Salt:                       0.45 Oz
Unsweetened Cocoa Powder:   0.45 Oz
Canola Oil:                26.88 Oz
Buttermilk:                20.05 Oz
Egg:                       10.08 Oz
Red Food Coloring:          2.35 Oz
Vanilla Extract:            0.34 Oz
Distilled Vinegar:          0.45 Oz

Total:                    112.0  Oz 
 

Please Select Cake Type; Enter 1 for Chocolate, 2 for Red Velvet, 3 for Lemon, q to quit: 3
Please Select Cake Size; Enter L for large, R for regular: R

4 Lb Lemon Cake Ingredient list: 

Butter:                     5.44 Oz
Sugar:                      9.60 Oz
Egg:                        5.76 Oz
Sifted Self-Rising Flour:   9.98 Oz
Buttermilk:                 5.76 Oz
Vanilla Extract:            0.13 Oz

Fillings: 

Egg Yolk:                  11.46 Oz
Sugar (Filling):            7.23 Oz
Butter (Filling):           1.34 Oz
Lemon Juice and Zest:       7.30 Oz

Total:                     64.0  Oz 
 

Please Select Cake Type; Enter 1 for Chocolate, 2 for Red Velvet, 3 for Lemon, q to quit: 3
Please Select Cake Size; Enter L for large, R for regular: L

7 Lb Lemon Cake Ingredient list: 

Butter:                     9.52 Oz
Sugar:                     16.80 Oz
Egg:                       10.08 Oz
Sifted Self-Rising Flour:  17.47 Oz
Buttermilk:                10.08 Oz
Vanilla Extract:            0.22 Oz

Fillings: 

Egg Yolk:                  20.05 Oz
Sugar (Filling):           12.66 Oz
Butter (Filling):           2.35 Oz
Lemon Juice and Zest:      12.77 Oz

Total:                    112.0  Oz 
 

Please Select Cake Type; Enter 1 for Chocolate, 2 for Red Velvet, 3 for Lemon, q to quit: 1
Please Select Cake Size; Enter L for large, R for regular: R

4 Lb Chocolate Cake Ingredient list: 

Flour:                     10.11 Oz
Sugar:                     15.68 Oz
Unsweetened Cocoa Powder:   3.58 Oz
Baking Powder:              0.26 Oz
Baking Soda:                0.38 Oz
Salt:                       0.26 Oz
Egg:                        5.76 Oz
Buttermilk:                11.52 Oz
Canola Oil:                 5.18 Oz
Vanilla Extract:            0.38 Oz
Boiling Water:             10.88 Oz

Total:                     64.0  Oz 
 

Please Select Cake Type; Enter 1 for Chocolate, 2 for Red Velvet, 3 for Lemon, q to quit: 1
Please Select Cake Size; Enter L for large, R for regular: R

4 Lb Chocolate Cake Ingredient list: 

Flour:                     10.11 Oz
Sugar:                     15.68 Oz
Unsweetened Cocoa Powder:   3.58 Oz
Baking Powder:              0.26 Oz
Baking Soda:                0.38 Oz
Salt:                       0.26 Oz
Egg:                        5.76 Oz
Buttermilk:                11.52 Oz
Canola Oil:                 5.18 Oz
Vanilla Extract:            0.38 Oz
Boiling Water:             10.88 Oz

Total:                     64.0  Oz 
 

Please Select Cake Type; Enter 1 for Chocolate, 2 for Red Velvet, 3 for Lemon, q to quit: q
Bye!
____________________________________________________________________________________________________________________________________________________________________________________
"""
