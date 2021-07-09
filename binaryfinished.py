import math
rawdata=input("Enter numbers seperated by a space in least to greatest: ")
usablelist=rawdata.split(" ")
value=input("Enter the value: ")
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
print("Index:", str(answer))
ordinaldict={0:"1st",1:"2nd",2:"3rd"}
try:
    ordinaldict[answer]
    ordinal=ordinaldict[answer]
except KeyError:
    ordinal=str(answer+1)+"th"
print(str(value),"is the",ordinal,"value in the list.")

    


