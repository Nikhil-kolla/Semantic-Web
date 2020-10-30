"""
This file is for testing purpose to observe whether my issue is resolved or not


"""

"Importing the updated module and other required modules."
import rdflib.plugins.sparql.queryDetails as comp
import rdflib.plugins.sparql as sparql

" Taking some query examples."




q1 = "SELECT ?x WHERE { ?x <http://xmlns.com/foaf/0.1/haha> ?k ." \
     " ?person <http://xmlns.com/foaf/0.1/knows> ?x .}"
q2 = "SELECT ?s WHERE { ?person <http://xmlns.com/foaf/0.1/knows> ?s ." \
     "?s <http://xmlns.com/foaf/0.1/haha> ?k .}"
q3= """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>


SELECT ?node ?nodeLabel ?superclass ?superclassLabel (group_concat(DISTINCT ?node2) as ?node2s) (group_concat(DISTINCT ?node2Label) as ?node2Labels)
where {



   OPTIONAL { ?node rdfs:subClassOf ?restriction.
              ?restriction a owl:Restriction ;
                owl:someValuesFrom ?node2 .
               ?node2 rdfs:label ?node2Label .

   }
    ?node rdf:type owl:Class ;
   rdfs:subClassOf ?superclass;
  rdfs:label ?nodeLabel . 
      
      
   ?superclass rdfs:label ?superclassLabel .

}
group by ?node ?nodeLabel ?superclass ?superclassLabel ?node2 ?node2Label
LIMIT 10

"""
q4= """
PREFIX  dc:  <http://purl.org/dc/elements/1.1/>
SELECT  ?title
WHERE   { ?x dc:title ?title
          FILTER regex(?title, "^SPARQL") 
        }
"""
q5="""

PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>


SELECT ?node ?nodeLabel ?superclass ?superclassLabel 
where {

 OPTIONAL { ?node rdfs:subClassOf ?restriction.
              ?restriction a owl:Restriction ;
                owl:someValuesFrom ?node2 .
               ?node2 rdfs:label ?node2Label .

   }

    ?node rdf:type owl:Class ;
   rdfs:subClassOf ?superclass;
  rdfs:label ?nodeLabel . 
      
      
   ?superclass rdfs:label ?superclassLabel .

}

LIMIT 10

"""

" Prepare all the queries for sparql engin"

preparedQ1 = sparql.prepareQuery(q1)
preparedQ2 = sparql.prepareQuery(q2)
preparedQ3 = sparql.prepareQuery(q3)
preparedQ4 = sparql.prepareQuery(q4)
preparedQ5 = sparql.prepareQuery(q5)

" Sample for printing the Query."
sparql.queryDetails.printFormalizedQuery((preparedQ1))

" Finding equivalence score of the sample queries"
print(comp.queryEquivalenceScore(preparedQ1,preparedQ2)) # This is for given queries in the issue
print(comp.queryEquivalenceScore(preparedQ4,preparedQ5))
print(comp.queryEquivalenceScore(preparedQ1,preparedQ4))
print(comp.queryEquivalenceScore(preparedQ3,preparedQ5))
