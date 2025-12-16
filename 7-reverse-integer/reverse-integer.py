class Solution(object):
    def reverse(self, x):
        sign = -1 if x < 0 else 1
        x = abs(x)
        y = 0

        while x:
            y = y * 10 + x % 10
            x //= 10

        y *= sign

        if -2**31 <= y <= 2**31 - 1:
            return y
        else:
            return 0
