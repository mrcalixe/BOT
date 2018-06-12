import re

Regexs = { 'pergunta_lugar'  : r'.*/RG .*/$pronome_pessoal_geral? $verbos_lugar/$verbo_indicativo_presente_geral .*/$determinante_geral? (locality=.*)/.* .*/Fit?',
           'pergunta_pessoa' : r'.*/$pronome_geral .*/$verbo_geral (name=.*)/nome_proprio_geral ?/Fit?'
           }


Regexs_Backup = {'nome' : r'(name=.*)/$nome_geral'}


Regexs_Especiais = { 'intro'               : r'$intro/.*',
                     'apresentacao_pessoa' : r'.*/$pronome_pessoal_geral? .*/$verbo_indicativo_presente_geral .*/$determinante_artigo_geral (name=.*)/$nome_proprio_geral',
                     'outro'               : r'$outro/.*'
}


mapa_substituicao = {'nome_geral'         : r'N\w+',
                     'nome_proprio_geral' : r'NP\w+',
                     'nome_comum_geral'   : r'NC\w+',

                     # Verbos
                     'verbo_geral'                     : r'V\w*',
                     'verbo_indicativo_presente_geral' : r'VMIP\w*',

                     # Conjução
                     'conjucao_sub'   : r'CS',
                     'conjucao_coord' : r'CC',

                     # Advérbios
                     'adverbio_geral' : r'RG',

                     # Pronomes
                     'pronome_geral'         : r'P\w*',
                     'pronome_pessoal_geral' : r'PP\w*',

                     # Determinantes
                     'determinante_geral'        : r'D\w*',
                     'determinante_artigo_geral' : r'DA\w*',

                     # Pontuação
                     'pontuacao' : r'F\w*',
                     'pergunta'  : r'Fit',

                     # Interjeição
                     'interjeicao' : r'I',

                     # Palavras reservadas
                     'verbos_lugar' : r'(ficar|estar|situar|localizar)',
                     'intro'        : r'(olá|boas)',
                     'outro'        : r'(xau|adeus)'
                     }


#Feita
def my_replace(t):
    r'''
    Function that replaces special characters in the Regular Expressions of the Linguistic Model
    :param t: regular expression of the linguistic model
    :return: the regular expression of the linguistic model transformed
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
    s = r''
    for (lemma, tag, word) in analise:
        aux = tag + r':' + lemma + r' '
        s = s + aux
    return s[:(len(s)) - 1]


def verifica_especiais(frase):
    matched = {}
    for reg_exp in Regexs_Especiais.keys():
        res = Regexs_Especiais[reg_exp].search(frase)
        if res:
            matched[reg_exp] = res.groupdict()
    return matched

def verifica(frase):
    matched = {}
    for reg_exp in Regexs.keys():
        res = Regexs[reg_exp].search(frase)
        if res:
            matched[reg_exp] = res.groupdict()
    return matched


def verifica_backup(frase):
    matched = {}
    for reg_exp in Regexs_Backup.keys():
        res = Regexs_Backup[reg_exp].search(frase)
        if res:
            matched[reg_exp] = res.groupdict()
    return matched

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