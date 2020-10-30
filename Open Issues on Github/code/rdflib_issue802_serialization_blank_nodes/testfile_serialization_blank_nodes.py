
from __future__ import print_function, unicode_literals
from rdflib import BNode, Graph, Literal, Namespace, RDF
from rdflib.compare import to_isomorphic, graph_diff, isomorphic

EX = Namespace('http://ex/')

def myComparison(g1,g2):
    print('len(graph_1):', len(g1))
    print('len(graph_2):', len(g2))
    iso1 = to_isomorphic(g1)
    iso2 = to_isomorphic(g2)

    print('Does two graphs isomorphic to eachother?',iso1 == iso2)


    in_both, in_first, in_second = graph_diff(iso1, iso2)
    print()
    print('Differences or same in the graphs(in_both):-')
    dump_nt_sorted(in_both)
    print(len(g2))
    print(len(g2))



def dump_nt_sorted(g):
    for l in sorted(g.serialize(format='nt').splitlines()):
        if l: print(l.decode('ascii'))


def test_list_with_bnodes():

    turtle_1 = '''
        @prefix ex: <http://www.ex.org/> .

        ex:a ex:x _:p1 , _:p2 .
        _:p1 ex:y ( _:i1 _:i2 _:i3 _:i4 ) .
        _:p2 ex:z _:p1. 
        '''
    graph_1 = Graph().parse(data=turtle_1, format='turtle')
    turtle_2 = graph_1.serialize(format='n3')
    graph_2 = Graph().parse(data=turtle_2, format='n3')
    # turtle_3 = graph_2.serialize(format='turtle')
    # graph_3 = Graph().parse(data=turtle_3, format='turtle')
    print('length of graph_1 is: ',len(graph_1))
    print('length of graph_2 is: ',len(graph_2))
    #print('length of graph_3 is: ', len(graph_3))
    #print('graph_1 and graph_2 are isomorphic? ',isomorphic(graph_1,graph_2))
    turtle_3 = graph_2.serialize(format='n3')
    graph_3 = Graph().parse(data=turtle_3, format='n3')

    turtle_4 = graph_1.serialize(format='xml')
    graph_4 = Graph().parse(data=turtle_4, format='xml')
    print('comparing graph1(given graph) and grraph2(serialized turtle one):-')
    myComparison(graph_1,graph_2)
    print()
    print()
    print()
    print('comparing graph2(turtle-14) and grraph3(n3-14):-')
    myComparison(graph_2,graph_3)
    print()
    print()
    print()
    print('comparing graph1(turtle) and grraph4(xml):-')
    myComparison(graph_1,graph_4)
    print()
    print()
    print()
    print('comparing graph1(turtle) and grraph3(n3-14):-')
    myComparison(graph_1, graph_3)

test_list_with_bnodes()


