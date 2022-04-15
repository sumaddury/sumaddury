"""
____________________________________________________________________________________________________________________________________________________________________________________
Filename:      Lab7ItPPart2.py

Author:        Sucheer Maddury

Date:          2021.07.25

Modifications: Sucheer Maddury - 2021.07.26
               Sucheer Maddury - 2021.07.27

Description:   This module performs the first stage of a cake making process.
               It's tasks include:
               1) Query a cake order
               2) Calculate the amounts, in oz, needed for each ingredient
               3) Repeat Step 1 - 2 until user enter 'q' or 'Q' to quit
               4) Print the Total ingredient amounts -
                  for each cake type ordered, print the ingredient amounts for
                  the total quantity of cake for both sizes
____________________________________________________________________________________________________________________________________________________________________________________
"""

def calc_ingrd(cake_wt, recipe):
    """
    ____________________________________________________________________________________________________________________________________________________________________________________
    Function:      calc_ingrd()

    Parameters:    cake_wt - the total weight of the cakes  
                   recipe - the dictionary with the ingredient percentages in order 

    Inputs:        None

    Outputs:       None

    Returns:       Returns a list with the calculated ingredient weights in order

    Author:        Sucheer Maddury

    Date:          2021.07.26

    Modifications: Sucheer Maddury - 2021.07.27 

    Description:   This function prints the ingredient list with each amount in oz. Tasks:
                   1) Iterates through each key in the recipe dictionary
                   2) Calculates the ingredient weight based on the recipe value and cake weight
                   3) Appends the ingredient weight to a list
                   4) Returns the complete list
    ____________________________________________________________________________________________________________________________________________________________________________________
    """
    ingrd_list=[]
    for key in recipe:
        ingrd_wt=cake_wt*recipe[key]/100
        ingrd_list.append(ingrd_wt)
    return ingrd_list

def print_ingrd(ingrd_list,ingrd_names):
    """
    ____________________________________________________________________________________________________________________________________________________________________________________
    Function:      print_ingrd()

    Parameters:    ingrd_list - list of the weights of each ingredient 
                   ingrd_names - list of all possible names of ingredients 

    Inputs:        None

    Outputs:       Prints the ingredients list with weight for each ingredient

    Returns:       None

    Author:        Sucheer Maddury

    Date:          2021.07.26

    Modifications: Sucheer Maddury - 2021.07.27 

    Description:   This function prints the ingredient list with each amount in oz. Tasks:
                   1) Iterates through each element in the ingredient list and the names list
                   2) If the weight in the ingredient list is greater than zero, the weight is printed out with the ingredient name, properly formatted
                   3) Calculates and prints the total weight 
    ____________________________________________________________________________________________________________________________________________________________________________________
    """
    for index in range(0,len(ingrd_list)):
        if ingrd_list[index] !=0:
            print("%-28s%5.1f Oz" % (ingrd_names[index]+": ", ingrd_list[index]))
    print()
    print("%-28s%5.1f Oz" % ("Total: ", sum(ingrd_list)) )

"""
*******************************************************************************
                             PROGRAM STARTS HERE
*******************************************************************************
"""
ingrd_names_list=["Flour","Sugar","Butter","Unsweetened Cocoa Powder","Baking Powder","Baking Soda","Salt","Canola Oil","Egg","Sifted Self Rising Flour",
"Buttermilk","Red Food Coloring","Vanilla Extract","Boiling Water","Distilled Vinegar","Filling - Egg Yolk","Filling - Sugar","Filling - Butter","Filling - Lemon Zest"]

choc_recipe={"FLOUR_PCT":15.8,"SUGAR_PCT":24.5,"BUTTER_PCT":0.0,"UNSWEETENED_COCOA_POWDER_PCT":5.6,"BAKING_POWDER_PCT":0.4,"BAKING_SODA_PCT":0.6,"SALT_PCT":0.4,"CANOLA_OIL_PCT":8.1,"EGG_PCT":9.0,
"SIFTED_SELF_RISING_FLOUR_PCT":0.0,"BUTTERMILK_PCT":18.0,"RED_FOOD_COLOR_PCT":0.0,"VANILLA_EXTRACT_PCT":0.6,"BOILING_WATER_PCT":17.0,"DISTILLED_VINEGAR_PCT":0.0,"EGG_YOLK_FILLING_PCT":0.0,
"SUGAR_FILLING_PCT":0.0,"BUTTER_FILLING_PCT":0.0,"LEMON_ZEST_FILLING_PCT":0.0}

redv_recipe={"FLOUR_PCT":22.4,"SUGAR_PCT":22.4,"BUTTER_PCT":0.0,"UNSWEETENED_COCOA_POWDER_PCT":0.4,"BAKING_POWDER_PCT":0.0,"BAKING_SODA_PCT":0.7,"SALT_PCT":0.4,"CANOLA_OIL_PCT":24.0,
"EGG_PCT":9.0,"SIFTED_SELF_RISING_FLOUR_PCT":0.0,"BUTTERMILK_PCT":17.9,"RED_FOOD_COLOR_PCT":2.1,"VANILLA_EXTRACT_PCT":0.3,"BOILING_WATER_PCT":0.0,"DISTILLED_VINEGAR_PCT":0.4,
"EGG_YOLK_FILLING_PCT":0.0,"SUGAR_FILLING_PCT":0.0,"BUTTER_FILLING_PCT":0.0,"LEMON_ZEST_FILLING_PCT":0.0}

lemo_recipe={"FLOUR_PCT":0.0,"SUGAR_PCT":15.0,"BUTTER_PCT":8.5,"UNSWEETENED_COCOA_POWDER_PCT":0.0,"BAKING_POWDER_PCT":0.0,"BAKING_SODA_PCT":0.0,"SALT_PCT":0.0,"CANOLA_OIL_PCT":0.0,
"EGG_PCT":9.0,"SIFTED_SELF_RISING_FLOUR_PCT":15.6,"BUTTERMILK_PCT":9.0,"RED_FOOD_COLOR_PCT":0.0,"VANILLA_EXTRACT_PCT":0.2,"BOILING_WATER_PCT":0.0,"DISTILLED_VINEGAR_PCT":0.0,
"EGG_YOLK_FILLING_PCT":17.9,"SUGAR_FILLING_PCT":11.3,"BUTTER_FILLING_PCT":2.1,"LEMON_ZEST_FILLING_PCT":11.4}

# Cake size weights in oz
LARGE_CAKE_WT = 7 * 16
REGULAR_CAKE_WT = 4 * 16

# initialize cake order data
choc_cake_wt = 0
large_choc_cake = 0
reg_choc_cake = 0

redv_cake_wt = 0
large_redv_cake = 0
reg_redv_cake = 0

lemo_cake_wt = 0
large_lemo_cake = 0
reg_lemo_cake = 0

"""
*******************************************************************************
                                    INPUT
*******************************************************************************
"""
# query cake type; if 'q' or 'Q' was entered then quit the program
cake_type = input("Please Select Cake Type; Enter 1 for Chocolate,"
                       " 2 for Red Velvet, 3 for Lemon, q to quit: ")

# don't bother query cake_size if to quit
if not( cake_type == 'q' or cake_type == 'Q' ):
    # query cake size
    cake_size = input("Please Select Cake Size; Enter L for large, R for regular: ")

# *************************************************************************
#                   Sentinel to take cake order input
# *************************************************************************
while not(cake_type == 'q' or cake_type == 'Q'):
    print()
    cake_type = eval(cake_type)

    if cake_type == 1:
        if cake_size == 'R' or cake_size == 'r':
            # keep track of the quantity ordered
            choc_cake_wt += REGULAR_CAKE_WT
            reg_choc_cake += 1
        elif cake_size == 'L' or cake_size == 'l':
            choc_cake_wt += LARGE_CAKE_WT
            large_choc_cake += 1

    elif cake_type == 2:
        if cake_size == 'R' or cake_size == 'r':
            # keep track of the quantity ordered
            redv_cake_wt += REGULAR_CAKE_WT
            reg_redv_cake += 1
        elif cake_size == 'L' or cake_size == 'l':
            redv_cake_wt += LARGE_CAKE_WT
            large_redv_cake += 1


    elif cake_type == 3:
        if cake_size == 'R' or cake_size == 'r':
            # keep track of the quantity ordered
            lemo_cake_wt += REGULAR_CAKE_WT
            reg_lemo_cake += 1
        elif cake_size == 'L' or cake_size == 'l':
            lemo_cake_wt += LARGE_CAKE_WT
            large_lemo_cake += 1


    # take next order - query cake type; if 'q' or 'Q' was entered then quit the program
    cake_type = input("Please Select Cake Type; Enter 1 for Chocolate,"
                      " 2 for Red Velvet, 3 for Lemon, q to quit: ")

    # don't bother query cake_size if to quit
    if not (cake_type == 'q' or cake_type == 'Q'):
        # query cake size
        cake_size = input("Please Select Cake Size; Enter L for large, R for regular: ")

    # end of while loop

print()
print()

"""
*******************************************************************************
                            CALCULATE & OUTPUT
*******************************************************************************
"""
#print header for Chocolate Cake before calculate
header = "Ingredient Quantities for %i Large and %i Regular Chocolate Cake\n" %\
         (large_choc_cake, reg_choc_cake)
if large_choc_cake>0 or reg_choc_cake>0:
    print(header)
    # Calculate ingredient amounts and output them
    choc_ingrd_list=calc_ingrd( choc_cake_wt,choc_recipe )
    print_ingrd(choc_ingrd_list,ingrd_names_list)
    print()
    print()

#print header for Red Velvet Cake before calculate
header = "Ingredient Quantities for %i Large and %i Regular Red Velvet Cake\n" %\
         (large_redv_cake, reg_redv_cake)
if large_redv_cake>0 or reg_redv_cake>0:
    print(header)
    # Calculate ingredient amounts and output them
    redv_ingrd_list=calc_ingrd( redv_cake_wt,redv_recipe )
    print_ingrd(redv_ingrd_list,ingrd_names_list)
    print()
    print()

#print header for Lemon Cake before calculate
header = "Ingredient Quantities for %i Large and %i Regular Lemon Cake\n" %\
         (large_lemo_cake, reg_lemo_cake)
if large_lemo_cake>0 or reg_lemo_cake>0:
    print(header)
    # Calculate ingredient amounts and output them
    lemo_ingrd_list=calc_ingrd( lemo_cake_wt,lemo_recipe )
    print_ingrd(lemo_ingrd_list,ingrd_names_list)
    print()
    print()

"""
RESULTS:
____________________________________________________________________________________________________________________________________________________________________________________
==================== RESTART: C:/Users/sumad/Lab7ItPPart2.py ===================
Please Select Cake Type; Enter 1 for Chocolate, 2 for Red Velvet, 3 for Lemon, q to quit: 2
Please Select Cake Size; Enter L for large, R for regular: L

Please Select Cake Type; Enter 1 for Chocolate, 2 for Red Velvet, 3 for Lemon, q to quit: 3
Please Select Cake Size; Enter L for large, R for regular: R

Please Select Cake Type; Enter 1 for Chocolate, 2 for Red Velvet, 3 for Lemon, q to quit: 3
Please Select Cake Size; Enter L for large, R for regular: L

Please Select Cake Type; Enter 1 for Chocolate, 2 for Red Velvet, 3 for Lemon, q to quit: 1
Please Select Cake Size; Enter L for large, R for regular: R

Please Select Cake Type; Enter 1 for Chocolate, 2 for Red Velvet, 3 for Lemon, q to quit: 1
Please Select Cake Size; Enter L for large, R for regular: R

Please Select Cake Type; Enter 1 for Chocolate, 2 for Red Velvet, 3 for Lemon, q to quit: 1
Please Select Cake Size; Enter L for large, R for regular: L

Please Select Cake Type; Enter 1 for Chocolate, 2 for Red Velvet, 3 for Lemon, q to quit: 2
Please Select Cake Size; Enter L for large, R for regular: R

Please Select Cake Type; Enter 1 for Chocolate, 2 for Red Velvet, 3 for Lemon, q to quit: 2
Please Select Cake Size; Enter L for large, R for regular: R

Please Select Cake Type; Enter 1 for Chocolate, 2 for Red Velvet, 3 for Lemon, q to quit: q


Ingredient Quantities for 1 Large and 2 Regular Chocolate Cake

Flour:                       37.9 Oz
Sugar:                       58.8 Oz
Unsweetened Cocoa Powder:    13.4 Oz
Baking Powder:                1.0 Oz
Baking Soda:                  1.4 Oz
Salt:                         1.0 Oz
Canola Oil:                  19.4 Oz
Egg:                         21.6 Oz
Buttermilk:                  43.2 Oz
Vanilla Extract:              1.4 Oz
Boiling Water:               40.8 Oz

Total:                      240.0 Oz


Ingredient Quantities for 1 Large and 2 Regular Red Velvet Cake

Flour:                       53.8 Oz
Sugar:                       53.8 Oz
Unsweetened Cocoa Powder:     1.0 Oz
Baking Soda:                  1.7 Oz
Salt:                         1.0 Oz
Canola Oil:                  57.6 Oz
Egg:                         21.6 Oz
Buttermilk:                  43.0 Oz
Red Food Coloring:            5.0 Oz
Vanilla Extract:              0.7 Oz
Distilled Vinegar:            1.0 Oz

Total:                      240.0 Oz


Ingredient Quantities for 1 Large and 1 Regular Lemon Cake

Sugar:                       26.4 Oz
Butter:                      15.0 Oz
Egg:                         15.8 Oz
Sifted Self Rising Flour:    27.5 Oz
Buttermilk:                  15.8 Oz
Vanilla Extract:              0.4 Oz
Filling - Egg Yolk:          31.5 Oz
Filling - Sugar:             19.9 Oz
Filling - Butter:             3.7 Oz
Filling - Lemon Zest:        20.1 Oz

Total:                      176.0 Oz
____________________________________________________________________________________________________________________________________________________________________________________
"""

