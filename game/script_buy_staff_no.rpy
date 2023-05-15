label buy_staff_no:
    r "Vou atrás daquele malandro e matar ele!"

    hide rashford

    scene bg snowy_house with Dissolve(1)

    r "É aqui que ele mora"

    r "Depois de bater de porta em porta esta foi a única que restou na cidade"

    show rashford neutral:
        xalign 0.25
        yalign 1.0

    "toc toc"

    "..."

    show mendigan neutral:
        xalign 0.75
        yalign 1.0
    with Dissolve(2.0)

    m "Saudações"

    r "Arrombado do caralho"

    m "?"

    m "Isso é jeito de cumprimentar alguém?"

    m "Tá com falta de pica?"

    r "CALA A BOCA! ME DEVOLVE A CURA!!"

    m "A propósito, não nos apresentamos ainda."

    m "Meu nome é Mendigan, vim do interior."

    r "TO POCO ME FODENDO, DEVOLVE LOGO OU ENTÃO..."

    jump buy_staff_done
