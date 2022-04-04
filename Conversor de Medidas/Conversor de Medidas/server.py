#!/usr/bin/python3

from datetime import datetime
import sys
import socket

# Funções auxiliares
def agora():
    agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S → ")
    print("\033[36m%s\033[0m" % agora, end="")

def conversor(grandeza, medida_origem, medida_destino, valor):
    prefixos = ["k", "h", "da", "", "d", "c", "m"]

    saida = ""
    if grandeza == 1 or grandeza == 2 or grandeza == 3:
        valor_convertido = valor * 10**(grandeza * (medida_destino-medida_origem))
        
        exp = ""
        if grandeza == 2:
            exp = "²"
        if grandeza == 3:
            exp = "³" 

        saida = str(valor) + " " + prefixos[medida_origem] + "m" + exp

        saida = saida + " ===> " + str(valor_convertido) + " " + prefixos[medida_destino] + "m" + exp
        
        return saida


# Servidor
def servidor(host="localhost", port=2022):
    # Criando um socket TCP
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Habilitando o reuso de endereço e porta
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # Bind
    agora() # Exibe data e hora atualizadas
    print("Iniciando o servidor em \033[33m%s\033[0m:\033[31m%s\033[0m." % (host, port))
    s.bind((host, port))
    n_max = 10
    s.listen(n_max)

    # Aceitando o cliente
    agora()
    print("Aguradando conexão como cliente.")
    cliente, endereco = s.accept()

    agora()
    print("Cliente conectado.")

    try:
        while True:
            agora()
            print("Aguardando mensagem do cliente.")
            print("Pressione CTRL+C para encerrar o servidor.")

            # Recebimento de dados do cliente
            dados = cliente.recv(2048) # Agurada dados do cliente

            if not dados:
                agora()
                print("Aguardando conexão com o cliente.")
                cliente, endereco = s.accept()

                agora()
                print("Cliente conectado.")
            else:
                # Exibindo os dados
                dados = dados.decode()
                #valor = dados.split(":")
                campos = dados.split("@")

                grandeza = int(campos[0])
                medida_origem = int(campos[1])
                medida_destino = int(campos[2])
                valor = float(campos[3])
                
                print("Grandeza = " + str(grandeza))
                print("Medida de origem = " + str(medida_origem))
                print("Medida de destino = " + str(medida_destino))
                print("Valor = " + str(valor))

                
                mensagem = conversor(grandeza, medida_origem, medida_destino, valor)

                cliente.send(mensagem.encode("utf-8"))
                agora()

    except socket.error as e:
        agora()
        print("Erro de socket: %s" % str(e))

    except Exception as e:
        agora()
        print("Outra exceção: %s" % str(e))

    finally:
        agora()
        print("Encerrando conexão.")
        s.close()
        return

# Executar o servidor com parâmetros
if __name__ == "__main__":
    n_args = len(sys.argv) - 1

    if n_args == 0:
        servidor()
    elif n_args == 1:
        servidor(sys.argv[1])
    elif n_args == 2:
        servidor(sys.argv[1], int(sys.argv[2]))
