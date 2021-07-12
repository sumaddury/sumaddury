#This is a program for the sorting method Bubble Sort.
import math
#Takes user input and splits the input into a list of integers/floats.
raw_data=(input("Enter numbers seperated by a space in least to greatest: ")).split(" ")
usable_data=[]
for word_number in raw_data:
    usable_data.append(eval(word_number))

#Bubble Sort is an array-sorting algorithm that works by progressively checking pairs of consecutive elements, and switching them if the order is not in least-to-greatest in this case.
def bubble_sort(user_list):
    list_length=len(user_list)
    for iteration in range(list_length):
        for itemindex in range(0, list_length-iteration-1):
            #Checks if the pair is in least-to-greatest, and if not, switches their order.
            if user_list[itemindex] > user_list[itemindex+1]:
                user_list[itemindex], user_list[itemindex+1] = user_list[itemindex+1], user_list[itemindex]
    #Returns the now-sorted list.
    return user_list

print(bubble_sort(usable_data))