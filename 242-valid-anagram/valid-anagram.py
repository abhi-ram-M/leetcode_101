class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        map_1 = {}
        map_2 = {}
        for ch in s:
            map_1[ch] = map_1.get(ch,0)+1
        for ch in t:
            map_2[ch] = map_2.get(ch,0)+1
        return map_1 == map_2
        

