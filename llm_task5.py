
import pandas as pd

# Load data
games_df = pd.read_csv("C:/Users/leena/Downloads/syracuse_lacrosse_2025_cleaned.csv")
players_df = pd.read_csv("C:/Users/leena/Downloads//syracuse_lacrosse_2025_player_stats.csv")

# Total games played
total_games = games_df.shape[0]

# Win-loss record
total_wins = games_df[games_df["Result"] == "W"].shape[0]
total_losses = games_df[games_df["Result"] == "L"].shape[0]

# Top goal scorer
top_goal_scorer = players_df.sort_values(by="Goals", ascending=False).iloc[0]

# Highest average points per game
players_df["Points_Per_Game"] = players_df["Points"] / players_df["Games_Played"]
top_ppg_player = players_df.sort_values(by="Points_Per_Game", ascending=False).iloc[0]

# Closest game
games_df["Goal_Diff"] = abs(games_df["SU_Score"] - games_df["Opponent_Score"])
closest_game = games_df.sort_values("Goal_Diff").iloc[0]

# Most goals scored in a game
most_goals_game = games_df.sort_values("SU_Score", ascending=False).iloc[0]

# Most consistent scorer (goals per game)
players_df["Goals_Per_Game"] = players_df["Goals"] / players_df["Games_Played"]
most_consistent = players_df.sort_values(by="Goals_Per_Game", ascending=False).iloc[0]

# Top assist player
top_assist_player = players_df.sort_values(by="Assists", ascending=False).iloc[0]

# Narrow losses (margin >= -3 and result = L)
games_df["Margin"] = games_df["SU_Score"] - games_df["Opponent_Score"]
narrow_losses = games_df[(games_df["Result"] == "L") & (games_df["Margin"] >= -3)]
num_narrow_losses = narrow_losses.shape[0]

# Largest win
largest_win = games_df[games_df["Result"] == "W"].sort_values(by="Margin", ascending=False).iloc[0]

# Output results
print(f"1. Total games: {total_games}")
print(f"2. Win/Loss record: {total_wins}W - {total_losses}L")
print(f"3. Top goal scorer: {top_goal_scorer['Player']} ({top_goal_scorer['Goals']} goals)")
print(f"4. Highest points per game: {top_ppg_player['Player']} ({top_ppg_player['Points_Per_Game']:.2f} PPG)")
print(f"5. Closest game: {closest_game['Opponent']} on {closest_game['Date']} ({closest_game['SU_Score']}-{closest_game['Opponent_Score']})")
print(f"6. Most goals in a game: {most_goals_game['Opponent']} ({most_goals_game['SU_Score']} goals)")
print(f"7. Most consistent scorer: {most_consistent['Player']} ({most_consistent['Goals_Per_Game']:.2f} goals/game)")
print(f"8. Top playmaker: {top_assist_player['Player']} ({top_assist_player['Assists']} assists)")
print(f"9. Narrow losses (<=3 goals): {num_narrow_losses}")
print(f"10. Largest win: {largest_win['Opponent']} on {largest_win['Date']} ({largest_win['SU_Score']}-{largest_win['Opponent_Score']}, margin {largest_win['Margin']})")
