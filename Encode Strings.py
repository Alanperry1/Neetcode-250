# Time Complexity: O(n) for encode, O(n) for decode - where n is total length of all strings
# Space Complexity: O(n) - Result string/list stores all characters
class Solution:

    def encode(self, strs: List[str]) -> str:
        res=''
        for string in strs:
            res+=str(len(string))+"#"+string
        
        return res
    
    def decode(self, s: str) -> List[str]:
        res,i=[],0
        while i<len(s):
            j=i
            while s[j]!="#":
                j+=1
            length=int(s[i:j])
            res.append(s[j+1:length+1+j])
            i=length+1+j
        return res
