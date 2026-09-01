from typing import List

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = []

        for i in range(len(nums)):
           ans.append(nums[nums[i]])
            

        return ans

s = Solution()

print(s.buildArray(nums = [0,2,1,5,3,4]))
            