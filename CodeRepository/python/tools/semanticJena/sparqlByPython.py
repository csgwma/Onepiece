from SPARQLWrapper import SPARQLWrapper, JSON  
  
# sparql = SPARQLWrapper("http://dbpedia.org/sparql")  
sparql = SPARQLWrapper("http://localhost:3030/TDB1/query")
sparql.setQuery(""" 
    prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    prefix owl: <http://www.w3.org/2002/07/owl#>

    SELECT ?subject ?predicate ?object
    WHERE {
    	?subject ?predicate ?object
    }
""")  

sparql.setReturnFormat(JSON)  
results = sparql.query().convert()  
  
for result in results["results"]["bindings"]:  
    print(result["subject"]["value"] + " "+ result["predicate"]["value"] + " " + result["object"]["value"]+ " .")  
