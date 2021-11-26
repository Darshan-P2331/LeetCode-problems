# one liner solution:
class Solution(object):
    def sortedSquares(self, nums):
        return sorted ([i*i for i in nums])


# Two Pointer method
class Solution:
    def sortedSquares(self, nums: List[int]) -> int:
        res = [None for _ in nums]
        left, right = 0, len(nums)-1
        for i in range(len(nums)-1,-1,-1):
            if abs(nums[left]) > abs(nums[right]):
                res[i] = nums[left] ** 2
                left += 1
            else:
                res[i] = nums[right] ** 2
                right -= 1
        return res
