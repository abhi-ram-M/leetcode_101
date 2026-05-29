class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = []
        set_nums = set(nums)
        for i in range(1,n+1):
            if i not in set_nums:
                result.append(i)
        return result

        