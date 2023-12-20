import pickle

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold

from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import OrdinalEncoder
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import roc_auc_score
from sklearn.metrics import mutual_info_score
from sklearn.metrics import f1_score

import warnings
warnings.filterwarnings('ignore')

# read and display general information about the dataset
df = pd.read_csv('telecom_customer_churn.csv')

df.columns = df.columns.str.lower().str.replace(' ', '_')
num_types = ['int64', 'float64']
numeric = list(df.select_dtypes(include=num_types))
for col in numeric:
    df[col].fillna(value=df[col].mean(), inplace=True)


categorical = list(df.select_dtypes(include='O'))
for col in categorical:
    most_occurring_word = df[col].mode()[0]
    df[col] = df[col].fillna(most_occurring_word)


encoder = OrdinalEncoder()
df['customer_status'] = encoder.fit_transform(df[['customer_status']])
df['customer_status'].value_counts(normalize=True)

# Split the Dataset into train and test
SEED = 42
df_full_train, df_test = train_test_split(df, test_size=0.2, random_state=SEED)

df_full_train = df_full_train.reset_index(drop=True)

# final features selected
numeric =  [ 'age',
 'number_of_dependents',
 'zip_code',
 'latitude',
 'longitude',
    'number_of_dependents',
    'number_of_referrals',
    'tenure_in_months',
    'monthly_charge',
    'total_charges',
    'total_refunds',
    'total_long_distance_charges',
    'total_revenue'
]

categorical = [
    'gender',
    'married',
    'city',
    'churn_reason',
    'churn_category',
    'city',
    'contract',
    'offer', 
    'internet_service',
    'device_protection_plan',
    'premium_tech_support',
    'streaming_tv',
    'streaming_movies',
    'streaming_music',
    'unlimited_data',
    'paperless_billing',
    'payment_method',
]

def train(data, y,model):
    dicts = data[categorical + numeric].to_dict(orient='records')

    dv = DictVectorizer(sparse=True)
    X_train = dv.fit_transform(dicts)

    m = model.fit(X_train, y)

    return dv, m

def predict(data, dv, model):
    dicts = data[categorical + numeric].to_dict(orient='records')

    X = dv.transform(dicts)

    y_pred_prob = model.predict_proba(X)

    return y_pred_prob


rf = RandomForestClassifier(
                max_depth=20,
                  n_estimators=20, 
                  min_samples_leaf=2,
                  random_state=1)
dv, model = train(df_full_train, df_full_train.customer_status,rf)
y_pred = predict(df_test, dv, model)


roc_auc = roc_auc_score(df_test.customer_status, y_pred_prob, average='micro', multi_class= 'ovr')  
print(f"ROC AUC Score: {roc_auc}")

output_file = f'model_C={1.0}.bin'
output_file


f_out = open(output_file, 'wb')
pickle.dump((dv,rf), f_out)
f_out.close()

