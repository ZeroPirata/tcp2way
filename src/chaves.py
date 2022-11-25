import rsa

def gerarChaves():
    size = input("Tamanho da chave: ")
    end = "src/keys/"
    (pubCli, priCli) = rsa.newkeys(int(size))
    generatorPubKeyPath = end + "CliKey" + "Pub.txt"
    PubKey = open(generatorPubKeyPath, "wb")
    PubKey.write(pubCli.save_pkcs1(format="PEM"))
    PubKey.close()
    generatorPriKeyPath = end + "CliKey" + "Pri.txt"
    PriKey = open(generatorPriKeyPath, "wb")
    PriKey.write(priCli.save_pkcs1(format="PEM"))
    PriKey.close()
    (pubServ, priServ) = rsa.newkeys(int(size))
    generatorPubKeyPath = end + "ServKey" + "Pub.txt"
    PubKey = open(generatorPubKeyPath, "wb")
    PubKey.write(pubServ.save_pkcs1(format="PEM"))
    PubKey.close()
    generatorPriKeyPath = end + "ServKey" + "Pri.txt"
    PriKey = open(generatorPriKeyPath, "wb")
    PriKey.write(priServ.save_pkcs1(format="PEM"))
    PriKey.close()

def renderWay(ways):
    arquivo = ""
    if ways == "cliente":
        arquivo = "Cliente"
    else:
        arquivo = "Server"
    return arquivo


def receberMensagemCriptografada(recebido, ways):
    arquvivo = renderWay(ways)
    secrete = "src/keys/message/Recebeu{event}Mensagem.txt".format(event=arquvivo)
    msg = open(secrete, "wb")
    msg.write(recebido)
    msg.close


def CriptoGrafarMensagem(ways):
    arquvivo = renderWay(ways)

    keyPub = ""

    if arquvivo == "Cliente":
        keyPub = "src/keys/CliKeyPub.txt"
    else:
        keyPub = "src/keys/ServKeyPub.txt"

    textoEncrypte = input().encode("utf-8")
    arq = open(keyPub, "rb")
    txt = arq.read()
    arq.close()
    pub = rsa.PublicKey.load_pkcs1(txt, format="PEM")
    msgc = rsa.encrypt(textoEncrypte, pub)
    return msgc


def traduzirMensagemCriptografada(ways):
    arquvivo = renderWay(ways)
    keyCliente = ""
    if arquvivo == "Cliente":
        keyCliente = "src/keys/CliKeyPri.txt"
        arquvivo = "Cliente"
    else:
        keyCliente = "src/keys/ServKeyPri.txt"
        arquvivo = "Server"

    mensagemRecebida = "src/keys/message/Recebeu{event}Mensagem.txt".format(
        event=arquvivo
    )

    arq = open(keyCliente, "rb")
    txt = arq.read()
    arq.close()

    pri = rsa.PrivateKey.load_pkcs1(txt, format="PEM")

    arq = open(mensagemRecebida, "rb")
    msgc = arq.read()
    arq.close()

    msg = rsa.decrypt(msgc, pri)

    print(msg.decode("utf-8"))
