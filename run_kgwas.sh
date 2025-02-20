#!/bin/bash

#SBATCH --job-name=kgwas
#SBATCH -N 1
#SBATCH -n 10
#SBATCH --mem=64Gb
#SBATCH -t 48:00:00
#SBATCH --output=logfiles/kgwas_%A_%a.out
#SBATCH --error=logfiles/kgwas_%A_%a.err
#SBATCH --array=2-44

##### RUN KGWAS IN ARRAY
# load conda 
module load anaconda
conda activate torch.cpu

# get into correct directory
DIR=/storage/restricted/srb6251/default/kgwas_emily/
cd $DIR

# set input directory
INDIR=$DIR/input_kgwas/

## define list of input files
FILES=($(ls $INDIR/*.txt | sort))

# select file based on array index
INPUT_FILE=${FILES[$SLURM_ARRAY_TASK_ID-1]}
echo "Starting KGWAS run on: $INPUT_FILE"

# run script
python my_kgwas.py "$INPUT_FILE"
