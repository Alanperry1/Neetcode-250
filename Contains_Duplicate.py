# Time Complexity: O(n) - Single pass through the array
# Space Complexity: O(n) - Hash map stores up to n elements
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen={}
        for i,num in enumerate(nums):
            if num in seen:
                return True
            seen[num]=i
        return False
