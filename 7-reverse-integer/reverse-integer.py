class Solution(object):
    def reverse(self, x):
        if -2**31 <= x <= 2**31 - 1 and x != 0:
            sign = -1 if x < 0 else 1
            x = abs(x)
            y = 0
            while x != 0:
                y = y * 10 + x % 10
                x = x // 10
            y = sign * y
            return y if -2**31 <= y <= 2**31 - 1 else 0
        else:
            return 0
