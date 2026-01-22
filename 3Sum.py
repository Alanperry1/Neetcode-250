# Time Complexity: O(n^2) - O(n log n) for sorting + O(n^2) for two-pointer approach
# Space Complexity: O(1) or O(n) - Depends on sorting algorithm (ignoring output space)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result=[]
        for i in range(len(nums)-2):
            left,right=i+1,len(nums)-1
            if i>0 and nums[i]==nums[i-1]:
                continue
            while left<right:
                total=nums[i]+nums[left]+nums[right]
                if total==0:
                    result.append([nums[i],nums[left],nums[right]])
                    while left<right and nums[left]==nums[left+1]:
                        left+=1
                    while left<right and nums[right]==nums[right-1]:
                        right-=1

                    left+=1
                    right-=1
                elif total>0:
                    right-=1
                elif total<0:
                    left+=1
                    
        return result
