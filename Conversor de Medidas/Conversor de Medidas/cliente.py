#!/usr/bin/python3

import sys
import socket

# Funções auxiliares
def e_decimal(str): # Verifica se um string é um número decimal
    try:
        float(str) # Tenta converter string para número de ponto flutuante
        return True # Se não ocorre erro, então retorna True
    except:
        return False # Caso contrario, retorna False


def menu_grandezas():
    print("\033[2J\033[1;1H")
    print("====== GRANDEZAS ======")
    print("1 - Comprimento")
    print("2 - Área")
    print("3 - Volume/Capacidade")
    print("4 - Massa")

    return int(input("Escolha a grandeza: "))

def menu_medidas(grandeza):
        medidas = []
        if grandeza == 1:
            medidas = [
                    "0 - Quilômetro (km)",
                    "1 - Hectômetro (hm)",
                    "2 - Decâmetro (dam)",
                    "3 - Metro (m)",
                    "4 - Decímetro (dm)",
                    "5 - Centímetro (cm)", 
                    "6 - Milímetro (mm)"
                ]

        if grandeza == 2:
            medidas = [
                    "0 - Quilômetro quadrado (km²)",
                    "1 - Hectômetro quadrado (hm²)",
                    "2 - Decâmetro quadrado (dam²)",
                    "3 - Metro quadrado (m²)",
                    "4 - Decímetro quadrado (dm²)",
                    "5 - Centímetro quadrado (cm²)",
                    "6 - Milímetro quadrado (mm²)"
                ]


        print("+++++ MEDIDAS +++++")
        for m in medidas:
            print(m)

        m1 = input("Escolha a medida de origem: ")
        m2 = input("Escolha a medida de destino: ")
        v = input("Insira o valor: ")

        msg = str(grandeza) + "@" + m1 + "@" + m2 + "@" + v
        
        return msg


# Cliente
def cliente(host = "localhost", port = 2022):
    # Criando um socket TCP/IP
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Conectando socket ao servidor
        print("Conectando no endereço %s na porta %s." % (host, port))
        s.connect((host, port))
        print("Conectado ao servidor.")

    except socket.error as e: # Erros de socket
        print("Erro de socket: %s" % str(e))
        print("Fechando a conexão.")
        s.close()
        return

    # Enviando dados
    try:
        while True: # Cliente funcionando em loop infinito
            print("Pressione CTRL-C ou CTRL-D para encerrar o cliente.")
            
            mensagem = menu_medidas(menu_grandezas())
            # Obtendo dados da entrada padrão
            #massa = ""
            #repetiu = False
            #while not e_decimal(massa): # Verifica a consistência dos dados
            #    if repetiu:
            #        print("Use um número decimal para a massa.")
            #    massa = input("\033[32mInsira a massa (em kg): \033[0m")
            #    repetiu = True

            #altura = ""
            #repetiu = False
            #while not e_decimal(altura): # Verifica a consistência dos dados
            #    if repetiu:
            #        print("Use um número decimal para a altura.")
            #    altura = input("\033[32mInsira a altura (em m): \033[0m")
            #    repetiu = True

            # Enviando mensagem ao servidor
            #mensagem = massa + ":" + altura # Concatena valores com separador
            print("\nEnviando a mensagem [%s]" % mensagem)
            s.sendall(mensagem.encode("utf-8")) # Codifica mensagem

            # Recebendo a mensagem do servidor contendo o IMC
            mensagem = s.recv(2048)
            # Extraíndo o IMC da mensagem recebida
            #imc = float(mensagem.decode())

            # Obtendo análise do IMC
            #resposta = analisar_imc(imc)
            # Exibindo resposta
            #print("\n\033[34ṃ»» IMC = " + f"{imc:1f}" + " kg/m² [" + str(resposta) + "]\033[0m\n")
            resposta = mensagem.decode()
            print("»»» " + resposta)

            input()

    except socket.error as e: # Erro de socket
        print("Erro de socket: %s" % str(e))

    except Exception as e: # Erro diversos
        print("Outras exceção: %s" % str(e))

    finally: # Finaliza a conxão e encerra o programa
        print("Encerrando conexão.")
        s.close() # Fecha socket
        return

# Executar cliente
if __name__ == "__main__":
    n_args = len(sys.argv) - 1 # Conta os argumentos da linha de comando

    if n_args == 0: # Zero argumentos
        cliente() # parâmetros padrão: cliente(host="localhost", port = 2022)
    elif n_args == 1: # Um argumento
        cliente(sys.argv[1]) # Usa host fornecido na linha de comando e porta padrão
    elif n_args == 2: # Dois argumentos
        cliente(sys.argv[1], int(sys.argv[2])) # Usa host e porta fornecidos na linha de comando

