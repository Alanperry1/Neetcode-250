# Time Complexity: O(n * k * log k) - n strings, each of length k, sorting takes k log k
# Space Complexity: O(n * k) - Hash map stores all strings
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs)==0:
            return []
        
        anagram={}
        
        for str in strs:
            new=''.join(sorted(str))
            if new in anagram.keys():
                anagram[new].append(str)
            else:
                anagram[new]=[str]
        
        return list(anagram.values())
