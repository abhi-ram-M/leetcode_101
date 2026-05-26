from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for word in strs:
            lst = [0]*26
            for letter in word:
                lst[ord(letter)-ord('a')] += 1
            lst = tuple(lst)
            dic[lst].append(word)
        return list(dic.values())






        

        
                

