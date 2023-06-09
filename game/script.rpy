﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define r = Character("Rashford")
define m = Character("Mendigan")
define e = Character("Enfermeira")
define v = Character("Vendedor")

# The game starts here.

label start:

    scene bg laboratory
    image tuboensaio = "images/tubo.png"
    
    show tuboensaio:
        xalign 0.3
        yalign 0.6

    r "Já é meia noite"

    show rashford neutral

    r "Estou bem próximo de conseguir descobrir a cura da Aids"

    r "Depois de anos de pesquisa e experiências"

    r "Sinto que hoje é o dia"

    r "É agora"

    r "AAAAAAAAAA DESCOBRI"

    "??? (barulho estranho)"

    r "o que é isso? tem alguém aí?"

    m "OPAAAAAAAAAAAAAAAA"

    show mendigan neutral at right with Dissolve(2.0)

    m "CHEGAY"

    r "Quem é você? O que tá fazendo aqui?"

    m "Comendo cú de curioso"

    r "..."

    m "Brinks"

    m "Vi que você descobriu a cura da Aids"

    m "AGORA PASSA PRA CÁ!!!"

    r "Ué, por que?"

    m "Porque eu vou vender"

    r "Mas fui eu que descobri, é minha propriedade"

    m "Idaí? Me dá logo"

    r "Não"

    m "Ah é?"

    show mendigan attacking

    m "Então pega no meu cajado!"

    show rashford hurt at left

    r "AAAAAA"

    r "VOCÊ NÃO PODE PEGAR"

    show mendigan neutral

    m "Por quê? O que eu ganho se eu deixar com você"

    r "Nada! Mas é uma questão básica de respeito pelo próximo!"

    m "Mas dá pra ver que você é mais rico que eu. Eu sou pobre."

    r "Não justifica!!"

    m "Blá blá blá. Tchau!"

    hide mendigan

    hide tuboensaio

    r "NÃAOOOOOOOOOOOOOOOOO"

    show rashford dead at left

    r "Acabou... como vou comprar dinheiro de joguinho online agora..."

    scene bg hospital with Dissolve(1)

    r "zzz"

    r "ahhh..."

    r "que grandão..."

    r "queria um cajado assim..."

    e "Sr. Rashford?"

    r "QUE??"

    show rashford neutral

    r "ONDE É QUE EU TO????"

    e "Se acalme! Você precisa ficar de repouso..."

    r "Tchau"

    scene bg snowy_street with Dissolve(1)

    r "Blé"

    show rashford neutral

    r "Tô puto"

    r "E triste"

    r "Não sei o que fazer"

    r "Preciso recuperar a minha receita"

    menu buy_staff:
        "O que fazer?"
        "Ir atrás do Mendigan":
            jump buy_staff_no
        "Comprar um cajado":
            jump buy_staff_yes

    label buy_staff_done:
        scene bg snowy_street with Dissolve(1)

        r "Onde eu estava com a cabeça?"

        r "Não tenho como enfrentar ele sem habilidade."

        r "Preciso comprar um cajado"

        r "Vou na loja de magias."

    scene bg store with Dissolve(1)

    show rashford neutral

    v "Olá! Como posso ajudar?"

    r "Estou procurando um cajado, comecei a aprender agora."

    v "Ah sim! Temos alguns modelos para iniciante. Qual tamanho você gostaria?"
    
    r "Humm... Tamanho importa?"

    v "Com certeza! Quanto maior melhor!"

    r "Okay, vou pegar este grandão aqui então.."

    v "Senhor! Este não é o cajado!"

    r "Ops, perdoe-me! Confundi."

    v "T-tudo bem..."

    v "Este é o cajado pra iniciante maior que tem"

    r "Opa, valeu! Vou levar."

    # This ends the game.

    return
