from Contato import *
import sqlite3

''' Trata de todas as operações com o banco de dados, tratamentos preliminares dos dados retornados  '''

class OperacoesDados:

    def __init__(self):

        self.__contato = None
        self.conexao = None
        self.campo = None
        self.valor = None
        self.index = None

    @property
    def contato(self):
        return self.__contato

    @contato.setter
    def contato(self, cont):
        self.__contato = cont

    # cod_operacao e o parametro referente ao tipo de operação com o banco de dados
    def operacao_bd(self, cod_operacao):

        try:
            self.conexao = sqlite3.connect('agenda.db')
            cursor = self.conexao.cursor()
            cursor.execute(""" CREATE TABLE IF NOT EXISTS agenda(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, nome TEXT, telefone INTEGER(11), email TEXT) """)
            
        except:
            print("Erro na conexão com o banco de dados")
            return False

        if cod_operacao == 1:#Inserir registro
            try:
                cursor.execute(""" INSERT INTO agenda(nome, telefone, email) VALUES(?,?,?) """, (self.__contato.nome, self.__contato.numero, self.__contato.email))
                self.conexao.commit()
                self.conexao.close()
                return True
            except Exception as erro:
                print(str(erro))
                self.conexao.close
                return False

        elif cod_operacao == 2:#Seleciona e retorna todos os registros de acordo com uma condição
            try:
                cursor.execute("""SELECT * FROM agenda WHERE """ + self.campo + """ = ? """, (self.valor,))
                dados = [line for line in cursor.fetchall()]
                self.conexao.commit()
                self.conexao.close()
                return dados                
            except Exception as erro:
                print(str(erro))
                self.conexao.close
                return False

        
        elif cod_operacao == 3:#Atualizar registro
            try:
                cursor.execute("""UPDATE agenda SET """ + self.campo + """ = ? WHERE id = ?""", (self.valor, self.index,))
                self.conexao.commit()
                self.conexao.close()
                return True
            except Exception as erro:
                print(str(erro))
                return False          

        elif cod_operacao == 4:#Deletar registro
            
            try:
                cursor.execute("""DELETE FROM agenda  WHERE id = ?""", (self.index,))
                self.conexao.commit()
                self.conexao.close()
                return True
            except Exception as erro:
                print(str(erro))
                self.conexao.close
                return False

        elif cod_operacao == 5:#Selecionae retorna todos os registros             
            try:
                cursor.execute(""" SELECT * FROM agenda""")
                dados = [line for line in cursor.fetchall()]
                self.conexao.commit()
                self.conexao.close()
                return dados
            except Exception as erro:
                print(str(erro))
                self.conexao.close

                
    def procurar_contato(self, campo, valor):
        
        '''Retorna o registro de procura de acordo com o campo passado como parametro, e a chave de procura'''
        contatos = self.operacao_bd(5)
        
        if campo == 1:
            retorno = [registro for registro in contatos if valor in registro[1]]
            return retorno
        elif campo == 2:
            retorno = [registro for registro in contatos if valor in str(registro[2])]
            return retorno
        elif campo == 3:
            retorno = [registro for registro in contatos if valor in registro[3]]
            return retorno
        elif campo == 4:
            retorno = [registro for registro in contatos if valor in str(registro)]
            return retorno

        
    def editar_contatos(self, campo, valor, index):
        
        self.valor = valor.title()
        self.index = index
        
        if campo == 1:
            self.campo = 'nome'
            edicao = self.operacao_bd(3)
            print('Contato editado com sucesso !') if edicao else print(f'Erro ao Editar contato')

        elif campo == 2:
            self.campo = 'telefone'
            self.valor = int(valor)
            edicao = self.operacao_bd(3)
            print('Contato editado com sucesso !') if edicao else print(f'Erro ao Editar contato')

        elif campo == 3:
            self.campo = 'email'
            edicao = self.operacao_bd(3)
            print('Contato editado com sucesso !') if edicao else print(f'Erro ao Editar contato')

        self.campo = None
        self.valor = None
        self.index = None


    def deletar_contatos(self, index):
        
        self.index = index
        deletar = self.operacao_bd(4)
        print('\nContato Deletado !') if deletar else print (f'Erro ao Deletar contato')
        self.index = None


    def listar_contatos(self):
        
        dados = self.operacao_bd(5)
        return sorted(dados, key = lambda contato: contato[1])# retorna os dados ordenados por odem alfabetica ou crescente 
