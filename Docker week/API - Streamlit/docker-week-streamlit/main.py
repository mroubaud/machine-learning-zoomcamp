import streamlit as st
import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score

st.title("Random Forest Model for Classification")

st.write("""Explore different hyperparameter and train a random forest model 
         in order to detect breast cancer""")

data = datasets.load_breast_cancer()
columns = data.feature_names
X=data.data
X=pd.DataFrame(data=X, columns = columns)
y=data.target

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.20, random_state=42)

def add_parameter_ui():
    params = dict()
    n_estimators = st.sidebar.slider('n_estimators', 1, 200)
    params['n_estimators'] = n_estimators
    max_depth = st.sidebar.slider('max_depth', 2, 15)
    params['max_depth'] = max_depth
    bootstrap = st.sidebar.selectbox('Use bootstrap?', ("Yes", "No"))
    if (bootstrap == "Yes"):
        bootstrap=True
    elif (bootstrap=="No"):
        bootstrap=False
    params['bootstrap'] = bootstrap
    return params

params = add_parameter_ui()
n_features = len(columns)

rfm = RandomForestClassifier(n_estimators=params["n_estimators"],
                             max_depth=params["max_depth"],
                             max_features=np.sqrt(n_features).astype(int),
                             bootstrap=params["bootstrap"])

rfm.fit(X_train, y_train)
y_preds = rfm.predict(X_test)

accuracy = np.round(accuracy_score(y_test, y_preds),2)
recall = np.round(recall_score(y_test, y_preds),2)
precision = np.round(precision_score(y_test, y_preds),2)
f1 = np.round(f1_score(y_test, y_preds),2)

st.write(f'Rando Forest Params = {params}')
st.write(f'Accuracy =', accuracy)
st.write(f'recall =', recall)
st.write(f'precision =', precision)
st.write(f'f1 =', f1)