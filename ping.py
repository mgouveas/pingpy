import os
import time

print("""
    ====================PingPy====================

    ===========Seja Bem-Vindo ao PingPy===========

    Escolha uma das opções do nosso sistema

    [S] - Teste Simples (Com apenas 1 host)
    [M] - Teste Multiplo (Arquivo .txt com lista de hosts)

    Informações Importantes:
        * Número padrão de pacotes enviados: 4 (Caso você não defina durante a execução)
        * Inserir um HOST por linha no arquivo hosts.txt (URL ou IPv4)

    ==============================================
    """)

type_test = str(input('Escolha sua opção: ')).upper()

match type_test:
    case 'S':
        ip = input("Insira o Host: ")
        num_pack = input("Número de pacotes: ")       
        print('\n')
        print('#'*60)
        print(f'Iniciando a análise do host: {ip}')
        os.system(f'ping -n {num_pack} {ip}')
        print('Finalizando análise.')
        print('#'*60)

        time.sleep(3)
    
    case 'M':
        with open('hosts.txt') as file:
            dump = file.read()
            dump = dump.splitlines()
            num_pack = input("Número de pacotes: ")
            
            if num_pack == "":
                num_pack = 4

            for ip in dump:
                print('\n')
                print('#'*60)
                print(f'Iniciando a análise do host: {ip}')
                os.system(f'ping -n {num_pack} {ip}')
                print('Finalizando análise.')
                print('#'*60)

                time.sleep(1)

input("Pressione <enter> para encerrar!")