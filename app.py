from flask import Flask, render_template, request, jsonify
import pandas as pd
import joblib
import warnings

app = Flask(__name__)

# Load the saved model and scaler
logistic_model = joblib.load('logistic_model.pkl')
scaler = joblib.load('scaler.pkl')

# Load fighters data
fighters_data = pd.read_csv('./datasets/fighters_data.csv')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    fighter_1_name = data.get('fighter_1')
    fighter_2_name = data.get('fighter_2')

    fighter_1 = fighters_data[fighters_data['name'] == fighter_1_name]
    fighter_2 = fighters_data[fighters_data['name'] == fighter_2_name]

    if fighter_1.empty or fighter_2.empty:
        return jsonify({'error': 'One or both fighters not found in the data.'}), 400

    fighter_1 = fighter_1.iloc[0]
    fighter_2 = fighter_2.iloc[0]

    feature_vector = [
        fighter_1['strikes_per_min'], fighter_1['striking_accuracy'], fighter_1['takedown_avg'],
        fighter_1['takedown_accuracy'], fighter_1['takedown_defense'], fighter_1['submission_avg'],
        fighter_2['strikes_per_min'], fighter_2['striking_accuracy'], fighter_2['takedown_avg'],
        fighter_2['takedown_accuracy'], fighter_2['takedown_defense'], fighter_2['submission_avg']
    ]

    with warnings.catch_warnings():
        warnings.simplefilter("ignore", category=UserWarning)
        feature_vector_scaled = scaler.transform([feature_vector])

    prediction = logistic_model.predict(feature_vector_scaled)
    winner = fighter_1_name if prediction[0] == 1 else fighter_2_name

    return jsonify({'fighter_1': fighter_1_name, 'fighter_2': fighter_2_name, 'predicted_winner': winner})

if __name__ == '__main__':
    app.run(debug=True)
