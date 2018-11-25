
from nltk.metrics.scores import (precision, recall,f_measure)
import collections
from rdflib import Graph, URIRef, RDF, Namespace

def evalues(folder):

    relevant = Graph()
    relevant.parse("./"+folder+"/relevant.owl")

    if folder in ["qald_test","qald_train"]:
        lemon = Namespace("http://www.monnet-project.eu/lemon#")    
    else: 
        lemon = Namespace("http://lemon-model.net/lemon#")

    reference = set()

    for s,p,o in relevant.triples((None, RDF.type, lemon.LexicalEntry)):
        for lexic, pre, form in relevant.triples((s, lemon.canonicalForm, None)):
            # print(relevant.value(form,lemon.writtenRep).lower())
            reference.add(relevant.value(form,lemon.writtenRep).lower())
        # for lexic, pre, form in relevant.triples((s, lemon.otherForm, None)):
        #     reference.add(relevant.value(form,lemon.writtenRep).lower())
        

    retrieved = Graph()
    retrieved.parse("./"+folder+"/retrieved.owl")

    ontolex = Namespace("http://www.w3.org/ns/lemon/ontolex#")

    test = set()
    for s,p,o in retrieved.triples((None, RDF.type, ontolex.MultiWordExpression)):
        # test.add(retrieved.label(s).lower())
        for lexic, pre, form in retrieved.triples((s, ontolex.canonicalForm, None)):
            # print(form)
            test.add(retrieved.value(form,ontolex.writtenRep).lower())

    for s,p,o in retrieved.triples((None, RDF.type, ontolex.Word)):
        for lexic, pre, form in retrieved.triples((s, ontolex.canonicalForm, None)):
            test.add(retrieved.value(form,ontolex.writtenRep).lower())

    print("Reference count: {}".format(len(reference)))
    print("Test count: {}".format(len(test)))

    p = precision(reference, test)
    r = recall(reference, test)
    f = f_measure(reference,test)

    print("Precision: {0:.2f} - Recall: {1:.2f} - F-measure: {2:.2f}".format(p,r,f))