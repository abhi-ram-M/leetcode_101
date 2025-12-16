class Solution(object):
    def reverse(self, x):
        if x == 0:
            return 0

        sign = -1 if x<0 else 1
        x = abs(x)
        y = 0
        while x:
            y = y*10 + x%10
            x = x//10
        if -2**31 < y < 2**31-1:
            return sign*y
        else:
            return 0
            