#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys, socket, pickle
import multiprocessing as mp


import FreeLing.APIs.python3.pyfreeling as freeling


def maco_options(lang,lpath, separator) :

    # create options holder
    opt = freeling.maco_options(lang);

    # Provide files for morphological submodules. Note that it is not
    # necessary to set file for modules that will not be used.
    opt.UserMapFile = "";
    opt.LocutionsFile = lpath + "locucions.dat";
    opt.AffixFile = lpath + "afixos.dat";
    opt.ProbabilityFile = lpath + "probabilitats.dat";
    opt.DictionaryFile = lpath + "dicc.src";
    opt.NPdataFile = lpath + "np.dat";
    opt.PunctuationFile = lpath + ".." + separator + "common" + separator + "punct.dat";
    opt.QuantitiesFile = lpath + ".." + separator + "common" + separator + "quantities_default.dat"
    return opt;


def init_freeling(lang):
    separator = '/'
    freeling.util_init_locale("default");
    path_freeling = "/usr/local/share/freeling/"+lang+separator
    tk = freeling.tokenizer(path_freeling+"tokenizer.dat")
    sp = freeling.splitter(path_freeling + "splitter.dat")
    morfo = freeling.maco(maco_options(lang, path_freeling, separator))
    morfo.set_active_options(False, # UserMap
                             True,  # NumbersDetection,
                             True,  # PunctuationDetection,
                             True,  # DatesDetection,
                             True,  # DictionarySearch,
                             True,  # AffixAnalysis,
                             False, # CompoundAnalysis,
                             True,  # RetokContractions,
                             True,  # MultiwordsDetection,
                             True,  # NERecognition,
                             True, # QuantitiesDetection,
                             True); # ProbabilityAssignment
    tagger = freeling.hmm_tagger(path_freeling + "tagger.dat", True, 2)
    sen = freeling.senses(path_freeling+"senses.dat")
    wsd = freeling.ukb(path_freeling+"ukb.dat")
    parser = freeling.dep_treeler(path_freeling+"dep_treeler/dependences.dat")

    #dump_freeling(tk, sp, morfo, tagger, sen, wsd, parser)
    return tk, sp, morfo, tagger, sen, wsd, parser

def ProcessSentences(ls, debug=False):
    estado = '--------------------------------------------------------------------------------------\n'
    processed = []
    # for each sentence in list
    for s in ls :
        # for each word in sentence
        for w in s :
            # print word form
            estado = estado + "| Palavra '"+w.get_form()+"'\n"
            # print possible analysis in word, output lemma and tag
            estado = estado + "|-- Possível análise: {"
            for a in w :
                lem, sens = extract_lemma_and_sense(a)
                estado = estado + " (" + lem + "," + a.get_tag() + "," + sens + ")"
            estado = estado + " }\n"
            #  print analysis selected by the tagger
            lem, sens = extract_lemma_and_sense(w)
            estado = estado + "|-- Análise selecionada: (" + lem + "," + w.get_tag() + "," + sens + ")\n"
            processed.append((w.get_lemma(), w.get_tag()))
        # sentence separator
        #estado = estado + "\n"
    estado += '--------------------------------------------------------------------------------------'
    if debug:
        print(estado)
        return processed
    else:
        return processed


def extract_lemma_and_sense(w) :
   lem = w.get_lemma()
   sens=""
   #if len(w.get_senses())>0 :
       #sens = str(w.get_senses())
   return lem, sens



def PoS(frase, tk, sp, morfo, tagger, sense, wsd, parser, debug=False):
    a = tk.tokenize(frase)
    b = sp.split(a)
    b = morfo.analyze(b)
    b = tagger.analyze(b)
    b = sense.analyze(b)
    b = wsd.analyze(b)
    b = parser.analyze(b)
    return ProcessSentences(b, debug=debug)


def server(args):
    print("A iniciar o servidor...")
    tk, sp, morfo, tagger, sense, wsd, parser = init_freeling("pt")
    if len(args) < 2:
        host = 'localhost'
        port = 1234
    else:
        host = args[1]
        port = int(args[2])
    sock = socket.socket()
    sock.bind((host, port))
    sock.listen(10)

    print("Servidor pronto.")

    while True:
        conn, addr = sock.accept()
        print("Ligado:", str(addr))
        while True:
            data = conn.recv(1024).decode()
            if not data:
                break
            print("Recebi:", str(data))
            pos = PoS(str(data), tk, sp, morfo, tagger, sense, wsd, parser)
            print("Enviei:", pos)
            conn.send(pickle.dumps(pos))
        conn.close()


def main(argv):
    p1 = mp.Process(target=server, args=(argv,))
    p1.start()

    while True:
        cmd = input()
        if cmd == "sair":
            p1.terminate()
            break

if __name__ == '__main__':
    main(sys.argv)