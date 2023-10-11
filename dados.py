from esquema import *
import datetime


lista_categorias = [
    {'descricao':'Papelaria'},
    {'descricao':'Perfumaria'},
    {'descricao':'Material Escolar'},
    {'descricao':'Cereais'},
    {'descricao':'Lacticinios'},
    {'descricao':'Frios'},
    {'descricao':'Material Limpeza'}
]
# Categoria.insert_many(lista_categorias).execute()

hoje = datetime.date.today()

lista_clientes = [
    {"nome":"willamy", "endereco":"São Mamede", "data_registro": hoje },
    {"nome":"vanessa", "endereco":"São Mamede", "data_registro":hoje },
    {"nome":"joao", "endereco":"Patos", "data_registro": hoje},
    {"nome":"maria", "endereco":"Santa Luzia", "data_registro": hoje},
    {"nome":"jose", "endereco":"São Mamede", "data_registro":hoje },
    {"nome":"jose maria", "endereco":"Ipueira", "data_registro": hoje},    
]

# Cliente.insert_many(lista_clientes).execute()

# lista_produtos = [
#     {"descricao":"Perfume 100ml",'id_categoria' : Categoria.select().where(Categoria.descricao == "Perfumaria"), "valor": 10.20 },
#     {"descricao":"Danone 150ml",'id_categoria' : Categoria.select().where(Categoria.descricao == "Lacticinios"), "valor": 5.50 },
#     {"descricao":"Caneta Bic esferográfica azul",'id_categoria' : Categoria.select().where(Categoria.descricao == "Material Escolar"), "valor": 1.5 },
#     {"descricao":"Arroz Branco camil 1kg",'id_categoria' : Categoria.select().where(Categoria.descricao == "Cereais"), "valor": 6.50 },
#     {"descricao":"Presunto Sadia",'id_categoria' : Categoria.select().where(Categoria.descricao == "Frios"), "valor": 19.70 },
#     {"descricao":"Desinfetante Quasar ",'id_categoria' : Categoria.select().where(Categoria.descricao == "Material Limpeza"), "valor": 7.40},
#     {"descricao":"Pepel A4 100fls",'id_categoria' : Categoria.select().where(Categoria.descricao == "Papelaria"), "valor": 8.20 },
# ]

# Produtos.insert_many(lista_produtos).execute()




# produtos = Produtos.select()
# for linha in produtos:
#     hist = Historico_Precos.create(
#         id_produto = linha.id,
#         valor = linha.valor,
#         data = datetime.date.today()
#     )

# função para inserir vendas
def inserirVenda(nomeCliente, nomeProduto, quant):
    venda1 = Vendas.create(
        id_produto = Produtos.select().where(Produtos.descricao == nomeProduto),
        id_cliente = Cliente.select().where(Cliente.nome == nomeCliente),
        data = datetime.date.today(),
        quantidade = quant,
        valor_unitario = Produtos.select(Produtos.valor).where(Produtos.descricao == nomeProduto),
        valor_total = Produtos.select(Produtos.valor * quant).where(Produtos.descricao == nomeProduto)
    )

# inserirVenda("willamy","Perfume 100ml", 100)
# inserirVenda("vanessa","Danone 150ml", 961)
# inserirVenda("joao","Danone 150ml", 25)
# inserirVenda("willamy","Caneta Bic esferográfica azul", 1144)
# inserirVenda("maria","Arroz Branco camil 1kg", 9)
# inserirVenda("vanessa","Arroz Branco camil 1kg", 15)
# inserirVenda("joao","Presunto Sadia", 140)
# inserirVenda("willamy","Presunto Sadia", 10)
# inserirVenda("vanessa","Desinfetante Quasar ", 24)
# inserirVenda("jose","Desinfetante Quasar ", 10)
# inserirVenda("jose maria","Pepel A4 100fls", 10)
# inserirVenda("willamy","Pepel A4 100fls", 210)
# inserirVenda("vanessa","Caneta Bic esferográfica azul", 10)
# inserirVenda("jose maria","Caneta Bic esferográfica azul", 10)
# inserirVenda("willamy","Queijo Mussarela natvile", 18)

