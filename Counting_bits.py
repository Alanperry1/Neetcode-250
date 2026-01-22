# Time Complexity: O(n * log n) - n iterations, each binary conversion is O(log n)
# Space Complexity: O(n) - Result arrays of size n+1
class Solution:
    def countBits(self, n: int) -> List[int]:
        result=[]
        new=[]
        for i in range(n+1):
            result.append(bin(i)[2:])
        for i in result:
            new.append(i.count("1"))
        return new
