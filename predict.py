import pandas as pd
import joblib
import warnings

# Load the saved model and scaler
logistic_model = joblib.load('logistic_model.pkl')
scaler = joblib.load('scaler.pkl')

# Load fighters data
fighters_data = pd.read_csv('./datasets/fighters_data.csv')

# Input: Names of the two fighters
fighter_1_name = "Nathaniel Wood"
fighter_2_name = "Morgan Charriere"

# Extract stats for each fighter
fighter_1 = fighters_data[fighters_data['name'] == fighter_1_name]
fighter_2 = fighters_data[fighters_data['name'] == fighter_2_name]

# Check if both fighters are found
if fighter_1.empty or fighter_2.empty:
    print("One or both fighters not found in the data. Please check the names.")
else:
    # Take the first match (if multiple entries exist)
    fighter_1 = fighter_1.iloc[0]
    fighter_2 = fighter_2.iloc[0]

    # Create feature vector as used during training
    feature_vector = [
        fighter_1['strikes_per_min'],
        fighter_1['striking_accuracy'],
        fighter_1['takedown_avg'],
        fighter_1['takedown_accuracy'],
        fighter_1['takedown_defense'],
        fighter_1['submission_avg'],
        fighter_2['strikes_per_min'],
        fighter_2['striking_accuracy'],
        fighter_2['takedown_avg'],
        fighter_2['takedown_accuracy'],
        fighter_2['takedown_defense'],
        fighter_2['submission_avg']
    ]

    # Scale the feature vector using saved scaler
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", category=UserWarning) # dont print warning to console
        feature_vector_scaled = scaler.transform([feature_vector])
    
    # Predict winner (1 = fighter_1, 0 = fighter_2)
    prediction = logistic_model.predict(feature_vector_scaled)

    print(f'{fighter_1_name} vs {fighter_2_name}:')
    print('------------')
    # Show result
    if prediction[0] == 1:
        print(f"{fighter_1_name} is predicted to win!")
    else:
        print(f"{fighter_2_name} is predicted to win!")
