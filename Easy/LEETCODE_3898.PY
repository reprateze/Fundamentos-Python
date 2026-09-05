class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        resultado = []

        for linha in matrix:
            cont = 0

            for valor in linha:
                if valor == 1:
                    cont += 1

            resultado.append(cont)

        return resultado


matrix = [
    [0, 1, 1],
    [1, 0, 1],
    [1, 1, 0]
]

solution = Solution()

print(solution.findDegrees(matrix))