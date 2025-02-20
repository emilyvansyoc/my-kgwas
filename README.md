# my-kgwas
Repository for scripts related to KGWAS 

Text file: 'mini_inputfile.txt' is a subset of GWAS summary statistics used as input to KGWAS. This is already formatted to KGWAS specifications and should run as-is. Output directly from PLINK, the column headers are briefly changed to match KGWAS specs and sample size is added ('N').

Python scripts:
1. kgwas-default-params.py: Run KGWAS on default parameters with KG that is downloaded upon install.
2. kgwas-full.py: Run KGWAS on the 'full' KG (downloaded from https://drive.google.com/file/d/14UcHzPRIbdMmnLPZCHx_4G-gz2pipeg9/view) using embedding settings from preprint
3. 
