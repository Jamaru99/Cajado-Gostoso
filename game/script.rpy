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

    mendigan "Por quê? O que eu ganho se eu deixar com você?"

    rashford "Nada! Mas é uma questão básica de respeito pelo próximo!"

    mendigan "Mas dá pra ver que você tem mais coisas que eu. Eu sou pobre."

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
            jump bad_ending1_mendigan_meeting
        "Comprar um cajado":
            rashford "Melhor eu comprar um cajado antes!"
            jump staff_store

    # This ends the game.

    return
