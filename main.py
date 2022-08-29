#print("Aluna: Isabeli Bora - Gestão da Tecnologia da Informação")
from random import choice as chooseRandom
from time import sleep


def adicionaCerebroEVerificaVencedor(indexJogador, jogadores):
    jogadores[indexJogador]['cerebros'] += 1
    print('Você comeu 1 cérebro! 🧠')

    if jogadores[indexJogador]['cerebros'] < 13:
        return False

    print('\nVocê ganhou! 🏆')

    return True


def adicionaTiroERetornaVida(indexJogador, jogadores):
    jogadores[indexJogador]['tiros'] += 1
    print('Você levou 1 tiro! 🎯')

    if jogadores[indexJogador]['tiros'] < 3:
        return True

    print('\nVocê morreu! 😵')

    return False


def mostraVitimaFugindo():
    print('1 vítima fugiu! 🏃‍')


def criaDado(variavel, faces, quantidade):
    for i in range(quantidade):
        variavel.append(faces)

print("\033[1;36mPROJETO DA DISCIPLINA: Implementação de jogo digital - ZOMBIE DICE (Protótipo Semana 4)\n")
print("Seja bem-vindo ao jogo Zombie Dice! \U0001f9df")

contJogadores = 0
while contJogadores < 2:
    contJogadores = int(input('\nPor favor, informe a quantidade de jogadores: '))

    if contJogadores < 2:
        print('ATENÇÃO!: Você precisa de pelo menos 2 jogadores!')

jogadores = []

for i in range(contJogadores):
    nome = ''

    while nome == '':
        nome = input('Informe o nome do jogador ' + str(i + 1) + ': ').strip()

        if nome == '':
            print('ATENÇÃO!: Você precisa informar um nome para o jogador!')

    jogadores.append({
        "nome": nome,
        "cerebros": 0,
        "tiros": 0,
    })

contRodada = 1
jogadorVez = 0
vencedor = False

while not vencedor:
    print('\n\n\n')
    print('Rodada número:', contRodada)
    print('Vez do jogador:', jogadores[jogadorVez]['nome'])

    dadosSorteados = []
    quantidadeDados = 3
    dados = []
    faceDadoVerde = ["C", "P", "C", "T", "P", "C"]
    faceDadoAmarelo = ["T", "P", "C", "T", "P", "C"]
    faceDadoVermelho = ["T", "P", "T", "C", "P", "T"]

    criaDado(dados, faceDadoVerde, 6)
    criaDado(dados, faceDadoAmarelo, 4)
    criaDado(dados, faceDadoVermelho, 3)

    for i in range(quantidadeDados):
        dadoSorteado = chooseRandom(dados)
        dados.remove(dadoSorteado)
        dadosSorteados.append(dadoSorteado)

    facesViradas = []
    print('Os dados virados são:', end=' ')

    for i in range(quantidadeDados):
        faceVirada = chooseRandom(dadosSorteados[i])
        facesViradas.append(faceVirada)

        separadorPrint = ' | '

        if i == (quantidadeDados - 1):
            separadorPrint = '\n\n'

        print(faceVirada, end=separadorPrint)

    print('Processando...')
    sleep(1.5)

    jogadorContinuaVivo = True

    for i in range(quantidadeDados):
        if not jogadorContinuaVivo:
            break

        if facesViradas[i] == 'C':
            jogadorVencedor = adicionaCerebroEVerificaVencedor(jogadorVez, jogadores)

            if jogadorVencedor:
                vencedor = jogadores[jogadorVez]
                break
        elif facesViradas[i] == 'T':
            jogadorContinuaVivo = adicionaTiroERetornaVida(jogadorVez, jogadores)

            if not jogadorContinuaVivo:
                jogadores.pop(jogadorVez)
                break
        elif facesViradas[i] == 'P':
            mostraVitimaFugindo()

    if len(jogadores) == 0 or vencedor:
        break

    print('\nAtualmente o placar está assim: ')
    for i in range(len(jogadores)):
        print('Nome:', jogadores[i]['nome'], end=' - ')
        print('Cérebros:', jogadores[i]['cerebros'], end=' - ')
        print('Tiros:', jogadores[i]['tiros'])

    contRodada += 1

    if jogadorContinuaVivo:
        continuaJogando = input("\nGostaria de continuar jogando? Digite 1 para SIM e qualquer outra tecla para "
                                    "NÃO! \n")
        if continuaJogando == "1":
            continue
        else:
            jogadores[jogadorVez]['tiros'] = 0

    jogadorVez += 1

    if jogadorVez >= len(jogadores):
        jogadorVez = 0

if not vencedor:
    print('\nTodos estão mortos')
else:
    print('\nO vencedor é:', vencedor['nome'])

    print('\n🎲 Fim de jogo! 🎲')

