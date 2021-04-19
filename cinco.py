import mysql.connector

#conectando ao banco de dados
#obs: a senha do banco de dados no MySql realmente não é essa. Essa é apenas um exemplo
conexao = mysql.connector.connect(user='root', password='MINHA_SENHA_DO_MYSQL', port='3306',
                              host='localhost', database='mercadinho')

# criando table de produtos
# cursor.execute("CREATE TABLE produtos (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, nome VARCHAR(30) NOT NULL, valor DECIMAL(5,2) NOT NULL)")

class Produto:
    #inicialmente nome é nulo e valor é 0
    def __init__(self):
        self.nome = None
        self.valor = 0

    # cadastrando um novo produto
    def cadastrar(self):
        cursor = conexao.cursor()
        # chamamos o comando do mysql para inserir valores na tabela de produtos já criada anteriormente que está no bd
        novo = "INSERT INTO produtos (nome, valor) values (%s, %s)"
        self.nome = input('nome do produto: ')
        self.valor = float(input('valor: '))

        # coloca-se os valores numa tupla antes de executar o comando com os valores inclusos
        dadosProduto = (self.nome, self.valor)
        
        cursor.execute(novo, dadosProduto)
        #confirmamos e imprimimos que o produto foi inserido
        conexao.commit()
        print(cursor.rowcount, "produto inserido com sucesso")
        #fecha-se a conexão quando termina a função
        cursor.close()

        return conexao.close()

    #excluindo produto pelo id
    def excluir(self):
        cursor = conexao.cursor()

        # mostra-se os produtos disponiveis na tabela
        print("#lista de produtos disponíveis#")
        print('id    nome')
        cursor.execute("SELECT id, nome FROM produtos")
        for (i,j) in cursor:
            print(i,"   ", j)

        # chamamos o comando para deletar no banco de dados através do id
        deletar = ("DELETE FROM produtos WHERE id = %s")
        id = input('produto que deve ser excluído: ')

        cursor.execute(deletar, tuple(id))

        print("produto excluido")

        conexao.commit()
        
        cursor.close()

        return conexao.close()


    def buscar(self):
        cursor = conexao.cursor()

        # damos um select no banco de dados para mostrar as informações do produto que pesquisamos pelo id
        consultar = ("select * from produtos where id = %s")
        id = input("codigo do produto que deseja consultar: ")
            
        cursor.execute(consultar, tuple(id))

        # percorrendo o cursor para mostrar as informações do produto
        for (id, nome, preco) in cursor:
            print('id',' nome',' preço')
            print(id, nome, preco)
    
        cursor.close()

        return conexao.close()

        
