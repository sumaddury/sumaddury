"""
Lab 2
Sucheer Maddury
6/30/2021
"""

individual_book_price=eval(input("Enter the price of the book: "))
quantity=eval(input("Enter the number of books: "))
books_cost=(0.6*individual_book_price)*quantity
shipping_cost=3.0+(0.75*(quantity-1.0))
total_cost=books_cost+shipping_cost
print("The total cost for", int(quantity), "books is:",total_cost)

"""
RESULT:
____________________________________________________________________________________________________________________________________________________________________________________
PS C:\Windows\System32\work> & C:/Users/sumad/AppData/Local/Programs/Python/Python38-32/python.exe c:/Users/sumad/Lab2ItP.py
Enter the price of the book: 24.95
Enter the number of books: 60
The total cost for 60 books is: 945.4499999999999
____________________________________________________________________________________________________________________________________________________________________________________
"""