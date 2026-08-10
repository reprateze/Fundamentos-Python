def fib(n):
    resultado = []
    a,b = 0,1

    while a < n:
        resultado.append(a)
        a,b = b, a + b

    return resultado


n = int(input("Escolha um numero para a sequencia:"))

result = fib(n)

print(result)

