# Array Search
class Solution:
    def ArraySearch(self,arr,x):
        for i in range(len(arr)):
            if arr[i]==x:
                return i
        return -1


if __name__=="__main__":
    arr=[1,2,3,4,5,6,7,8,9]
    x=5
    sol=Solution()
    print(sol.ArraySearch(arr,x))