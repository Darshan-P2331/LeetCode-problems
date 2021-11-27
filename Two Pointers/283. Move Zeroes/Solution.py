class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero = []
        nonzero = []
        for i in nums:
            if i == 0:
                zero.append(i)
            else:
                nonzero.append(i)
        
        nums[:] = nonzero+zero
