# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define rashford = Character("Rashford")
define mendigan = Character("Mendigan")
define nurse = Character("Nurse")
define seller = Character("Seller")
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

    rashford "Depois de anos de pesquisa nurse experiências"

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

    nurse "Sr. Rashford?"

    rashford "QUE??"

    show rashford neutral

    rashford "ONDE É QUE EU TO????"

    nurse "Se acalme! Você precisa ficar de repouso..."

    rashford "Tchau"

    scene bg snowy_street with Dissolve(1)

    rashford "Blé"

    show rashford neutral

    rashford "Tô puto"

    rashford "nurse triste"

    rashford "Não sei o que fazer"

    rashford "Preciso recuperar a minha receita"

    menu buy_staff:
        "O que fazer?"
        "Ir atrás do Mendigan":
            jump buy_staff_no
        "Comprar um cajado":
            jump buy_staff_yes

    label buy_staff_done:
        scene bg snowy_street with Dissolve(1)

        rashford "Onde eu estava com a cabeça?"

        rashford "Não tenho como enfrentar ele sem habilidade."

        rashford "Preciso comprar um cajado"

        rashford "Vou na loja de magias."

    scene bg store with Dissolve(1)

    show rashford neutral

    seller "Olá! Como posso ajudar?"

    rashford "Estou procurando um cajado, comecei a aprender agora."

    seller "Ah sim! Temos alguns modelos para iniciante. Qual tamanho você gostaria?"
    
    rashford "Humm... Tamanho importa?"

    seller "Com certeza! Quanto maior melhor!"

    rashford "Okay, vou pegar este grandão aqui então.."

    seller "Senhor! Este não é o cajado!"

    rashford "Ops, perdoe-me! Confundi."

    seller "T-tudo bem..."

    seller "Este é o cajado pra iniciante maior que tem"

    rashford "Opa, valeu! Vou levar."

    scene bg snowy_street with Dissolve(1)

    "Eis que estou andando nurse..."

    show mendy neutral at right

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
