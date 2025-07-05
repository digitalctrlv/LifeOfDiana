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

photo2 = URIRef(lod + "LadyDianaWithAIDSPatient")
LadyDiana_uri = URIRef(lod + "LadyDiana")


g.add((LadyDiana_uri, OWL.sameAs, URIRef("http://viaf.org/viaf/107032638")))

LadyDCharity = read_csv("../final_csv/AIDs_photo.csv", keep_default_na = None, encoding="utf-8")

for _,row in LadyDCharity.iterrows():
    g.add((photo2, dc.title, Literal(row["Object"])))
    g.add((photo2, RDF.type, schema[row["Type"]]))
    g.add((photo2, schema.creator, Literal(row["Photo Credits"])))
    g.add((photo2, schema.identifier, Literal(row["Name"])))
    g.add((photo2, schema.copyrightHolder, Literal(row["Source"]))) 
    g.add((photo2, schema.dateCreated, Literal(row["Creation date"], datatype=XSD.date)))
    g.add((photo2, schema.uploadDate, Literal(row["Upload date"], datatype=XSD.date)))  
    g.add((photo2, schema.provider, URIRef("http://viaf.org/viaf/151544970")))
    g.add((photo2, dc.subject, Literal("Princess Diana and Aids Patients ")))
    g.add((photo2, schema.locationCreated, dbr.Middlesex_Hospital))
    g.add((photo2, FOAF.depicts, LadyDiana_uri))
    g.add((schema.Photograph, RDFS.subClassOf, dcmitype.StillImage))
    g.add((dcmitype.StillImage, RDFS.subClassOf, schema.Image))
    g.add((schema.Image, RDFS.subClassOf, schema.CreativeWork))


g.serialize(format="turtle", destination="LadyDianaWithAIDSPatient.ttl")