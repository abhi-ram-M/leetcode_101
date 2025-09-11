class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)
        subset = []
        def backtrack(index,subset):
            if index >= n:
                result.append(subset.copy())
                return 
            subset.append(nums[index])
            backtrack(index+1,subset)
            subset.pop()
            backtrack(index+1,subset)
        backtrack(0,subset)
        return result
        




