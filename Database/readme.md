Python scripts to build a mothur-like reference database: a fasta and a taxonomy files.</p>
The <i>01_epost_fetch_sequences.py</i> script will allow to query NCBI website and download (in GeneBank format) the results from the query, in this case 12S.</p>
The <i>02_extract_sequences_from_gb.py</i> script will allow to extract the fasta sequence from the downloaded genebank file, in a format that mothur will accept.</p>
The <i>03_create_taxonomy.py</i> script extracts the hierarchical taxonomy info from the downloaded genebank file and creates a mothur-like taxonomy file. This will have the hierarchical classification, allowing to study resuls at supraspecies level.</p>
You might also want to first run all your representative sequences against GenBank (BLAST), download all results as a gb file, and then create your taxonomy and reference database and run</p> <i>classify.seqs(fasta=yourlastfasta, template=templatefasta, taxonomy=templatetaxonomy)</i></p> in mothur to just get the hierarchical classification from your fasta (the species identified should be the same as in the GenBank BLAST).</p>
Please cite this repository if using these scripts!</p>

Authors:

Luca Peruzza

Leocadio Blanco Bercial

Tim Noyes
