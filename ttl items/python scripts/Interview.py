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

interview = URIRef(lod + "EngagementInterview")

LadyDiana_uri = URIRef(lod + "LadyDiana")
Charles_uri = URIRef(lod + "Charles")
Buckingham = URIRef(lod + "BuckinghamPalace")
royals = URIRef(lod + "RoyalFamily")

#Diana and Charles
g.add((LadyDiana_uri, OWL.sameAs, URIRef("http://viaf.org/viaf/107032638")))
g.add((Charles_uri, OWL.sameAs, URIRef("http://viaf.org/viaf/84034215")))
g.add((Charles_uri, schema.memberOf, royals))
g.add((royals, OWL.sameAs, dbr.British_royal_family))

EngagementInterview = read_csv("../final_csv/engagement_interview.csv", keep_default_na = None, encoding="utf-8")

for _,row in EngagementInterview.iterrows():

    g.add((interview, dc.title, Literal(row["name"])))
    g.add((interview, dc.language, Literal("en", datatype=XSD.language)))
    g.add((interview, schema.dateCreated, Literal("1981-02-24", datatype=XSD.date)))
    g.add((interview, schema.identifier, Literal(row["identifier"])))
    g.add((interview, RDF.type, dcmitype.MovingImage))
    g.add((dcmitype.MovingImage, RDFS.subClassOf, schema.Image))
    g.add((schema.Image, RDFS.subClassOf, schema.CreativeWork))
    g.add((interview, schema.genre, Literal(row["genre"]) ))
    g.add((interview, schema.uploadDate, Literal("2022-02-24", datatype=XSD.date)))
    g.add((interview, schema.copyrightHolder, Literal("ITN archive")))
    g.add((interview, schema.publisher, Literal(row["author"])))
    g.add((interview, schema.creator, dbr.BBC))
    g.add((interview, schema.provider, dbr.YouTube))
    g.add((interview, schema.locationCreated, Buckingham))
    g.add((Buckingham, OWL.sameAs, URIRef("https://viaf.org/en/viaf/135411769")))
    g.add((interview, crm.P14, LadyDiana_uri))
    g.add((interview, crm.P14, Charles_uri))

g.serialize(format="turtle", destination="EngagementInterview.ttl")