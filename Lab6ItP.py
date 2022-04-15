"""
____________________________________________________________________________________________________________________________________________________________________________________
Filename:      Lab6ItP.py

Author:        Sucheer Maddury

Date:          2021.07.20

Modifications: Sucheer Maddury - 2021.07.21

Description:   This program demonstrates the use of functions and files to:
               1) read the cake orders from a text file
               2) calculate how much of each ingredient is needed by calling 1 of 3 functions with the correct parameters
               3) convert these to the appropriate unit
               4) write these results to another text file in an organized fashion
____________________________________________________________________________________________________________________________________________________________________________________
"""
"""
************************************************************************************************************************************************************************************
PART 1: Write the ingredients list to a file
************************************************************************************************************************************************************************************
"""
def chocolate_cake_calculator(weight,file_handle):
    """
    ____________________________________________________________________________________________________________________________________________________________________________________
    Function:      chocolate_cake_calculator(weight,file_handle)

    Parameters:    weight - the weight of the desired cake size in pounds (lbs)
                   file_handle - the opened file handle the user wishes to open and write to

    Inputs:        None

    Outputs:       Writes the cake type and cake size in addition to the amount of each ingredient needed in ounces (oz), and the total weight in ounces (oz) to a file in the argument

    Returns:       None

    Author:        Sucheer Maddury

    Date:          2021.07.20

    Modifications: None

    Description:   This function:
                   1) receives the weight and file_handle parameters
                   2) multiples the weight value by the correct percentage for each of the 11 ingredients
                   3) converts the values for each of the 11 ingredients into ounces (oz)
                   4) writes them to the specified file
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
    file_handle.write(str(weight)+" Lb "+"Chocolate Cake Ingredient list:"+"\n"+"\n")
    file_handle.write("Flour:                   "+flour+" Oz"+"\n")
    file_handle.write("Sugar:                   "+sugar+" Oz"+"\n")
    file_handle.write("Unsweetened Cocoa Powder:"+unsweetened_cocoa_powder+" Oz"+"\n")
    file_handle.write("Baking Powder:           "+baking_powder+" Oz"+"\n")
    file_handle.write("Baking Soda:             "+baking_soda+" Oz"+"\n")
    file_handle.write("Salt:                    "+salt+" Oz"+"\n")
    file_handle.write("Egg:                     "+egg+" Oz"+"\n")
    file_handle.write("Buttermilk:              "+buttermilk+" Oz"+"\n")
    file_handle.write("Canola Oil:              "+canola_oil+" Oz"+"\n")
    file_handle.write("Vanilla Extract:         "+vanilla_extract+" Oz"+"\n")
    file_handle.write("Boiling Water:           "+boiling_water+" Oz"+"\n")
    file_handle.write("\n"+"Total:                   "+total+"  Oz"+"\n"+"\n"+"\n")

def red_velvet_cake_calculator(weight,file_handle):
    """
    ____________________________________________________________________________________________________________________________________________________________________________________
    Function:      red_velvet_cake_calculator(weight,file_handle)

    Parameters:    weight - the weight of the desired cake size in pounds (lbs)
                   file_handle - the opened file handle the user wishes to open and write to
    
    Inputs:        None

    Outputs:       Writes the cake type and cake size in addition to the amount of each ingredient needed in ounces (oz), and the total weight in ounces (oz) to a file in the argument

    Returns:       None

    Author:        Sucheer Maddury

    Date:          2021.07.20

    Modifications: None

    Description:   This function:
                   1) receives the weight and file_handle parameters
                   2) multiples the weight value by the correct percentage for each of the 11 ingredients
                   3) converts the values for each of the 11 ingredients into ounces (oz)
                   4) writes them to the specified file
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
    file_handle.write(str(weight)+" Lb "+"Red Velvet Cake Ingredient list:"+"\n"+"\n")
    file_handle.write("Flour:                   "+flour+" Oz"+"\n")
    file_handle.write("Sugar:                   "+sugar+" Oz"+"\n")
    file_handle.write("Baking Soda:             "+baking_soda+" Oz"+"\n")
    file_handle.write("Salt:                    "+salt+" Oz"+"\n")
    file_handle.write("Unsweetened Cocoa Powder:"+unsweetened_cocoa_powder+" Oz"+"\n")
    file_handle.write("Canola Oil:              "+canola_oil+" Oz"+"\n")
    file_handle.write("Buttermilk:              "+buttermilk+" Oz"+"\n")
    file_handle.write("Egg:                     "+egg+" Oz"+"\n")
    file_handle.write("Red Food Coloring:       "+red_food_coloring+" Oz"+"\n")
    file_handle.write("Vanilla Extract:         "+vanilla_extract+" Oz"+"\n")
    file_handle.write("Distilled Vinegar:       "+distilled_vinegar+" Oz"+"\n")
    file_handle.write("\n"+"Total:                   "+total+"  Oz"+"\n"+"\n"+"\n")

def lemon_cake_calculator(weight,file_handle):
    """
    ____________________________________________________________________________________________________________________________________________________________________________________
    Function:      lemon_cake_calculator(weight,file_handle)

    Parameters:    weight - the weight of the desired cake size in pounds (lbs)
                   file_handle - the opened file handle the user wishes to open and write to

    Inputs:        None

    Outputs:       Writes the cake type and cake size in addition to the amount of each ingredient needed in ounces (oz), and the total weight in ounces (oz) to a file in the argument

    Returns:       None

    Author:        Sucheer Maddury

    Date:          2021.07.20

    Modifications: None

    Description:   This function:
                   1) receives the weight and file_handle parameters
                   2) multiples the weight value by the correct percentage for each of the 11 ingredients
                   3) converts the values for each of the 11 ingredients into ounces (oz)
                   4) writes them to the specified file
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
    file_handle.write(str(weight)+" Lb "+"Lemon Cake Ingredient list:"+"\n"+"\n")
    file_handle.write("Butter:                  "+butter+" Oz"+"\n")
    file_handle.write("Sugar:                   "+sugar+" Oz"+"\n")
    file_handle.write("Egg:                     "+egg+" Oz"+"\n")
    file_handle.write("Sifted Self-Rising Flour:"+sifted_self_rising_flour+" Oz"+"\n")
    file_handle.write("Buttermilk:              "+buttermilk+" Oz"+"\n")
    file_handle.write("Vanilla Extract:         "+vanilla_extract+" Oz"+"\n")
    file_handle.write("\n"+"Fillings:"+"\n"+"\n")
    file_handle.write("Egg Yolk:                "+yolk_egg_filling+" Oz"+"\n")
    file_handle.write("Sugar (Filling):         "+filling_sugar+" Oz"+"\n")
    file_handle.write("Butter (Filling):        "+filling_butter+" Oz"+"\n")
    file_handle.write("Lemon Juice and Zest:    "+lemon_juice_zest_filling+" Oz"+"\n")
    file_handle.write("\n"+"Total:                   "+total+"  Oz"+"\n"+"\n"+"\n")

def cake_list_interpreter(list_cake_types,list_cake_sizes,file_handle):
    """
    ____________________________________________________________________________________________________________________________________________________________________________________
    Function:      cake_list_interpreter(list_cake_types,list_cake_sizes,file_handle)

    Parameters:    list_cake_types - list of all the cake-type numbers (1: chocolate, 2: red velvet, 3: lemon)
                   list_cake_sizes - list of all the cake-sizes (R: regular, L: large)
                   file_handle - the opened file handle the user wishes to open and write to

    Inputs:        None

    Outputs:       Calls the ingredient_function_caller() function with the correct arguments, which will then call another function that writes to a file

    Returns:       None

    Author:        Sucheer Maddury

    Date:          2021.07.20

    Modifications: Sucheer Maddury - 2021.07.21

    Description:   This function:
                   1) receives list_cake_types, list_cake_sizes, and file_handle parameters
                   2) calls the ingredient_function_caller() function for each of the cake type-cake size pairs on the correct file
    ____________________________________________________________________________________________________________________________________________________________________________________
    """
    for index in range(0,len(list_cake_types)):
        ingredient_function_caller(list_cake_types[index],list_cake_sizes[index],file_handle)

def ingredient_function_caller(type,size,file_handle):
    """
    ____________________________________________________________________________________________________________________________________________________________________________________
    Function:      ingredient_function_caller(type,size,file_handle)

    Parameters:    type - the flavor of the cake (1: chocolate, 2: red velvet, 3: lemon)
                   size - the size of the cake (R: regular, L: large)
                   file_handle - the opened file handle the user wishes to open and write to

    Inputs:        None

    Outputs:       Calls the appropriate function with weight, which then writes the ingredients to a text file

    Returns:       None

    Author:        Sucheer Maddury

    Date:          2021.07.20

    Modifications: Sucheer Maddury - 2021.07.21

    Description:   This function:
                   1) receives type, size, and file_handle parameters
                   2) finds the appropriate function and the appropriate weight
                   3) calls the appropriate function with the correct weight and file arguments
    ____________________________________________________________________________________________________________________________________________________________________________________
    """
    if size=="R":
        cake_weight=4
    elif size=="L":
        cake_weight=7
    else:
        file_handle.write("Invalid Cake Type and/or Size")
    if type=="1":
        chocolate_cake_calculator(cake_weight,file_handle)
    elif type=="2":
        red_velvet_cake_calculator(cake_weight,file_handle)
    elif type=="3":
        lemon_cake_calculator(cake_weight,file_handle)
    else:
        file_handle.write("Invalid Cake Type and/or Size")

"""
************************************************************************************************************************************************************************************
PART 2: Read the cake orders list from a text file
************************************************************************************************************************************************************************************
"""
def cake_order_reader(file_handle):
    """
    ____________________________________________________________________________________________________________________________________________________________________________________
    Function:      cake_order_reader(file_handle)

    Parameters:    file_handle - the opened file handle the user wishes to open and read

    Inputs:        None

    Outputs:       None

    Returns:       Returns a list of the cake types, and a list of the cake sizes

    Author:        Sucheer Maddury

    Date:          2021.07.20

    Modifications: Sucheer Maddury - 2021.07.21

    Description:   This function:
                   1) receives file_handle parameter
                   3) reads the file line-by-line
                   4) appends each cake type and cake size based on string index
                   5) returns these 2 lists
    ____________________________________________________________________________________________________________________________________________________________________________________
    """
    list_cake_types=[]
    list_cake_sizes=[]
    for line in file_handle:
        if len(line)>1:
            list_cake_types.append(line[0])
            list_cake_sizes.append(line[4])
    return([list_cake_types,list_cake_sizes])

"""
************************************************************************************************************************************************************************************
PROGRAM STARTS HERE
************************************************************************************************************************************************************************************
"""
program_read_file_name="c:/Users/sumad/cake_orders.txt"
program_write_file_name="c:/Users/sumad/cake_ingredients_list.txt"
read_file_handle=open(program_read_file_name)
program_list_cake_types, program_list_cake_sizes = cake_order_reader(read_file_handle)
read_file_handle.close()
write_file_handle=open(program_write_file_name,"w")
cake_list_interpreter(program_list_cake_types,program_list_cake_sizes,write_file_handle)
write_file_handle.close()

