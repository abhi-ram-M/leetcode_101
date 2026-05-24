class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        if 1 <= n <= 10**5:
            mapp = {}
            for n in nums:
                if n in mapp:
                    return True
                mapp[n] = mapp.get(n,0)+1
            return False

        