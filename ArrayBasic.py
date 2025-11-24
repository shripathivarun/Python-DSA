from array import *
vals =array('i',[1,3,69,-69,786])
newArr=array(vals.typecode,(a**2 for a in vals))
for e in newArr:
    print(e)
#while loop
#iteration
#condition
# increment decrement by yourself
i=0
while i<len(newArr):
    print(newArr[i])
    i+=1