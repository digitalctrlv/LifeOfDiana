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


palace = URIRef(lod +"KensingtonPalace")


#importan uris
LadyDiana_uri = URIRef(lod + "LadyDiana")
NottinghamHouse = URIRef(lod + "NottinghamHouse")
royals = URIRef(lod + "RoyalFamily")
apartments = URIRef(lod + "Apartments")
Charles_uri = URIRef(lod + "Charles")

g.add((LadyDiana_uri, OWL.sameAs, URIRef("http://viaf.org/viaf/107032638")))
g.add((Charles_uri, OWL.sameAs, URIRef("http://viaf.org/viaf/84034215")))
g.add((Charles_uri, schema.memberOf, royals))
g.add((royals, OWL.sameAs, dbr.British_royal_family))

KensingtonPalace = read_csv("../final_csv/kensingtonpalace-meta.csv", keep_default_na=False, encoding="utf-8")

for _, row in KensingtonPalace.iterrows():
    g.add((LadyDiana_uri, schema.homeLocation, apartments))
    g.add((apartments, schema.isPartOf, palace))
    g.add((palace, dc.title, Literal(row["Object"])))
    g.add((palace, RDF.type, URIRef("http://vocab.getty.edu/page/aat/300005743")))
    g.add((palace, dcterms.replaces, NottinghamHouse))
    g.add((crm.E8, crm.P24, NottinghamHouse))
    g.add((crm.E8, crm.P23, dbr.Daniel_Finch))
    g.add((crm.E8, crm.P22, royals))
    g.add((royals, schema.owns, palace))
    g.add((NottinghamHouse, schema.creationDate, Literal("1605", datatype=XSD.gYear)))
    g.add((NottinghamHouse, schema.creator, Literal("Sir George Coppin")))
    g.add((royals, OWL.sameAs, dbr.British_royal_family))

    g.add((palace, schema.creator, dbr.Christopher_Wren))
    g.add((dbr.Christopher_Wren, FOAF.name, Literal("Chrisopher Wren")))
    g.add((palace, schema.genre, URIRef("http://vocab.getty.edu/page/aat/300107014")))
    g.add((palace, schema.material, Literal("Stone")))
    g.add((palace, OWL.sameAs, URIRef("https://viaf.org/en/viaf/172644537")))
    g.add((palace, schema.address, Literal(row["statutoryAdress1"])))
    g.add((palace, schema.sourceOrganization, dbr.Historic_England))
    g.add((palace, schema.publishDate, Literal(row["dateFirstListed"])))
    g.add((palace, schema.identifier, Literal(row["listEntryNumber"])))
    g.add((URIRef("http://vocab.getty.edu/page/aat/300005743"), RDFS.subClassOf, URIRef("http://vocab.getty.edu/page/aat/300264550")))
    g.add((URIRef("http://vocab.getty.edu/page/aat/300264550"), RDFS.subClassOf, schema.CreativeWork))
    g.add((Charles_uri, schema.owns, palace))


g.serialize(format="turtle", destination="KensingtonPalace.ttl")