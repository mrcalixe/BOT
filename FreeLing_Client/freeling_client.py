#!/usr/bin/python3
# -*- coding: utf-8 -*-

import socket, pickle, json
import subprocess as sp
from graphviz import Digraph


class Client:
    def __init__(self, host='localhost', port=1234):
        '''self.sock = socket.socket()
        self.sock.connect((host, port))'''
        print("Ligado ao servidor.")

    def Tokenize(self, frase):
        self.sock.send(pickle.dumps({'token': frase}))
        recv = self.sock.recv(1024)
        loaded = pickle.loads(recv)
        print("Tokenize:", loaded)
        return loaded

    def PoS(self, frase):
        '''self.sock.send(pickle.dumps({'pos': frase}))
        recv = self.sock.recv(1024)
        loaded = pickle.loads(recv)
        print("PoS:", loaded)
        return loaded'''
        res = analyse(frase)
        dot, pos = extract(res['sentences'][0])
        return pos

    def Split(self, frase):
        self.sock.send(pickle.dumps({'split': frase}))
        recv = self.sock.recv(1024)
        loaded = pickle.loads(recv)
        print("Split:", loaded)
        return loaded

    def close(self):
        #self.sock.close()
        pass


def analyse(frase):
    frase_in = frase.encode('utf-8')
    res = sp.run(["/usr/local/bin/analyzer_client", "localhost:5000"], stdout=sp.PIPE, input=frase_in)
    return json.loads(res.stdout.decode('utf-8'))


def generate_Nodes_Edges(Tree, Nodos, Arestas):
    #Tree é sempre uma lista com nodos
    for nodo in Tree:
        Nodos += [nodo['word']]
        if 'token' in nodo:
            del(nodo['token'])
        if 'children' in nodo.keys():
            for filho in nodo['children']:
                if 'token' in filho:
                    del (filho['token'])
                Arestas += [(nodo['word'], filho['word'],filho['function'])]
                Tree, Nodos, Arestas = generate_Nodes_Edges([filho], Nodos, Arestas)
    return Tree, Nodos, Arestas


'''
Dicionário com a Árvore de Dependências e nodos com as respetivas funções
 
'''


def extract(analysis, view=True):
    # Árvore de dependências
    analise = analysis['dependencies']

    dep_tree = {}

    dot = Digraph()
    tree, nodes, edges = generate_Nodes_Edges(analise, [], [])

    dep_tree['nodos'] = nodes
    dep_tree['tree'] = tree


    for n in nodes: dot.node(n)
    for (a, b, c) in edges:
        dot.edge(a, b, label=c)
    dot.render('dot_out.gv', view=view)

    # PoS
    tokens = analysis['tokens']
    pos = []
    for i in range(len(tokens)):
        tk = tokens[i]
        pos += [(tk['lemma'], tk['tag'], tk['form'])]

    return dep_tree, pos
