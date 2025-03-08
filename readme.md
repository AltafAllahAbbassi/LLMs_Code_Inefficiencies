
## Replication Package: A Taxonomy of Inefficiencies in LLM-Generated Code

This repository contains the replication package for our study "A Taxonomy of Inefficiencies in LLM-Generated Code." It includes datasets, survey materials, figures, and scripts used in our analysis.

  

📂 Repository Structure

1. ***Dataset***
- data/: Contains the labeled dataset of inefficient LLM-generated code.
- data/raw_data/: Includes the original unprocessed code generated by models.
- data/ineff_dataset.csv: Provides the labelled generated-codes with existing inefficiencies.

2. ***Survey***
- /survey/: Contains the survey used to evaluate our taxonomy: (i) The survey form (ii) Anonymized survey responses.

3. ***Figures***
We provide visual representations related to our study, including: (i) The taxonomy of inefficiencies (ii) Co-occurrence heat maps matrices, both per model and across models.

4. **Scripts**
The repository also includes scripts used in our study for:
- Extracting users who use LLM-generated code (extract_users.py).
- Generating code from models (generate_code.py).
- Judging code inefficiencies (judger.py).
- Analyzing the dataset and survey responses (ineffEval_analysis.ipynb and survey_results_analysis.ipynb).



📌 *For further details, please refer to our paper: A Taxonomy of Inefficiencies in LLM-Generated Code.*