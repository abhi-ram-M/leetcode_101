class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if (1 <= n <= 10**4):
            temp = []
            for i in range(n):
                if nums[i] != 0:
                    temp.append(nums[i])
            nz = len(temp)
            for j in range(nz):
                nums[j] = temp[j]
            for k in range(nz,n):
                nums[k] = 0
        