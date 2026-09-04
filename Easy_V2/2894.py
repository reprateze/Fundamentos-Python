class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        aux = []
        total = 0
        total2 = 0

        while n > -1:
            aux.append(n)
            n -= 1

        for i in aux:
            if i % m == 0:
                total += i
            else:
                total2 += i

        return total2 - total