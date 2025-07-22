class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res ={}
        for word in strs:
            k = [0]*26
            for ch in word:
                k[ord(ch)-ord('a')] += 1
            key = tuple(k)
            if key in res:
                res[key].append(word)
            else:
                res[key] = [word]
        return list(res.values())



        

        
                

