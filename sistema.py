import mysql.connector                     

class Clientes:
    def __init__(self, nome, sobre_nome, telefone, email):
        self.nome = nome
        self.sobre_nome = sobre_nome
        self.telefone = telefone
        self.email = email

class Historico:
    def __init__(self, cliente_id, dia_chamada, descricao_oportunidade, tipo_de_contato, notas):
        self.cliente_id = cliente_id 
        self.dia_chamada = dia_chamada
        self.descricao_oportunidade = descricao_oportunidade
        self.tipo_de_contato = tipo_de_contato
        self.notas = notas 

class OportunidadeDeVendas:
    def __init__(self, cliente_id, descricao_oportunidade, valor_estimado, tipo_venda, notas):
        self.cliente_id = cliente_id
        self.descricao_oportunidade = descricao_oportunidade
        self.valor_estimado = valor_estimado
        self.tipo_venda = tipo_venda
        self.notas = notas

class SistemaCRM:
    def __init__(self):
        self.conexao = mysql.connector.connect(
            host='localhost',
            user='root',
            password='he182555@',
            database='crm_db'
        ) 
        self.cursor = self.conexao.cursor()

    def adicionar_clientes(self, cliente):
        sql = "INSERT INTO clientes (nome, sobre_nome, telefone, email) VALUES (%s, %s, %s, %s)"
        valores = (cliente.nome, cliente.sobre_nome, cliente.telefone, cliente.email)
        self.cursor.execute(sql, valores)
        self.conexao.commit()
        print('Cliente adicionado com sucesso.')

    def listar_contatos(self):
        self.cursor.execute("SELECT nome, sobre_nome, telefone, email FROM clientes")
        contatos = self.cursor.fetchall()
        for contato in contatos:
            print(f"Nome: {contato[0]}, Sobrenome: {contato[1]}, Telefone: {contato[2]}, Email: {contato[3]}")

    def fechar_conexao(self):
        self.cursor.close()
        self.conexao.close()

# Criando uma instância de SistemaCRM
sistema = SistemaCRM()

# Criando instâncias de Clientes
contato1 = Clientes('Rafael', 'Costa', '99991323468', 'rafael@gmail.com')
contato2 = Clientes('Bronie', 'Melo', '99991096256', 'brownie@gmail.com')

# Adicionando clientes ao sistema
sistema.adicionar_clientes(contato1)
sistema.adicionar_clientes(contato2)

# Listando contatos
print('Listar contatos')
sistema.listar_contatos()

# Fechando a conexão
sistema.fechar_conexao()
