import re
file=open('C:/Users/sumad/regex_sum_1172315.txt')
y=[]
for line in file:
    x=re.findall('[0-9]+',line)
    if len(x)>0:
        for numberstring in x:
            y.append(numberstring)
list=[int(element) for element in y]
sum=sum(list)
print(sum)

