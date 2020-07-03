import requests, sys
import csv

filepath = 'Selected_Enhancers_toClone_3_primers.txt'

with open(filepath) as fp:
    a2 = fp.readlines()
with open('Selected_Enhancers_toClone_3_primers_reduced.csv', mode='w') as csvOut:
    out_writer = csv.writer(csvOut, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    out_writer.writerow(['SEQUENCE_ID','PRIMER_LEFT_SEQUENCE','PRIMER_RIGHT_SEQUENCE','PRODUCT_SIZE'])
    e_list = []
    for i in a2:
            if i.startswith('SEQUENCE_ID='):
                e_list.append(i.split('=')[1].strip())
            if i.startswith('PRIMER_PAIR_NUM_RETURNED=0'):
                out_writer.writerow(e_list)
                e_list = []
            if i.startswith('PRIMER_LEFT_0_SEQUENCE='):
                e_list.append(i.split('=')[1].strip())
            if i.startswith('PRIMER_RIGHT_0_SEQUENCE='):
                e_list.append(i.split('=')[1].strip())
            if i.startswith('PRIMER_PAIR_0_PRODUCT'):
                e_list.append(i.split('=')[1].strip())
                out_writer.writerow(e_list)
                e_list = []