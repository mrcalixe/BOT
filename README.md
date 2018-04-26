# BOT

Repositório com o código e projeto do estágio na Accenture

Versão 0.1-alpha


## Introdução

Utilizando técnicas de Machine Learning, está-se a desenvolver um Bot com capacidade de interpretar
linguagem natural através de uma modelação de Expressões Regulares mais sofisticadas.


## API's utilizadas

+ [**FreeLing**](http://nlp.lsi.upc.edu/freeling/)
+ [**Jspell**](http://natura.di.uminho.pt/wiki/doku.php?id=ferramentas:jspell)
+ [**Wikipedia**](https://wikipedia.readthedocs.io/en/latest/quickstart.html)
+ [**Google Maps API**](https://github.com/googlemaps/google-maps-services-python)

## Instalação no WSL, FreeLing, NLTK, PyCharm.
Para instalar em Linux, basta saltar os passos 1,2,4.
1. Instalação do WSL (Windows Subsystem Linux): Abrir uma PowerShell em modo de administrador e executar:
    ```visual basic
    Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux
    ``` 
Nota: para abrir um PowerShell em modo administrador, basta carregar no menu iniciar, escrever powershell, clical no lado direito do rato encima da powershell e selecionar executar como administrador.

2. Depois do computador reiniciar, abrir novamente uma PowerShell em modo de administrador e executar:
    ```visual basic
    bash
    ```
    E instalar a aplicação Ubuntu da loja Microsoft.
3. Abrir a aplicação Ubuntu e executar o seguinte comando:
    ```bash
    sudo apt update ; sudo apt upgrade ; sudo apt install git python-dev python3-dev python3-pip python-pip gcc g++ build-essential swig python3-enchant
    sudo pip3 install -U numpy nltk wikipedia
    ```
4. Seguir através deste [**tutorial**](https://gist.github.com/dentechy/de2be62b55cfd234681921d5a8b6be11) como ativar e configurar o SSH no Ubuntu
5. Instalação do BOT, FreeLing e API para python.
    ```bash
    git clone https://github.com/mrcalixe/BOT.git
    cd BOT
    git submodule init
    git submodule update
    git config submodule.FreeLing.active false
    cd Freeling
    sudo apt-get install build-essential automake autoconf libtool
    autoreconf --install
    ./configure
    make
    sudo make install
    cd APIs/python3
    make
    ```
6. Abrir o PyCharm, abrir o projeto, e configurar o interpretador remoto através de SSH.


## Módulos

### FreeLing

Contém ainda o repositório da API do FreeLing como submódulo Git.

|FreeLing                |Descrição
| ---------------------  | ----------------------------------------------------
|freeling_server.py      | Servidor FreeLing python. |
|freeling_client.py      | Cliente para o servidor python FreeLing. |
|freeling_wrapper.py     | Inicializa a API do FreeLing com as opções de análise morfológica e inicialização dos tokenizer, splitter, analisador morfológico e tagger.

### Expressões Regulares

|Expressões Regulares    |Descriçãao
| ---------------------  | ----------------------------------------------------
|reg_exps.py             | Módulo responsável pela modelação e processamento das expressões regulares. |
|regex_debugger.py       | Módulo para facilitar o debugging do módulo das expressões regulares com um cliente para o FreeLing. |

### Base de Dados

|Base de Dados           |Descrição
| ---------------------  | ----------------------------------------------------
|DB.py                   | Base de dados com o conhecimento do BOT (keywords e significado das mesmas; frases com as ações realizadas). |

### Wrappers

|Wrappers de API's       |Descrição
| ---------------------  | ----------------------------------------------------
|google_maps_wrapper.py  | Módulo que faz o wrap da API do Google Maps Places. |
|wikipedia_wrapper.py    | Módulo responsável pela procura de informação na Wikipedia. |

### Ideias e módulos que já não são desnecessários

|Módulos desnecessários  |Descrição
| ---------------------  | ----------------------------------------------------
|Names_Parser            | Contém os submódulos necessários para o parsing para CSV dos nomes próprios. |
|Knowledge_DB            | Base de dados em SQLite para armazenar o conhecimento. |
|Ideias                  | Contém módulos que com algumas ideias e com o classificador de género utilizado para aprender  trabalhar com a NLTK. |

### Ficheiros Latex

Mais tarde vão ser adicionados mais ficheiros como por exemplo o ficheiro da dissertação

|Latex                   |Descrição
| ---------------------  | ----------------------------------------------------
|Modelo_Linguistico.tex  | Modelo linguístico do BOT

### Machine Learning

|Machine Learning        |Descrição
| ---------------------  | ----------------------------------------------------
|ml.py                   | Módulo principal responsável por toda a parte de Machine Learning. |

### Módulos de funcionamento

|Módulo de funcionamento | Descrição
| ---------------------  | ----------------------------------------------------
|main.py                 | Main principal de execução do Bot. |
|aux_functions.py        | Módulo responsável pela inicialização e carregamento das base de dados e estado do Bot. |


## Pastas
+ Apontamentos - serve para criar notas e ficheiros com apontamentos e diários de trabalhos.
+ Esquema de reuniões - serve para armazenar os apontamentos tirados nas reuniões
+ Knowledge_DB - armazena o ficheiro da base de dados do conhecimento
+ Ideias - contém alguns módulos com ideias de coisas que possam vir a ser úteis


## Utilizarção

Correr no terminal em primeiro um servidor FreeLing:
(Quando não se passam parámetros a este módulo, é assumido o ip localhost e a porta 1234)
```bash
    ./freeling_server.py localhost 1234
```

A sintaxe deste módulo é:
+ Endereço ao qual o servidor vai usar
+ Porta a ser usada pelo servidor


Para correr o programa:
(Quando não se passam parámetros a este módulo, é assumido o ip localhost e a porta 1234)
```bash
    ./main localhost 1234
```

A sintaxe deste módulo é:
+ Endereço ao qual o cliente se vai ligar
+ Porta da ligação


## Notas

Mais tarde, implementarei o servidor Freeling num servidor meu 
para que esteja sempre ligado e qualquer pessoa o possa utilizar



## Tags (resumidas) do FreeLing
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
|Z   | Numeral
