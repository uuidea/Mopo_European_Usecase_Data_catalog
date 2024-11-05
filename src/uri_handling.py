from validators import uri
import validators
from rdflib import Graph, Namespace, URIRef, Literal, BNode
from rdflib.namespace import FOAF, DCTERMS, DCAT, PROV, OWL, RDFS, RDF, XMLNS, SKOS, SOSA, ORG, SSN, XSD, SH, PROF

prefix_dictionary= {
    "foaf":FOAF,
    "dcterms" : DCTERMS,
    "dct" : DCTERMS,
    "dcat" : DCAT,
    "prov" : PROV,
    "owl" :  OWL,
    "rdfs" : RDFS,
    "rdf" : RDF,
    "xml" :XMLNS,
    "xmlns" : XMLNS, 
    "skos": SKOS,
    "sosa" : SOSA,
    "org" :ORG,
    "ssn" : SSN,
    "xsd" : XSD,
    "sh": SH,
    "prof": PROF,
    "dx-prof": PROF,
    "dqv": "http://www.w3.org/ns/dqv#",
    "iso": "https://iso25000.com/index.php/en/iso-25000-standards/iso-25012/",
    "p-plan": "<http://purl.org/net/p-plan#>"
}

def identifier_to_uri(identifier: str, namespace: Namespace) -> URIRef :
    # checks if identifier str is a valid uri and if it is not, turns it into a uri
    identifier= str(identifier)
    if validators.uri.uri(identifier):
        uri=identifier
    else :
        no_space_id= identifier.replace(' ', '_')
        uri= namespace[no_space_id]
    return uri

def literal_or_uri(string : str):
    # checks if string is value or uri and returns as appropriate type
    string = str(string)
    split_str = string.split(":")
    if validators.uri.uri(string):
        value= URIRef(string)
    elif len(split_str) == 2 and split_str[0] in prefix_dictionary :
        value = str_abbrev_namespace_to_full_namespace(str_uri= string)

    else :
        value = Literal(string) 

    return value   

def str_abbrev_namespace_to_full_namespace(str_uri: str):
    split_at_colon= str_uri.split(":")
    full_namespace_str= str(prefix_dictionary[split_at_colon[0]])+str(split_at_colon[1])
    full_namespace=URIRef(full_namespace_str)
    return full_namespace




