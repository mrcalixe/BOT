# BOT

Repositório com o código e projeto do estágio na Accenture


## Introdução

Utilizando técnicas de Machine Learning, está-se a desenvolver um Bot com capacidade de interpretar
linguagem natural através de uma modelação de Expressões Regulares mais sofisticadas.


## API's utilizadas

+ [**FreeLing**](http://nlp.lsi.upc.edu/freeling/)
+ [**Jspell**](http://natura.di.uminho.pt/wiki/doku.php?id=ferramentas:jspell)
+ [**Wikipedia**](https://wikipedia.readthedocs.io/en/latest/quickstart.html)

## Módulos
|Módulo              |Descrição
| ------------------ | ----------------------------------------------------
|ml.py               | Main principal de execução do Bot. |
|Dicionario          | Contém o dicionário. |
|Names_Parser        | Contém os submódulos necessários para o parsing para CSV dos nomes próprios. | 
|freeling_wrapper.py | Inicializa a API do FreeLing com as opções de análise morfológica e inicialização dos tokenizer, splitter, analisador morfológico e tagger.
|ml.py               | Módulo principal responsável por toda a parte de Machine Learning. |
|reg_exps.py         | Módulo responsável pela modelação e processamento das expressões regulares. |
|aux_functions.py    | Módulo responsável pela inicialização e carregamento das base de dados e estado do Bot. |
|web_search.py       | Módulo responsável pela procura de informação na Web. |


## Pastas
+ Apontamentos - serve para criar notas e ficheiros com apontamentos e diários de trabalhos.
+ Esquema de reuniões - serve para armazenar os apontamentos tirados nas reuniões
+ Knowledge_DB - armazena o ficheiro da base de dados do conhecimento
+ Ideias - contém alguns módulos com ideias de coisas que possam vir a ser úteis

## Tags do FreeLing
|Tag |Valor
|----|----------------------------
|AO  | Adjectivo Ordinal
|AQ  | Adjectivo Qualificativo
|CS  | Conjunção Subordinativa
|CC  | Conjunção Coordenativa
|DA  | Determinante Artigo
|DD  | Determinante Demonstrativo
|DI  | Determinante Indefinido
|DP  | Determinante Possessivo
|I   | Interjeição
|NC  | Nome Comum
|NP  | Nome Próprio
|PD  | Pronome Demonstrativo
|PE  | Pronome Exclamativo
|PI  | Pronome Indefinido
|PP  | Pronome Pessoal
|PR  | Pronome Relativo
|PT  | Pronome Interrogativo
|PX  | Pronome Possessivo
|RG  | Advérbio Geral
|RN  | Advérbio Negativo
|SP  | Preposição
|VG  | Verbo: Gerúndio
|VI  | Verbo: Modo Indicativo
|VM  | Verbo: Modo Imperativo
|VN  | Verbo: Infinitivo
|VP  | Verbo: Particípio
|VS  | Verbo: Modo Conjuntivo
|Z  | Numeral