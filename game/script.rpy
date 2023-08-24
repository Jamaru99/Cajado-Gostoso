# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define rashford = Character("Rashford")
define mendigan = Character("Mendigan")
define enfermeira = Character("Enfermeira")
define vendedor = Character("Vendedor")
define mendy = Character("Mendy")

# The game starts here.

label start:

    scene bg laboratory
    image tuboensaio = "images/tubo.png"
    
    show tuboensaio:
        xalign 0.3
        yalign 0.6

    rashford "Já é meia noite"

    show rashford neutral

    rashford "Estou bem próximo de conseguir descobrir a cura da Aids"

    rashford "Depois de anos de pesquisa e experiências"

    rashford "Sinto que hoje é o dia"

    rashford "É agora"

    rashford "AAAAAAAAAA DESCOBRI"

    "??? (barulho estranho)"

    rashford "o que é isso? tem alguém aí?"

    mendigan "OPAAAAAAAAAAAAAAAA"

    show mendigan neutral at right with Dissolve(2.0)

    mendigan "CHEGAY"

    rashford "Quem é você? O que tá fazendo aqui?"

    mendigan "Comendo cú de curioso"

    rashford "..."

    mendigan "Brinks"

    mendigan "Vi que você descobriu a cura da Aids"

    mendigan "AGORA PASSA PRA CÁ!!!"

    rashford "Ué, por que?"

    mendigan "Porque eu vou vender"

    rashford "Mas fui eu que descobri, é minha propriedade"

    mendigan "Idaí? Me dá logo"

    rashford "Não"

    mendigan "Ah é?"

    show mendigan attacking

    mendigan "Então pega no meu cajado!"

    show rashford hurt at left

    rashford "AAAAAA"

    rashford "VOCÊ NÃO PODE PEGAR"

    show mendigan neutral

    mendigan "Por quê? O que eu ganho se eu deixar com você"

    rashford "Nada! Mas é uma questão básica de respeito pelo próximo!"

    mendigan "Mas dá pra ver que você é mais rico que eu. Eu sou pobre."

    rashford "Não justifica!!"

    mendigan "Blá blá blá. Tchau!"

    hide mendigan

    hide tuboensaio

    rashford "NÃAOOOOOOOOOOOOOOOOO"

    show rashford dead at left

    rashford "Acabou... como vou comprar dinheiro de joguinho online agora..."

    scene bg hospital with Dissolve(1)

    rashford "zzz"

    rashford "ahhh..."

    rashford "que grandão..."

    rashford "queria um cajado assim..."

    enfermeira "Sr. Rashford?"

    rashford "QUE??"

    show rashford neutral

    rashford "ONDE É QUE EU TO????"

    enfermeira "Se acalme! Você precisa ficar de repouso..."

    rashford "Tchau"

    scene bg snowy_street with Dissolve(1)

    rashford "Blé"

    show rashford neutral

    rashford "Tô puto"

    rashford "E triste"

    rashford "Não sei o que fazer"

    rashford "Preciso recuperar a minha receita"

    menu buy_staff:
        "O que fazer?"
        "Ir atrás do Mendigan":
            $ buy_staff_choice = False
            jump buy_staff_no
        "Comprar um cajado":
            $ buy_staff_choice = True
            rashford "Melhor eu comprar um cajado antes!"
            jump staff_store

    label buy_staff_done:
        scene bg snowy_street with Dissolve(1)

        rashford "Onde eu estava com a cabeça?"

        rashford "Não tenho como enfrentar ele sem de mãos vazias."

        rashford "Preciso comprar um cajado"

        rashford "Vou na loja de magias."

    label staff_store:

        scene bg store with Dissolve(1)

        show rashford neutral

        vendedor "Olá! Como posso ajudar?"

        rashford "Estou procurando um cajado, comecei a aprender agora."

        vendedor "Ah sim! Temos alguns modelos para iniciante. Qual tamanho você gostaria?"
        
        rashford "Humm... Tamanho importa?"

        vendedor "Com certeza! Quanto maior melhor!"

        rashford "Okay, vou pegar este grandão aqui então.."

        vendedor "Senhor! Este não é o cajado!"

        rashford "Ops, perdoe-me! Confundi."

        vendedor "T-tudo bem..."

        vendedor "Este é o cajado pra iniciante maior que tem"

        rashford "Opa, valeu! Vou levar."

        if buy_staff_choice == True: 
            rashford "Agora vou atrás daquele maluco!"
            jump buy_staff_yes

    label meeting_mendy:

        scene bg snowy_street with Dissolve(1)

        "Rashford sai da loja e tropeça em uma moça que estava passando"

        show mendy neutral:
            xalign 0.75
            yalign 1.0

        show rashford neutral:
            xalign 0.25
            yalign 1.0

        rashford "Opa, foi mal senhorita..."

        rashford "Pera..."

        rashford "Mendy???"

        mendy "o-oi..."

        rashford "Quanto tempo! Como você tá?"

        mendy "Tô bem... e você?"

        rashford "Tô bem também."

        mendy "Que bom.."

        rashford "Sim. Tchau!"

        mendy "Ér... Rashford..."

        rashford "Diga."

        mendy "Você tá bem mesmo?"

        rashford "Humm... Na verdade não. Mas sempre respondo que ta tudo bem."

        mendy "Entendo... Vi que está andando com um cajado..."

        rashford "Ah sim! Estou furioso!"

        mendy "E posso saber o porquê?"

        rashford "Um maluco roubou a minha descoberta científica que iria curar a cidade inteira da pandemia, e vai ficar com os créditos!"

        mendy "Oh.. Que droga.."

        rashford "Agora vou lá matar ele!"

        mendy "Espera!"

        rashford "O que foi?"

        mendy "Rash... Você sabe usar um cajado?"

        rashford "..."

        rashford "Como assim? Não é só apontar e atirar?"

        mendy "Não.. precisa de muita prática."

        rashford "Puta merda!"

        mendy "Ér.. se você quiser eu te ensino..."

        rashford "Sério? De graça?"

        mendy "Ah pode ser... Ou então pode me pagar em favores.."

        rashford "Pois eu faço o que você quiser!"

        mendy "Ok, então vamos ali no parque treinar."

        rashford "Fechou!"

    # This ends the game.

    return
