import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
fights_data = pd.read_csv('../datasets/fights_data.csv')

# Function to determine win style based on sig strikes and takedowns
def determine_win_style(row):
    winner = row['winner']
    if winner == row['fighter_1']:
        sig_str_winner = row['fighter_1_sig_str']
        sig_str_loser = row['fighter_2_sig_str']
        td_winner = row.get('fighter_1_td', 0)
        td_loser = row.get('fighter_2_td', 0)
    elif winner == row['fighter_2']:
        sig_str_winner = row['fighter_2_sig_str']
        sig_str_loser = row['fighter_1_sig_str']
        td_winner = row.get('fighter_2_td', 0)
        td_loser = row.get('fighter_1_td', 0)
    else:
        # Fights that resulted in draw or no contest
        return 'Unknown'

    # take the data of the winner
    sig_str_win = sig_str_winner > sig_str_loser
    td_win = td_winner > td_loser

    if sig_str_win and not td_win:
        return 'Strikes Only'
    elif td_win and not sig_str_win:
        return 'Takedowns Only'
    elif sig_str_win and td_win:
        return 'Both'
    else:
        return 'Unknown'

# Create a new column
fights_data['win_style'] = fights_data.apply(determine_win_style, axis=1)

# Count and display the results
win_style_counts = fights_data['win_style'].value_counts()
print(win_style_counts)

win_style_counts.plot(kind='bar', color=['blue', 'green', 'orange', 'gray'])
plt.title('Win Style Distribution: Strikes vs Takedowns')
plt.xlabel('Win Style')
plt.ylabel('Number of Fights')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
