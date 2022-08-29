# print("Aluna: Isabeli Bora - Gestão da Tecnologia da Informação")
from random import choice as chooseRandom
from time import sleep


# Função para adicionar +1 para a propriedade "cerebros" do objeto do jogador e verificar se ganhou
def adicionaCerebroEVerificaVencedor(indexJogador, jogadores):
    # Adiciona +1 para a propriedade de "cerebros" do jogador
    jogadores[indexJogador]['cerebros'] += 1
    print('Você comeu 1 cérebro! 🧠')

    # Se a contagem de cérebros for menor que 13, significa que o jogador ainda não ganhou, então retorna False antecipadamente
    if jogadores[indexJogador]['cerebros'] < 13:
        return False

    # Senão, printa a mensagem de vitória na tela e retorna True logo em seguida
    print('\nVocê ganhou! 🏆')

    return True


# Função para adicionar +1 para propriedade "tiros" do objeto de jogador
def adicionaTiroERetornaVida(indexJogador, jogadores):
    # Adiciona +1 para a propriedade de "tiros" do jogador
    jogadores[indexJogador]['tiros'] += 1
    print('Você levou 1 tiro! 🎯')

    # Se a contagem de tiros for menor que 3, significa que o jogador ainda está vivo, então retorna True antecipadamente
    if jogadores[indexJogador]['tiros'] < 3:
        return True

    # Senão, printa a mensagem de informando que o jogador morreu e retorna False logo em seguida
    print('\nVocê morreu! 😵')

    return False


# Função para mostrar os passos (vítima que fugiu)
def mostraVitimaFugindo():
    print('1 vítima fugiu! 🏃‍')

# Função para criar os dados atribuindo a uma variavel de acordo com a quantidade e faces
def criaDado(variavel, faces, quantidade):
    for i in range(quantidade):
        variavel.append(faces)


print("\033[1;36mPROJETO DA DISCIPLINA: Implementação de jogo digital - ZOMBIE DICE (Protótipo Semana 4)\n")
print("Seja bem-vindo ao jogo Zombie Dice! \U0001f9df")

# Código para pedir a quantidade de jogadores
contJogadores = 0
while contJogadores < 2:
    contJogadores = int(input('\nPor favor, informe a quantidade de jogadores: '))

    # Se o jogador inserir uma quantidade de jogadores menor que 2 irá mostrar um aviso na tela
    if contJogadores < 2:
        print('ATENÇÃO!: Você precisa de pelo menos 2 jogadores!')

# Criado um array para armazenar os jogadores
jogadores = []

for i in range(contJogadores):
    nome = ''

    while nome == '':
        # Solicitação da entrada do nome do jogador, removendo os espaços do começo e final da resposta do input
        nome = input('Informe o nome do jogador ' + str(i + 1) + ': ').strip()

        # Caso o jogador tente inserir uma string vazia passará um alerta de invalidez
        if nome == '':
            print('ATENÇÃO!: Você precisa informar um nome para o jogador!')

    # Inserção do objeto do jogador dentro do array de jogadores
    jogadores.append({
        "nome": nome,
        "cerebros": 0,
        "tiros": 0,
    })

# Criação das variaveis usadas para a execução das rodadas
contRodada = 1
jogadorVez = 0
vencedor = False

# Enquanto não tiver vencedor, as rodadas continuarão acontecendo
while not vencedor:
    # Exibição do número da rodada e nome do jogador
    print('\n\n\n')
    print('Rodada número:', contRodada)
    print('Vez do jogador:', jogadores[jogadorVez]['nome'])

    # Criação de variável para armazenar os dados da rodada, a quantidade e os dados que estão no tubo
    dadosSorteados = []
    quantidadeDados = 3
    dados = []

    # Criação das faces dos dados: Verdes | Amarelos | Vermelhos
    faceDadoVerde = ["C", "P", "C", "T", "P", "C"]
    faceDadoAmarelo = ["T", "P", "C", "T", "P", "C"]
    faceDadoVermelho = ["T", "P", "T", "C", "P", "T"]

    criaDado(dados, faceDadoVerde, 6)
    criaDado(dados, faceDadoAmarelo, 4)
    criaDado(dados, faceDadoVermelho, 3)

    # Sorteio dos dados da rodada
    for i in range(quantidadeDados):
        # Execução da funçãao random.choice para escolher aleatoriamente dentro do array de dados
        dadoSorteado = chooseRandom(dados)
        # Execução da função remove para remover o dado já sorteado do tubo
        dados.remove(dadoSorteado)
        dadosSorteados.append(dadoSorteado)

    facesViradas = []
    print('Os dados virados são:', end=' ')

    # Sorteio das faces dos dados da rodada
    for i in range(quantidadeDados):
        # Execução da funçãao random.choice para escolher aleatoriamente dentro do array de dadosSorteados[i]
        faceVirada = chooseRandom(dadosSorteados[i])
        facesViradas.append(faceVirada)

        separadorPrint = ' | '

        if i == (quantidadeDados - 1):
            separadorPrint = '\n\n'

        # Impressão da face virada do dado
        print(faceVirada, end=separadorPrint)

    print('Processando...')
    sleep(1.5)

    # Variavel de controle de vida do jogador, caso o jogador leve 3 tiros, essa variavel será False
    jogadorContinuaVivo = True

    for i in range(quantidadeDados):
        # Verificação se o jogador já não está morto nesta rodada antes de executar todas as ações de faces
        if not jogadorContinuaVivo:
            break

        if facesViradas[i] == 'C':
            jogadorVencedor = adicionaCerebroEVerificaVencedor(jogadorVez, jogadores)

            # Verifica se o jogador já não ganhou, e se sim, atribui ele para a variavel de controle de vencedor e para o loop do for
            if jogadorVencedor:
                vencedor = jogadores[jogadorVez]
                break
        elif facesViradas[i] == 'T':
            jogadorContinuaVivo = adicionaTiroERetornaVida(jogadorVez, jogadores)

            # Verifica se o jogador já não morreu, e se não, retira ele do array de jogadores através do index
            if not jogadorContinuaVivo:
                jogadores.pop(jogadorVez)
                break
        elif facesViradas[i] == 'P':
            mostraVitimaFugindo()

    # Se não tiver mais jogadores vivos ou já tivermos um vencedor, quebra o loop do while e finaliza o jogo
    if len(jogadores) == 0 or vencedor:
        break

    # Impressão do placar informando os pontos dos jogadores
    print('\nAtualmente o placar está assim: ')
    for i in range(len(jogadores)):
        print('Nome:', jogadores[i]['nome'], end=' - ')
        print('Cérebros:', jogadores[i]['cerebros'], end=' - ')
        print('Tiros:', jogadores[i]['tiros'])

    # Aumentamos o número da rodada
    contRodada += 1

    # Caso o jogador deseje continuar jogando irá continuar na próxima rodada, se não passa a vez para o outro jogador
    if jogadorContinuaVivo:
        continuaJogando = input("\nGostaria de continuar jogando? Digite 1 para SIM e qualquer outra tecla para "
                                "NÃO! \n")

        # Jogamos para a próxima execução do while caso o jogador deseje continuar jogando, sem zerar a contagem de tiros
        if continuaJogando == "1":
            continue
        else:
            # Zeramos a contagem de tiros caso o jogador não queira mais jogar e ainda continue vivo
            jogadores[jogadorVez]['tiros'] = 0

    jogadorVez += 1

    # Caso esta roda tenha sido do último jogador, definimos que o próximo jogador será o primeiro da lista novamente
    if jogadorVez >= len(jogadores):
        jogadorVez = 0

# Caso não tenha nenhum vencedor e acabe o jogo, significa que não tem nenhum sobrevivente, então é mostrado isso na tela
if not vencedor:
    print('\nTodos estão mortos')
else:
    print('\nO vencedor é:', vencedor['nome'])

    print('\n🎲 Fim de jogo! 🎲')
