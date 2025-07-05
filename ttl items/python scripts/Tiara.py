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
dress = URIRef(lod + "WeddingDress")
tiara = URIRef(lod + "Tiara")
wedding = URIRef(lod + "RoyalWedding")
Spencers = URIRef(lod + "SpencerFamily")
royals = URIRef(lod + "RoyalFamily")

g.add((LadyDiana_uri, OWL.sameAs, URIRef("http://viaf.org/viaf/107032638")))
g.add((Charles_uri, OWL.sameAs, URIRef("http://viaf.org/viaf/84034215")))
g.add((Charles_uri, schema.memberOf, royals))
g.add((royals, OWL.sameAs, dbr.British_royal_family))

SpencerTiara = read_csv("../final_csv/Spencer Tiara.csv", keep_default_na = None, encoding="utf-8")

for _, row in SpencerTiara.iterrows():
    g.add((tiara, dc.title, Literal(row["object"])))
    g.add((tiara, RDF.type, URIRef("http://vocab.getty.edu/aat/300046046")))
    g.add((tiara, schema.creator, Literal(row["creator"])))
    g.add((tiara, dc.relation, dress))
    g.add((tiara, schema.dateCreated, Literal(row["date"],datatype=XSD.gYear)))
    g.add((tiara, schema.material, Literal(row["material"])))
    g.add((tiara, schema.location, Literal(row["location"])))
    g.add((tiara, schema.copyrightHolder, Spencers))
    g.add((Spencers, OWL.sameAs, dbr.Spencer_family))
    g.add((URIRef("http://vocab.getty.edu/aat/300046046"), RDFS.subClassOf, URIRef("http://vocab.getty.edu/page/aat/300209261")))
    g.add((URIRef("http://vocab.getty.edu/page/aat/300209261"), RDFS.subClassOf, schema.CreativeWork))

    g.add((wedding, crm.P16, tiara))
    g.add((wedding, RDF.type, schema.Event))
    g.add((wedding, schema.location, URIRef("http://vocab.getty.edu/tgn/7011781")))
    g.add((wedding, dc.date, Literal("1981-07-29", datatype=XSD.date)))
    g.add((wedding, crm.P14, LadyDiana_uri))
    g.add((wedding, crm.P14, Charles_uri))
    

g.serialize(format="turtle", destination="Tiara.ttl")
