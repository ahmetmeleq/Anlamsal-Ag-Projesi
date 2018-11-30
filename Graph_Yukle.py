import rdflib


cizge = rdflib.Graph()
cizge.load('http://dbpedia.org/resource/Mathematics')


for nesne, yuklem, ozne in cizge:
    print(nesne)
