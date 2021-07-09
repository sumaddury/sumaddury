#This is a program for binary search, an algorithm that finds the index of a user-inputed value in an array
import math
rawdata=input("Enter a sorted list of numbers, each seperated by a white space: ")
userarray=rawdata.split(" ")
uservalue=input("Enter the value: ")
def binarysearch(usablelist, value):
    leftpointer=0
    rightpointer=len(usablelist)-1
    while True:
        middleindex=(float(leftpointer)+float(rightpointer))/2.0
        whole=middleindex.is_integer()
        if whole==True:
            median=float(usablelist[int(middleindex)])
            newmiddleforless=int(middleindex)
            newmiddleformore=int(middleindex)
        elif whole==False:
            median=(float(usablelist[math.floor(middleindex)])+float(usablelist[math.ceil(middleindex)]))/2.0
            newmiddleforless=int(math.ceil(middleindex))
            newmiddleformore=int(math.floor(middleindex))
        if median==float(value):
            answer=int(middleindex)
            break
        elif median<float(value):
            leftpointer=newmiddleformore
        elif median>float(value):
            rightpointer=newmiddleforless
        if rightpointer-leftpointer==1:
            answerdraft=leftpointer
            for searchv in usablelist[leftpointer:rightpointer+1]:
                if searchv==value:
                    answer=answerdraft
                    break
                answerdraft+=1
    return answer
finalindex=binarysearch(userarray, uservalue)
print("Index:", str(finalindex))
ordinaldict={0:"1st",1:"2nd",2:"3rd"}
try:
    ordinaldict[finalindex]
    ordinal=ordinaldict[finalindex]
except KeyError:
    ordinal=str(finalindex+1)+"th"
print(str(uservalue),"is the",ordinal,"value in the list.")

    


