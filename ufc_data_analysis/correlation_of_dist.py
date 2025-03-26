import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
fights_data = pd.read_csv('../datasets/fights_data.csv')

# Extract winner's strike location data
def get_winner_strike_location(row):
    if row['winner'] == row['fighter_1']:
        return pd.Series({
            'winner_distance': row['f1_sig_distance'],
            'winner_clinch': row['f1_sig_clinch'],
            'winner_ground': row['f1_sig_ground']
        })
    elif row['winner'] == row['fighter_2']:
        return pd.Series({
            'winner_distance': row['f2_sig_distance'],
            'winner_clinch': row['f2_sig_clinch'],
            'winner_ground': row['f2_sig_ground']
        })
    else:
        return pd.Series({'winner_distance': None, 'winner_clinch': None, 'winner_ground': None})

# Apply to extract winner's strike data
fights_data[['winner_distance', 'winner_clinch', 'winner_ground']] = fights_data.apply(get_winner_strike_location, axis=1)

# Drop rows with missing strike data
valid_strike_data = fights_data.dropna(subset=['winner_distance', 'winner_clinch', 'winner_ground'])

# Compute total sig strikes for winners
valid_strike_data['winner_total_strikes'] = valid_strike_data[['winner_distance', 'winner_clinch', 'winner_ground']].sum(axis=1)

# Correlation between strike types and total significant strikes
correlations = valid_strike_data[['winner_distance', 'winner_clinch', 'winner_ground', 'winner_total_strikes']].corr()

# Print correlation values
print("Correlation of Strike Type with Total Significant Strikes:")
print(correlations['winner_total_strikes'][:-1])  # Exclude correlation with itself

# Visualize correlation matrix with heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(correlations, annot=True, cmap='coolwarm', fmt=".2f", square=True)
plt.title('Correlation Matrix of Winner Strike Types')
plt.show()
