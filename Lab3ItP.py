"""
____________________________________________________________________________________________________________________________________________________________________________________
Filename:      Lab3ItP.py

Author:        Sucheer Maddury

Date:          2021.07.07

Modifications: Sucheer Maddury – 2021.07.08
               Sucheer Maddury - 2021.07.09

Description:   This program demonstrates the use of functions to:
               1) perform indentation
               2) center a string on the screen using indentation
               3) prompt the user for a string & screen width, center the string, and print the returned number of indentations
____________________________________________________________________________________________________________________________________________________________________________________
"""
"""
____________________________________________________________________________________________________________________________________________________________________________________
Function:      Indent(user_string, number_of_spaces)

Parameters:    user_string - user-inputed string to indented and printed
               number_of_spaces - number of spaces to be indented

Outputs:       Prints the string with indentation with user-inputed number of spaces

Returns:       None

Author:        Sucheer Maddury

Date:          2021.07.07

Modifications: Sucheer Maddury - 2021.07.08

Description:   This function prints a string with a user-inputed number of white spaces indented in-front of it.
____________________________________________________________________________________________________________________________________________________________________________________
"""
def indent(user_string, number_of_spaces):
    indented_string=int(number_of_spaces)*" "+str(user_string)
    print(indented_string)
"""
____________________________________________________________________________________________________________________________________________________________________________________
Function:      Center(user_string, number_of_spaces)

Parameters:    user_string - user-inputed string to indented and printed
               screen_width - number of spaces that the user-screen spans, to be used to calculate how much the string should be indented to center the string

Outputs:       Prints the string with the apporpriate indentation to center the string

Returns:       Number of white spaces it took to center the string

Author:        Sucheer Maddury

Date:          2021.07.08

Modifications: None

Description:   This function prints a string centered in the middle of the screen given a user-inputed screen width.
____________________________________________________________________________________________________________________________________________________________________________________
"""
def center(user_string, screen_width):
    string_length=len(user_string)
    left_indentation=(int(screen_width)-string_length)//2
    indent(user_string, left_indentation)
    return left_indentation
"""
____________________________________________________________________________________________________________________________________________________________________________________
Function:      read_n_center_text()

Parameters:    None

Outputs:       Centered user-inputed string and number of white spaces used to indent the string to the center of the screen

Returns:       None

Author:        Sucheer Maddury

Date:          2021.07.08

Modifications: Sucheer Maddury - 2021.07.09

Description:   Calls the Center() function and then prints the returned number of white spaces the Center() function used.
____________________________________________________________________________________________________________________________________________________________________________________
"""
def read_n_center_text():
    user_string=input("Type Text String: ")
    screen_width=input("Enter Screen Width: ")
    print("Indented by", center(user_string, screen_width), "white spaces")
"""
RESULTS:
indent()
____________________________________________________________________________________________________________________________________________________________________________________
====================== RESTART: C:\Users\sumad\Lab3ItP.py ======================
>>> indent("Hello", 0)
Hello
>>> indent("Hi", 5)
     Hi
____________________________________________________________________________________________________________________________________________________________________________________
read_n_center_text()
____________________________________________________________________________________________________________________________________________________________________________________
====================== RESTART: C:\Users\sumad\Lab3ItP.py ======================
>>> read_n_center_text()
Type Text String: my lucky number is 888
Enter Screen Width: 80
                             my lucky number is 888
Indented by 29 white spaces
____________________________________________________________________________________________________________________________________________________________________________________
"""





