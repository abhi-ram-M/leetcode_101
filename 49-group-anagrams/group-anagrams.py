class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for word in strs:
            k = [0]*26
            for ch in word:
                k[ord(ch)-ord('a')] += 1
            key = tuple(k)
            if key in anagrams:
                anagrams[key].append(word)
            else:
                anagrams[key] = [word]
        return list(anagrams.values())



        

        
                

