class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        l = 0
        r = n-1
        while l<r:
            while l<r and not self.is_as(s[l]):
                l+=1
            while l<r and not self.is_as(s[r]):
                r-=1
            if s[l].lower()!=s[r].lower():
                return False
            l+=1
            r-=1
        return True


    def is_as(self,c):
        return ('a'<=c<='z') or ('A'<=c<='Z') or ('0'<=c<='9')