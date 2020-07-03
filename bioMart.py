from biomart import BiomartServer
server = BiomartServer("http://useast.ensembl.org/biomart/martview/ec08e701a2d216b5bfcc4361a79f4156?VIRTUALSCHEMANAME=default&ATTRIBUTES=ggallus_gene_ensembl.default.feature_page.ensembl_gene_id|ggallus_gene_ensembl.default.feature_page.ensembl_transcript_id&FILTERS=&VISIBLEPANEL=mainpanel")
print(server.show_datasets())