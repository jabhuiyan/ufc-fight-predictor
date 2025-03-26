import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import skew

# Load dataset
fighters_data = pd.read_csv('../datasets/fighters_data.csv')

# Columns to visualize
selected_columns = ['striking_accuracy', 'takedown_avg', 'takedown_accuracy', 'takedown_defense', 'submission_avg']

# Show mean, median and skewness
print(f"{'Feature':<20}{'Mean':>10}{'Median':>10}{'Skewness':>12}")
print("-" * 52)

for column in selected_columns:
    col_mean = fighters_data[column].mean()
    col_median = fighters_data[column].median()
    col_skewness = skew(fighters_data[column].dropna())
    
    print(f"{column:<20}{col_mean:>10.2f}{col_median:>10.2f}{col_skewness:>12.2f}")


# --- Plot Mean vs Median ---
plt.figure(figsize=(10, 6))
bar_width = 0.35
index = range(len(stats_df))

plt.bar(index, stats_df['Mean'], bar_width, label='Mean', color='skyblue')
plt.bar([i + bar_width for i in index], stats_df['Median'], bar_width, label='Median', color='salmon')

plt.xlabel('Feature', fontsize=12)
plt.ylabel('Value', fontsize=12)
plt.title('Mean vs Median for Each Feature', fontsize=14)
plt.xticks([i + bar_width / 2 for i in index], stats_df['Feature'], rotation=45)
plt.legend()
plt.tight_layout()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# Plot normal distribution with skewness
for column in selected_columns:
    data = fighters_data[column].dropna()
    col_skewness = skew(data)
    
    plt.figure(figsize=(8, 5))
    sns.histplot(data, kde=True, color='mediumpurple', bins=30)
    plt.title(f'Distribution of {column}', fontsize=14)
    plt.xlabel(column, fontsize=12)
    plt.ylabel('Frequency', fontsize=12)
    
    # Annotate skewness value
    plt.text(0.95, 0.95, f"Skewness: {col_skewness:.2f}", 
             ha='right', va='top', transform=plt.gca().transAxes,
             fontsize=12, bbox=dict(facecolor='white', alpha=0.7, edgecolor='gray'))
    
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.show()