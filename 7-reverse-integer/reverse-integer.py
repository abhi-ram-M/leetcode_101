class Solution(object):
    def reverse(self, x):
        if x == 0:
            return 0
        sign = -1 if x < 0 else +1
        x = abs(x)
        y = 0
        while x>0:
            y = (y*10) +(x%10)
            x = x//10
        if y>2**31:
            return 0
        return y*sign
    
    
        