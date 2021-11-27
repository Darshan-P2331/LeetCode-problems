class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i, n in enumerate(numbers):
            if target-n in numbers[i+1:]:
                return [i+1, numbers[i+1:].index(target-n)+2+i]


# Approach 2

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, h = 0, len(numbers) - 1
        while l < h:
            if numbers[l] + numbers[h] == target:
                return [l + 1, h + 1]
            if numbers[l] + numbers[h] > target:
                h -= 1
            else:
                l += 1
