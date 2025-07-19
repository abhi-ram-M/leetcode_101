class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)

        nums  = sorted(nums)
        count = 0
        last_small = float('-inf')
        longest = 0
        for num in nums:
            if num - 1 ==last_small:
                count += 1
            elif num != last_small:
                count = 1
            last_small = num
            longest = max(longest,count)
        return longest
                