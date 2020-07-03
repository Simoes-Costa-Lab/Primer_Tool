import requests, sys, os, subprocess, time
server = "https://rest.ensembl.org"
seq = "/sequence/id/"
typ = "?type=cdna"
output = open("cDNA.txt", "w")
filepath = 'Transcripts.txt'
with open(filepath) as fp:
	for line in fp.readlines():	
		u = line.strip()
		ext = seq + u + typ
		r = requests.get(server+ext, headers={ "Content-Type" : "text/plain"})
		output.write("SEQUENCE_ID="+ u + "\n" + "SEQUENCE_TEMPLATE=" + r.text + "\n" + "=" +"\n")
