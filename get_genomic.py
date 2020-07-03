import requests, sys, os, subprocess, time
server = "https://rest.ensembl.org"
seq = "/sequence/region/chicken/"
output = open("genomic.txt", "w")
filepath = 'locations.txt'
with open(filepath) as fp:
	for line in fp.readlines():	
		u = line.strip()
		ext = seq + u + "?expand_5prime=500;expand_3prime=500;"
		r = requests.get(server+ext, headers={ "Content-Type" : "text/plain"})
		output.write("SEQUENCE_ID="+ u + "\n" + "SEQUENCE_TEMPLATE=" + r.text + "\n" + "=" +"\n")
