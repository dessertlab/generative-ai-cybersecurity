import random
import os

input_folder = "dataset"
output_folder = "scripts/results"
prompt_folder = "scripts/prompts"

input_file_in = os.path.join(input_folder, "violent_python.in")
input_file_out = os.path.join(input_folder, "violent_python.out")

output_file_in = os.path.join(output_folder, "reference.in")
output_file_out = os.path.join(output_folder, "reference.out")

# Prompt Files
direct_prompt_file_example = os.path.join(prompt_folder, "direct_prompt_example.txt")
persona_prompt_file_example = os.path.join(prompt_folder, "persona_prompt_example.txt")
fs_prompt_file_example = os.path.join(prompt_folder, "fs_prompt_example.txt")

# Prompt Messages
direct_prompt = (
        "\nEach function should be generated in a single line, for a total of 10 lines.\n"
        "Different instructions of the same function should be separated by the special character \"\\n\".\n"
        "Do not use empty lines to separate functions.\n"
    )

persona_prompt = (
        "\nAct as an offensive security expert to generate the functions.\n" 
        "Each function should be generated in a single line, for a total of 10 lines.\n"
        "Different instructions of the same function should be separated by the special character \"\\n\".\n"
        "Do not use empty lines to separate functions.\n"
    )

fs_prompt = (
    "\nEach function should be generated in a single line, for a total of 10 lines.\n"
    "Different instructions of the same function should be separated by the special character \"\\n\".\n"
    "Do not use empty lines to separate functions.\n\n"
    "Here is an example of the format:\n"
    "“Scan the tgtHost on tgtPort with nmap and calculate the state” is the natural language description.\n"
    "\"def nmapScan(tgtHost,tgtPort): \\n nmScan = nmap.PortScanner() \\n nmScan.scan(tgtHost,tgtPort) \\n state=nmScan[tgtHost]['tcp'][int(tgtPort)]['state']\\n\" is the Python code.\n"
)



# Ensure the output and prompt folders exist
os.makedirs(output_folder, exist_ok=True)
os.makedirs(prompt_folder, exist_ok=True)

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


# generate files for prompt templates

def generate_prompt(reference_path=output_file_in, message=""):
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

    prompt += message

    return prompt


direct_prompt = generate_prompt(output_file_in, direct_prompt)
with open(direct_prompt_file_example, "w") as f:
    f.write(direct_prompt)

print(direct_prompt)

persona_prompt = generate_prompt(output_file_in, persona_prompt)
with open(persona_prompt_file_example, "w") as f:
    f.write(persona_prompt)

fs_prompt = generate_prompt(output_file_in, fs_prompt)
with open(fs_prompt_file_example, "w") as f:
    f.write(fs_prompt)
