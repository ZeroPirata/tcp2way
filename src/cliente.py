import socket
from threading import Thread
from chaves import (
    CriptoGrafarMensagem,
    receberMensagemCriptografada,
    traduzirMensagemCriptografada,
)

global tcp_con


def receber():
    global tcp_con
    while True:
        msg = tcp_con.recv(1024)
        receberMensagemCriptografada(msg, "cliente")
        print("Server diz: ")
        traduzirMensagemCriptografada("cliente")


def enviar():
    global tcp_con
    print("Para sair use CTRL+X\n")
    msg = CriptoGrafarMensagem("serve")
    while msg != "\x18":
        tcp_con.send(msg)
        msg = CriptoGrafarMensagem("serve")
    tcp_con.close()


# Endereco IP do Servidor
SERVER = "127.0.0.1"

# Porta que o Servidor esta escutando
PORT = 5002

tcp_con = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (SERVER, PORT)
tcp_con.connect(dest)


t_rec = Thread(target=receber, args=())
t_rec.start()

t_env = Thread(target=enviar, args=())
t_env.start()
