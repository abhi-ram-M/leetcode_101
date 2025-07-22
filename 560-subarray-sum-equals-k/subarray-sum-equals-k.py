class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
       
        n = len(nums)
        if (1 <= n <= 2 * 10**4):
            res = 0
            prefix_sums = {0:1}
            curr_sum = 0
            for num in nums:
                curr_sum += num
                diff = curr_sum -k
                res += prefix_sums.get(diff,0)
                prefix_sums[curr_sum] = prefix_sums.get(curr_sum,0)+1
            return res
                

        

            

