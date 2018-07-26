import rdflib as rdf
from SPARQLWrapper import SPARQLWrapper, JSON

g = rdf.Graph()



def test():
    sparql = SPARQLWrapper("http://dbpedia.org/sparql")
    sparql.setReturnFormat(JSON)

    query = """
        SELECT DISTINCT ?river ?pais
        WHERE {
            ?river a <http://dbpedia.org/ontology/River> .
            ?river ?related <http://dbpedia.org/resource/Esposende> .
            ?river a:sourceCountry ?pais .
        }
    """

    sparql.setQuery(query)  # the previous query as a literal string

    return sparql.query().convert()



def test2_com_lingua(lang):
    sparql = SPARQLWrapper("http://dbpedia.org/sparql")
    sparql.setReturnFormat(JSON)

    query = """
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX foaf: <http://xmlns.com/foaf/0.1/>
        SELECT ?film ?description ?film_name WHERE {
            ?film rdf:type <http://dbpedia.org/ontology/Film>.
            ?film foaf:name ?film_name.
            ?film rdfs:comment ?description .
            FILTER (LANG(?description)='pt' && ?film_name="Transformers"@en)
        }
    """
    sparql.setQuery(query)  # the previous query as a literal string

    return sparql.query().convert()


t = test()
#print(t)
#print('----------------------------------------------------------------------------------------------------')
t2 = test2_com_lingua('pt')
#print(t2)