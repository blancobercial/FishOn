#from the gz files from the illumina, create the stability file with the samples R1 and R2
make.file(inputdir=./, type=gz, prefix=best)
#you can edit the best.files file to put better names to the samples if the ones from illumina are too cryptic
#read mothur instructions to understand the structure of the stability file.
#Next step: make contigs - Delta q is low so correction is very unlikely (ambiguities will stay and be removed later)
#insert very high to avoid false inserts. 
#Since the Fragment is small enough, you should reach the end of the fragment, so trimoverlap will help cleaning
make.contigs(file=best.files, deltaq=10, insert=30, trimoverlap=T, processors=40)
summary.seqs(fasta=current)
#remove reads with any ambiguity, and less than 160 bp - not real
screen.seqs(fasta=current, group=current, qfile=current, minlength=160, maxambig=0)
summary.seqs(fasta=current, name=current)
#remove sequences with homopolimers of more than 10 bp
screen.seqs(fasta=current, group=current, qfile=current, maxhomop=10)
summary.seqs(fasta=current, name=current)
#get unique seqs to make like easier
unique.seqs(fasta=current)
summary.seqs(fasta=current, name = current)
#align against the reference, this is from Mitofish
align.seqs(fasta=current, template=ShortRef.fas)
summary.seqs(fasta=current, name = current)
#remove all sequences that do not reach the end of the alignment (incomplete).
#You might need to check the alignemtn is 179 bp long first. If you have non-fish contaminants you might have longer reads
screen.seqs(fasta=current, name=current, group=current, end=179)
summary.seqs(fasta=current, name = current)
#remove all sequences that do not beging at the beginning of the alignment (incomplete)
screen.seqs(fasta=current, name=current, group=current, start=1)
summary.seqs(fasta=current, name = current)
#again unique - there will be some
unique.seqs(fasta=current, name=current)
summary.seqs(fasta=current, name = current)
#removing chimeras
chimera.vsearch(fasta=current, name=current, group=current, dereplicate=t)
remove.seqs(fasta=current, accnos=current, name=current, group=current, dups=f)
summary.seqs(fasta=current, name = current)
unique.seqs(fasta=current, name=current)
get.current()
#with the new mothur version, this is equivalent to the swarm approach of a distance matrix of 1 bp, but much faster.
#This is equivalent to SVAs
pre.cluster(fasta=current, name=current, group=current, diffs=1, method=deblur)
summary.seqs(fasta=current, count=current)
get.current()
#removing the gaps form the alignments - cleaner fastas
degap.seqs(fasta=current)
#make a table with counts
count.seqs(count=current, compress=f)
get.current()
quit()
#after this, you have a fasta file with the reference sequence, and a count_table with the number of reads for each reference sequence.
#Those refernce sequences are equivalent to SVA or mOTUs at 100% similarity. IDs can be obtained form GenBank, or using a dedicated
#database create with the python scripts found in this repository, but then an extra step should be used to classify the sequences: 
#"classify.seqs(fasta=yourlastfasta, template=templatefasta, taxonomy=templatetaxonomy)".
#Include few other taxa (invertebrates, urochordata, mammalia, reptilia, etc) in the database, to be sure you flag all contaminants.
#You should obtain a file with the hierarchical classification according with your database. 
#All tables can be used in any dedicated software (R, excel, Primer) for analyses
#In case of doubt check Mothur manual. This pipeline was run in Mothur Ver. 1.42.2
