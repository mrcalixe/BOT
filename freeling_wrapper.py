# -*- coding: utf-8 -*-

from functools import reduce
import APIs.FreeLing4.APIs.python.freeling as freeling


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
    return opt;


def init_freeling(lang):
    freeling.util_init_locale("default");
    path_freeling = "/usr/local/share/freeling/"+lang+"/"
    tk = freeling.tokenizer(path_freeling+"tokenizer.dat")
    sp = freeling.splitter(path_freeling + "splitter.dat")
    morfo = freeling.maco(maco_options(lang, path_freeling))
    morfo.set_active_options(False, # UserMap
                             True,  # NumbersDetection,
                             True,  # PunctuationDetection,
                             True,  # DatesDetection,
                             True,  # DictionarySearch,
                             True,  # AffixAnalysis,
                             True, # CompoundAnalysis,
                             True,  # RetokContractions,
                             True,  # MultiwordsDetection,
                             True,  # NERecognition,
                             True, # QuantitiesDetection,
                             True); # ProbabilityAssignment
    tagger = freeling.hmm_tagger(path_freeling + "tagger.dat", True, 2)

    return tk, sp, morfo, tagger

def ProcessSentences(ls):

    # for each sentence in list
    for s in ls :
        # for each word in sentence
        for w in s :
            # print word form
            print("word '"+w.get_form()+"'")
            # print possible analysis in word, output lemma and tag
            print("  Possible analysis: {",end="")
            for a in w :
                print(" ("+a.get_lemma()+","+a.get_tag()+")",end="")
            print(" }")
            #  print analysis selected by the tagger
            print("  Selected Analysis: ("+w.get_lemma()+","+w.get_tag()+")")
        # sentence separator
        print("")