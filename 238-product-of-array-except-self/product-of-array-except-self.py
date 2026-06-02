import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        op = [1]
        for i in range(len(nums)-1,0,-1):
            op.append(op[-1]*nums[i])
        op = op[::-1]
        left = 1
        for i in range(len(nums)):
            op[i] = op[i]*left
            left = left*nums[i]
        return op

