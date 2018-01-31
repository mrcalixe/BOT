# BOT

Repositório com o código e projeto do estágio na Accenture


## Introdução

Utilizando técnicas de Machine Learning, está-se a desenvolver um Bot com capacidade de interpretar
linguagem natural através de uma modelação de Expressões Regulares mais sofisticadas.


## API's utilizadas

+ [**FreeLing**](http://nlp.lsi.upc.edu/freeling/)
+ [**Jspell**](http://natura.di.uminho.pt/wiki/doku.php?id=ferramentas:jspell)

## Módulos
|Módulo|Descrição
|------|--------
|ml.py | Main principal de execução do Bot. |
|Dicionario | Contém o dicionário. |
|Names_Parser | Contém os submódulos necessários para o parsing para CSV dos nomes próprios. | 
|freeling_wrapper.py | Inicializa a API do FreeLing com as opções de análise morfológica e inicialização dos tokenizer, splitter, analisador morfológico e tagger.
|ml.py | Módulo principal responsável por toda a parte de Machine Learning. |
|reg_exps.py | Módulo responsável pela modelação e processamento das expressões regulares. |
|aux_functions.py | Módulo responsável pela inicialização e carregamento das base de dados e estado do Bot. |


## Pastas
+ Apontamentos - serve para criar notas e ficheiros com apontamentos e diários de trabalhos.
+ Esquema de reuniões - serve para armazenar os apontamentos tirados nas reuniões
+ Knowledge_DB - armazena o ficheiro da base de dados do conhecimento