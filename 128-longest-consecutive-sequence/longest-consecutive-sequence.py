class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) > 0:
            set_nums = set(nums)
            longest =1
            for n in set_nums:
                
                if n-1 not in set_nums:
                    num = n
                    count = 0
                    while num+1 in set_nums:
                        count += 1
                        num += 1
                    longest = max(longest,count+1)
            return longest
        return 0


        



                