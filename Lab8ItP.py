"""
____________________________________________________________________________________________________________________________________________________________________________________
Filename:      Lab8ItP.py

Author:        Sucheer Maddury

Date:          2021.07.28

Modifications: Sucheer Maddury - 2021.07.29

Description:   This program demonstrates the use of OOP (Object Oriented Programming) to:
               1) Define a class with changeable attributes to decide cake type
               2) Calculate an ingredient list based on the defined attributes with a function built into the object
               3) Print them out with a function built into the object
____________________________________________________________________________________________________________________________________________________________________________________
"""
class cake:
    """
    ____________________________________________________________________________________________________________________________________________________________________________________
    Class:         cake(type,size)

    Parameters:    type - the cake flavor (1: Chocolate, 2: Red Velvet, or 3: Lemon)  
                   size - the size of the cake (L: Large, R: Regular) 

    Inputs:        None

    Outputs:       __str__() function prints all the ingredients and their weights in order

    Returns:       calc_ingrd() function returns a list of the ingredient weights in order

    Author:        Sucheer Maddury

    Date:          2021.07.28

    Modifications: Sucheer Maddury - 2021.07.29

    Description:   This class defines a cake object that can be 1 of 3 flavors and 1 of 2 sizes
    ____________________________________________________________________________________________________________________________________________________________________________________
    """
    def __init__(self,type,size):
        #Instead of using if loops to determine recipe, name, and other attributes, dictionaries and indexes are used to save time and promote efficiency and modularity
        self.possible_recipes={1:{"FLOUR_PCT":15.8,"SUGAR_PCT":24.5,"BUTTER_PCT":0.0,"UNSWEETENED_COCOA_POWDER_PCT":5.6,"BAKING_POWDER_PCT":0.4,"BAKING_SODA_PCT":0.6,"SALT_PCT":0.4,"CANOLA_OIL_PCT":8.1,"EGG_PCT":9.0,
        "SIFTED_SELF_RISING_FLOUR_PCT":0.0,"BUTTERMILK_PCT":18.0,"RED_FOOD_COLOR_PCT":0.0,"VANILLA_EXTRACT_PCT":0.6,"BOILING_WATER_PCT":17.0,"DISTILLED_VINEGAR_PCT":0.0,"EGG_YOLK_FILLING_PCT":0.0,
        "SUGAR_FILLING_PCT":0.0,"BUTTER_FILLING_PCT":0.0,"LEMON_ZEST_FILLING_PCT":0.0},
        2:{"FLOUR_PCT":22.4,"SUGAR_PCT":22.4,"BUTTER_PCT":0.0,"UNSWEETENED_COCOA_POWDER_PCT":0.4,"BAKING_POWDER_PCT":0.0,"BAKING_SODA_PCT":0.7,"SALT_PCT":0.4,"CANOLA_OIL_PCT":24.0,
        "EGG_PCT":9.0,"SIFTED_SELF_RISING_FLOUR_PCT":0.0,"BUTTERMILK_PCT":17.9,"RED_FOOD_COLOR_PCT":2.1,"VANILLA_EXTRACT_PCT":0.3,"BOILING_WATER_PCT":0.0,"DISTILLED_VINEGAR_PCT":0.4,
        "EGG_YOLK_FILLING_PCT":0.0,"SUGAR_FILLING_PCT":0.0,"BUTTER_FILLING_PCT":0.0,"LEMON_ZEST_FILLING_PCT":0.0},
        3:{"FLOUR_PCT":0.0,"SUGAR_PCT":15.0,"BUTTER_PCT":8.5,"UNSWEETENED_COCOA_POWDER_PCT":0.0,"BAKING_POWDER_PCT":0.0,"BAKING_SODA_PCT":0.0,"SALT_PCT":0.0,"CANOLA_OIL_PCT":0.0,
        "EGG_PCT":9.0,"SIFTED_SELF_RISING_FLOUR_PCT":15.6,"BUTTERMILK_PCT":9.0,"RED_FOOD_COLOR_PCT":0.0,"VANILLA_EXTRACT_PCT":0.2,"BOILING_WATER_PCT":0.0,"DISTILLED_VINEGAR_PCT":0.0,
        "EGG_YOLK_FILLING_PCT":17.9,"SUGAR_FILLING_PCT":11.3,"BUTTER_FILLING_PCT":2.1,"LEMON_ZEST_FILLING_PCT":11.4}}
        self.possible_names={1:"Chocolate",2:"Red Velvet",3:"Lemon"}
        self.possible_weights={"L":112,"l":112,"R":64,"r":64}
        self.size_possible_full_names={"L":"Large","l":"Large","R":"Regular","r":"Regular"}
        self.ingrd_names_list=["Flour","Sugar","Butter","Unsweetened Cocoa Powder","Baking Powder","Baking Soda","Salt","Canola Oil","Egg","Sifted Self Rising Flour",
        "Buttermilk","Red Food Coloring","Vanilla Extract","Boiling Water","Distilled Vinegar","Filling - Egg Yolk","Filling - Sugar","Filling - Butter","Filling - Lemon Zest"]
        self.type=type
        self.size=size
        self.recipe=self.possible_recipes[type]
        self.name=self.possible_names[type]
        self.size_full_name=self.size_possible_full_names[size]
        self.weight=self.possible_weights[size]
        self.ingrd_list=self.calc_ingrd(self.weight,self.recipe)
    def __str__(self):
        #Uses already defined attributes to print
        print()
        self.header="Ingredient Quantities for "+self.size_full_name+" "+self.name+" Cake"
        print(self.header)
        print()
        for index in range(0,len(self.ingrd_list)):
            if self.ingrd_list[index] !=0:
                print("%-28s%5.1f Oz" % (self.ingrd_names_list[index]+": ", self.ingrd_list[index]))
        return ""
    def calc_ingrd(self,weight,recipe):
        #This function must be called to define the ingrd_list attribute
        self.ingrd_list=[]
        for key in recipe:
            self.ingrd_list.append(weight*recipe[key]/100)
        return self.ingrd_list

"""
____________________________________________________________________________________________________________________________________________________________________________________
TEST CODE (6 CASES, OBJECT INSTANTIATION)
____________________________________________________________________________________________________________________________________________________________________________________
"""
reg_choc_cake=cake(1,"R")
lrg_choc_cake=cake(1,"L")
reg_redv_cake=cake(2,"R")
lrg_redv_cake=cake(2,"L")
reg_lemo_cake=cake(3,"R")
lrg_lemo_cake=cake(3,"L")

"""
____________________________________________________________________________________________________________________________________________________________________________________
RESULTS PRINTING 
____________________________________________________________________________________________________________________________________________________________________________________
"""
print(reg_choc_cake)
print(lrg_choc_cake)
print(reg_redv_cake)
print(lrg_redv_cake)
print(reg_lemo_cake)
print(lrg_lemo_cake)

"""
RESULTS:
____________________________________________________________________________________________________________________________________________________________________________________
====================== RESTART: C:\Users\sumad\Lab8ItP.py ======================

Ingredient Quantities for Regular Chocolate Cake

Flour:                       10.1 Oz
Sugar:                       15.7 Oz
Unsweetened Cocoa Powder:     3.6 Oz
Baking Powder:                0.3 Oz
Baking Soda:                  0.4 Oz
Salt:                         0.3 Oz
Canola Oil:                   5.2 Oz
Egg:                          5.8 Oz
Buttermilk:                  11.5 Oz
Vanilla Extract:              0.4 Oz
Boiling Water:               10.9 Oz


Ingredient Quantities for Large Chocolate Cake

Flour:                       17.7 Oz
Sugar:                       27.4 Oz
Unsweetened Cocoa Powder:     6.3 Oz
Baking Powder:                0.4 Oz
Baking Soda:                  0.7 Oz
Salt:                         0.4 Oz
Canola Oil:                   9.1 Oz
Egg:                         10.1 Oz
Buttermilk:                  20.2 Oz
Vanilla Extract:              0.7 Oz
Boiling Water:               19.0 Oz


Ingredient Quantities for Regular Red Velvet Cake

Flour:                       14.3 Oz
Sugar:                       14.3 Oz
Unsweetened Cocoa Powder:     0.3 Oz
Baking Soda:                  0.4 Oz
Salt:                         0.3 Oz
Canola Oil:                  15.4 Oz
Egg:                          5.8 Oz
Buttermilk:                  11.5 Oz
Red Food Coloring:            1.3 Oz
Vanilla Extract:              0.2 Oz
Distilled Vinegar:            0.3 Oz


Ingredient Quantities for Large Red Velvet Cake

Flour:                       25.1 Oz
Sugar:                       25.1 Oz
Unsweetened Cocoa Powder:     0.4 Oz
Baking Soda:                  0.8 Oz
Salt:                         0.4 Oz
Canola Oil:                  26.9 Oz
Egg:                         10.1 Oz
Buttermilk:                  20.0 Oz
Red Food Coloring:            2.4 Oz
Vanilla Extract:              0.3 Oz
Distilled Vinegar:            0.4 Oz


Ingredient Quantities for Regular Lemon Cake

Sugar:                        9.6 Oz
Butter:                       5.4 Oz
Egg:                          5.8 Oz
Sifted Self Rising Flour:    10.0 Oz
Buttermilk:                   5.8 Oz
Vanilla Extract:              0.1 Oz
Filling - Egg Yolk:          11.5 Oz
Filling - Sugar:              7.2 Oz
Filling - Butter:             1.3 Oz
Filling - Lemon Zest:         7.3 Oz


Ingredient Quantities for Large Lemon Cake

Sugar:                       16.8 Oz
Butter:                       9.5 Oz
Egg:                         10.1 Oz
Sifted Self Rising Flour:    17.5 Oz
Buttermilk:                  10.1 Oz
Vanilla Extract:              0.2 Oz
Filling - Egg Yolk:          20.0 Oz
Filling - Sugar:             12.7 Oz
Filling - Butter:             2.4 Oz
Filling - Lemon Zest:        12.8 Oz
____________________________________________________________________________________________________________________________________________________________________________________
"""