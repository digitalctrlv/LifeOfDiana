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

Charles_uri = URIRef(lod + "Charles")
Spencers = URIRef(lod + "SpencerFamily")
funeral = URIRef(lod + "LadyDFuneral")
wedding = URIRef(lod + "RoyalWedding")
divorce = URIRef(lod + "Divorce")
Buckingham = URIRef(lod + "BuckinghamPalace")
NottinghamHouse = URIRef(lod + "NottinghamHouse")
royals = URIRef(lod + "RoyalFamily")
apartments = URIRef(lod + "Apartments")
LadyDiana_uri = URIRef(lod + "LadyDiana")

bridge = URIRef(lod + "AlmaBridge")
photo1 = URIRef(lod + "LadyDianaOnHolidayInPortofino")
tvs = URIRef(lod + "TheCrown")
book = URIRef(lod + "DianaHerTrueStory")
dress = URIRef(lod + "WeddingDress")
tiara = URIRef(lod + "Tiara")
interview = URIRef(lod + "EngagementInterview")
palace = URIRef(lod +"KensingtonPalace")


g.add((LadyDiana_uri, OWL.sameAs, URIRef("http://viaf.org/viaf/107032638")))
g.add((Charles_uri, OWL.sameAs, URIRef("http://viaf.org/viaf/84034215")))
g.add((Charles_uri, schema.memberOf, royals))
g.add((royals, OWL.sameAs, dbr.British_royal_family))

TheCrown =  read_csv("../final_csv/The Crown.csv", keep_default_na = False, encoding = "utf-8")

for _, row in TheCrown.iterrows():
   
    languages = {"English" : "en"}
    lang_data1 = languages.get(row["Language"], "und")

    Peter_uri= URIRef(lod + "PeterMorgan")
    Elizabeth_uri = URIRef(lod + "ElizabethDebicki")
    Emma_uri = URIRef(lod + "EmmaLouiseCorrin")
    LBP_uri = URIRef(lod + "LeftBankPictures")
    SPT_uri = URIRef(lod + "SonyPictureTelevision")
    Stars = row["Stars"].split(",")
    star1 = Stars[0].strip()
    star2 = Stars[1].strip()
    Productors = row["Production companies"].split(",")
    Prod1 = Productors[0].strip()
    Prod2 = Productors[1].strip()
    Prod3 = Productors[2].strip()

    g.add((tvs, dc.title, Literal(row["name"])))
    g.add((tvs, RDF.type, schema[row["type"]]))
    g.add((tvs, OWL.sameAs, URIRef("https://viaf.org/en/viaf/3838148997596659870003")))
    g.add((tvs, schema.uploadDate, Literal(row["Release date"], datatype=XSD.date)))
    g.add((tvs, dc.language, Literal(lang_data1, datatype=XSD.language)))
    g.add((tvs, schema.genre, Literal(row["Genres"])))
    g.add((tvs, schema.locationCreated, Literal(row["Filming locations"])))
    g.add((schema.TVSeries, RDFS.subClassOf, dcmitype.MovingImage))
    g.add((dcmitype.MovingImage, RDFS.subClassOf, schema.Image))
    g.add((schema.Image, RDFS.subClassOf, schema.CreativeWork))
    g.add((tvs, schema.provider, URIRef("https://viaf.org/en/viaf/110144647635343459670")))

    #creator triples
    g.add((tvs, schema.creator, Peter_uri))
    g.add((Peter_uri, OWL.sameAs, URIRef("https://www.wikidata.org/wiki/Q948122")))
    g.add((Peter_uri, FOAF.name, Literal(row["Creator"])))
    
    #elizabeth triples
    g.add((tvs, schema.actor, Elizabeth_uri))
    g.add((Elizabeth_uri, FOAF.name, Literal(star2)))
    g.add((Elizabeth_uri, OWL.sameAs, URIRef("http://viaf.org/viaf/305280245")))
    g.add((Elizabeth_uri, schema.roleName, LadyDiana_uri))
    
    #emma triples
    g.add((tvs, schema.actor, Emma_uri))
    g.add((Emma_uri, FOAF.name, Literal(star1)))
    g.add((Emma_uri, OWL.sameAs, URIRef("http://viaf.org/viaf/1883161881819434100005")))
    g.add((Emma_uri, schema.roleName, LadyDiana_uri))

    #prod triples
    g.add((tvs, schema.producer, LBP_uri))
    g.add((LBP_uri, FOAF.name, Literal(Prod1)))
    g.add((LBP_uri, OWL.sameAs, URIRef("http://viaf.org/viaf/130591214")))

    g.add((tvs, schema.producer, SPT_uri))
    g.add((SPT_uri, FOAF.name, Literal(Prod3)))
    g.add((SPT_uri, OWL.sameAs, URIRef("https://www.wikidata.org/wiki/Q652390")))

    g.add((tvs, schema.producer, Literal(Prod2)))

    g.add((tvs, FOAF.depicts, LadyDiana_uri)) 
    g.add((tvs, FOAF.depicts, Charles_uri)) 
    g.add((tvs, FOAF.depicts, funeral))
    g.add((tvs, FOAF.depicts, photo1))
    g.add((tvs, FOAF.depicts, bridge))
    g.add((tvs, FOAF.depicts, book))
    g.add((tvs, FOAF.depicts, dress))
    g.add((tvs, FOAF.depicts, tiara))
    g.add((tvs, FOAF.depicts, wedding)) 
    g.add((tvs, FOAF.depicts, funeral))  
    g.add((tvs, FOAF.depicts, royals))  
    g.add((tvs, FOAF.depicts, Buckingham)) 
    g.add((tvs, FOAF.depicts, NottinghamHouse))  
    g.add((tvs, FOAF.depicts, palace))   


g.serialize(format="turtle", destination="TheCrown.ttl")
    