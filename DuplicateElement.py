# finding dup element in array
class Solution:
    def DuplicateElements(self,nums):
        seen=set()# a box that only stores UNIQUE values
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False


if __name__=="__main__":
    nums = [1, 2, 3, 1]
    nums1= [1,2,3,4]
    nums2=[1,1,1,3,3,4,3,2,4,2]
    s=Solution()
    print(s.DuplicateElements(nums))
    print(s.DuplicateElements(nums2))
    print(s.DuplicateElements(nums1))