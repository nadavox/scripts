how to create a virtual environment for the diffrenet scripts:

### Step 1: Install Anaconda

Download and install Anaconda from the [official website](https://www.anaconda.com/products/individual) to ensure you have all the necessary tools and packages to run this application.

### Step 2: Create a New Environment

Open your terminal or command prompt and create a new virtual environment specifically for this project by running:

```bash
conda create --name script_{name_of_the_sscript}_venv python=3.11
```

This command creates a new Conda environment named `script_{name_of_the_sscript}_venv` with Python 3.11.

### Step 3: Activate the Environment

Activate the newly created environment with:

```bash
conda activate {name_of_the_sscript}_venv
```

### Step 4: Deactivate the Environment
```bash
conda deactivate
```

### delete the environment

deactivate the environment and then run the following command
```bash
conda env remove --name {name_of_the_sscript}_venv

```

### Note:
Before proceeding to install the required packages, ensure you are using the correct pip associated with your virtual environment. Run:

```bash
where pip
```

a list of all the environments:
```bash
conda env list
```