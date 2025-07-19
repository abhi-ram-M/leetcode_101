class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        comap = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in comap:
                return [comap[complement], i]
            comap[num] = i


