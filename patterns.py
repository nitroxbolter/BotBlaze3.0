def check_patterns(cores, enviar_sinal, correcao, analise_sinal, cor_sinal):
    """Verifica os padrões de sinais e envia mensagens correspondentes."""
    
    if analise_sinal:
        correcao(cores, cor_sinal)
    else:
        if cores[0:2] == ['V', 'P']:
            cor_sinal = '⚫️'
            padrao = '🥷🏼Samurai🥷🏼'
            enviar_sinal(cor_sinal, padrao)
            analise_sinal = True

        elif cores[0:3] == ['V', 'P', 'V']:
            cor_sinal = '⚫️'
            padrao = '👑King👑'
            enviar_sinal(cor_sinal, padrao)
            analise_sinal = True

    return analise_sinal, cor_sinal
