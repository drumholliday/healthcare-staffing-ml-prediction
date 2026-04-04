<strong> **DO NOT DISTRIBUTE OR PUBLICLY POST SOLUTIONS TO THESE LABS. MAKE ALL FORKS OF THIS REPOSITORY WITH SOLUTION CODE PRIVATE. PLEASE REFER TO THE STUDENT CODE OF CONDUCT AND ETHICAL EXPECTATIONS FOR COLLEGE OF INFORMATION TECHNOLOGY STUDENTS FOR SPECIFICS. ** </strong>

# WESTERN GOVERNORS UNIVERSITY

## D797 - ARTIFICIAL INTELLIGENCE AND MACHINE LEARNING FOUNDATIONS FOR COMPUTER SCIENTISTS

Welcome to D797 Artificial Intelligence and Machine Learning Foundations for Computer Scientists!

For specific task instructions and requirements for this assessment, please refer to the course page.

## Project Overview

This project analyzes hospital staffing data to support workforce management decisions. Although the dataset does not directly include staff skill information, workforce demand and potential staffing gaps are inferred using Productive Hours per Adjusted Patient Day (PH/APD), which serves as an indicator of staffing workload and efficiency.
A **Random Forest Regressor** is used to model and predict staffing efficiency based on multiple factors such as productive hours, facility characteristics, and operational data.

---

## Dataset

The dataset used for this project is:

- `Hospital_Staffing_dataset.csv`

The dataset includes information such as:
- Year
- Facility Name
- County Name
- Type of Control
- Hours Type
- Productive Hours
- Productive Hours per Adjusted Patient Day (PH/APD)

---

## Data Preparation

The dataset was prepared using the following steps:

- Removed non-informative column (`Facility Number`)
- Handled missing values using data imputation
- Converted date fields into a numerical duration feature
- Encoded categorical variables using one-hot encoding
- Split data into training (80%) and testing (20%) sets

---

## Model

The model used in this project is:

- **Random Forest Regressor**

Key configuration:
- `n_estimators = 10` (reduced to improve runtime performance)
- `random_state = 3`

---

## Model Evaluation

The model was evaluated using:

- **Mean Squared Error (MSE)**
- **R2 Score**

Example output: 
```
Model Evaluation:
MSE: 5.2999
R2: 0.7732
```
---
## How to Run the Project

1. Navigate to the project directory
2. Ensure the dataset is located in the `data/` folder
3. Run the following command: 
`python main.py`

## Final Notes

- This project focuses on building and explaining a machine learning model rather than optimizing multiple models.
- "PH/APD" is used as a proxy measure for staffing efficiency and workload demand.