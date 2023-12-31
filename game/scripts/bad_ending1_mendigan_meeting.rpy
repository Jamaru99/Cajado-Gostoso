label bad_ending1_mendigan_meeting:
    rashford "Vou atrás daquele malandro e matar ele!"

    hide rashford

    scene bg snowy_house with Dissolve(1)

    rashford "É aqui que ele mora"

    rashford "Depois de bater de porta em porta esta foi a única que restou na cidade"

    show rashford neutral:
        xalign 0.25
        yalign 1.0

    "toc toc"

    "..."

    show mendigan neutral:
        xalign 0.75
        yalign 1.0
    with Dissolve(2.0)

    mendigan "Saudações"

    rashford "Arrombado do caralho"

    mendigan "?"

    mendigan "Isso é jeito de cumprimentar alguém?"

    show mendigan attacking

    show rashford dead at left

    "SE FODEO"

    return
