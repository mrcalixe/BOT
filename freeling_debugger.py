#!/usr/bin/python3
# -*- coding: utf-8 -*-

from Wrappers.freeling_wrapper import *


tk, sp, morfo, tagger, sense, wsd, parser = init_freeling("pt")


def print_dep_tree(tree, frase):
    def has_key(d, key):
        try:
            if d[key]:
                return True
            else:
                return True
        except KeyError:
            return False
    with open("dep_tree.dot", "w") as outfile:
        rank = []
        outfile.write("digraph hierarchy {\n")
        i = tree.begin()
        while i != tree.end():
            rank.append(i.get_word().get_lemma())
            if not i.is_root():
                j = i.get_parent()
                aux = "    "
                aux += "\""+j.get_word().get_lemma()+"\""
                aux += " -> "
                aux += "\""+i.get_word().get_lemma()+"\""
                aux += "[label=\""
                aux += i.get_label()+"\"]\n"
                print("A imprimir:", aux)
                outfile.write(aux)
            i.incr()
        '''aux = "{rank = same;"
        for k in rank:
            aux += " \""+k+"\";"
        aux += "}\n"
        outfile.write(aux)'''
        outfile.write("}\n")


def analise(frase):
    a = tk.tokenize(frase)
    b = sp.split(a)
    b = morfo.analyze(b)
    b = tagger.analyze(b)
    b = sense.analyze(b)
    b = wsd.analyze(b)
    b = parser.analyze(b)
    return b

def main():
    print("Initializing FreeLing...")
    global tk, sp, morfo, tagger, sense, wsd, parser
    print("Ready.")
    while True:
        cmd = input("freeling_debugger$ ")
        if cmd == "sair":
            break
        elif cmd == "":
            pass
        elif cmd == "token":
            cmd2 = input("tokenize:")
            print(tk.tokenize(cmd2))
        elif cmd == "split":
            cmd2 = input("split:")
            tmp = tk.tokenize(cmd2)
            print(sp.split(tmp))
        else:
            print(PoS(cmd, tk, sp, morfo, tagger, sense, wsd, parser, debug=True))
