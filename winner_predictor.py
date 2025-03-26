import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
import xgboost as xgb
import joblib

# Load the datasets
fights_data = pd.read_csv('./datasets/fights_data.csv')
fighters_data = pd.read_csv('./datasets/fighters_data.csv')

# Drop unnecessary columns
fights_data = fights_data.drop(columns=['event_name', 'method', 'round_num', 'time'])
fighters_data = fighters_data.drop(columns=['height_cm', 'weight_kg', 'reach_cm'])

# Drop rows with missing values in both datasets
fights_data.dropna(inplace=True)
fighters_data.dropna(inplace=True)

# Merge the two datasets on fighter names
data_merged = pd.merge(fights_data, fighters_data, left_on='fighter_1', right_on='name', suffixes=('_1', '_fighter_1'))
data_merged = pd.merge(data_merged, fighters_data, left_on='fighter_2', right_on='name', suffixes=('_1', '_fighter_2'))

# Create the target variable: 'winner' (1 for fighter 1, 0 for fighter 2)
winner_bin = []
for i in range(len(data_merged['winner'])):
    if data_merged['winner'][i] == data_merged['fighter_1'][i]:
        winner_bin.append(1)
    elif data_merged['winner'][i] == data_merged['fighter_2'][i]:
        winner_bin.append(0)
    else:
        # In case of draws or no contest
        winner_bin.append(0.5)
data_merged['winner_label'] = winner_bin

# Drop the 'winner' column after creating the target
data_merged = data_merged.drop(columns=['winner'])

# Feature selection:
features = ['strikes_per_min_1', 'striking_accuracy_1', 'takedown_avg_1', 'takedown_accuracy_1', 'takedown_defense_1', 'submission_avg_1',
            'strikes_per_min_fighter_2', 'striking_accuracy_fighter_2', 'takedown_avg_fighter_2', 'takedown_accuracy_fighter_2',
            'takedown_defense_fighter_2', 'submission_avg_fighter_2']

X = data_merged[features]
y = data_merged['winner_label']

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Feature scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Model training and evaluation
models = {
    "Logistic Regression": LogisticRegression(max_iter=1000),
    "Random Forest": RandomForestClassifier(),
    "XGBoost": xgb.XGBClassifier(eval_metric='mlogloss')
}

# Store results
results = {}

for model_name, model in models.items():
    model.fit(X_train_scaled, y_train)
    y_pred = model.predict(X_test_scaled)
    accuracy = accuracy_score(y_test, y_pred)
    results[model_name] = {
        'accuracy': accuracy,
        'classification_report': classification_report(y_test, y_pred)
    }

# Display results
for model_name, result in results.items():
    print(f"{model_name} - Accuracy: {result['accuracy']}")
    print(result['classification_report'])

# pickle the most accurate model
joblib.dump(models['Logistic Regression'], 'logistic_model.pkl')
joblib.dump(scaler, 'scaler.pkl')

