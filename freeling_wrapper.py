#!/usr/bin/python3
# -*- coding: utf-8 -*-

from functools import reduce
import APIs.FreeLing4.APIs.python3.pyfreeling as freeling
import pickle


def maco_options(lang,lpath) :

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
    opt.PunctuationFile = lpath + "../common/punct.dat";
    opt.QuantitiesFile = lpath + "../common/quantities_default.dat"
    return opt;


def init_freeling(lang):
    freeling.util_init_locale("default");
    path_freeling = "/usr/local/share/freeling/"+lang+"/"
    try:
        (tk, sp, morfo, tagger, sen, wsd, tagger) = readback_freeling()
    except AttributeError and FileNotFoundError:
        tk = freeling.tokenizer(path_freeling+"tokenizer.dat")
        sp = freeling.splitter(path_freeling + "splitter.dat")
        morfo = freeling.maco(maco_options(lang, path_freeling))
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


def dump_freeling(tk, sp, morfo, tagger, sen, wsd, parser):
    with open('tokenizer.dump', 'wb') as tk_output:
        pickle.dump(tk, tk_output, pickle.HIGHEST_PROTOCOL)

    with open('sp.dump', 'wb') as sp_output:
        pickle.dump(sp, sp_output, pickle.HIGHEST_PROTOCOL)

    with open('morfo.dump', 'wb') as morfo_output:
        pickle.dump(morfo, morfo_output, pickle.HIGHEST_PROTOCOL)

    with open('tagger.dump', 'wb') as tagger_output:
        pickle.dump(tagger, tagger_output, pickle.HIGHEST_PROTOCOL)

    with open('sen.dump', 'wb') as sen_output:
        pickle.dump(sen, sen_output, pickle.HIGHEST_PROTOCOL)

    with open('wsd.dump', 'wb') as wsd_output:
        pickle.dump(wsd, wsd_output, pickle.HIGHEST_PROTOCOL)

    with open('parser.dump', 'wb') as parser_output:
        pickle.dump(parser, parser_output, pickle.HIGHEST_PROTOCOL)


def readback_freeling():
    with open('tokenizer.dump', 'rb') as tk_input:
        tk = pickle.load(tk_input)

    with open('sp.dump', 'rb') as sp_input:
        sp = pickle.load(sp_input)

    with open('morfo.dump', 'rb') as morfo_input:
        morfo = pickle.load(morfo_input)

    with open('tagger.dump', 'rb') as tagger_input:
        tagger = pickle.load(tagger_input)

    with open('sen.dump', 'rb') as sen_input:
        sen = pickle.load(sen_input)

    with open('wsd.dump', 'rb') as wsd_input:
        wsd = pickle.load(wsd_input)

    with open('parser.dump', 'rb') as parser_input:
        parser = pickle.load(parser_input)

    return tk, sp, morfo, tagger, sen, wsd, parser