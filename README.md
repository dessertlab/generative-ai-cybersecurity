# Generative AI in Cybersecurity: Generating Offensive Code from Natural Language

This repository contains the materials and scripts for the talk titled **"Generative AI in Cybersecurity: Generating Offensive Code from Natural Language"** by Pietro Liguori, University of Naples Federico II, DESSERT group. The talk is part of **ARTISAN 2024: Summer School on the role and effects of ARTificial Intelligence in Secure ApplicatioNs**.

## Python Setup

Ensure you have Python installed on your system. If not, you can use a virtual environment with Anaconda to avoid working directly on your machine. Follow the steps below:

### Anaconda Installation

1. **Install Anaconda3**:
    - Ensure you have Anaconda3 installed. If not, you can download the installer from [here](https://repo.anaconda.com/archive/Anaconda3-2021.05-Linux-x86_64.sh).
    - Use the `wget` command to download the installer:
      ```bash
      wget https://repo.anaconda.com/archive/Anaconda3-2021.05-Linux-x86_64.sh
      ```
    - Make the installer executable:
      ```bash
      chmod +x Anaconda3-2021.05-Linux-x86_64.sh
      ```
    - Run the installer:
      ```bash
      bash Anaconda3-2021.05-Linux-x86_64.sh
      ```
    - You may need to add the Anaconda directory to the PATH environment variable. For example, add this line to your `bashrc` file:
      ```bash
      export PATH="/path_to_anaconda/anaconda3/bin:$PATH"
      ```

### Creating the Virtual Environment

2. **Create a Python 3.9 virtual environment**:
    - Create a virtual environment using the command:
      ```bash
      conda create -n yourenvname python=3.9
      ```
      Replace `yourenvname` with your desired environment name.

3. **Activate the environment**:
    - Activate the created environment with the command:
      ```bash
      source activate yourenvname
      ```

You are now ready to install dependencies and work within your virtual environment.



## Part 1: Automatic Code Generation and Evaluation

### Description

In the `Violent-Python-functions` folder, we have `.in` and `.out` files containing the NL (Natural Language) descriptions and the corresponding Python functions, respectively.

### Extracting a Subset

Now, we will extract a random subset of 10 samples from this dataset.

1. **Run the script**:
    - In the main directory, run the `create_subset.py` script with the following command:
      ```bash
      python create_subset.py
      ```

2. **Results**:
    - The script will create a `results` folder containing `subset.in` and `subset.out` files.
    - The `subset.in` file contains the 10 randomly extracted NL descriptions.
    - The `subset.out` file contains the corresponding 10 Python functions and serves as our ground truth for evaluation.

### Generating Outputs with AI Models

Next, you will generate 10 outputs using generative AI models like [ChatGPT](https://chat.openai.com/) and [Claude Sonnet](https://www.anthropic.com/index/introducing-claude).

> [!CAUTION]
> Pay attention to the structure of the code snippets. As you can see, the Python codes are all *single-line*. In fact, multi-line instructions are separated from each other with `\n`.

3. **Generate Outputs**:
    - Use the NL descriptions stored in the `subset.in` file to generate the 10 outputs using the AI models.
    - Ensure the AI models generate the outputs line by line as required for the evaluation.
    - Save the model outputs in a file named `output.out` in the `results` folder.
    - Make sure the model has generated the code in single-line format (with multi-line instructions separated by `\n`).

    Example prompt:
    ```plaintext
    Generate Python functions corresponding to the following NL descriptions.

    Generate the functions, one per line. The functions should be single-line, i.e., if there are multi-line instructions, they should be separated by the \n character. Do not use empty lines to separate the outputs. 

    1. [NL description]
    2. [NL description]
    ...
    10. [NL description]
    ```

4. **Install Dependencies**:
    - Before running the script to calculate similarity metrics, install the required dependencies using:
      ```bash
      pip install -r requirements.txt --user
      ```

5. **Calculate Similarity Metrics**:
    - In the main directory, run the script `output_similarity_metrics` to calculate the output similarity metrics between the model predictions (`output.out`) and the ground truth reference (`subset.out`):
      ```bash
      python output_similarity_metrics.py
      ```

Follow these steps to ensure that your generated outputs are correctly formatted and evaluated against the ground truth in `subset.out`.


## Part 2: Prompt Engineering

### Description

In this part, we will repeat the code generation process using the AI models, but this time applying a prompt engineering technique discussed during the talk. The goal is to observe if this technique improves the quality of the generated code.

### Steps

1. **Apply Prompt Engineering**:
    - Use the same NL descriptions stored in the `subset.in` file.
    - Modify your prompts according to the prompt engineering techniques learned during the talk.

    Example prompt:
    ```plaintext
    Generate Python functions corresponding to the following NL descriptions.

    Generate the functions, one per line. The functions should be single-line, i.e., if there are multi-line instructions, they should be separated by the \n character. Do not use empty lines to separate the outputs.

    1. [NL description]
    2. [NL description]
    ...
    10. [NL description]
    ```

    Examples of prompts can be found in the `prompt_examples` folder.

2. **Generate Outputs**:
    - Generate the 10 outputs using the AI models with the engineered prompts.
    - Save the model outputs in a file named `output_prompt_pattern.out` in the `results` folder, where `prompt_pattern` is the name of the pattern used (e.g., persona, few-shot).
    - Ensure the model has generated the code in single-line format (with multi-line instructions separated by `\n`).

3. **Calculate Similarity Metrics**:
    - In the main directory, open the script `output_similarity_metrics.py`.
    - Update the `file_hypes` variable to `output_prompt_pattern.out`.
    - Update the `output_filename` variable from `subset_output.txt` to `subset_output_prompt_pattern.txt`.
    - Run the script to calculate the output similarity metrics between the model predictions (`output_prompt_pattern.out`) and the ground truth reference (`subset.out`):
      ```bash
      python output_similarity_metrics.py
      ```

4. **Compare Results**:
    - Execute the script `plot_metrics_comparison.py` to compare the results:
      ```bash
      python plot_metrics_comparison.py
      ```
    - The script reads the metric values from the files `subset_output.txt` and `subset_output_prompt_pattern.txt` and creates bar charts to visualize the differences between the metrics.

Follow these steps to apply prompt engineering and evaluate its impact on the code generation quality.



## Credits

This repository and the materials were developed by:

- Alessio Foggia (alessio.foggia@unina.it)
- Cristina Improta (cristina.improta@unina.it)
- Pietro Liguori (pietro.liguori@unina.it)
