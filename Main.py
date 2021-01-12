from Contato import *
from Dados import *
import time

conn = OperacoesDados()# Instancia para a classe de operação com o banco de dados


def get_registro(operacao = ''):
    
    #Operação comum a edição e exclusão de registro do banco de dados. Lista os registros cada um com um id e partir deste ID a operação e feita
    
    registros = listar_contatos('get')# Obtém o dicionário criado em listar contatos

    #caso obtenha nenhum registro
    if not registros:
        return False
    
    index = input('\nDigite o número de índice do contato a ser ' + operacao + ' ou "voltar" para retornar ao menu principal: ')

    #Validação dos campos
    if index.lower() == 'voltar':
        return 1
    
    elif not index.isnumeric() or int(index) > len(registros) or int(index) <= 0 :
        print('\nId inválido\n')
        time.sleep(1)
        return 2
    
    else:
        #retorna o registro de acordo com o index informado pelo usuário
        return registros[int(index)]


def listar_contatos(modo = ''):

    #Cria um dicionário com um id e o registro e os exibe para o usuário, se o parametro modo='get' este ainda retornará todos os registros
    
    index = 0
    registros = {} #este dicionário irá receber uma chave que é a variavel index e para cada novo indice este receberá um tupla que serão os registros obtidos no banco de dados 
    dados = conn.listar_contatos()

    #Tenta obter os registros, faz a validação da tentativa
    if len(dados) == 0:
        print('Não há registros para Exibir')
        time.sleep(2)
        return False
    
    for contato in dados:
        
        index +=1
        registros[index] = contato
        print(f'{index} - Nome: {contato[1]}\n  - Telefone: {contato[2]}\n  - Email: {contato[3]}\n')

    if modo == 'get':
        return registros
    else:
        ok = input('\nPressione Enter para retornar ao menu principal ')
        

def add_contato():

    print( 30 * '=' + ' Adicionar Contato ' + 30 * '=')
    
    cont = Contato()
    cont.nome = input("Digite o Nome: ")
    cont.numero = input("Digite o Telefone: ")
    cont.email =  input("Digite o E-mail: ")
    
    salvar = input('\nSalvar Contato? (Y/N): ' ).lower()
    agenda = OperacoesDados()
    agenda.contato = cont
    if salvar == 'y':
        operacao = agenda.operacao_bd(1)
        print('\nContato Salvo !') if (operacao) else  print('Erro ao Salvar Contato')
        time.sleep(1)


def procurar_contato():

    # Pode - se fazer a busca nos registros por um campo especifico ou por todos
    
    print( 30 * '=' + ' Adicionar Contato ' + 30 * '=')

    print('1 - Nome\n2 - Telefone\n3 - Email\n4 - Tudo\n')
    
    opcao = input('Digite a opção para a busca desejada, ou "voltar" para retornar ao menu principal: ')
    if opcao.lower() == 'voltar':
        return
    elif not opcao.isnumeric() or int(opcao) > 4 or int(opcao) <= 0:
        print('\nDigite uma opção válida')
        time.sleep(1)
        procurar_contato()
        return

    print()
    procura = input('Digite a chave para a busca, ou "voltar" para retornar ao menu principal: ').title()
    
    # validação dos campos
    if procura.lower() == 'voltar':
        return
    elif opcao == 2 and not procura.isnumeric():
        print('\nPreencha um número válido\n')
        procurar_contato()
        return

    retorno = conn.procurar_contato(int(opcao), procura)
    if len(retorno) == 0:
        print('Nenhum contato encontrado para a chave digitada')
        time.sleep(1)
        return
       
    for registro in retorno:
        print(f'\nNome: {registro[1]}\nTelefone: {registro[2]}\nEmail: {registro[3]}\n')
      
    ok = input('\nPressione Enter para retornar ao menu principal ')  
    
    
def editar_contato():

    # Edita um contato de acordo com o ID gerado informado pelo usuário
    
    print( 30 * '=' + ' Editar Contato ' + 30 * '=')
    
    reg = get_registro('editado')
    #Tenta obter os registros, faz a validação da tentativa
    if not reg :
        return 
    if reg == 1:
        return
    elif reg == 2:
        editar_contato()
        return
    
    else:
        print()
        print(f'{1} - Nome: {reg[1]}')
        print(f'{2} - Telefone: {reg[2]}')
        print(f'{3} - Email: {reg[3]}')
        
        index = input('\nDigite o índice do campo a ser editado ou "voltar" para retornar ao menu principal: ')

        #validação dos campos
        if index.lower() == 'voltar':
            return 
        
        elif not index.isnumeric() or (int(index) < 1 and int(index) > 3):
            print('\nCampo inválido\n')
            editar_contato()
            return
        
        valor = input('\nDigite a atualização para o campo selecionado: ')
        print()
        conn.editar_contatos(int(index), valor, reg[0])
        time.sleep(1)

        
def deletar_contato():

    # Deleta um contato de acordo com o ID gerado pelo usuário 

    print( 30 * '=' + ' Deletar Contato ' + 30 * '=')
    
    reg = get_registro('deletado')
    #Tenta obter os registros, faz a validação da tentativa
    if not reg:
        return            
    if not isinstance(reg, tuple):
        if reg == 1:
            return
        elif reg == 2:
            deletar_contato()
            return
        
    id_deletar = reg[0]# a partir do id de registro informado pelo usuário, obtém - se o id do registro no banco de dados.
    conn.deletar_contatos(id_deletar)
    time.sleep(1)

# Menu de opções de entrada do programa
while(1):
    
    print(80 * '=')
    opcao = input('\nOlá, o que devemos fazer? \n\n1- Adicionar Contato\n2- Procurar Contato\n3- Editar Contato\n4- Deletar Contato\n5- Listar Contatos\n6- Sair\n\nDigite o número da Opção escolhida: ')
    if opcao == '1':
        print()
        add_contato()
        
    elif opcao == '2':
        print()
        procurar_contato()
        
    elif opcao == '3':
        print()
        editar_contato()
        
    elif opcao == '4':
        print()
        deletar_contato()
        
    elif opcao == '5':
        print()
        listar_contatos()
        
    elif opcao == '6':
        break
    
    else:
        print('\nDigite uma opção valida')
        time.sleep(1)
        
       
       
    
    







