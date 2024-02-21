#!/bin/bash

#SBATCH --account OPEN-29-7
#SBATCH --time=05:00:00
#SBATCH --partition=qgpu
#SBATCH --error=errors/%x-%j.out
#SBATCH --output=logs/%x-%j.err
#SBATCH --mail-user=varun.burde@cvut.cz
#SBATCH --mail-type=ALL

conda deactivate
module load CMake/3.21.1-GCCcore-11.2.0
module load CUDA
module load Python/3.9.6-GCCcore-11.2.0

source ../venv/bin/activate

python run_arthem.py
