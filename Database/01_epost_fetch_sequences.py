#Download all whatever sequences (incl. partial genomes) from Genbank
# Works with Python2.7 and 3.6
#original link: https://www.biostars.org/p/43970/
#!/usr/bin/env python

# Dependencies:
import sys
#import  urllib.request #Uncomment this for python3.6
from urllib2 import HTTPError   #Uncomment this for python2.7
from Bio      import Entrez
from datetime import datetime

#Parameters:
faa_output = "One_20180125_cichliformes.test.txt"		#Output file name
output_handle = open(faa_output, "w")					#Creates the file if it does not exist
Entrez.email = "your_email@something.com"					#You have to tell ncbi who you are
#query= '("Oreochromis macrochir"[Organism] OR Oreochromis macrochir[All Fields]) AND mitochondrion[All Fields] AND complete[All Fields] AND genome.[All Fields]'
query='(12S[All Fields] AND ("Cichliformes"[Organism] OR Cichliformes[All Fields])) AND animals[filter]'    #This is an example query. For your own query: do a search on ncbi website for what you want and copy, paste the content of the "search details" box in here.
db="nucleotide"             	#Alternative databases: pubmed, nuccore...
retmax=10**9			#Max number of results to be retrieved
retmode='text'
rettype='gb'			#Alternative= 'fasta'
batchSize=250			#Sequences will be downloaded in batches of size 1000

#Get list of entries for given query
sys.stderr.write( "Getting list of GIs for term=%s ...\n" % query )
handle = Entrez.esearch( db=db,term=query,retmax=retmax )       #Searching the entrez databases with Entrez.search() and get ID list
giList = Entrez.read(handle)['IdList']

#Print info about number of results
sys.stderr.write( "Downloading %s entries from NCBI %s database in batches of %s entries...\n" % ( len(giList),db,batchSize ) )

#Post NCBI query
search_handle     = Entrez.epost( db, id=",".join( giList ) ) 		#Uploads list of identifiers (Bio.Entrez.epost() ) and avoids problems with super long URLs. Then downloads data with EFetch thanks to history present in WebEnv and QueryKey.
search_results    = Entrez.read( search_handle )
webenv,query_key  = search_results["WebEnv"], search_results["QueryKey"]

#Fecthes all results in batch of batchSize entries at once
for start in range( 0,len(giList)+1,batchSize ):
  #Prints info during download
  tnow = datetime.now()
  sys.stderr.write( "\t%s\t%s / %s\n" % ( datetime.ctime(tnow),start,len(giList) ) )
  handle=Entrez.efetch(db=db,retmode=retmode,rettype=rettype,retstart=start,retmax=batchSize,webenv=webenv,query_key=query_key)
  #sys.stdout.write( handle.read() )		#Prints out the results grouped by the variable  handle
  output_handle.write(handle.read())		#Writes the output in faa_output.
output_handle.close()       #Saves everything
print("That's all folks")
