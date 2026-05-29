class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mapp = {}
        for i in nums:
            mapp[i] = mapp.get(i,0)+1
        for key,val in mapp.items():
            if val >= (len(nums)/2):
                return key


        