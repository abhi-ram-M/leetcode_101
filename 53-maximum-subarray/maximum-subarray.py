class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        if 1 <= n <= 10**5:
            maxi = float('-inf')
            total = 0
            for i in range(0,n):
                total += nums[i]
                maxi = max(total,maxi)
                if total<0:
                    total = 0
            return maxi
            