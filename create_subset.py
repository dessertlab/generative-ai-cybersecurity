import random
import os

input_folder = "dataset"
output_folder = "1-code_correctness/results"

input_file_in = os.path.join(input_folder, "violent_python.in")
input_file_out = os.path.join(input_folder, "violent_python.out")

output_file_in = os.path.join(output_folder, "reference.in")
output_file_out = os.path.join(output_folder, "reference.out")

# Ensure the output folder exists
os.makedirs(output_folder, exist_ok=True)

with open(input_file_in, 'r') as fin:
    dataset_in = fin.readlines()

with open(input_file_out, 'r') as fout:
    dataset_out = fout.readlines()

subset_size = 10

# Select 10 random indices, keeping the same index for both files
unique_numbers = random.sample(range(len(dataset_in)), subset_size)
subset_in = [dataset_in[i] for i in unique_numbers]
subset_out = [dataset_out[i] for i in unique_numbers]

# Write the subsets to the output files
with open(output_file_in, 'w') as f_in:
    f_in.writelines(subset_in)
with open(output_file_out, 'w') as f_out:
    f_out.writelines(subset_out)