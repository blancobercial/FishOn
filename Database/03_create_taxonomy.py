### Script to extract taxonomy from GeneBank result file. Taxonomy info is stored in seq_record.annotations['taxonomy'] ready for mothur to be used as a taxonomy file

from Bio import SeqIO

#Parameters:
gbk_input = "input.txt"      	#Input file
faa_output = "taxonomy.txt"		#Output file

input_handle  = open(gbk_input, "r")
output_handle = open(faa_output, "w")

num_sequences=0   	#counter number 1, counts sequences present in database
empty_sequences=0   	#counter number 2, counts results where the sequence is empty
for seq_record in SeqIO.parse(input_handle, "genbank") :
    output_handle.write("%s\t%s;%s\n" % (seq_record.name, ";".join(seq_record.annotations['taxonomy']),seq_record.annotations['organism']))     #Writes results in output file according to the format specified inside " ", using string formatting notation '%s'. Taxonomic classifications are joined into one string and the elements are separated by "; ".
    num_sequences +=1              	#Counter increased by 1 at every cycle
    if str(seq_record.seq) == '':   	#Condition for empty sequences, increases the empty_sequences counter by 1:
        empty_sequences +=1
print "I counted", empty_sequences, "empty sequences in database out of ", num_sequences, "in total"

output_handle.close()
input_handle.close()
print "Completed"
