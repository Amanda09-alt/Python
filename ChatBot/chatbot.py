def saudacoes_GUI (nome):
    import random
    frases = ["Bom dia! Meu nome é " + nome + " como você está? " , "Olá!" , "Oi, tudo bem?"]
    print(frases[random.randint(0,2)])


def recebeTexto():
    texto = "Cliente: " + input("cliente: ")
    palavraProibida = ["boco" , "olk"]
    for p in palavraProibida:
        if p in texto:
            print("Não vem não! Me respeite!")
            return recebeTexto()
    return texto
        

def buscarResposta_GUI(nome, texto):
    with open("BaseDados.txt","a+", encoding="utf-01") as conhecimento:
        conhecimento.seek(0)
        while True:
            viu = conhecimento.readline()
            if viu != "":
                if texto.replace("Cliente: ","")=="Tchau":
                    print(nome+ ": volte sempre!")
                    return "Fim"
                elif viu.strip().lower() == texto.strip().lower():
                    proximalinha = conhecimento.readline()
                    if "ChatBot: " in proximalinha:
                        return proximalinha
            else:
                print("Me desculpe, não sei o que falar!")
                conhecimento.write("\n" + texto)
                resposta_user = input("O que esperava?\n")
                conhecimento.write("\n" +"ChatBot: "+resposta_user)
                return "Hum..."


def exibeResposta(resposta, nome):
    print(resposta.replace("ChatBot",nome))
    if resposta == "fim":
        return "fim"
    return "continua"

def exibeResposta_GUI(texto, resposta, nome):
    return resposta.replace("ChatBot",nome)