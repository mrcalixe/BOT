#!/usr/bin/python3
# -*- coding: utf-8 -*-

from SPARQLWrapper import SPARQLWrapper, JSON

sparql = SPARQLWrapper("http://dbpedia.org/sparql")
sparql.setQuery("""
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    SELECT ?label
    WHERE {SELECT * WHERE {
  ?x rdfs:label "New York City"@en.
  ?x dbpedia-owl:populationTotal ?pop.
  ?x dbpedia-owl:abstract ?abstract.
}}
""")
sparql.setReturnFormat(JSON)
results = sparql.query().convert()

for result in results["results"]["bindings"]:
    if result["label"]['xml:lang'] == 'pt':
        print(result["label"]["value"])