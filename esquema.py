from peewee import PostgresqlDatabase, Model, TextField, IntegerField, DoubleField, ForeignKeyField, DateTimeField, DateField

db = PostgresqlDatabase('ativ06_orm2', user='postgres', port='5433', password='postgres')

class BaseModel(Model):
    class Meta():
        database = db

class Categoria(BaseModel):
    descricao = TextField()

class Cliente(BaseModel):
    nome = TextField()
    endereco = TextField()
    data_registro = DateField()

class Produtos(BaseModel):
    descricao = TextField()
    id_categoria = ForeignKeyField(Categoria,backref='produtos')
    valor = DoubleField()



class Historico_Precos(BaseModel):
    id_produto = ForeignKeyField(Produtos, backref='historico_precos' )
    valor = DoubleField()
    data = DateField()

class Vendas(BaseModel):
    id_produto = ForeignKeyField(Produtos, backref='vendas')
    id_cliente = ForeignKeyField(Cliente, backref = 'vendas')
    data = DateField()
    quantidade = IntegerField()
    valor_unitario = DoubleField()
    valor_total = DoubleField()



lista_tabelas = [Vendas, Historico_Precos, Produtos, Cliente, Categoria]

db.connect()
db.create_tables(lista_tabelas)
db.close()

