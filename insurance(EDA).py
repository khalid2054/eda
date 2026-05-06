import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from scipy.stats import pearsonr
from scipy.stats import chi2_contingency

df = pd.read_csv('insurance.csv')

# data info
print(df.head(10))
print(df.info())
print(df.describe())
print(df.shape)

# check null value
print(df.isna().sum())
print(df.duplicated().sum())
df.drop_duplicates(inplace=True)
print(df.duplicated().sum())
print(df.nunique())

# EDA - raw data (charges not yet transformed)
numeric_column = df[['age', 'bmi', 'children', 'charges']]

fig, axes = plt.subplots(2, 2, figsize=(12, 8))
axes = axes.flatten()

for i, col in enumerate(numeric_column.columns):  
    sns.histplot(numeric_column[col], bins=20, kde=True, ax=axes[i])
    axes[i].set_title(col)

plt.tight_layout()
plt.show()

sns.countplot(x=df['children'], data=df)
plt.show()
sns.countplot(x=df['sex'], data=df)
plt.show()
sns.countplot(x=df['smoker'], data=df)
plt.show()

# data processing
df_cleaned = df.copy() 

df_cleaned['charges'] = np.log(df_cleaned['charges']) 
sns.histplot(df_cleaned['charges'], bins=20, kde=True)
plt.show()



print(df_cleaned['sex'].value_counts())
df_cleaned['sex'] = df_cleaned['sex'].map({'male': 0, 'female': 1})

print(df_cleaned['smoker'].value_counts())
df_cleaned['smoker'] = df_cleaned['smoker'].map({'no': 0, 'yes': 1})

df_cleaned.rename(columns={'sex': 'is_female', 'smoker': 'is_smoker'}, inplace=True)

print(df_cleaned['region'].value_counts())
df_cleaned = pd.get_dummies(df_cleaned, columns=['region'], drop_first=True)
sns.histplot(df_cleaned['bmi'])
plt.show()

df_cleaned['bmi_category'] = pd.cut(
    df_cleaned['bmi'],
    bins=[0,18.5,24.5,29.5,float('inf')],
    labels= ['underweight' , 'normal', 'overweight', 'obesity']
)
df_cleaned = pd.get_dummies(df_cleaned, columns=['bmi_category'], drop_first=True)
df_cleaned=df_cleaned.astype(int)

# scikit learn
col = ['age' , 'bmi', 'children']
scaler = StandardScaler()
df_cleaned[col]= scaler.fit_transform(df_cleaned[col])
print(df_cleaned.columns.tolist())

# Pearson Correlation Calculation
selected_features = [
    'age', 'bmi', 'children', 'is_female', 'is_smoker',
    'region_northwest', 'region_southeast', 'region_southwest',
    'bmi_category_normal', 'bmi_category_overweight', 'bmi_category_obesity'
]


correlations = {
    feature: pearsonr(df_cleaned[feature], df_cleaned['charges'])[0]
    for feature in selected_features
}

correlation_df = pd.DataFrame(list(correlations.items()), columns=['Feature', 'Pearson Correlation'])
correlation_df.sort_values(by='Pearson Correlation', ascending=False)
print(correlation_df)

cat_features = [
    'is_female', 'is_smoker',
    'region_northwest', 'region_southeast', 'region_southwest',
    'bmi_category_normal', 'bmi_category_overweight', 'bmi_category_obesity'
]
alpha = 0.05

df_cleaned['charges_bin'] = pd.qcut(df_cleaned['charges'], q=4, labels=False, duplicates='drop')
chi2_results = {}

for col in cat_features:
    contingency = pd.crosstab(df_cleaned[col], df_cleaned['charges_bin'])
    chi2_stat, p_val, _, _ = chi2_contingency(contingency)
    decision = 'Reject Null (Keep Feature)' if p_val < alpha else 'Accept Null (Drop Feature)'
    chi2_results[col] = {
        'chi2_statistic': chi2_stat,
        'p_value': p_val,
        'Decision': decision
    }

chi2_df = pd.DataFrame(chi2_results).T
chi2_df =chi2_df.sort_values(by='p_value')
print(chi2_df)

final_df = df_cleaned[[
    'age', 'bmi', 'children',
    'is_smoker', 'bmi_category_obesity', 'bmi_category_overweight',
    'bmi_category_normal', 'region_southeast', 'is_female'
]]
print(final_df.head(10))
