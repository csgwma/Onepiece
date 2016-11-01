from SPARQLWrapper import SPARQLWrapper, JSON  
  
# sparql = SPARQLWrapper("http://dbpedia.org/sparql")  
sparql = SPARQLWrapper("http://10.101.93.212:3030/TDBtest/update")

#update sql 
queryString = "INSERT DATA { <http://example/book1> <http://purl.org/dc/elements/1.1/title> "Third" . }" 
sparql.setQuery(queryString) 
sparql.method = 'POST'
sparql.query()

