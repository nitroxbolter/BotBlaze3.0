def check_patterns(cores, enviar_sinal, correcao, analise_sinal, cor_sinal):
    """Verifica os padrões de sinais e envia mensagens correspondentes."""

    if analise_sinal:
        correcao(cores, cor_sinal)
    else:
        padrões = {
            ('V', 'P'): '🥷🏼Samurai🥷🏼',
            ('V', 'P', 'V'): '👑King👑',
        }

        for seq, padrao in padrões.items():
            if len(cores) >= len(seq) and cores[:len(seq)] == list(seq):
                cor_sinal = '⚫️'
                enviar_sinal(cor_sinal, padrao)
                analise_sinal = True
                break

    return analise_sinal, cor_sinal
