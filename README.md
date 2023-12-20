# Telecom Customer Churn Service
#### Data was obtained from kaggle [🙁📡 Telecom Customer Churn Prediction](https://www.kaggle.com/datasets/shilongzhuang/telecom-customer-churn-by-maven-analytics)
### Problem Statement
The goal of the project is to identify customers that are at risk of churning. The dataset contains information about customers with a target label of indicating the status of the customer.
Identifying customers at risk of churning is essential for companies that provide services. Since the problem is to diferentiate among customers that Stayed, Churned or Joined, two classification models are trained and compared and the best performing model is chosen for training and prediction.

## Table of Contents

- [Project Structure](#projectstr)
- [Data](#data)
- [Running The Project](#run)
- [Deployment](#deploy)


## Project Structure
1. ReadME.md("https://github.com/sam47-asfaw/Churn-Service/edit/main/README.md"): contains all the information about the project.

2. notebook.ipynb("https://github.com/sam47-asfaw/Churn-Service/edit/main/notebook.ipynb"): contains the following  
 * Data ingestion and preparation
 * Exploratory Data Analysis
 * feature engineering and selection
 * model training, hyperparameter optimization and model selection

3. model_C=1.0.bin("https://github.com/sam47-asfaw/Churn-Service/edit/main/model_C=1.0.bin"): final model in pickle format
   
4. train.py("https://github.com/sam47-asfaw/Churn-Service/edit/main/train.py"): python script that trains the final selected model



5. predict.py("https://github.com/sam47-asfaw/Churn-Service/edit/main/predict.py"): flask api that serves the final result of model

6. requirements.txt("https://github.com/sam47-asfaw/Churn-Service/edit/main/requirements.txt"): file containing the required dependencies that have to be installed for the local enviroment

7. Dockerfile("https://github.com/sam47-asfaw/Churn-Service/edit/main/Dockerfile"): file with instruction on how to containerize the project.

8. test.py("https://github.com/sam47-asfaw/Churn-Service/edit/main/test.py"): script used to test the final model  

## Data
About dataset
  Identifying customers at risk of churning (leaving or discontinuing the use of a service) is crucial for service providers for several    reasons: revenue retention, customer lifetime value (CLV), customer acquisition costs (CAC), brand loyalty and reputation, operational 
  efficiency etc.
  
Contents
 This dataset contains 2 tables, in CSV format:
* Only one of the CSV files was used for the project. 
* The Customer Churn table contains information on all 7,043 customers from a Telecommunications company in California in Q2 2022
* Each record represents one customer, and contains details about their demographics, location, tenure, subscription services, status for the quarter (joined, stayed, or churned), and more!

## Running The Project
clone this repository:

