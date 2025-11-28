# Alternates in an array
class Solution:
    def getAlternatesInarray(self,arr):
        res=[]
        for i in range(0,len(arr),2):
            res.append(arr[i])
        return res
if __name__=="__main__":
    arr=[1,2,3,4,5,6]
    sol=Solution()
    print(sol.getAlternatesInarray(arr))