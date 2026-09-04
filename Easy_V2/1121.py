precos = [100, 250, 80, 500, 120]

resultado = list(
    map(lambda x: f"{x * 1.15:.2f}", precos)
)

print(resultado)