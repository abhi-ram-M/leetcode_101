class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        count=0
        for i in range(n):
                if nums[i] != 0:
                    nums[count] = nums[i]
                    count += 1
        for i in range(count, n):
                nums[i] = 0
                            
                    
        