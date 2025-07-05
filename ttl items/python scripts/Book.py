from pandas import read_csv
from rdflib import Namespace, RDF, OWL, Literal, XSD, RDFS, URIRef, Graph, FOAF


lod = Namespace("https://github.com/digitalctrlv/LifeOfDiana/")
schema = Namespace("https://schema.org/")
dc = Namespace("http://purl.org/dc/elements/1.1/")
dcterms = Namespace("http://purl.org/dc/terms/")
crm = Namespace("http://www.cidoc-crm.org/cidoc-crm/")
wd = Namespace("https://www.wikidata.org/wiki/")
dcmitype = Namespace("http://purl.org/dc/dcmitype/")
dbo = Namespace("http://dbpedia.org/ontology/")
dbr = Namespace("http://dbpedia.org/resource/")

g = Graph()

g.bind("schema", schema)
g.bind("dc", dc)
g.bind("dcterms", dcterms)
g.bind("crm", crm)
g.bind("wd", wd)
g.bind("lod", lod)
g.bind("dcmitype", dcmitype)
g.bind("dbo", dbo)
g.bind("dbr", dbr)

LadyDiana_uri = URIRef(lod + "LadyDiana")
Charles_uri = URIRef(lod + "Charles")
divorce = URIRef(lod + "Divorce")
royals = URIRef(lod + "RoyalFamily")
apartments = URIRef(lod + "Apartments")
book = URIRef(lod + "DianaHerTrueStory")
palace = URIRef(lod +"KensingtonPalace")

g.add((LadyDiana_uri, OWL.sameAs, URIRef("http://viaf.org/viaf/107032638")))
g.add((Charles_uri, OWL.sameAs, URIRef("http://viaf.org/viaf/84034215")))
g.add((Charles_uri, schema.memberOf, royals))
g.add((royals, OWL.sameAs, dbr.British_royal_family))

DianaHerTrueStory = read_csv("../final_csv/Book.csv")

for _, row in DianaHerTrueStory.iterrows():

    languages = {"English" : "en"}
    lang_data1 = languages.get(row["Language"], "und")

    Andrew_uri = URIRef(lod + "AndrewMorton")
    Archi_uri = URIRef(lod + "Archiginnasio")
    
    g.add((book, dc.title, Literal(row["Object"])))
    g.add((book, RDF.type, schema[row["Type"]]))
    g.add((schema.Book, RDFS.subClassOf, schema.Text))
    g.add((schema.Text, RDFS.subClassOf, schema.CreativeWork))

    #Andrew triples
    g.add((book, schema.creator, Andrew_uri))
    g.add((Andrew_uri, OWL.sameAs, URIRef("http://viaf.org/viaf/22238479")))
    g.add((Andrew_uri, FOAF.name, Literal(row["Creator"])))
    g.add((book, schema.datePublished, Literal(row["Date"], datatype=XSD.gYear)))
    g.add((book, dc.language, Literal(lang_data1, datatype=XSD.language)))
    g.add((book, schema.genre, Literal(row["Genre"])))
    g.add((book, schema.publisher, Literal(row["Publisher"])))
    g.add((book, schema.identifier, Literal(row["ISBN"])))
    g.add((book, dc.subject, LadyDiana_uri))
    g.add((book, dc.subject, royals))
    g.add((book, dc.subject, divorce))
    g.add((book, dc.subject, Charles_uri))
    g.add((book, schema.mentions, palace))
    g.add((book, schema.mentions, apartments))

    #Archiginnasio triples
    g.add((book, schema.sourceOrganization, Archi_uri))
    g.add((Archi_uri, OWL.sameAs, dbr.Archiginnasio_of_Bologna))
    g.add((Archi_uri, schema.location, URIRef("http://viaf.org/viaf/5185150647115410860003")))

g.serialize(format="turtle", destination="DianaHerTrueStory.ttl")