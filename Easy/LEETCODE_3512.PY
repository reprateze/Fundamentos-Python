from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        return sum(nums) % k


aux = [3, 9, 7]
k = 5

solution = Solution()

print(solution.minOperations(aux, k))