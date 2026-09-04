def criar_produto(*args,**kwargs):
    produto = {
        "nome": args [0],
        "preco": args[1]
    }

    produto.update(kwargs)
    return produto


produto = criar_produto(
    "Notebook",
    3500,
    categoria="Eletrônicos",
    marca="Dell",
    estoque=10
)

print(produto)