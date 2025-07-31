
# Visualizations for Syracuse Women's Lacrosse 2025

import pandas as pd
import matplotlib.pyplot as plt

# Load data
games_df = pd.read_csv("C:/Users/leena/Downloads/syracuse_lacrosse_2025_cleaned.csv")
players_df = pd.read_csv("C:/Users/leena/Downloads//syracuse_lacrosse_2025_player_stats.csv")

# Top Scorers
top_scorers = players_df.sort_values(by="Goals", ascending=False)
plt.figure(figsize=(10, 6))
plt.bar(top_scorers["Player"], top_scorers["Goals"])
plt.xticks(rotation=45, ha='right')
plt.title("Top Scorers - Syracuse Women's Lacrosse 2025")
plt.xlabel("Player")
plt.ylabel("Goals Scored")
plt.tight_layout()
plt.show()

# Win/Loss Trend
games_df["Game_Result"] = games_df["Result"].apply(lambda x: 1 if x == "W" else 0)
plt.figure(figsize=(12, 5))
plt.plot(games_df["Date"], games_df["Game_Result"], marker='o', linestyle='-')
plt.xticks(rotation=45)
plt.yticks([0, 1], ["Loss", "Win"])
plt.title("Win/Loss Trend Over Season")
plt.xlabel("Date")
plt.ylabel("Result")
plt.grid(True)
plt.tight_layout()
plt.show()
