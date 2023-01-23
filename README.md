## Identify Customer Segment
## Project Overview
### In this project, we need to work with real-life data provided by Bertelsmann partners AZ Direct and Arvato Finance Solution. The data here concerns a company that performs mail-order sales in Germany. Their main question of interest is to identify facets of the population that are most likely to be purchasers of their products for a mailout campaign. The main job will be to use unsupervised learning techniques to organize the general population into clusters, then use those clusters to see which of them comprise the main user base for the company. Prior to applying the machine learning methods, it is required to assess and clean the data in order to convert the data into a usable form.

## Install
### This project uses Python 3 and is designed to be completed through the Jupyter Notebooks IDE. The following libraries are used in this project:

### NumPy
### pandas
### Sklearn / scikit-learn
### Matplotlib (for data visualization)
### Seaborn (for data visualization) 

## Methodology Used 
### Step 0: Load the Data
#### There are four files associated with this project (not including this one): 
#### 1. Udacity_AZDIAS_Subset.csv: Demographics data for the general population of Germany; 891211 persons (rows) x 85 features (columns).
#### 2. Udacity_CUSTOMERS_Subset.csv: Demographics data for customers of a mail-order company; 191652 persons (rows) x 85 features (columns).
#### 3. Data_Dictionary.md: Detailed information file about the features in the provided datasets.
#### 4. AZDIAS_Feature_Summary.csv: Summary of feature attributes for demographics data; 85 features (rows) x 4 columns

### Step 1: Preprocessing
### Step 1.1: Assess Missing Data
#### Step 1.1.1: Convert Missing Value Codes to NaNs
#### Step 1.1.2: Assess Missing Data in Each Column
#### Step 1.1.3: Assess Missing Data in Each Row

### Step 1.2: Select and Re-Encode Features
#### Step 1.2.1: Re-Encode Categorical Features
#### Step 1.2.2: Engineer Mixed-Type Features 
#### Step 1.2.3: Complete Feature Selection

### Step 1.3: Create a Cleaning Function

### Step 2: Feature Transformation
### Step 2.1: Apply Feature Scaling
### Step 2.2: Perform Dimensionality Reduction
### Step 2.3: Interpret Principal Components

### Step 3: Clustering
### Step 3.1: Apply Clustering to General Population
### Step 3.2: Apply All Steps to the Customer Data
### Step 3.3: Compare Customer Data to Demographics Data

## Acknowledgements
### Dataset Credit - AZ Direct GMBH
### Others: Thanks to Udacity for excellent course material and also to the mentors for timely help.
