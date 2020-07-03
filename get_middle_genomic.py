import requests, sys, os, subprocess, time
server = "https://rest.ensembl.org"
seq = "/sequence/region/chicken/"
output = open("Selected_Enhancers_toClone_3_genomic.txt", "w")
filepath = 'Selected_Enhancers_toClone_3.txt'
with open(filepath) as fp:
	for line in fp.readlines():	
		u = line.strip()
		u_len = int(u.split(':')[2]) - int(u.split(':')[1])
		u_fmt = (u.split(':')[0] + ":" + str(int(u.split(':')[1])+round(u_len/2)) +
				".." + str(int(u.split(':')[1])+round(u_len/2)+1))
		print(u_fmt)
		ext = seq + u_fmt + "?expand_5prime=750;expand_3prime=750;"
		r = requests.get(server+ext, headers={ "Content-Type" : "text/plain"})
		output.write("SEQUENCE_ID="+ u + "\n" + "SEQUENCE_TEMPLATE=" + r.text + "\n" + "=" +"\n")
