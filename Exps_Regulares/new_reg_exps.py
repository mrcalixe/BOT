import re

exemplo = r'.*/RG .*/PP? (verbo=$verbos)/.* (lugar=.*)/.* ?/Fit'

pergunta_lugar_v2 = r'.*/RG .*/PP? $verbos/.* (locality=.*)/.* ?/Fit?'

mapa_substituicao = {'nome_geral': r'N\w+',
                     'nome_proprio_geral': r'NP\w+',
                     'nome_comum_geral': r'NC\w+',

                     # Verbos
                     'verbo_geral': r'V\w*',
                     'verbo_indicativo_presente_geral': r'VMIP\w*',

                     # Conjução
                     'conjucao_sub': r'CS',
                     'conjucao_coord': r'CC',

                     # Advérbios
                     'adverbio_geral': r'RG',

                     # Pronomes
                     'pronome_geral': r'P\w*',
                     'pronome_pessoal_geral': r'PP\w*',

                     # Determinantes
                     'determinante_geral': r'D\w*',
                     'determinante_artigo_geral': r'DA\w*',

                     # Pontuação
                     'pontuacao': r'F\w*',
                     'pergunta': r'Fit',

                     # Interjeição
                     'interjeicao': r'I',
                     'interjeicao_intro': r'(olá|boas)',
                     'interjeicao_outro': r'(xau|adeus)',

                     # Palavras reservadas
                     'verbos_lugar': r'(ficar|estar|situar|localizar)'
                     }


def my_replace(t):
    a, b = t
    if '=' in a:
        a = a.replace('(', '').replace(')', '')

    if a == r'.*':
        a = r'\w+'

    if b == r'.*':
        b = r'\w+'

    if r'$' in a:
        i = a.find('$')
        aux = a[:i]
        subs = mapa_substituicao[a[i + 1:]]
        # print('Substituir $ na pos', i,'por', subs)
        aux += subs
        a = aux

    if r'.*' in a:
        i = a.find(r'.*')
        aux = a[:i]
        aux += r'\w+'
        a = aux
        # print(r'Substituir .* na pos', i, r'por .* =>', a)

    # print('Replaced:', t,'with',(a,b))
    return (a, b)


def compile(reg_exp):
    regex = r''
    # Primeiro passo é substituir todas as strings
    # Exemplo: .* por \w+, $verbo por (verbo1|verbo2|...), etc
    tokens = map(lambda x: tuple(x.split('/')), reg_exp.split())
    # [('.*', 'RG'), ('.*', 'PP?'), ('(Verbo=$verbos)', '.*'), ('(Lugar=.*)', '.*'), ('?', 'Fit')]
    tokens = map(lambda x: my_replace(x), tokens)
    # [('.*', 'RG'), ('.*', 'PP?'), ('Verbo=$verbos', '.*'), ('Lugar=.*', '.*'), ('?', 'Fit')]

    tokens = list(tokens)
    for a, b in tokens:
        # Ver em a se tem algum grupo para fazer catch
        if '=' in a and b[-1] == '?':
            i = a.find('=')
            regex += r'(' + b[:-1] + r'\:' + r'(?P<' + a[:i] + '>' + a[i + 1:] + r')){0,1}\s* '
        elif '=' in a:
            i = a.find('=')
            regex += r'(' + b + r'\:' + r'(?P<' + a[:i] + '>' + a[i + 1:] + r'))\s* '
        elif b[-1] == '?':
            regex += r'(' + b[:-1] + r'\:' + a + r'){0,1}\s* '
        else:
            regex += r'(' + b + r'\:' + a + r')\s* '

    return regex
