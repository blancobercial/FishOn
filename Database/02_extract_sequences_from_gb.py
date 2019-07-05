### Script to extract sequences from GeneBank result file, or any other element from the dictionary in seq_record.annotations or in seq_record.seq and format it in fasta for mothur
from Bio import SeqIO

gbk_input = "input_from_genebank.txt"     		#Input file.
faa_output = "sequences.fasta"		#Output file.

input_handle  = open(gbk_input, "r")
output_handle = open(faa_output, "w")

num_sequences =0   	#counter number  1, counts sequences present in database
empty_sequences =0   	#counter number  2, counts results where the sequence is empty
for seq_record in SeqIO.parse(input_handle, "genbank") :
    output_handle.write(">%s organism %s\t%s\n%s\n"      #Write results in output file according to the format specified inside " ", using the string formatting notation '%s':
           %(seq_record.name, seq_record.annotations['organism'], seq_record.description, str(seq_record.seq)))		# Accession number, scientific name, description, sequence
    num_sequences +=1              #Counter increased by 1 at every cycle
    if str(seq_record.seq) == '':   #Condition for empty sequences, increases the empty_sequences counter by 1:
        empty_sequences +=1
print "I counted", empty_sequences, "empty sequences in database, out of ", num_sequences, "in total"

output_handle.close()
input_handle.close()
print "Completed"
