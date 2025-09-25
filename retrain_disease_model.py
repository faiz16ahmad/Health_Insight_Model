import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import joblib

# Load the training data
train_data = pd.read_csv('data/Training.csv')

# Separate features and target
X = train_data.drop(['prognosis'], axis=1)
y = train_data['prognosis']

# Create and train the random forest classifier
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X, y)

# Save the model
joblib.dump(rf_model, 'models/randomforest_disease_pred.pkl')
print("Disease prediction model retrained and saved successfully!")