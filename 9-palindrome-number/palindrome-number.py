class Solution(object):
    def isPalindrome(self, x):
        if x<0:
            return False
        z = x
        y = 0
        while z:
            y = y*10 + z%10
            z = z//10
        return y == x


        