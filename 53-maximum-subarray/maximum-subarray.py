class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        maxi = float('-inf')
        count = 0
        for num in nums:
            count += num
            maxi = max(count,maxi)
            if count < 0:
                count = 0
        return maxi