label mendy_trainning:
    scene bg snowy park with Dissolve(1)

    mendy "Primeiro você pega assim..."

    mendy "E faz assim..."

    rashford "Tô fazendo certo?"

    mendy "Pode ser mais bruto."

    mendy "Faça esse cajado destruir tudo!"

    scene black with Dissolve(1)

    "KABOOMMM"

    mendy "Wow!"

    scene bg snowy park with Dissolve(1)

    rashford "Já deu 5 horas..."

    show rashford staff:
        xalign 0.25
        yalign 1.0

    show mendy neutral:
        xalign 0.75
        yalign 1.0

    "..."

    mendy "Quer descansar um pouco?"

    mendy "Já fez um ótimo progresso!"

    rashford "Sim, melhor a gente ir dormir."

    mendy "Ér..."

    rashford "O que foi?"

    mendy "E-Eu tava pensando de a gente ir no bar tomar uma... Mas deixa, você deve estar cansado..."

    menu go_to_bar:
        "BORA TOMAR UMA":
            rashford "BORA TOMAR UMA!!!!!"
            jump bar_talk
        "Dormir":
            rashford "O sono ajuda a reter o aprendizado, melhor irmos dormir."

            mendy "Verdade..."

            rashford "Você mora longe e já está de madrugada. Quer passar a noite lá em casa?"

            mendy "aaaaa asdasd huassdopf"

            rashford "Que? Você está bem?"

            mendy "Q-quero sim! Obrigada!"

            rashford "Então vamos"

            jump rashford_house

