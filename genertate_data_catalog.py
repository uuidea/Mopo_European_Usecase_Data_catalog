
from SimpleMDDataCatalog.spreadsheet_to_ld import spreadsheet_to_ld_catalog
from SimpleMDDataCatalog.generate_catalog import generate_catalog



graph = spreadsheet_to_ld_catalog(uri="https://www.tools-for-energy-system-modelling.org/DataCatalog#",
                              output_graph= 'docs/datacatalog.ttl', 
                              input_sheet='catalog.xlsx') 


graph.serialize(destination= 'docs/datacatalog.ttl', 
                format= 'ttl') # i dont know why this is necesary, the above function should take cae of this

generate_catalog(repo_url= "https://github.com/joepvgenuchten/mopo-eu-data-validation", 
                 input_file="docs/datacatalog.ttl", 
                 output_dir='docs/')