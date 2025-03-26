import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('../datasets/fights_data.csv')

# Handle missing values in 'winner' column (for draws or no contest)
df['winner'] = df['winner'].fillna('Draw')

# Create new columns for fighter statistics (differences between fighters)
df['kd_diff'] = df['fighter_1_kd'] - df['fighter_2_kd']
df['sig_head_diff'] = df['f1_sig_head'] - df['f2_sig_head']
df['sig_body_diff'] = df['f1_sig_body'] - df['f2_sig_body']
df['sig_leg_diff'] = df['f1_sig_leg'] - df['f2_sig_leg']
df['sig_distance_diff'] = df['f1_sig_distance'] - df['f2_sig_distance']
df['sig_clinch_diff'] = df['f1_sig_clinch'] - df['f2_sig_clinch']
df['sig_ground_diff'] = df['f1_sig_ground'] - df['f2_sig_ground']
df['td_diff'] = df['fighter_1_td'] - df['fighter_2_td']
df['sub_att_diff'] = df['fighter_1_sub_att'] - df['fighter_2_sub_att']
df['rev_diff'] = df['fighter_1_rev'] - df['fighter_2_rev']
df['ctrl_diff'] = df['fighter_1_ctrl'] - df['fighter_2_ctrl']

# Convert winner column to binary (1 for fighter_1 win, 0 for fighter_2 win, and 0.5 for draw)
winner_bin = []
for i in range(len(df['winner'])):
    if df['winner'][i] == df['fighter_1'][i]:
        winner_bin.append(1)
    elif df['winner'][i] == df['fighter_2'][i]:
        winner_bin.append(0)
    else:
        winner_bin.append(0.5)
        
df['winner_binary'] = winner_bin


# Select features for correlation analysis
features = ['kd_diff', 'sig_head_diff', 'sig_body_diff', 'sig_leg_diff', 'sig_distance_diff',
            'sig_clinch_diff', 'sig_ground_diff', 'td_diff', 'sub_att_diff', 'rev_diff', 'ctrl_diff']

# Calculate correlations between features and the binary winner
corr_matrix = df[features + ['winner_binary']].corr()



# Visualize the correlation matrix
plt.figure(figsize=(12, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f', vmin=-1, vmax=1)
plt.title('Correlation of Features with Winner Binary Outcome')
plt.show()

# Investigate the most correlated features with the winner binary
print(corr_matrix['winner_binary'].sort_values(ascending=False))
