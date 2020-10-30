import rdflib
from rdflib import Namespace
from rdflib import URIRef, BNode, Literal, Graph
from rdflib.namespace import FOAF , XSD, RDFS
from rdflib import Namespace
from rdflib.namespace import  DC, DCTERMS, DOAP, FOAF,   OWL , RDF, RDFS,  SKOS,  VOID, XMLNS, XSD


g = rdflib.Graph()
ns = Namespace("http://example.org/people/")
# Given Issue code :

g.add((URIRef(ns+"Answer"), RDF.type, RDFS.Datatype))
g.add((URIRef(ns+"Answer"), OWL.unionOf, (XSD.string, XSD.boolean,XSD.positiveInteger)))
g.add((URIRef(ns+"answer_value"), RDF.type, RDF.Property))
# Domain of URI ns.answer_value will be the datatypes that are given in the tuple
g.add((URIRef(ns+"answer_value"), RDFS.domain, URIRef(ns+"Question")))
# Setting the range for the URI ns.answer_value as the datatypes that we have taken in the above tuples
g.add((URIRef(ns+"answer_value"), RDFS.range, URIRef(ns+"Answer")))

# We handled the issue and generalised the code
# Trying various tuples of datatypes

g_two = rdflib.Graph()
n = Namespace("http://sweb.org/check/")
g_two.add((URIRef(n+"canStore"), RDF.type, RDFS.Datatype))
g_two.add((URIRef(n+"canStore"), OWL.unionOf, (XSD.negativeInteger,XSD.positiveInteger)))


print(g_two.serialize(format='turtle').decode("utf-8"))





















# for s, p, o in g:
#     print('Triple starts:-')
#     print('subject:-       ',s)
#     print('predicate:-     ',p)
#     print('object:-        ',o)
#     print('Triple Ends..!')
