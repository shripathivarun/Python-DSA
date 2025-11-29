class Solution:
    def isSorted(self, arr) -> bool:
        n = len(arr)

        for i in range(n - 1):       # go till second last element
            if arr[i] > arr[i + 1]:  # if current > next → not sorted
                return False

        return True                  # if no problem found → sorted
if __name__=="__main__":
    arr=[10,20,30,40,50]
    arr1=[90, 80, 100, 70, 40, 30]
    print(Solution().isSorted(arr))
    print(Solution().isSorted(arr1))


