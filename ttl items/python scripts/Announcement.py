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

announcement = URIRef(lod + "DivorceAnnouncement")

#importan uris
LadyDiana_uri = URIRef(lod + "LadyDiana")
Charles_uri = URIRef(lod + "Charles")
royals = URIRef(lod + "RoyalFamily")
divorce = URIRef(lod + "Divorce")

#Diana and Charles
g.add((LadyDiana_uri, OWL.sameAs, URIRef("http://viaf.org/viaf/107032638")))
g.add((Charles_uri, OWL.sameAs, URIRef("http://viaf.org/viaf/84034215")))
g.add((Charles_uri, schema.memberOf, royals))
g.add((royals, OWL.sameAs, dbr.British_royal_family))

DivorceAnnouncement = read_csv("../final_csv/ny-divorce-meta.csv", keep_default_na = False, encoding="utf-8")

for _,row in DivorceAnnouncement.iterrows():
    g.add((announcement, dc.title, Literal(row["headline"])))
    g.add((announcement, RDF.type, schema.NewsArticle))
    g.add((schema.NewsArticle, RDFS.subClassOf, schema.Text))
    g.add((schema.Text, RDFS.subClassOf, schema.CreativeWork))
    g.add((announcement, dc.language, Literal("en", datatype=XSD.language)))
    g.add((announcement, schema.publisher, dbr.The_New_York_Times))
    g.add((dbr.The_New_York_Times, FOAF.name, Literal(row["publisher"])))
    g.add((announcement, schema.publishDate, Literal("1996-08-29", datatype=XSD.date)))
    g.add((announcement, schema.copyrightHolder, dbr.The_New_York_Times))
    g.add((announcement, schema.isPartOf, Literal(row["isPartOf"])))
    g.add((announcement, schema.articleSection, Literal(row["articleSection"])))
    g.add((announcement, schema.pagination, Literal(row["pageNumber"])))
    g.add((announcement, schema.locationCreated, URIRef("http://vocab.getty.edu/page/tgn/7007567")))
    g.add((dbr.The_New_York_Times, schema.location, URIRef("http://vocab.getty.edu/page/tgn/7007567")))
    g.add((announcement, dc.subject, divorce))
    
    g.add((announcement, schema.creator, dbr.Sarah_Lyall))
    g.add((dbr.Sarah_Lyall, FOAF.name, Literal(row["author"])))

    g.add((divorce, crm.P14, Charles_uri))
    g.add((divorce, crm.P14, LadyDiana_uri))
    g.add((divorce, RDF.type, schema.Event))


g.serialize(format="turtle", destination="DivorceAnnouncement.ttl")