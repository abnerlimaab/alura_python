import random

def roda_roda():
    print("Seja bem-vindo ao Roda Roda PY!")
    quantidade_jogadores = int(input("Informe o número de jogadores: "))
    jogadores = []

    palavra_secreta = sorteia_palavra_secreta()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)

    index = 0
    while (len(jogadores) < quantidade_jogadores):
        jogador = input("Nome do {}º Jogador: ".format(index + 1))
        jogadores.append(jogador)
        index += 1

    print(jogadores)
    print(letras_acertadas)
    jogar(jogadores, palavra_secreta, letras_acertadas)

def jogar(jogadores, palavra_secreta, letras_acertadas):
    index = 0
    while (index < len(jogadores) and "_" in letras_acertadas):
        chama_jogador(jogadores[index])
        rodada(palavra_secreta, letras_acertadas)
        if index == len(jogadores) - 1:
            index = 0
        else:
            index += 1

    print("Fim do jogo, Parabéns {} , você ganhou!!".format(jogadores[index - 1]))

def sorteia_palavra_secreta():
    arquivo = open("palavras_roda_roda.txt", "r")
    palavras = []
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    arquivo.close()

    numero = random.randrange(0, len(palavras))
    return palavras[numero].upper()

def feedback_apresentador(acertou_chute):
    if (acertou_chute):
        print("Voce acertou!")
    else:
        print("Voce errou! \n Próximo Jogador...")

def chama_jogador(nome_jogador):
    print("Agora é a sua vez, {}".format(nome_jogador))

def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]

def pede_chute():
    chute = input("Qual chute?")
    chute = chute.strip().upper()
    return chute

def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra
        index += 1

def rodada(palavra_secreta, letras_acertadas):

    perdeu = False
    erros = 0
    acertou = False

    while (not perdeu and not acertou):
        chute = pede_chute()
        acertou_chute = chute in palavra_secreta

        if acertou_chute:
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
            feedback_apresentador(acertou_chute)
        else:
            erros += 1
            feedback_apresentador(acertou_chute)

        perdeu = erros == 1
        acertou = "_" not in letras_acertadas

        print("Letras acertadas até o momento \n", letras_acertadas)

if (__name__ == "__main__"):
    roda_roda()
