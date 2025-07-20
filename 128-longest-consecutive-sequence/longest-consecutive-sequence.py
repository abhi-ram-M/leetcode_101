class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set()
        for i in nums:
            set_nums.add(i)
        longest = 0
        for num in set_nums:
            if num-1 not in set_nums:
                x = num
                count = 1
                while x+1 in set_nums:
                    count += 1
                    x += 1
                longest = max(longest,count)
        return longest



                