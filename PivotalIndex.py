class Solution:
    def pivotIndex(self, nums):
        total = sum(nums)
        left_sum = 0

        for i, num in enumerate(nums):
            if left_sum == (total - left_sum - num):
                return i
            left_sum += num

        return -1


if __name__ == "__main__":
    nums = [1, 7, 3, 6, 5, 6]
    obj = Solution()
    print(obj.pivotIndex(nums))