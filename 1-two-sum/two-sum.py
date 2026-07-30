class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        if n >= 2 or n < 10**4:
            mapp = {}
            for ind,val in enumerate(nums):
                k = target - val
                if k in mapp:
                    return [ind,mapp[k]]
                mapp[val] = ind


