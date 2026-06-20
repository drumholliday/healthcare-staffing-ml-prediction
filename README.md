# Healthcare Staffing ML Prediction

## Overview

Healthcare Staffing ML Prediction is a machine learning project that analyzes hospital staffing data to support workforce planning and operational decision-making. The project uses staffing, facility, and productivity data to predict **Productive Hours per Adjusted Patient Day (PH/APD)**, a metric that can help indicate staffing workload, efficiency, and potential resource demand.

A **Random Forest Regressor** is used to model relationships between hospital staffing features and PH/APD values. The project demonstrates data preprocessing, feature engineering, supervised machine learning, model evaluation, and interpretation in a healthcare operations context.

## Project Purpose

The purpose of this project is to explore how machine learning can be applied to healthcare staffing analysis.

The project is designed to:

* Analyze hospital staffing and productivity data
* Prepare raw healthcare operations data for machine learning
* Use PH/APD as a proxy measure for staffing efficiency and workload demand
* Train a regression model to predict staffing-related outcomes
* Evaluate model performance using standard regression metrics
* Provide a foundation for future healthcare workforce prediction tools

## Dataset

The dataset used for this project is:

```text
Hospital_Staffing_dataset.csv
```

The dataset includes healthcare staffing and facility information such as:

* Year
* Facility name
* County name
* Type of control
* Hours type
* Productive hours
* Productive hours per adjusted patient day
* Facility and operational attributes

## Target Variable

The target variable for this project is:

```text
Productive Hours per Adjusted Patient Day (PH/APD)
```

PH/APD is used as an indicator of staffing workload and efficiency. Although the dataset does not directly include detailed staff skill or role information, PH/APD provides a useful measure for analyzing staffing demand relative to patient activity.

## Data Preparation

The dataset was prepared for machine learning using the following steps:

1. Loaded the hospital staffing dataset from a CSV file.
2. Removed non-informative or unnecessary columns.
3. Handled missing values using data imputation.
4. Converted date or time-related values into usable numerical features.
5. Encoded categorical variables using one-hot encoding.
6. Split the dataset into training and testing sets.
7. Prepared feature columns and target values for model training.

## Machine Learning Model

The model used in this project is:

```text
Random Forest Regressor
```

A Random Forest Regressor was selected because it can model nonlinear relationships, handle mixed feature types after preprocessing, and reduce overfitting by combining predictions from multiple decision trees.

## Model Configuration

Example model configuration:

```python
RandomForestRegressor(
    n_estimators=10,
    random_state=3
)
```

The number of estimators was kept relatively small to improve runtime performance during development and testing.

## Model Evaluation

The model was evaluated using standard regression metrics:

### Mean Squared Error

Mean Squared Error measures the average squared difference between predicted and actual values. Lower values indicate better performance.

### R2 Score

The R2 score measures how well the model explains variation in the target variable. Higher values generally indicate better model fit.

Example output:

```text
Model Evaluation:
MSE: 5.2999
R2: 0.7732
```

Actual results may vary depending on the dataset version, preprocessing steps, and model configuration.

## Technologies Used

* Python
* pandas
* NumPy
* scikit-learn
* Random Forest Regression
* CSV data processing
* Git
* GitHub

## Project Structure

```text
healthcare-staffing-ml-prediction/
├── data/
│   └── Hospital_Staffing_dataset.csv
│
├── main.py
├── README.md
└── requirements.txt
```

The exact file structure may vary depending on the current version of the project.

## How to Run the Project

### Prerequisites

Make sure Python is installed. This project also requires common data science libraries such as pandas and scikit-learn.

If a `requirements.txt` file is included, install dependencies with:

```bash
pip install -r requirements.txt
```

### Run the Program

From the project root directory, run:

```bash
python main.py
```

Depending on your Python environment, you may need to use:

```bash
python3 main.py
```

## Expected Output

The program trains the machine learning model and prints evaluation results such as:

```text
Model Evaluation:
MSE: 5.2999
R2: 0.7732
```

The output may also include information about data loading, preprocessing, model training, and prediction results.

## Interpretation

This project uses PH/APD as a proxy for staffing efficiency and workload demand. A lower or higher PH/APD value may suggest differences in staffing intensity, productivity, or patient care workload depending on the facility context.

The model is intended for learning and exploratory analysis. It should not be used as a production healthcare staffing decision system without additional validation, domain review, and compliance evaluation.

## Portfolio Highlights

This project demonstrates experience with:

* Data cleaning and preprocessing
* Feature engineering
* One-hot encoding categorical variables
* Regression modeling
* Random Forest machine learning
* Model evaluation with MSE and R2
* Healthcare operations analysis
* Python data science workflows
* Git and GitHub version control

## Future Enhancements

Possible future improvements include:

* Add additional regression models for comparison
* Tune Random Forest hyperparameters
* Add cross-validation
* Add feature importance analysis
* Add data visualizations
* Add model performance charts
* Add exploratory data analysis notebooks
* Add a dashboard for staffing predictions
* Add a Flask or FastAPI backend
* Add a frontend for uploading datasets and viewing predictions
* Improve documentation around assumptions and limitations

## Academic and Portfolio Note

This project was created for academic learning and portfolio development. It demonstrates foundational machine learning concepts, healthcare data analysis, supervised regression modeling, and model evaluation.

If this repository contains coursework-derived solution code or restricted lab materials, it should be kept private and used only in accordance with applicable academic integrity and code of conduct expectations.

## Author

Drum Holliday

## License

This project is currently for educational and portfolio purposes. A formal license can be added later if the project is prepared for public reuse.
