"""
____________________________________________________________________________________________________________________________________________________________________________________
Filename:      Lab7ItP.py

Author:        Sucheer Maddury

Date:          2021.07.24

Modifications: Sucheer Maddury - 2021.07.25
               Sucheer Maddury - 2021.07.26

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
def chocolate_cake_calculator(weight):
    """
    ____________________________________________________________________________________________________________________________________________________________________________________
    Function:      chocolate_cake_calculator(weight)

    Parameters:    weight - the weight of the desired cake size in pounds (lbs)

    Inputs:        None

    Outputs:       Prints the cake type and cake sizes in addition to the amount of each ingredient needed in ounces (oz), and the total weight in ounces (oz)

    Returns:       None

    Author:        Sucheer Maddury

    Date:          2021.07.16

    Modifications: Sucheer Maddury - 2021.07.24

    Description:   This function:
                   1) recieves the weight parameter
                   2) multiples the weight value by the correct percentage for each of the 11 ingredients
                   3) converts the values for each of the 11 ingredients into ounces (oz)
                   4) displays them in an organized fashion
    ____________________________________________________________________________________________________________________________________________________________________________________
    """
    choc_flour_prop=0.158
    choc_sugar_prop=0.245
    choc_unsweet_cocoa_powder_prop=0.056
    choc_baking_powder_prop=0.004
    choc_baking_soda_prop=0.006
    choc_salt_prop=0.004
    choc_egg_prop=0.09
    choc_buttermilk_prop=0.18
    choc_canola_oil_prop=0.081
    choc_vanilla_extract_prop=0.006
    choc_boiling_water_prop=0.17
    flour=weight*choc_flour_prop
    sugar=weight*choc_sugar_prop
    unsweetened_cocoa_powder=weight*choc_unsweet_cocoa_powder_prop
    baking_powder=weight*choc_baking_powder_prop
    baking_soda=weight*choc_baking_soda_prop
    salt=weight*choc_salt_prop
    egg=weight*choc_egg_prop
    buttermilk=weight*choc_buttermilk_prop
    canola_oil=weight*choc_canola_oil_prop
    vanilla_extract=weight*choc_vanilla_extract_prop
    boiling_water=weight*choc_boiling_water_prop
    total=flour+sugar+unsweetened_cocoa_powder+baking_powder+baking_soda+salt+egg+buttermilk+canola_oil+vanilla_extract+boiling_water
    print("Ingredient Quantities for",large_cake_count,"Large and",reg_cake_count,"Regular Chocolate Cake")
    print()
    print("%-28s%5.1f Oz" % ("Flour:", flour))
    print("%-28s%5.1f Oz" % ("Sugar:", sugar))
    print("%-28s%5.1f Oz" % ("Unsweetened Cocoa Powder:", unsweetened_cocoa_powder))
    print("%-28s%5.1f Oz" % ("Baking Powder:", baking_powder))
    print("%-28s%5.1f Oz" % ("Baking Soda:", baking_soda))
    print("%-28s%5.1f Oz" % ("Salt:", salt))
    print("%-28s%5.1f Oz" % ("Egg:", egg))
    print("%-28s%5.1f Oz" % ("Buttermilk:", buttermilk))
    print("%-28s%5.1f Oz" % ("Canola Oil:", canola_oil))
    print("%-28s%5.1f Oz" % ("Vanilla Extract:", vanilla_extract))
    print("%-28s%5.1f Oz" % ("Boiling Water:", boiling_water))
    print()
    print("%-28s%5.1f Oz" % ("Total:", total))
    print("\n")

def red_velvet_cake_calculator(weight):
    """
    ____________________________________________________________________________________________________________________________________________________________________________________
    Function:      red_velvet_cake_calculator(weight)

    Parameters:    weight - the weight of the desired cake size in pounds (lbs)
    
    Inputs:        None

    Outputs:       Prints the cake type and cake sizes in addition to the amount of each ingredient needed in ounces (oz), and the total weight in ounces (oz)

    Returns:       None

    Author:        Sucheer Maddury

    Date:          2021.07.16

    Modifications: Sucheer Maddury - 2021.07.24

    Description:   This function:
                   1) recieves the weight parameter
                   2) multiples the weight value by the correct percentage for each of the 11 ingredients
                   3) converts the values for each of the 11 ingredients into ounces (oz)
                   4) displays them in an organized fashion
    ____________________________________________________________________________________________________________________________________________________________________________________
    """
    redv_flour_prop=0.224
    redv_sugar_prop=0.224
    redv_unsweet_cocoa_powder_prop=0.004
    redv_baking_soda_prop=0.007
    redv_salt_prop=0.004
    redv_egg_prop=0.09
    redv_buttermilk_prop=0.179
    redv_canola_oil_prop=0.24
    redv_vanilla_extract_prop=0.003
    redv_red_food_color_prop=0.021
    redv_distilled_vinegar_prop=0.004
    flour=weight*redv_flour_prop
    sugar=weight*redv_sugar_prop
    unsweetened_cocoa_powder=weight*redv_unsweet_cocoa_powder_prop
    baking_soda=weight*redv_baking_soda_prop
    salt=weight*redv_salt_prop
    egg=weight*redv_egg_prop
    buttermilk=weight*redv_buttermilk_prop
    canola_oil=weight*redv_canola_oil_prop
    vanilla_extract=weight*redv_vanilla_extract_prop
    red_food_coloring=weight*redv_red_food_color_prop
    distilled_vinegar=weight*redv_distilled_vinegar_prop
    total=flour+sugar+unsweetened_cocoa_powder+baking_soda+salt+egg+buttermilk+canola_oil+vanilla_extract+red_food_coloring+distilled_vinegar
    print("Ingredient Quantities for",large_cake_count,"Large and",reg_cake_count,"Regular Red Velvet Cake")
    print()
    print("%-28s%5.1f Oz" % ("Flour:", flour))
    print("%-28s%5.1f Oz" % ("Sugar:", sugar))
    print("%-28s%5.1f Oz" % ("Unsweetened Cocoa Powder:", unsweetened_cocoa_powder))
    print("%-28s%5.1f Oz" % ("Baking Soda:", baking_soda))
    print("%-28s%5.1f Oz" % ("Salt:", salt))
    print("%-28s%5.1f Oz" % ("Egg:", egg))
    print("%-28s%5.1f Oz" % ("Buttermilk:", buttermilk))
    print("%-28s%5.1f Oz" % ("Canola Oil:", canola_oil))
    print("%-28s%5.1f Oz" % ("Vanilla Extract:", vanilla_extract))
    print("%-28s%5.1f Oz" % ("Red Food Coloring:", red_food_coloring))
    print("%-28s%5.1f Oz" % ("Distilled Vinegar:", distilled_vinegar))
    print()
    print("%-28s%5.1f Oz" % ("Total:", total))
    print("\n")

def lemon_cake_calculator(weight):
    """
    ____________________________________________________________________________________________________________________________________________________________________________________
    Function:      lemon_cake_calculator(weight)

    Parameters:    weight - the weight of the desired cake size in pounds (lbs)

    Inputs:        None

    Outputs:       Prints the cake type and cake sizes in addition to the amount of each ingredient needed in ounces (oz), and the total weight in ounces (oz)

    Returns:       None

    Author:        Sucheer Maddury

    Date:          2021.07.16

    Modifications: Sucheer Maddury - 2021.07.24

    Description:   This function:
                   1) recieves the weight parameter
                   2) multiples the weight value by the correct percentage for each of the 6 ingredients and 4 fillings
                   3) converts the values for each of the 6 ingredients and 4 fillings into ounces (oz)
                   4) displays them in an organized fashion
    ____________________________________________________________________________________________________________________________________________________________________________________
    """
    lmn_butter_prop=0.085
    lmn_sifted_self_rising_flour_prop=0.156
    lmn_sugar_prop=0.15
    lmn_egg_prop=0.09
    lmn_buttermilk_prop=0.09
    lmn_vanilla_extract_prop=0.002
    lmn_yolk_egg_fill_prop=0.179
    lmn_sugar_fill_prop=0.113
    lmn_butter_fill_prop=0.021
    lmn_lemon_juice_zest_fill_prop=0.114
    butter=weight*lmn_butter_prop
    sifted_self_rising_flour=weight*lmn_sifted_self_rising_flour_prop
    sugar=weight*lmn_sugar_prop
    egg=weight*lmn_egg_prop
    buttermilk=weight*lmn_buttermilk_prop
    vanilla_extract=weight*lmn_vanilla_extract_prop
    yolk_egg_filling=weight*lmn_yolk_egg_fill_prop
    filling_sugar=weight*lmn_sugar_fill_prop
    filling_butter=weight*lmn_butter_fill_prop
    lemon_juice_zest_filling=weight*lmn_lemon_juice_zest_fill_prop
    total=butter+sugar+egg+sifted_self_rising_flour+buttermilk+vanilla_extract+yolk_egg_filling+filling_butter+filling_sugar+lemon_juice_zest_filling
    print("Ingredient Quantities for",large_cake_count,"Large and",reg_cake_count,"Regular Lemon Cake")
    print()
    print("%-28s%5.1f Oz" % ("Butter:", butter))
    print("%-28s%5.1f Oz" % ("Sifted Self Rising Flour:", sifted_self_rising_flour))
    print("%-28s%5.1f Oz" % ("Sugar:", sugar))
    print("%-28s%5.1f Oz" % ("Egg:", egg))
    print("%-28s%5.1f Oz" % ("Buttermilk:", buttermilk))
    print("%-28s%5.1f Oz" % ("Vanilla Extract:", vanilla_extract))
    print("%-28s%5.1f Oz" % ("Filling - Egg Yolk:", yolk_egg_filling))
    print("%-28s%5.1f Oz" % ("Filling - Sugar:", filling_sugar))
    print("%-28s%5.1f Oz" % ("Filling - Butter:", filling_butter))
    print("%-28s%5.1f Oz" % ("Filling - Lemon Zest:", lemon_juice_zest_filling))
    print()
    print("%-28s%5.1f Oz" % ("Total:", total))
    print("\n")

def cake_type_and_size_adder():
    """
    ____________________________________________________________________________________________________________________________________________________________________________________
    Function:      cake_type_and_size_adder()

    Parameters:    None

    Inputs:        cake_type - the cake flavor (chocolate, red velvet, lemon, or 'q' to exit the program)
                   cake_size - the cake size (L for 7 Lb Large, or R for 4 Lb Regular)

    Outputs:       None

    Returns:       Returns cake_type, with the purpose of recognizing when the user has quit (when they enter cake_type as 'q')

    Author:        Sucheer Maddury

    Date:          2021.07.25

    Modifications: None

    Description:   This function:
                   1) Prompts the user for the cake type and size
                   2) Converts the use cake size into uppercase if possible
                   3) Adds the cake size into the list in the correct dictionary value
                   4) Returns the cake type
    ____________________________________________________________________________________________________________________________________________________________________________________
    """
    cake_type=input("Please Select Cake Type; Enter 1 for Chocolate, 2 for Red Velvet, 3 for Lemon, q to quit: ")
    if not (cake_type=="q" or cake_type=="Q"):
        cake_size=input("Please Select Cake Size; Enter L for large, R for regular: ")
        try:
            cake_size.upper()
        except:
            pass
        try:
            cake_orders[int(cake_type)].append(cake_size)
        except:
            pass
    return cake_type

"""
____________________________________________________________________________________________________________________________________________________________________________________
                                                                                PROGRAM STARTS HERE
____________________________________________________________________________________________________________________________________________________________________________________
"""
cake_orders={1:[],2:[],3:[]}
sentinel=cake_type_and_size_adder()
while not (sentinel=="q" or sentinel=="Q"):
    sentinel=cake_type_and_size_adder()
    print()
print("\n")
for key in cake_orders:
    if len(cake_orders[key])>0:
        reg_cake_count=cake_orders[key].count("R")
        large_cake_count=cake_orders[key].count("L")
        total_weight=reg_cake_count*4+large_cake_count*7
        if key==1:
            chocolate_cake_calculator(float(total_weight*16))
        elif key==2:
            red_velvet_cake_calculator(float(total_weight*16))
        elif key==3:
            lemon_cake_calculator(float(total_weight*16))

"""
RESULTS:
____________________________________________________________________________________________________________________________________________________________________________________
====================== RESTART: C:/Users/sumad/Lab7ItP.py ======================
Please Select Cake Type; Enter 1 for Chocolate, 2 for Red Velvet, 3 for Lemon, q to quit: 2
Please Select Cake Size; Enter L for large, R for regular: R

Please Select Cake Type; Enter 1 for Chocolate, 2 for Red Velvet, 3 for Lemon, q to quit: 3
Please Select Cake Size; Enter L for large, R for regular: L

Please Select Cake Type; Enter 1 for Chocolate, 2 for Red Velvet, 3 for Lemon, q to quit: 3
Please Select Cake Size; Enter L for large, R for regular: R

Please Select Cake Type; Enter 1 for Chocolate, 2 for Red Velvet, 3 for Lemon, q to quit: 3
Please Select Cake Size; Enter L for large, R for regular: L

Please Select Cake Type; Enter 1 for Chocolate, 2 for Red Velvet, 3 for Lemon, q to quit: 1
Please Select Cake Size; Enter L for large, R for regular: R

Please Select Cake Type; Enter 1 for Chocolate, 2 for Red Velvet, 3 for Lemon, q to quit: 1
Please Select Cake Size; Enter L for large, R for regular: L

Please Select Cake Type; Enter 1 for Chocolate, 2 for Red Velvet, 3 for Lemon, q to quit: 2
Please Select Cake Size; Enter L for large, R for regular: L

Please Select Cake Type; Enter 1 for Chocolate, 2 for Red Velvet, 3 for Lemon, q to quit: q


Ingredient Quantities for 1 Large and 1 Regular Chocolate Cake

Flour:                       27.8 Oz
Sugar:                       43.1 Oz
Unsweetened Cocoa Powder:     9.9 Oz
Baking Powder:                0.7 Oz
Baking Soda:                  1.1 Oz
Salt:                         0.7 Oz
Egg:                         15.8 Oz
Buttermilk:                  31.7 Oz
Canola Oil:                  14.3 Oz
Vanilla Extract:              1.1 Oz
Boiling Water:               29.9 Oz

Total:                      176.0 Oz


Ingredient Quantities for 1 Large and 1 Regular Red Velvet Cake

Flour:                       39.4 Oz
Sugar:                       39.4 Oz
Unsweetened Cocoa Powder:     0.7 Oz
Baking Soda:                  1.2 Oz
Salt:                         0.7 Oz
Egg:                         15.8 Oz
Buttermilk:                  31.5 Oz
Canola Oil:                  42.2 Oz
Vanilla Extract:              0.5 Oz
Red Food Coloring:            3.7 Oz
Distilled Vinegar:            0.7 Oz

Total:                      176.0 Oz


Ingredient Quantities for 2 Large and 1 Regular Lemon Cake

Butter:                      24.5 Oz
Sifted Self Rising Flour:    44.9 Oz
Sugar:                       43.2 Oz
Egg:                         25.9 Oz
Buttermilk:                  25.9 Oz
Vanilla Extract:              0.6 Oz
Filling - Egg Yolk:          51.6 Oz
Filling - Sugar:             32.5 Oz
Filling - Butter:             6.0 Oz
Filling - Lemon Zest:        32.8 Oz

Total:                      288.0 Oz
____________________________________________________________________________________________________________________________________________________________________________________
"""