#!/usr/bin/python3
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
    opt.QuantitiesFile = lpath + "../common/quantities_default.dat"
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

    return tk, sp, morfo, tagger, sen, wsd, parser

def ProcessSentences(ls, debug=False):
    estado = ""
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
                estado = estado + " (" + a.get_lemma() + "," + a.get_tag() + ")"
            estado = estado + " }\n"
            #  print analysis selected by the tagger
            estado = estado + "|-- Análise selecionada: (" + w.get_lemma() + "," + w.get_tag()  + ")\n"
            processed.append((w.get_lemma(), w.get_tag()))
        # sentence separator
        estado = estado + "\n"
    if debug:
        print(estado)
        return processed
    else:
        return processed


def extract_lemma_and_sense(w) :
   lem = w.get_lemma()
   sens=""
   if len(w.get_senses())>0 :
       sens = w.get_senses()[0][0]
   return lem, sens


## -----------------------------------------------
## Do whatever is needed with analyzed sentences
## -----------------------------------------------
def ProcessSentences2(ls):
    # for each sentence in list
    for s in ls :
        # for each predicate in sentence
        for pred in s.get_predicates() :
            lsubj=""; ssubj=""; ldobj=""; sdobj=""
            # for each argument of the predicate
            for arg in pred :
                # if the argument is A1, store lemma and synset in ldobj, sdobj
                if arg.get_role()=="A1" :
                    (ldobj,sdobj) = extract_lemma_and_sense(s[arg.get_position()])
                # if the argument is A0, store lemma and synset in lsubj, subj
                elif arg.get_role()=="A0" :
                    (lsubj,ssubj) = extract_lemma_and_sense(s[arg.get_position()])
            # Get tree node corresponding to the word marked as argument head
            head = s.get_dep_tree().get_node_by_pos(arg.get_position())
            # check if the node has dependency is "by" in passive structure
            if lsubj=="by" and head.get_label=="LGS" :
                # get first (and only) child, and use it as actual subject
                head = head.get_nth_child(0)
                (lsubj,ssubj) = extract_lemma_and_sense(head.get_word())

            #if the predicate had both A0 and A1, we found a complete SVO triple. Let's output it.
            if lsubj!="" and ldobj!="":
                (lpred,spred) = extract_lemma_and_sense(s[pred.get_position()])
                print ("SVO : (pred:   " , lpred, "[" + spred + "]")
                print ("       subject:" , lsubj, "[" + ssubj + "]")
                print ("       dobject:" , ldobj, "[" + sdobj + "]")
                print ("      )")
