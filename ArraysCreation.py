# There are six different ways to create an array
#array()
#linspace()
#arange()
#zeros()
#ones()
#d.type prints the data type of the elements
from numpy import*
arr= array([4,7,89,98,56,45])
print(arr.dtype)
# one float value converts the whole array into float
from numpy import *
arr=array([4,5,6,7,3,5.4])
print(arr.dtype)
from numpy  import *
arr=array([4,5,6,7,3,5],float)
print(arr.dtype)
#linspace
# divides the output into ten parts
from numpy import *
arr=linspace(2,16,10)
print(arr)
#arange: which the third part tells how many values to skip
from numpy import *
arr=arange(1,15,2)
print(arr)
#logspace- num: tells how many parts to split
from numpy import *
arr=logspace(1,40,5)
print(arr)
