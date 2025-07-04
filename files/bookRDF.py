import xml.etree.ElementTree as ET
from rdflib import Graph, Namespace, RDF, FOAF, XSD, Literal, URIRef, XSD, OWL

Book = ET.parse("SamplePage.xml")

root = Book.getroot()

ns = {"tei":"http://www.tei-c.org/ns/1.0"}

g = Graph()

schema = Namespace("https://schema.org/")
wdt = Namespace("http://www.wikidata.org/prop/direct/")
lod = Namespace("https://github.com/digitalctrlv/LifeOfDiana/")

g.bind("wdt", wdt)
g.bind("lod", lod)

for person in root.findall(".//tei:person", ns):
    id = person.get("{http://www.w3.org/XML/1998/namespace}id")
    uri = lod[id]
    g.add((uri, RDF.type, FOAF.Person))
    ac = person.get("sameAs")
    if ac is not None:  
        g.add((uri, OWL.sameAs, URIRef(ac)))
    
    pers_name = person.find("tei:persName", ns)
    if pers_name is not None and pers_name.text is not None:
        name = pers_name.text.strip()
        if name:
            g.add((uri, FOAF.name, Literal(name)))
    
    birth = person.find("tei:birth[@when]", ns)
    if birth is not None:
        birth = birth.get("when")
        if len(birth) == 4 and birth.isdigit():
            datatype = XSD.gYear
        else:
            datatype = XSD.date

        g.add((uri, FOAF.birthday, Literal(birth, datatype=datatype)))

    death = person.find("tei:death[@when]", ns)
    if death is not None:
        death = death.get("when")
        if len(death) == 4 and death.isdigit():
            datatype = XSD.gYear
        else:
            datatype = XSD.date
    
        g.add((uri, schema.deathDate, Literal(death, datatype=datatype)))
    
    positionHeld = person.find("tei:roleName", ns)
    if positionHeld is not None and positionHeld.text:
        role = positionHeld.text.strip()

        g.add((uri, wdt.P39, Literal(role)))
    

    relations = root.find(".//tei:listRelation", ns)
    if relations is not None:
        relation_list = relations.findall("tei:relation", ns)
        for relation in relation_list:
            rel_name = relation.get("name")
            active = relation.get("active")
            passive = relation.get("passive")

            if active is None or passive is None:
                continue  

            active = active.split()
            passive = passive.split()

            a_uris = [lod[id.lstrip("#")] for id in active]
            p_uris = [lod[id.lstrip("#")] for id in passive]
            
            if rel_name == "parent":
                 for a_uri in a_uris:
                     for p_uri in p_uris:
                        g.add((a_uri, schema.children, p_uri))

            if rel_name == "child":
                for a_uri in a_uris:
                    for p_uri in p_uris:
                        g.add((a_uri, schema.parent, p_uri))

            if rel_name == "brother" or rel_name == "sister":
                 for a_uri in a_uris:
                    for p_uri in p_uris:
                        g.add((a_uri, schema.sibling, p_uri))
                    
            
author_name = root.find(".//tei:titleStmt/tei:author/tei:persName", ns)
if author_name is not None:
    id = author_name.get("ref")
    author_uri = lod[id]

book_title = root.find(".//tei:sourceDesc/tei:bibl/tei:title[@type='main']", ns)
if book_title is not None:
    id = book_title.get("{http://www.w3.org/XML/1998/namespace}id")
    book_uri = lod[id]

g.add((book_uri, schema.author, author_uri))

publishDate = root.find(".//tei:sourceDesc/tei:bibl/tei:date", ns)
if publishDate is not None:
    publishDate = publishDate.get("when")

publishPlace = root.find(".//tei:sourceDesc/tei:bibl/tei:pubPlace", ns)
if publishPlace is not None:
    publishPlace_id = publishPlace.get("ref")

publisher = root.find(".//tei:sourceDesc/tei:bibl/tei:publisher", ns)
if publisher is not None:
    id = publisher.get("{http://www.w3.org/XML/1998/namespace}id")
    publisher_uri = lod[id]

g.add((book_uri, schema.datePublished, Literal(publishDate, datatype = XSD.gYear)))
g.add((book_uri, schema.locationCreated, URIRef(publishPlace_id)))
g.add((book_uri, schema.publisher, publisher_uri))
      

triples = set(g)

print(len(g))
for t in triples:
    print(t)

g.serialize(format="turtle", destination="XML_to_RDF.ttl")



