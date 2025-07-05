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

song = URIRef(lod + "CandleInTheWind")
funeral = URIRef(lod + "LadyDFuneral")

CandleInTheWind = read_csv("../final_csv/Candle in the Wind 1997.csv", keep_default_na = False, encoding = "utf-8")

for _, row in CandleInTheWind.iterrows():
    
    languages = {"English" : "en"}
    lang_data = languages.get(row["lyrics in languages"], "und")

    #creating useful uris
    publisher = URIRef(lod + "songPublisher")
    Elton_uri = URIRef(lod + "EltonJohn")
    lyr_and_contr = URIRef(lod + "BernieTaupin")
   
    g.add((song, dc.title, Literal(row["Title"])))
    g.add((song, RDF.type, schema.MusicComposition))
    g.add((schema.MusicComposition, RDFS.subClassOf, schema.CreativeWork))
    g.add((song, OWL.sameAs, URIRef(wd + row["Wikidata"]))) 
    g.add((song, dc.language, Literal(lang_data, datatype=XSD.language)))
    g.add((song, schema.identifier, Literal(row["ISWC"])))
    g.add((song, schema.isBasedOn, Literal(row["revision of"])))
    g.add((song, schema.dateCreated, Literal(row["Date"], datatype=XSD.date)))
    g.add((song, schema.duration, Literal(row["Length"]))) 
    g.add((song, schema.genre, Literal("Singer-songwriter")))
    g.add((song, schema.genre, dbr.Rock_music))
    g.add((song, schema.genre, dbr.Ballad))
    g.add((song, schema.genre, dbr.Classic_rock))
    g.add((song, schema.genre, dbr.Pop))
    g.add((funeral, schema.workPerformed, song))
    g.add((funeral, RDF.type, schema.Event))
    g.add((song, schema.locationCreated, URIRef("http://vocab.getty.edu/page/tgn/1100068"))) # westminster
    g.add((funeral, schema.location, URIRef("http://vocab.getty.edu/page/tgn/1100068"))) # westminster
    g.add((song, schema.about, LadyDiana_uri))

    #Elton triples
    g.add((song, schema.creator, Elton_uri)) 
    g.add((Elton_uri, FOAF.name, Literal(row["composer"])))
    g.add((Elton_uri, OWL.sameAs, URIRef("http://viaf.org/viaf/84034533"))) 

    #Bernie triples
    g.add((song, schema.contributor, lyr_and_contr)) 
    g.add((song, schema.lyricist, lyr_and_contr))
    g.add((lyr_and_contr, FOAF.name, Literal(row["revised by"]))) 
    g.add((lyr_and_contr, OWL.sameAs, dbr.Bernie_Taupin))

    #publisher triples
    g.add((song, schema.publisher, publisher))
    g.add((publisher, OWL.sameAs, URIRef("https://www.wikidata.org/wiki/Q57818158")))
    g.add((publisher, FOAF.name, Literal(row["publisher"]) ))


g.serialize(format="turtle", destination="CandleInTheWind.ttl")