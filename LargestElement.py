class Solution:
     def Largest(self,arr):
         max_value=arr[0]
         for num in arr[1:]:
            if  num>max_value:
                  max_value=num
         return max_value

if __name__=="__main__":
    arr = [1, 8, 7, 56, 90]
    obj=Solution()
    print(obj.Largest(arr))





















