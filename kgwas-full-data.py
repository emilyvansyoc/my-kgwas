## run KGWAS on the 'full' data with preprint embedding settings
# EVS 2/2025
from kgwas import KGWAS, KGWAS_Data
import sys # to get filename from command line argument
import os
##### get input file
def process_file(file_path):
    """Function that takes the file path as input and processes it"""
    print(f"Processing file: {file_path}")
    # You can pass 'file_path' to other functions or libraries as needed.
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python my_script.py <input_file_path>")
        sys.exit(1)
    input_file_path = sys.argv[1]  # Get the file path from the command-line argument
    process_file(input_file_path)
    base_name = os.path.splitext(os.path.basename(input_file_path))[0]
    print(f"Saving KGWAS output as: {base_name}")
#### run KGWAS
data = KGWAS_Data(data_path = "/full_kgwas_data/")
data.load_kg(snp_init_emb = 'baselineLD', go_init_emb = 'random', gene_init_emb = 'pops')
## load my data
data.load_external_gwas(input_file_path)
data.process_gwas_file()
data.prepare_split()
data.lr_uni # prints the head of the file -> make sure everything looks OK
# train the model
run = KGWAS(data, exp_name=base_name)
run.initialize_model()
run.train(epoch = 10)
