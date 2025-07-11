class Solution(object):
    def isPalindrome(self, x):
        if x<0:
            return False
        elif x <= 2**31 - 1:
            z = x
            y=0
            while z>0:
                y = y*10 + z%10
                z = z// 10
            return y==x

        