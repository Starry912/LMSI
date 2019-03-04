# LMSI
MSI detection algorithm
The program is based on python2.7, so you first need to configure the python2.7 environment.
Steps
Pretreatment:
1. Index the bam file with samtools, sort (by readname) and convert to sam
2. Remove the duplicate and error read in the sam file with LMSI RemoveNameError.py (note the input and outpath in RemoveNameError.py)
3. Execute run.sh in the fileclass (note the path python "input file" "output result file")
