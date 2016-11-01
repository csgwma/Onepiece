#!/usr/bin/python
# -*- coding:utf-8 -*-

import urllib2
from datetime import datetime
from SPARQLWrapper import SPARQLWrapper, JSON, XML, N3, RDF
  
sparql = SPARQLWrapper("http://dbpedia.org/sparql")  

sparql.setQuery(""" 
	PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
	PREFIX dbo: <http://dbpedia.org/ontology/>
	PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
	PREFIX dc:  <http://purl.org/dc/elements/1.1/>

	SELECT distinct ?birthdate ?thumbnail ?scientist ?name ?description  WHERE {
	?scientist rdf:type dbo:Scientist ;
    	       dbo:birthDate ?birthdate ;
        	   rdfs:label ?name ;
        	   dc:description ?description 
 	FILTER ((lang(?name)="en")&&(lang(?description)="en")&&(STRLEN(STR(?birthdate))>6)&&(SUBSTR(STR(?birthdate),6)=SUBSTR(STR(bif:curdate('')),6))) .
 	OPTIONAL { ?scientist dbo:thumbnail ?thumbnail . }
} ORDER BY ?birthdate
""")  

sparql.setReturnFormat(JSON)  
results = sparql.query().convert()  

# Create HTML output

print '<html><head><title>Scientific Birthdays of Today</title></head>'

#extract Weeekday %A / Month %B / Day of the month %d by formatting today's data accordingly
datum = datetime.today().strftime("%A %B %d")
print '<body><h1>Scientific Birthdays of {}</h1>'.format(datum)

print '<ul>'

for result in results["results"]["bindings"]:
	if("scientist" in result):
		#Create Wikipedia Link
		url = "http://en.wikipedia.org/wiki/" + result["scientist"]["value"].encode('ascii', 'ignore').split('/')[-1]
	else:
		url = 'NONE'
	if("name" in result): 
		name =  result["name"]["value"].encode('ascii', 'ignore')
	else:
		name = 'NONE'

	if("birthdate" in result):
		date = result["birthdate"]["value"].encode('ascii', 'ignore')
	else:
		date = 'NONE'
	if("description" in result):
		description = result["description"]["value"].encode('ascii', 'ignore')
	else:
		description = 'NONE'
	if("thumbnail" in result):
		pic = result["thumbnail"]["value"].encode('ascii', 'ignore')
	else:
		pic = 'http://upload.wikimedia.org/wikipedia/commons/7/7a/Question_Mark.gif'

	#parse date as datetime
	dt = datetime.strptime(date, '%Y-%m-%d')
	print '<li><b>{}</b> -- <img src="{}" height="60px"> <a href="{}">{}</a>, {} </li>'.format(dt.year, pic.replace("300px","60"), url, name, description)

print '</ul>'
print '</body></html>'
  
