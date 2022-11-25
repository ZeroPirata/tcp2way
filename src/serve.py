# Servidor TCP
import socket
from threading import Thread
from chaves import (
    receberMensagemCriptografada,
    CriptoGrafarMensagem,
    traduzirMensagemCriptografada,
)

global tcp_con


def enviar():
    global tcp_con
    msg = CriptoGrafarMensagem("cliente")
    while True:
        tcp_con.send(msg)
        msg = CriptoGrafarMensagem("cliente")


# Endereco IP do Servidor
HOST = ""

# Porta que o Servidor vai escutar
PORT = 5002

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(1)

while True:
    tcp_con, cliente = tcp.accept()
    print("Concetado por ", cliente)
    t_env = Thread(target=enviar, args=())
    t_env.start()
    while True:
        msg = tcp_con.recv(1024)
        if not msg:
            break
        receberMensagemCriptografada(msg, "server")
        print("Cliente diz:")
        traduzirMensagemCriptografada("serve")
    print("Finalizando conexao do cliente", cliente)
    tcp_con.close()
