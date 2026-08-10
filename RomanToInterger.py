class Solution:
    def romanToInt(self, s: str) -> int:
        romanos = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        resultado = 0

        for i in range(len(s)):
            atual = romanos[s[i]]

            if i + 1 < len(s) and atual < romanos[s[i+1]]:
                resultado -= atual
            else:
                resultado += atual

        return resultado

aux = Solution()
teste = "XVII"
print(aux.romanToInt(teste))
        