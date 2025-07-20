class Solution:
    def firstUniqChar(self, s: str) -> int:
        mapp = {}
        for ch in s:
            mapp[ch] = mapp.get(ch,0)+1
        for k,ch in enumerate(s):
            if mapp[ch] == 1:
                return k
        return -1
