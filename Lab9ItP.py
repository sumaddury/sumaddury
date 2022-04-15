def main():
    input_handle=open("C:/Users/sumad/Downloads/lab9_input.txt")
    name_count=0
    name_len_dict={}
    for line in input_handle:
        if len(line)>0:
            name_count+=1
            name_len_dict[line.rstrip()]=len(line.rstrip())
    min_name_len=[list(name_len_dict.keys())[0],list(name_len_dict.values())[0]]
    max_name_len=[list(name_len_dict.keys())[0],list(name_len_dict.values())[0]]
    for key,value in name_len_dict:
        if value>max_name_len[1]:
            max_name_len[0],max_name_len[1]=key,value
        elif value<min_name_len[1]:
            min_name_len[0],min_name_len[1]=key,value
    print("There are",name_count,"names in the class list")
    print("The shortest name is",min_name_len[0],"and has",min_name_len[1],"characters")
    print("The longest name is",max_name_len[0],"and has",max_name_len[1],"characters")
    print("\n")
    add_name()
    sentinel="y"
    while sentinel=="y" or sentinel=="Y":
        print("\n")
        print_names(get_length())
        print("\n")
        sentinel=input("Continue? y/n: ")


def get_length():
    valid_input_condition=False
    while valid_input_condition==False:
        name_len=input("What name length would you like? ")
        try:
            if min_name_len[1]<=name_len<=max_name_len[1]:
                valid_input_condition=True
        except:
            pass
    return name_len
    
def print_names(length):
    print("Name(s) with length",length)
    exists=False
    for key,value in name_len_dict:
        if length==value:
            exists=True
            print(key)
    if exists==False:
        print("None")

def add_name():
    name=input("Enter a name with length between",min_name_len[1],"and",max_name_len[1],": ")
    name_len_dict[name]=len(name)

name_len_dict={}
min_name_len=[]
max_name_len=[]
main()

