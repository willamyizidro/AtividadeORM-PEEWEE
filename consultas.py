from esquema import *
import datetime

# 1 - Liste todo o histórico de preços (valor, data) do produto 
# "Caneta Bic esferográfica azul".

def imprimirHistoricoPrecos(nome):
    cons = Historico_Precos.select(Historico_Precos.data, Historico_Precos.valor).where(Produtos.descricao == nome).join(Produtos)
    if cons:
        print("Historico de preços do produto: ", nome)
        for linha in cons:
            print("Valor: R$",linha.valor , "Data: ",linha.data )
        print()

imprimirHistoricoPrecos("Caneta Bic esferográfica azul")


# 2 - Liste descrição e preço de todos os produtos da categoria "Papelaria", 
# ordenados no menor para o maior preço.

def imprimirListaCategoria(cat):
    cons = Produtos.select(Produtos.descricao, Produtos.valor).where(Categoria.descricao == cat).join(Categoria).order_by(Produtos.valor.asc())
    if cons:
        print("lista de produtos da categoria: ", cat)
        for linha in cons:
            print("Descricao: ",linha.descricao, " || Valor: R$", linha.valor)

    print()

imprimirListaCategoria("Papelaria")

# 3 - Recupere os nomes dos clientes que fizeram ao menos uma compra com valor 
# superior a R$ 5.000,00 no mês de setembro/2022. Exiba-os em ordem alfabética.
def imprimirRelacaoCompraCliente(mes, ano , valor):
    cons = Cliente.select(Cliente.nome).where((Vendas.valor_total > valor) & (Vendas.data.year == ano) &(Vendas.data.month == mes) ).join(Vendas).order_by(Cliente.nome.asc()).group_by(Cliente.nome)
    if cons:
        print("Relação de cliente que compraram acima de: R$",valor, " no mes de:",mes," no ano de: ",ano)
        for linha in cons:
            print(linha.nome)

    print()

imprimirRelacaoCompraCliente(10,2023, 1)