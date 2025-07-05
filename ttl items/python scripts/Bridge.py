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

g.add((LadyDiana_uri, OWL.sameAs, URIRef("http://viaf.org/viaf/107032638")))

bridge = URIRef(lod + "AlmaBridge")

AlmaBridge = read_csv("../final_csv/Alma Bridge.csv", keep_default_na=False,encoding = "utf-8")

for _, row in AlmaBridge.iterrows():

    g.add((bridge, dc.title, Literal(row["Item"])))
    g.add((bridge, schema.startDate, Literal(row["Beginning of works"], datatype=XSD.gYear)))
    g.add((bridge, schema.endDate, Literal(row["Completion"], datatype=XSD.gYear)))
    g.add((bridge, RDF.type, URIRef("http://vocab.getty.edu/aat/300007838")))
    g.add((bridge, schema.material, Literal(row["Material"])))
    g.add((bridge, schema.location, URIRef("https://www.wikidata.org/wiki/Q90")))
    g.add((bridge, schema.geoCrosses, URIRef("http://viaf.org/viaf/316432461")))
    g.add((bridge, schema.creator, Literal(row["Architecture"])))
    g.add((bridge, schema.creator, Literal(row["Engineering"])))
    g.add((bridge, schema.copyrightHolder, Literal(row["Owner"])))
    g.add((URIRef("http://vocab.getty.edu/aat/300007838"), RDFS.subClassOf, URIRef("http://vocab.getty.edu/page/aat/300264550")))
    g.add((URIRef("http://vocab.getty.edu/page/aat/300264550"), RDFS.subClassOf, schema.CreativeWork))
    g.add((LadyDiana_uri, schema.deathPlace, bridge))

g.serialize(format="turtle", destination="AlmaBridge.ttl")
    