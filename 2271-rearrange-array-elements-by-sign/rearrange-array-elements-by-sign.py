class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:

        n = len(nums)
        res = [0]*n
        p,n = 0,1
        for i,e in enumerate(nums):
            if e>0:
                res[p] = e
                p += 2
            else:
                res[n] = e
                n+=2
        return res



