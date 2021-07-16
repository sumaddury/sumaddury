
#This is a program for the sorting method Radix Sort.
import math
#Takes user input and splits the input into a list of integers/floats.
raw_data=(input("Enter numbers seperated by a space: ")).split(" ")
usable_data=[]
for word_number in raw_data:
    usable_data.append(eval(word_number))

#Takes a list and converts it into a list of sub-lists, each sub-list containing all the numbers from the original list of a certain place value.
def bucket_sort(user_list):
    temp_user_list=[]
    for element in user_list:
        temp_user_list.append(element)
    highest_digit_count=1
    temporary_number_storage=[]
    bucket_list=[]
    deletion_numbers=[]
    for element in temp_user_list:
        if len(str(element))>highest_digit_count:
            highest_digit_count=len(str(element))
    for digit_count in range(1,highest_digit_count+1):
        for element in temp_user_list:
            if len(str(element))==digit_count:
                temporary_number_storage.append(element)
                deletion_numbers.append(element)
        for number in deletion_numbers:
            temp_user_list.remove(number)
        bucket_list.append(temporary_number_storage)
        deletion_numbers=[]
        temporary_number_storage=[]
    return bucket_list

#Sorts a list by a certain place value
def place_value_sort(user_list, digit):
    string_list=[]
    for int_item in user_list:
        string_list.append(str(int_item))
    for iteration in range(len(user_list)):
        for itemindex in range(0, len(user_list)-iteration-1):
            if int((str(string_list[itemindex]))[len(str(int_item))-digit]) > int((str(string_list[itemindex+1]))[len(str(int_item))-digit]):
                string_list[itemindex], string_list[itemindex+1] = string_list[itemindex+1], string_list[itemindex]
    user_list=[int(string_item) for string_item in string_list]
    return user_list

#First calls the bucket_sort() function on the user_list, and then calls the place_value_sort() function on each place value for each of the sub-lists.
def radix_sort(user_list):
    bucket_list=bucket_sort(user_list)
    user_list=[]
    for single_place_value_list in bucket_list:
        for digit in range(1,len(str(single_place_value_list[0]))+1):
            single_place_value_list=place_value_sort(single_place_value_list,digit)
        user_list.extend(single_place_value_list)
    return user_list

print(radix_sort(usable_data))

