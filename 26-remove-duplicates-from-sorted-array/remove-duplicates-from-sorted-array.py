class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if not (1 <= n <= 3 * 10**4):
            return

        if not n<=1:
            freq_map = {}
            for i in range(n):
                freq_map[nums[i]] = 0
            j = 0
            for k in freq_map:
                nums[j] = k
                j+=1
            return j
        else:
            return 
            
