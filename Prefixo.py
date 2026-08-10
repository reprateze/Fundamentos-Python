class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        pref = strs[0]

        for i in strs[1:]:
            while not i.startswith(pref):
                pref = pref[:-1]
                if pref == "":
                    return ""

        return pref


teste = input("Palavras para verificar prefixo: ")

lista = teste.split(",")

aux = Solution()

resultado = aux.longestCommonPrefix(lista)

print(resultado)