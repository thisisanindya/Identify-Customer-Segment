# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 00:33:17 2021

@author: Anindya Chaudhuri
"""


# import libraries here; add more as necessary
import numpy as np
import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

def clean_data(azdias):
    """
    Perform feature trimming, re-encoding, and engineering for demographics
    data
    
    INPUT: Demographics DataFrame
    OUTPUT: Trimmed and cleaned demographics DataFrame
    """
    
    # Put in code here to execute all main cleaning steps:
    # convert missing value codes into NaNs, ...
    from IPython.display import display
   
    # Load in the feature summary file.
    feat_info = pd.read_csv("AZDIAS_Feature_Summary.csv", delimiter = ";")
    
    total_features = feat_info.shape[0]
    for feature_no in range(total_features):
        feature_name = azdias.columns[feature_no]
        values_for_missing_or_unknown = feat_info.iloc[feature_no, 3]
        values_for_missing_or_unknown = values_for_missing_or_unknown[1:-1].split(',')
        if (values_for_missing_or_unknown == ['']):
            continue
        else:
            for missing_value in values_for_missing_or_unknown:
                if azdias[feature_name].dtype =='object':
                    azdias.loc[azdias[feature_name]==missing_value,feature_name] = np.nan 
                else:   
                    missing_value = int(missing_value)
                    azdias.loc[azdias[feature_name]==missing_value,feature_name] = np.nan 
    
    # Write it to a file for future purpose            
    azdias.to_csv('azdias_NaN.csv')
    
    
    # select, re-encode, and engineer column values.
    print(feat_info['type'].value_counts())
    
    # Assess categorical variables: which are binary, which are multi-level, and
    # which one needs to be re-encoded?
    print()
    all_category = feat_info[feat_info['type'] == 'categorical']['attribute'].values
    print("All Category = ", all_category)
    
    print()
    categorical_features = [x for x in all_category if x in azdias.columns]
    print("Categorical Features = ", categorical_features)
    
    print()
    binary_categorical_features = [x for x in categorical_features if azdias[x].nunique()==2]
    print("Binary Categorical Features = ", binary_categorical_features)
    
    print()
    multilevel_categorical_features = [x for x in categorical_features if azdias[x].nunique() > 2]
    print("Multilevel Categorical Features = ", multilevel_categorical_features)
    
    print()
    print(azdias[binary_categorical_features])
    
    print()
    print(azdias[multilevel_categorical_features])
    
    
    print("Summary of Unique Categorical Features =\n", azdias[categorical_features].nunique())
    
    # Re-encode categorical variable(s) to be kept in the analysis.
    
    # A. Convert non-numeric binary value to numeric ones - OST_WEST_KZ
    
    azdias.loc[azdias['OST_WEST_KZ']=='W','OST_WEST_KZ']=0
    azdias.loc[azdias['OST_WEST_KZ']=='O','OST_WEST_KZ']=1
    
    
    # B. Drop the feture CAMEO DEU_2015 which has 44 unique values which is too
    # many for one feature
    multilevel_categorical_features.remove('CAMEO_DEU_2015')
    azdias.drop('CAMEO_DEU_2015', axis=1, inplace=True)
    
    # C. Convert multi-level category into dummy variables 
    for column in multilevel_categorical_features:
        data = azdias[column][azdias[column].notnull()]
        dummies = pd.get_dummies(data, prefix=column)
        azdias = azdias.join(dummies)
        azdias.drop([column], axis=1, inplace=True)
        
    print()
    print("Finished Re-encoding Categorical Variables... ")
    all_columns = azdias.head()
    for i, column in enumerate(all_columns):
        print(i+1, column)
    
    
    # Investigate "PRAEGENDE_JUGENDJAHRE" and engineer two new variables.
    mixed_features = feat_info[feat_info['type'] == 'mixed']['attribute'].values
    mixed_featues_azdias = [x for x in mixed_features if x in azdias.columns] 
    
    # MAINSTREAM and AVANTGRADE information of PRAEGENDE_JUGENDJAHRE feature from 
    # data dictionary
    MAINSTREAM = [1, 3, 5, 8, 10, 12, 14]
    AVANTGRADE = [2, 4, 6, 7, 9, 11, 13, 15]
    
    def what(type):
        if type in MAINSTREAM:
            return 1
        elif type in AVANTGRADE:
            return 0
        else:
            return type
    
    azdias['PRAEGENDE_JUGENDJAHRE_MAINSTREAM'] = azdias['PRAEGENDE_JUGENDJAHRE'].apply(what)
    # print(azdias['PRAEGENDE_JUGENDJAHRE_MAINSTREAM'])
    
    # variable mapping for decade
    count = [count+1 for count in range(15)]
    years = [40, 40, 50, 50, 60, 60, 60, 70, 70, 80, 80, 80, 80, 90, 90]
    decade = pd.Series(years, index = count)
    azdias['PRAEGENDE_JUGENDJAHRE_DECADE'] = azdias['PRAEGENDE_JUGENDJAHRE'].map(decade)
    
    print()
    print("Done with PRAEGENDE_JUGENDJAHRE Feature...")
    all_columns = azdias.head()
    for i, column in enumerate(all_columns):
        print(i+1, column)
        
                                                                                
    # Investigate "CAMEO_INTL_2015" and engineer two new variables.
    azdias.loc[azdias['CAMEO_INTL_2015'].notnull(),'CAMEO_INTL_2015_WEALTH'] = azdias.loc[azdias['CAMEO_INTL_2015'].notnull(),'CAMEO_INTL_2015'].map(lambda x:int(str(x)[0]))
    azdias.loc[azdias['CAMEO_INTL_2015'].notnull(),'CAMEO_INTL_2015_LIFESTAGE'] = azdias.loc[azdias['CAMEO_INTL_2015'].notnull(),'CAMEO_INTL_2015'].map(lambda x:int(str(x)[1]))
    
    # Remove all mixed variables
    azdias.drop(mixed_featues_azdias, axis=1, inplace=True)
    
    print()
    print("After Removing Mixed Features... ")
    all_columns = azdias.head()
    for i, column in enumerate(all_columns):
        print(i+1, column)
    # Return the cleaned dataframe.
    
    return azdias 


# Load in the general demographics data.
azdias = pd.read_csv("Udacity_AZDIAS_Subset.csv", delimiter = ";")
clean_data(azdias)

print()
# Load in the general demographics data.
customers = pd.read_csv('Udacity_CUSTOMERS_Subset.csv',sep=';')
customers=clean_data(customers)
