import random
import os

input_folder = "dataset"
output_folder = "scripts/results"

input_file_in = os.path.join(input_folder, "violent_python.in")
input_file_out = os.path.join(input_folder, "violent_python.out")

output_file_in = os.path.join(output_folder, "reference.in")
output_file_out = os.path.join(output_folder, "reference.out")
prompt_file_example = os.path.join(output_folder, "prompt_example.txt")

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


def generate_prompt(reference_path=output_file_in):
    """
    Reads the reference.in file and generates a formatted prompt
    to use with generative AI models.
    """
    with open(reference_path, "r") as f:
        descriptions = [line.strip() for line in f.readlines() if line.strip()]

    if len(descriptions) != 10:
        raise ValueError(f"Expected 10 NL descriptions, found {len(descriptions)}")

    prompt = "Generate 10 Python functions starting from the following 10 natural language (NL) descriptions:\n\n"
    
    for i, desc in enumerate(descriptions, 1):
        prompt += f"{i}. {desc}\n"

    prompt += (
        "\nEach function should be generated in a single line, for a total of 10 lines.\n"
        "Different instructions of the same function should be separated by the special character \"\\n\".\n"
        "Do not use empty lines to separate functions.\n"
    )

    return prompt

prompt = generate_prompt(output_file_in)
with open(prompt_file_example, "w") as f:
    f.write(prompt)

print(prompt)
