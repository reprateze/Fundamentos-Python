from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numeros_vistos = set()
        tem_repetido = False

        for i in nums:  
            if i in numeros_vistos:
               tem_repetido = True
               break
            numeros_vistos.add(i)

        print(tem_repetido)


s = Solution()

vetor = [1, 2, 3, 2, 4, 1, 5]
s.containsDuplicate(vetor)
            
        