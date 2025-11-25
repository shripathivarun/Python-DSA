from operator import concat

from numpy import *
arr1= array([3,5,7,9,11])
arr2= array([4,5,6,7,9])
arr3=concat(arr1)+ concat(arr2)
print(arr3)

