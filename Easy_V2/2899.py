from typing import List
class Solution:
    def lastVisitedIntegers(self, nums: List[int]) -> List[int]:
        seen = []
        ans = []
        k = 0

        for i in nums:
            if i != -1:
                seen.insert(0,i)
                k = 0

            else:
                k += 1

                if k <= len(seen):
                    ans.append(seen[k-1])

                else:
                    ans.append(-1)

        return ans


    
nums = [1,2,-1,-1,-1]


s = Solution()

print(s.lastVisitedIntegers(nums))
          
            
               







