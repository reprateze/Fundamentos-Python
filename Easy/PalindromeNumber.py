class Solution:
    def isPalindrome(self, x: int) -> bool:
        aux = str(x)
        return aux == aux[::-1]
    

num = int(input("Informe um numero para verificacao:"))

aux = Solution()

result = aux.isPalindrome(num)

print(result)