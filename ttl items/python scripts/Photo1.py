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

photo1 = URIRef(lod + "LadyDianaOnHolidayInPortofino")
LadyDiana_uri = URIRef(lod + "LadyDiana")

g.add((LadyDiana_uri, OWL.sameAs, URIRef("http://viaf.org/viaf/107032638")))

LadyDonYacht = read_csv("../final_csv/Lady Diana on holiday in Portofino.csv", keep_default_na = False, encoding = "utf-8")

for _, row in LadyDonYacht.iterrows():
  
    g.add((photo1, schema.creator, Literal(row["Credits"])))
    g.add((photo1, schema.identifier, Literal(row["Name of the item"])))
    g.add((photo1, schema.copyrightHolder, Literal(row["Source"])))
    g.add((photo1, schema.dateCreated, Literal(row["Creation date"], datatype=XSD.date)))
    g.add((photo1, schema.uploadDate, Literal(row["Upload date"], datatype=XSD.date)))  
    g.add((schema.Photograph, RDFS.subClassOf, dcmitype.StillImage))
    g.add((dcmitype.StillImage, RDFS.subClassOf, schema.Image))
    g.add((schema.Image, RDFS.subClassOf, schema.CreativeWork))
    g.add((photo1, RDF.type, schema.Photograph))
    g.add((photo1, dc.title, Literal(row["Item"])))
    g.add((photo1, schema.provider, URIRef("http://viaf.org/viaf/151544970")))
    g.add((photo1, dc.subject, Literal("Lady Diana, Princess of Wales, sitting on the diving board of Mohammed Al Fayed's private yacht 'Jonikal' as a seagull flies overhead")))
    g.add((photo1, schema.locationCreated, URIRef("https://www.wikidata.org/wiki/Q232782")))
    g.add((photo1, FOAF.depicts, LadyDiana_uri))
    
g.serialize(format="turtle", destination="LadyDianaOnHolidayInPortofino.ttl")