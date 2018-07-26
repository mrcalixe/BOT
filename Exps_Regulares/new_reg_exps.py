import re

Regexs = {
    'pergunta_lugar'  : r'.*/RG .*/$pronome_pessoal_geral? $verbos_lugar/$verbo_indicativo_presente_geral .*/$determinante_geral? (locality=.*)/.* .*/Fit?',
    'pergunta_pessoa' : r'.*/$pronome_geral .*/$verbo_geral (name=.*)/nome_proprio_geral ?/Fit?'
}


Regexs_Backup = {
    #'nome' : r'(name=.*)/$nome_geral'
}


Regexs_Especiais = {
    'intro'               : r'$intro/.*',
    'apresentacao_pessoa' : r'.*/$pronome_pessoal_geral? .*/$verbo_indicativo_presente_geral .*/$determinante_artigo_geral (name=.*)/$nome_proprio_geral',
    'outro'               : r'$outro/.*'
}

mapa_acoes = {
    'pergunta_lugar'      : ['procura_lugar'],
    'pergunta_pessoa'     : ['pergunta_pessoa'],
    'intro'               : ['bem_vindo'],
    'apresentacao_pessoa' : ['bem_vindo'],
    'outro'               : ['adeus']
}

mapa_substituicao = {
    # Adjetivos
    'adjetivo_geral' : r'A\w+',

    # Advérbios
    'adverbio_geral' : r'RG',

    # Conjuções
    'conjucao_sub'   : r'CS',
    'conjucao_coord' : r'CC',

    # Determinantes
    'determinante_geral'        : r'D\w*',
    'determinante_artigo_geral' : r'DA\w*',

    # Interjeição
    'interjeicao' : r'I',

    #Nomes
    'nome_geral'         : r'N\w+',
    'nome_proprio_geral' : r'NP\w+',
    'nome_comum_geral'   : r'NC\w+',

    # Preposição
    'preposicao' : r'SP',

    # Pronomes
    'pronome_geral'         : r'P\w*',
    'pronome_pessoal_geral' : r'PP\w*',

    # Verbos
    'verbo_geral'                     : r'V\w*',
    'verbo_indicativo_presente_geral' : r'VMIP\w*',


    # Pontuação
    'pontuacao' : r'F\w*',
    'pergunta'  : r'Fit',

    # Palavras reservadas
    'verbos_lugar' : r'(ficar|estar|situar|localizar)',
    'verbo_ser'    : r'ser',
    'intro'        : r'(olá|boas)',
    'outro'        : r'(xau|adeus)'
}


#Feita
def my_replace(t):
    r'''
    Function that replaces special characters in the Regular Expressions of the Linguistic Model
    :param t: str <- regular expression of the linguistic model
    :return: (a,b) <- the regular expression of the linguistic model transformed
    '''
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

    if r'$' in b:
        if r'?' in b:
            i = b.find('$')
            aux = b[:i]
            subs = mapa_substituicao[ b[i+1 : -1] ]
            # print('Substituir $ na pos', i,'por', subs)
            aux += subs
            aux += r'?'
            b = aux
        else:
            i = b.find('$')
            aux = b[:i]
            subs = mapa_substituicao[b[i + 1:]]
            # print('Substituir $ na pos', i,'por', subs)
            aux += subs
            b = aux

    if r'.*' in a:
        i = a.find(r'.*')
        aux = a[:i]
        aux += r'\w+'
        a = aux
        # print(r'Substituir .* na pos', i, r'por .* =>', a)

    # print('Replaced:', t,'with',(a,b))
    return (a, b)


#Feita
def compile(reg_exp):
    r'''
    Compile a given Linguistic Regular Expression into a Regular Expression
    :param reg_exp:
    :return:
    '''
    regex = r''
    tokens = map(lambda x: tuple(x.split('/')), reg_exp.split())
    tokens = map(lambda x: my_replace(x), tokens)

    tokens = list(tokens)
    for a, b in tokens:
        # Ver em a se tem algum grupo para fazer catch
        if '=' in a and b[-1] == '?':
            i = a.find('=')
            regex += r'(' + b[:-1] + r'\:' + r'(?P<' + a[:i] + '>' + a[i + 1:] + r')){0,1}\s*'
        elif '=' in a:
            i = a.find('=')
            regex += r'(' + b + r'\:' + r'(?P<' + a[:i] + '>' + a[i + 1:] + r'))\s*'
        elif b[-1] == '?':
            regex += r'(' + b[:-1] + r'\:' + a + r'){0,1}\s*'
        else:
            regex += r'(' + b + r'\:' + a + r')\s*'

    return re.compile(regex, re.IGNORECASE)


#Feita
def parse_analise(analise):
    r'''
    Function that transform the analysis from FreeLing to conform with the Linguistic Model
    :param analise: str <- FreeLing output
    :return: str <- Parsed FreeLing output
    '''
    s = r''
    for (lemma, tag, word) in analise:
        aux = tag + r':' + lemma + r' '
        s = s + aux
    return s[:(len(s)) - 1]


#Feita
def verifica_especiais(frase):
    r'''
    Function that verifies if a given sentence belongs to the special kind, like, Hello, Goodbye, etc.
    :param frase: str
    :return: dict
    '''
    matched = {}
    for reg_exp in Regexs_Especiais.keys():
        res = Regexs_Especiais[reg_exp].search(frase)
        if res:
            matched[reg_exp] = res.groupdict()
    return matched


#Feita
def verifica(frase):
    r'''
    Function that verifies if a given sentence as a match in the Model
    :param frase: str
    :return: dict
    '''
    matched = {}
    for reg_exp in Regexs.keys():
        res = Regexs[reg_exp].search(frase)
        if res:
            matched[reg_exp] = res.groupdict()
    return matched


#Feita
def verifica_backup(frase):
    r'''
    Function that verifies if a given sentence belongs to the Backup category of the Model
    :param frase: str
    :return: dict
    '''
    matched = {}
    for reg_exp in Regexs_Backup.keys():
        res = Regexs_Backup[reg_exp].search(frase)
        if res:
            matched[reg_exp] = res.groupdict()
    return matched


###################################################
# Criação e compilação das expressões             #
# regulares dadas pela criação de contextos       #
###################################################

Contexto = {
    'Mundia' : {
        #RG:quando VMIP3S0:ser DA0MS0:o AQ0MS00:próximo NCMS000:jogo SP:de DA0MS0:o NP00000:mundial Fit:?
        'prox_jogo' : r'.*/RG */$verbo_ser */$determinante_geral */$nome_comum */$preposicao? */$determinante_geral? mundial/$nome_geral .*/Fit?',
        'vencedor_de' : r'',
        'resumo' : r'',
        'tuplos': {
            'vencedor' : ('equipa_1', 'vencedor', 'equipa_2')
        }
    }
}


###################################################
# Compilação das Expressões do Modelo Linguístico #
###################################################

for k in Regexs:
    Regexs[k] = compile(Regexs[k])


#Regexs_Backup = compile(Regexs_Backup)
for k in Regexs_Backup:
    Regexs_Backup[k] = compile(Regexs_Backup[k])


#Regexs_Especiais = compile(Regexs_Especiais)
for k in Regexs_Especiais:
    Regexs_Especiais[k] = compile(Regexs_Especiais[k])