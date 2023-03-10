from __future__ import barry_as_FLUFL
import pyodbc
from random import randint
import pytz
from datetime import datetime

dados_conexao = ("Driver={SQLite3 ODBC Driver}; Server=localhost; Database=bancopoo.db;")

conexao = pyodbc.connect(dados_conexao)

cursor = conexao.cursor()


#cursor.execute(f"INSERT INTO bancodados (Nome, Cpf, Agencia, Numconta, Saldo, limite) VALUES ('thais', '654321', 78956, 123789, 1000, 10000)")

#cursor.commit()


def validacao_login(login, senha):
         
        cursor.execute(f"SELECT Cpf FROM bancodados WHERE Cpf = '{login}'")
        cpf_login = cursor.fetchall()
            
        cursor.execute(f"SELECT Senha FROM bancodados WHERE Senha = '{senha}'")
        senha_login = cursor.fetchall()
            
        
        return cpf_login, senha_login




class BancoPoo:

    
    
    def __init__(self, Agencia):
        cursor.execute(f"SELECT Nome FROM bancodados WHERE Agencia = '{Agencia}'")
        nome_tab = cursor.fetchall()
        self.nome = nome_tab[0][0]
        
        cursor.execute(f"SELECT Cpf FROM bancodados WHERE Agencia = '{Agencia}'")
        cpf_tab = cursor.fetchall()
        self.cpf = cpf_tab[0][0]
        
        
        cursor.execute(f"SELECT Agencia FROM bancodados WHERE Agencia = '{Agencia}'")
        agc_tab = cursor.fetchall()
        self.agencia = agc_tab[0][0]
        
        
        cursor.execute(f"SELECT Numconta FROM bancodados WHERE Agencia = '{Agencia}'")
        num_tab = cursor.fetchall()
        self.num_conta = num_tab[0][0]
        
        
        cursor.execute(f"SELECT Saldo FROM bancodados WHERE Agencia = '{Agencia}'")
        saldo_tab = cursor.fetchall()
        self.saldo = saldo_tab[0][0]
        
        
        cursor.execute(f"SELECT limite FROM bancodados WHERE Agencia = '{Agencia}'")
        lim_tab = cursor.fetchall()
        self.limite = lim_tab[0][0]
    
        
        cursor.execute(f"SELECT Senha FROM bancodados WHERE Agencia = '{Agencia}'")
        pass_tab = cursor.fetchall()
        self.senha = pass_tab[0][0]
        

        cursor.execute(f"SELECT Validacao FROM bancodados WHERE Agencia = '{Agencia}'")
        valid_tab = cursor.fetchall()
        self.validacao = valid_tab[0][0]
        
        
        #cursor.execute(f"INSERT INTO bancodados (Nome, Cpf, Agencia, Numconta, Saldo, limite, Senha, Validacao) VALUES ('{self.nome}', '{self.cpf}', '{self.agencia}', '{self.num_conta}', {self._saldo}, {self._limite}, '{self._senha}', {self.validacao} )")
        
        #cursor.commit()
        
          

        
def _gerar_numero_conta():  
    '''
    Fun????o que gera um n??mero de 6 digitos, sendo que cada digito pode ser de 1 at?? 9.
        
    N??o exige nenhum par??metro.
        
    Retorna uma variavel com um n??mero de 6 digitos aleat??rios cada vez que ?? executada.
        
    '''
    num_conta= ''

    for i in range(5):
        num_conta += str(randint(1,9))
        
    return num_conta  




def _data_hora():
        '''
        Fun????o que entrega de forma formatada o hor??rio atual, levando em conta o fuso hor??rio de Braisilia - DF (dias/meses/anos  horas:minutos:segundos)
        
        N??o exige nenhum par??metro.
        
        Retorna uma vari??vel com o hor??rio formatado em que a fun????o foi rodada.
        
        '''
        fuso_brazil = pytz.timezone('Brazil/East') #horario de brasilia
        horario_brazil = datetime.now(fuso_brazil)
        
        return horario_brazil.strftime('%d/%m/%Y  %H:%M:%S')
    
             


while True:

    print(' ______________________________________________')

    print('|           BANCO - POO                        |')

    print('|______________________________________________|') 

    print('|PRESSIONE 1 PARA LOGIN                        |')

    print('|PRESSIONE 2 PARA CADASTRAR CLIENTE            |')

    print('|PRESSIONE 3 PARA CONSULTAR SALDO              |')

    print('|PRESSIONE 4 P/ CONSULTA DE DADOS DA CONTA     |')
     
    print('|PRESSIONE 5 PARA SAQUES                       |')

    print('|PRESSIONE 6 PARA DEP??SITO                     |')
    
    print('|PRESSIONE 7 PARA TRANSFER??NCIAS               |')
    
    print('|PRESSIONE 8 PARA EXIBIR EXTRATO DA CONTA      |')

    print('|PRESSIONE 0 PARA SAIR DO SISTEMA              |')

    print('|______________________________________________|')
          

    opc = int(input('>> '))
    
    if opc == 0:  
        login = input('Para sair do Sistema informe seu CPF: ')    
        
        cursor.execute(f"SELECT Validacao FROM bancodados WHERE Cpf = '{login}'")
        valid_acesso = cursor.fetchall()
            
        if valid_acesso == []:
            print('\nCpf Incorreto.') 
        
        else:
            print('\nSaindo do sistema!\n')         
            cursor.execute(f"UPDATE bancodados SET Validacao = 0  WHERE Cpf = '{login}'")
            cursor.commit()
            cursor.close()
            conexao.close()
            break
    
    if opc == 1:
            
            login = input('Digite seu CPF (com pontos e tra??o): ')
            senha = input('Digite sua Senha (8 Dig??tos): ')
            
            cursor.execute(f"SELECT Validacao FROM bancodados WHERE Cpf = '{login}'")
            valid_acesso = cursor.fetchall()
            
            if valid_acesso == [] :
                print('\nCpf ou Senha Incorretos. Confira os dados!')    
                
            elif valid_acesso[0][0] == 1:
                print('\nVoc?? j?? est?? logado!')
            
            else:  
                validacao_login(login,senha)
                    
                dados_login = validacao_login(login,senha)
                
                if dados_login[0] == [] or dados_login[1] == []:
                    print('\nCPF ou Senha Incorretos!')
                    
                else:
                    cursor.execute(f"UPDATE bancodados SET Validacao = 1  WHERE Cpf = '{login}'")
                    cursor.commit()
                    
                    cursor.execute(f"SELECT Nome FROM bancodados WHERE Cpf = '{login}'")
                    nome_bem_vindo = cursor.fetchall()
                    print(f'\nAcesso liberado! Seja bem vindo(a) {nome_bem_vindo[0][0]}')
                    
    
    if opc == 2:
        
        login = input('Digite seu CPF (com pontos e tra??o) PARA CADASTRAR UM NOVO CLIENTE: ')
        senha = input('Digite sua Senha (8 Dig??tos): ')
        
        cursor.execute(f"SELECT Validacao FROM bancodados WHERE Cpf = '{login}' AND Senha = '{senha}'")
        valid_acesso = cursor.fetchall()
            
        if valid_acesso == []:
            print('\nCpf ou Senha Incorretos. Confira os dados ou fa??a Login!') 
            
        elif valid_acesso[0][0] == 0:
            print('\nCpf ou Senha Incorretos. Confira os dados ou fa??a Login!') 
            
        
        else:       
            while True:    
                nome = input('Digite o nome do Titular da conta: ')
                nome.upper() 
                nome.strip()
                if not nome.isalpha():
                    print('Somente Letras!')
                            
                else: 
                    cpf = input('Digite um CPF (com pontos e tra??o): ')
                    if not '-' in cpf or not '.' in cpf:
                        print('O CPF deve ter "-" e "." !')
                        break
                        
                    cursor.execute(f"SELECT Cpf FROM bancodados WHERE Cpf = '{cpf}'")
                    cpf_validacao = cursor.fetchall()
                    
                    if cpf_validacao == []:
                        
                        senha_creat = input('Digite uma Senha (8 Dig??tos): ')
                                
                        if len(senha_creat) < 8 or len(senha_creat) > 8:
                            print('A Senha deve conter 8 d??gitos')
                                    
                        else:
                            #conta = BancoPoo(nome, cpf, senha_creat)
                            saldo = 0
                            limite = -1000
                            validacao = 0
                            
                            cursor.execute(f"INSERT INTO bancodados (Nome, Cpf, Agencia, Numconta, Saldo, limite, Senha, Validacao) VALUES ('{nome}', '{cpf}', '{str(_gerar_numero_conta())}', '{str(_gerar_numero_conta())}', {saldo}, {limite}, '{senha_creat}', {validacao} )")
        
                            cursor.commit()
                            
                            print('\nCadastro efetuado com sucesso!\n')
                            break
                            
                    elif cpf_validacao[0][0] == cpf:
                        print('Esse CPF j?? est?? cadastrado no sistema')
                        
                        
    
    if opc == 3:
        login = input('Digite seu CPF (com pontos e tra??o) PARA EXIBIR SEU SALDO: ')
        senha = input('Digite sua Senha (8 Dig??tos): ')
        
        cursor.execute(f"SELECT Validacao FROM bancodados WHERE Cpf = '{login}' AND Senha = '{senha}'")
        valid_acesso = cursor.fetchall()
         
        if valid_acesso == []:
            print('\nCpf ou Senha Incorretos. Confira os dados ou fa??a Login!\n')  
            
        elif valid_acesso[0][0] == 0:
            print('\nCpf ou Senha Incorretos. Confira os dados ou fa??a Login!') 
    
    
        else:
            cursor.execute(f"SELECT Saldo FROM bancodados  WHERE Cpf = '{login}'")
            saldo = cursor.fetchall()
            
            print(f'\nSeu saldo ?? de R$ {saldo[0][0]:,.2f}\n')
            

    
     
    if opc == 4:
        login = input('Digite seu CPF (com pontos e tra??o) PARA EXIBIR OS DADOS DA SUA CONTA: ')
        senha = input('Digite sua Senha (8 Dig??tos): ')
        
        cursor.execute(f"SELECT Validacao FROM bancodados WHERE Cpf = '{login}' AND Senha = '{senha}'")
        valid_acesso = cursor.fetchall()
        
        if valid_acesso == []:
            print('\nCpf ou Senha Incorretos. Confira os dados ou fa??a Login!\n')  
            
        elif valid_acesso[0][0] == 0:
            print('\nCpf ou Senha Incorretos. Confira os dados ou fa??a Login!') 
    
    
        else:
            cursor.execute(f"SELECT Nome, Agencia, Numconta, Senha FROM bancodados  WHERE Cpf = '{login}'")
            dados_conta = cursor.fetchall()
               
            print('\n----DADOS DA CONTA----\n')
            print(f'Nome = {dados_conta[0][0]}')
            print(f'Agencia = {dados_conta[0][1]}')
            print(f'Numero da Conta = {dados_conta[0][2]}')
            print(f'Senha = {dados_conta[0][3]}')
    
    
    if opc == 5:
        agc = input('Digite o N??mero da sua Agencia PARA SACAR VALORES DA SUA CONTA: ')
        numconta = input('Digite o N??mero da sua Conta: ')
        
        cursor.execute(f"SELECT Validacao FROM bancodados WHERE Agencia = '{agc}' AND Numconta = '{numconta}'")
        valid_acesso = cursor.fetchall()
        
        if valid_acesso == []:
            print('\nAgencia ou N??mero da conta Incorretos. Confira os dados ou fa??a Login!\n')  
            
        elif valid_acesso[0][0] == 0:
            print('\nAgencia ou N??mero da conta Incorretos. Confira os dados ou fa??a Login!') 
    
    
        else:
            valor = int(input('Digite o valor a ser Sacado da sua Conta: '))
            
            cliente = BancoPoo(agc)
            
            if (cliente.saldo - valor) > cliente.limite:
                cliente.saldo -= valor
                
            
                print(f'\n Voc?? Sacou R$ {valor:,.2f} da sua conta banc??ria!')
                
                transacoes = (f'SACADO R$ {valor:,.2f}, SALDO: R$ {cliente.saldo:,.2f} -> {_data_hora()}')
            
                cursor.execute(f"INSERT INTO Extrato (Conta, Transacao) VALUES ('{cliente.num_conta}', '{transacoes}')")
                cursor.commit()
                
                cursor.execute(f"UPDATE bancodados SET Saldo = {cliente.saldo} WHERE Agencia =  '{agc}'")
                cursor.commit()
            
            else:
                print('\nVoc?? n??o tem Saldo o suficiente para o Saque!')   
    
    
                
    if opc == 6:
        agc = input('Digite o N??mero da sua Agencia PARA DEPOSITAR VALORES NA SUA CONTA: ')
        numconta = input('Digite o N??mero da sua Conta: ')
        
        cursor.execute(f"SELECT Validacao FROM bancodados WHERE Agencia = '{agc}' AND Numconta = '{numconta}'")
        valid_acesso = cursor.fetchall()
        
        if valid_acesso == []:
            print('\nAgencia ou N??mero da conta Incorretos. Confira os dados ou fa??a Login!\n')  
            
        elif valid_acesso[0][0] == 0:
            print('\nAgencia ou N??mero da conta Incorretos. Confira os dados ou fa??a Login!') 
    
    
        else:
            valor = int(input('Digite o valor a ser Depositado na sua Conta: '))
            
            cliente = BancoPoo(agc)
            
            cliente.saldo += valor
                
            
            print(f'\n Voc?? Depositou R$ {valor:,.2f} na sua conta banc??ria!')
                
            transacoes = (f'DEPOSITADO R$ {valor:,.2f}, SALDO: R$ {cliente.saldo:,.2f} -> {_data_hora()}')
            
            cursor.execute(f"INSERT INTO Extrato (Conta, Transacao) VALUES ('{cliente.num_conta}', '{transacoes}')")
            cursor.commit()
                
            cursor.execute(f"UPDATE bancodados SET Saldo = {cliente.saldo} WHERE Agencia =  '{agc}'")
            cursor.commit()
            
    
    
            
    if opc == 7:
        
        while True:
            agc1 = input('Digite o N??mero da sua Agencia PARA TRANSFERIR VALORES DA SUA CONTA: ')
            numconta1 = input('Digite o N??mero da sua Conta: ')
            
            cursor.execute(f"SELECT Validacao FROM bancodados WHERE Agencia = '{agc1}' AND Numconta = '{numconta1}'")
            valid_acesso = cursor.fetchall()
            
            if valid_acesso == []:
                print('\nAgencia ou N??mero da conta Incorretos. Confira os dados ou fa??a Login!\n')
                break
                
            elif valid_acesso[0][0] == 0:
                print('\nAgencia ou N??mero da conta Incorretos. Confira os dados ou fa??a Login!')
                break
                
            
            else:  
                agc2 = input('Digite o N??mero da Agencia QUE IRA RECEBER O VALOR: ')
                numconta2 = input('Digite o N??mero da Conta QUE IRA RECEBER O VALOR: ')
                
                cursor.execute(f"SELECT Validacao FROM bancodados WHERE Agencia = '{agc2}' AND Numconta = '{numconta2}'")
                valid_acesso = cursor.fetchall()
                
                if valid_acesso == []:
                    print('\nAgencia ou N??mero da conta N??o Existem.\n')
                    break                                        
            
                else:
                    valor = int(input('Digite o valor a ser Transferido da sua Conta: '))
                    
                    cliente = BancoPoo(agc1)
                    cliente2 = BancoPoo(agc2)
                    
                    
                    if (cliente.saldo - valor) > cliente.limite:
                        cliente.saldo -= valor
                        cliente2.saldo += valor
                        
                        print(f'\n Voc?? Transferiu R$ {valor:,.2f}! para {cliente2.nome}.\n')
                        
                        transacoes = (f'TRANSFERIDO R$ {valor:,.2f} para {cliente2.nome}, SALDO: R$ {cliente.saldo:,.2f} -> {_data_hora()}')
                        transacoes2 = (f'RECEB.TRANSFER R$ {valor:,.2f} de {cliente.nome}, SALDO: R$ {cliente2.saldo:,.2f} -> {_data_hora()}')
                    
                        cursor.execute(f"INSERT INTO Extrato (Conta, Transacao) VALUES ('{cliente.num_conta}', '{transacoes}')")
                        cursor.commit()
                        
                        cursor.execute(f"INSERT INTO Extrato (Conta, Transacao) VALUES ('{cliente2.num_conta}', '{transacoes2}')")
                        cursor.commit()
                        
                        cursor.execute(f"UPDATE bancodados SET Saldo = {cliente.saldo} WHERE Agencia =  '{agc1}'")
                        cursor.commit()
                        
                        cursor.execute(f"UPDATE bancodados SET Saldo = {cliente2.saldo} WHERE Agencia =  '{agc2}'")
                        cursor.commit()
                        break
                    
                    else:
                        print('Voc?? n??o tem Saldo o Suficiente para fazer a transfer??ncia!')
                        break
                    
    if opc == 8:
        agc = input('Digite o N??mero da sua Agencia PARA EXIBIR O EXTRATO DA SUA CONTA: ')
        numconta = input('Digite o N??mero da sua Conta: ')
        
        cursor.execute(f"SELECT Validacao FROM bancodados WHERE Agencia = '{agc}' AND Numconta = '{numconta}'")
        valid_acesso = cursor.fetchall()
        
        if valid_acesso == []:
            print('\nAgencia ou N??mero da conta Incorretos. Confira os dados ou fa??a Login!\n')  
            
        elif valid_acesso[0][0] == 0:
            print('\nAgencia ou N??mero da conta Incorretos. Confira os dados ou fa??a Login!') 
    
    
        else:
            cursor.execute(f"SELECT Conta, Transacao FROM Extrato WHERE Conta = '{numconta}'")
            extrato = cursor.fetchall()
            
            
            for linha in extrato:
                print(f'\n{linha[1]}')
                    
                    
            
            
                   
            
                   
    
        
        
        
            
            
            
            
            

        




