import pandas as pd
from validators import uri
import validators
from rdflib import Graph, Namespace, URIRef, Literal, BNode
from rdflib.namespace import FOAF, DCTERMS, DCAT, PROV, OWL, RDFS, RDF, XMLNS, SKOS, SOSA, ORG, SSN, XSD
from uri_handling import literal_or_uri, identifier_to_uri, str_abbrev_namespace_to_full_namespace
from import_catalog import parse_catalog, create_index, create_dataset_pages, create_concept_pages, get_lineage, create_metric_pages

def generate_catalog(repo_url: str, input_file: str= './docs/catalog.ttl', output_dir: str= './docs/'):

    catalog_graph= parse_catalog(input_file=input_file)
    create_index(catalog_graph= catalog_graph, output_dir=output_dir, repo_url=repo_url)
    create_dataset_pages(catalog_graph=catalog_graph, output_dir=output_dir)
    create_concept_pages(catalog_graph=catalog_graph, output_dir=output_dir)
    create_metric_pages(catalog_graph=catalog_graph, output_dir=output_dir)

# mopo example
    
# input_file='/home/joep/Documents/uuidea/git/Mopo_European_Usecase_Data_catalog/docs/datacatalog.ttl'
# output_dir= '/home/joep/Documents/uuidea/git/Mopo_European_Usecase_Data_catalog/docs/'
# repo_url= 'https://github.com/uuidea/Mopo_European_Usecase_Data_catalog'
# generate_catalog(repo_url=repo_url, input_file=input_file, output_dir=output_dir)

# test repo

repo_url= 'https://github.com/uuidea/Mopo_European_Usecase_Data_catalog'
input_file='./docs/datacatalog.ttl'

generate_catalog(repo_url=repo_url, input_file=input_file)