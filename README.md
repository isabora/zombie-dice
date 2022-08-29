<p align="center">
  <a href="https://github.com/isabora/zombie-dice">
    <img src="readme.png" alt="readme-logo" width="80" height="80">
  </a>

  <h3 align="center">
    zombie-dice
  </h3>
  <p align="center">
    <a href="https://github.com/isabora/zombie-dice/blob/master/README.md"><strong>Explore a documentação »</strong></a>
    <br />
    <br />
    <a href="https://github.com/isabora/zombie-dice/issues">Reporte um bug</a>
    ·
    <a href="https://github.com/isabora/zombie-dice/issues">Requisite uma funcionalidade</a>
  </p>
</p>

<details open="open">
  <summary><h2 style="display: inline-block">📜 Sumário</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">Sobre o projeto</a>
    </li>
    <li><a href="#usage">Uso</a></li>
  </ol>
</details>

## 📋 Sobre o projeto

O jogo é composto por um tubo que armazena 13 dados de 6 faces. Existem 3 tipos de dados diferentes: verdes, vermelhos e
amarelos. Os dados possuem 3 símbolos diferentes (tiro, cérebro e passos). Os dados vermelhos são os mais difíceis,
possuem um número maior de faces com o símbolo tiro. Os verdes são os mais fáceis, o maior número de faces do dado é de
cérebro. Os dados amarelos são intermediários as faces dos dados possuem a mesma quantidade cérebros, tiros e passos. Em
um rodada, cada jogador tem um turno para jogar. No turno, o jogador deve pegar aleatoriamente 3 dados do tubo e lançar,
sempre os três dados juntos. Quando a face do dado cair virada com símbolo para "cérebro", é porque o jogador comeu um
cérebro. Caso a face do dado cair virada com o símbolo para "passos", a vítima fugiu, se o jogador decidir continuar a
lançar os dados em seu turno, os dados que caíram com a face para “passos” deverão ser lançados novamente. Para lançar
novamente os três dados o jogador completa a quantidade retirando outros dados do tubo, sempre lançando os três dados. O
objetivo é comer 13 cérebros para vencer o jogo, no entanto, existem os tiros de espingarda! Se por acaso o jogador
levar três tiros de espingarda ele perde e sai do jogo. No seu turno, após lançar os dados, o jogador pode decidir parar
ou continuar a jogar. Caso decida parar, você contabiliza os cérebros para próxima jogada, já os dados de tiro são
zerados para próxima rodada.

![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)
![Python](https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white)


## 🏁 Uso

Clone o projeto e entre na raiz do diretório

```bash
$ git clone https://github.com/isabora/zombie-dice

$ cd zombie-dice
```

Rode a aplicação:

```bash
$ py main.py
```
