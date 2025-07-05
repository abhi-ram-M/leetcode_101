class Solution:
    def func(self, num):
        if num == 0 or num ==1:
            return num
        else :
            return self.func(num-1)+self.func(num-2)
    def fib(self, n: int) -> int:
        if n<0 or n>30:
            return None
        ans = self.func(n)
        return ans
        