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

#items:
bridge = URIRef(lod + "AlmaBridge")
photo1 = URIRef(lod + "LadyDianaOnHolidayInPortofino")
song = URIRef(lod + "CandleInTheWind")
tvs = URIRef(lod + "TheCrown")
photo2 = URIRef(lod + "LadyDianaWithAIDSPatient")
book = URIRef(lod + "DianaHerTrueStory")
dress = URIRef(lod + "WeddingDress")
tiara = URIRef(lod + "Tiara")
interview = URIRef(lod + "EngagementInterview")
palace = URIRef(lod +"KensingtonPalace")
announcement = URIRef(lod + "DivorceAnnouncement")

#importan uris
LadyDiana_uri = URIRef(lod + "LadyDiana")
Charles_uri = URIRef(lod + "Charles")
Spencers = URIRef(lod + "SpencerFamily")
funeral = URIRef(lod + "LadyDFuneral")
wedding = URIRef(lod + "RoyalWedding")
divorce = URIRef(lod + "Divorce")
Buckingham = URIRef(lod + "BuckinghamPalace")
NottinghamHouse = URIRef(lod + "NottinghamHouse")
royals = URIRef(lod + "RoyalFamily")
apartments = URIRef(lod + "Apartments")


#Diana and Charles
g.add((LadyDiana_uri, OWL.sameAs, URIRef("http://viaf.org/viaf/107032638")))
g.add((Charles_uri, OWL.sameAs, URIRef("http://viaf.org/viaf/84034215")))


#first item
LadyDonYacht = read_csv("C:/Users/Utente/Desktop/LifeOfDiana/final_csv/Lady Diana on holiday in Portofino.csv", keep_default_na = False, encoding = "utf-8")

for _, row in LadyDonYacht.iterrows():
  
    g.add((photo1, schema.creator, Literal(row["Credits"])))
    g.add((photo1, schema.identifier, Literal(row["Name of the item"])))
    g.add((photo1, schema.copyrightHolder, Literal(row["Source"])))
    g.add((photo1, schema.dateCreated, Literal(row["Creation date"], datatype=XSD.date)))
    g.add((photo1, schema.uploadDate, Literal(row["Upload date"], datatype=XSD.date)))  
    g.add((photo1, RDFS.subClassOf, dcmitype.StillImage))
    g.add((dcmitype.StillImage, RDFS.subClassOf, schema.Image))
    g.add((schema.Image, RDFS.subClassOf, schema.CreativeWork))

    #triples outside the csv
    g.add((photo1, RDF.type, schema.Photograph))
    g.add((photo1, dc.title, Literal(row["Item"])))
    g.add((photo1, schema.provider, URIRef("http://viaf.org/viaf/151544970")))
    g.add((photo1, dc.subject, Literal("Lady Diana, Princess of Wales, sitting on the diving board of Mohammed Al Fayed's private yacht 'Jonikal' as a seagull flies overhead")))
    g.add((photo1, schema.locationCreated, URIRef("https://www.wikidata.org/wiki/Q232782")))
    g.add((photo1, FOAF.depicts, LadyDiana_uri))
    

#second item
CandleInTheWind = read_csv("C:/Users/Utente/Desktop/LifeOfDiana/final_csv/Candle in the Wind 1997.csv", keep_default_na = False, encoding = "utf-8")

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
    g.add((song, schema.workPerformed, funeral))
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
    

#third item
TheCrown =  read_csv("C:/Users/Utente/Desktop/LifeOfDiana/final_csv/The Crown.csv", keep_default_na = False, encoding = "utf-8")

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
    

#fourth item
AlmaBridge = read_csv("C:/Users/Utente/Desktop/LifeOfDiana/final_csv/Alma Bridge.csv", keep_default_na=False,encoding = "utf-8")

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


#fifth item
LadyDCharity = read_csv("C:/Users/Utente/Desktop/LifeOfDiana/final_csv/AIDs_photo.csv", keep_default_na = None, encoding="utf-8")

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


#sixth item
DianaHerTrueStory = read_csv("C:/Users/Utente/Desktop/LifeOfDiana/final_csv/Book.csv")

for _, row in DianaHerTrueStory.iterrows():

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


#item seven
WeddingDress = read_csv("C:/Users/Utente/Desktop/LifeOfDiana/final_csv/Wedd_dress.csv", keep_default_na = None, encoding="utf-8")

for _, row in WeddingDress.iterrows():
    g.add((dress, dc.title, Literal(row["Title"])))
    g.add((dress, RDF.type, URIRef("http://vocab.getty.edu/aat/300255177")))
    g.add((dress, schema.creator, Literal(row["Creator"])))
    g.add((dress, schema.material, Literal(row["Materials"])))
    g.add((dress, schema.color, Literal("Ivory")))
    g.add((dress, dc.relation, tiara))
    g.add((dress, schema.copyrightHolder, Spencers))
    g.add((dress, schema.copyrightHolder, Literal(row["Creator"])))
    g.add((dress, schema.location, Literal(row["Current Location"])))
    g.add((URIRef("http://vocab.getty.edu/aat/300255177"), RDFS.subClassOf, URIRef("http://vocab.getty.edu/page/aat/300209261")))
    g.add((URIRef("http://vocab.getty.edu/page/aat/300209261"), RDFS.subClassOf, schema.CreativeWork))
    g.add((wedding, crm.P16, dress))
    g.add((wedding, RDF.type, schema.Event))
    g.add((wedding, schema.location, URIRef("http://vocab.getty.edu/tgn/7011781")))
    g.add((wedding, dc.date, Literal("1981-07-29", datatype=XSD.date)))
    
    

#item eight
SpencerTiara = read_csv("C:/Users/Utente/Desktop/LifeOfDiana/final_csv/Spencer Tiara.csv", keep_default_na = None, encoding="utf-8")

for _, row in SpencerTiara.iterrows():
    g.add((tiara, dc.title, Literal(row["object"])))
    g.add((tiara, RDF.type, URIRef("http://vocab.getty.edu/aat/300046046")))
    g.add((tiara, schema.creator, Literal(row["creator"])))
    g.add((tiara, dc.relation, dress))
    g.add((tiara, schema.dateCreated, Literal(row["date"],datatype=XSD.gYear)))
    g.add((tiara, schema.material, Literal(row["material"])))
    g.add((tiara, schema.location, Literal(row["location"])))
    g.add((tiara, schema.copyrightHolder, Spencers))
    g.add((URIRef("http://vocab.getty.edu/aat/300046046"), RDFS.subClassOf, URIRef("http://vocab.getty.edu/page/aat/300209261")))
    g.add((URIRef("http://vocab.getty.edu/page/aat/300209261"), RDFS.subClassOf, schema.CreativeWork))
    g.add((wedding, crm.P16, tiara))


#item nine
EngagementInterview = read_csv("C:/Users/Utente/Desktop/LifeOfDiana/final_csv/engagement_interview.csv", keep_default_na = None, encoding="utf-8")

for _,row in EngagementInterview.iterrows():
    g.add((interview, dc.title, Literal(row["name"])))
    g.add((interview, dc.language, Literal(lang_data1, datatype=XSD.language)))
    g.add((interview, schema.dateCreated, Literal("1981-02-24", datatype=XSD.date)))
    g.add((interview, schema.identifier, Literal(row["identifier"])))
    g.add((interview, RDF.type, dcmitype.MovingImage))
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


#ten item
KensingtonPalace = read_csv("C:/Users/Utente/Desktop/LifeOfDiana/final_csv/kensingtonpalace-meta.csv", keep_default_na=False, encoding="utf-8")

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
    g.add((Charles_uri, schema.owns, palace))

#item eleven
DivorceAnnouncement = read_csv("C:/Users/Utente/Desktop/LifeOfDiana/final_csv/panorama1995-object-meta.csv", keep_default_na = False, encoding="utf-8")

for _,row in DivorceAnnouncement.iterrows():
    g.add((announcement, dc.title, Literal(row["title"])))
    g.add((announcement, RDF.type, schema.NewsArticle))
    g.add((schema.NewsArticle, RDFS.subClassOf, schema.Text))
    g.add((announcement, dc.language, Literal(lang_data1, datatype=XSD.language)))
    g.add((announcement, schema.publisher, dbr.The_New_York_Times))
    g.add((announcement, schema.copyrightHolder, dbr.The_New_York_Times))
    g.add((announcement, schema.isPartOf, Literal("CXLV, 50534")))
    g.add((announcement, schema.articleSection, Literal("A")))
    g.add((announcement, schema.pagination, Literal("9")))
    g.add((announcement, schema.locationCreated, URIRef("http://vocab.getty.edu/page/tgn/7007567")))
    g.add((dbr.The_New_York_Times, schema.location, URIRef("http://vocab.getty.edu/page/tgn/7007567")))
    g.add((announcement, dc.subject, divorce))
    
    g.add((announcement, schema.creator, dbr.Sarah_Lyall))
    g.add((dbr.Sarah_Lyall, FOAF.name, Literal("Sarah Lyall")))

    g.add((divorce, crm.P14, Charles_uri))
    g.add((divorce, crm.P14, LadyDiana_uri))
    g.add((divorce, RDF.type, schema.Event))

g.add((Charles_uri, schema.memberOf, royals))

for triples in g:
    print(triples)

print(len(g))
g.serialize(format="turtle", destination="ItemsDataset.ttl")
