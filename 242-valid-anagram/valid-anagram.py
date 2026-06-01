class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mapp = {}
        for i in range(2):
            if i == 0:
                k=s
            else:
                k=t
            kk = [0]*26
            for i in k:
                kk[ord(i)-ord('a')] += 1
            mapp[k] = kk
        if mapp[s] == mapp[t]:
            return True
        else:
            return False 



