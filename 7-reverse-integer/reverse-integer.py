class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return x
        if x<0 :
            sign = -1
        else:
            sign = +1
        x = abs(x)
        reverse = 0

        while x>0:
           reverse = (reverse * 10) + (x%10)
           x //= 10
        if reverse >2**31:
            return 0
        return sign*reverse