# Visualizations for Syracuse Women's Lacrosse 2025

import pandas as pd
import matplotlib.pyplot as plt

# Load data
games_df = pd.read_csv("C:/Users/leena/Downloads/syracuse_lacrosse_2025_cleaned.csv")
players_df = pd.read_csv("C:/Users/leena/Downloads/syracuse_lacrosse_2025_player_stats.csv")

# 1. Top Scorers
top_scorers = players_df.sort_values(by="Goals", ascending=False).head(10)
plt.figure(figsize=(10, 6))
plt.bar(top_scorers["Player"], top_scorers["Goals"], color="orange")
plt.xticks(rotation=45, ha='right')
plt.title("Top 10 Goal Scorers - Syracuse Women's Lacrosse 2025")
plt.xlabel("Player")
plt.ylabel("Goals Scored")
plt.tight_layout()
plt.show()

# 2. Win/Loss Trend
games_df["Game_Result"] = games_df["Result"].apply(lambda x: 1 if x == "W" else 0)
plt.figure(figsize=(12, 5))
plt.plot(games_df["Date"], games_df["Game_Result"], marker='o', linestyle='-', color="green")
plt.xticks(rotation=45)
plt.yticks([0, 1], ["Loss", "Win"])
plt.title("Win/Loss Trend Over Season")
plt.xlabel("Date")
plt.ylabel("Result")
plt.grid(True)
plt.tight_layout()
plt.show()

# 3. Goals vs. Shots Correlation
plt.figure(figsize=(8, 6))
plt.scatter(players_df["Shots"], players_df["Goals"], color="blue", alpha=0.7)
plt.title("Goals vs. Shots - Player Performance")
plt.xlabel("Shots Taken")
plt.ylabel("Goals Scored")
for i, player in enumerate(players_df["Player"]):
    plt.annotate(player, (players_df["Shots"][i], players_df["Goals"][i]), fontsize=8, alpha=0.7)
plt.grid(True)
plt.tight_layout()
plt.show()

# 4. Points Per Game (≥5 Games Played)
players_df["Points_Per_Game"] = players_df["Points"] / players_df["Games_Played"]
eligible_players = players_df[players_df["Games_Played"] >= 5].sort_values(by="Points_Per_Game", ascending=False)
plt.figure(figsize=(10, 6))
plt.bar(eligible_players["Player"], eligible_players["Points_Per_Game"], color="purple")
plt.xticks(rotation=45, ha='right')
plt.title("Points Per Game (≥5 GP) - Syracuse Women's Lacrosse 2025")
plt.xlabel("Player")
plt.ylabel("Points Per Game")
plt.tight_layout()
plt.show()
