import math
raw_data=(input("Enter numbers seperated by a space: ")).split(" ")
usable_data=[]
for word_number in raw_data:
    usable_data.append(eval(word_number))

def merge_sort(user_list):
    list_length=len(user_list)
    if list_length>1:
        center=list_length//2
        left_list=user_list[:center]
        right_list=user_list[center:]
        merge_sort(left_list)
        merge_sort(right_list)
        left_list_length=len(left_list)
        right_list_length=len(right_list)
        l_i = 0
        r_i = 0
        u_l_i = 0
        while l_i<left_list_length and r_i<right_list_length:
            if left_list[l_i]<right_list[r_i]:
                user_list[u_l_i]=left_list[l_i]
                l_i+=1
            else:
                user_list[u_l_i]=right_list[r_i]
                r_i+=1
            u_l_i+=1
        while l_i<left_list_length:
            user_list[u_l_i]=left_list[l_i]
            l_i+=1
            u_l_i+=1
        while r_i<right_list_length:
            user_list[u_l_i]=right_list[r_i]
            r_i+=1
            u_l_i+=1
    return user_list

print(merge_sort(usable_data))


