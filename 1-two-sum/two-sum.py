class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapp = {}
        for ind,val in enumerate(nums):
            k = target - val
            if k in mapp:
                return [ind,mapp[k]]
            mapp[val] = ind


