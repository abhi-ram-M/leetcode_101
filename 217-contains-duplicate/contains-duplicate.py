class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        if 1 <= n <= 10**5:
            mapp = {}
            for i in range(n):
                if nums[i] in mapp:
                    return True
                mapp[nums[i]] = mapp.get(nums[i],0)+1
            return False
            

        