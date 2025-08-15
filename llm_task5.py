import pandas as pd

# Load Data
games_df = pd.read_csv("C:/Users/leena/Downloads/syracuse_lacrosse_2025_cleaned.csv")
players_df = pd.read_csv("C:/Users/leena/Downloads/syracuse_lacrosse_2025_player_stats.csv")

# Baseline LLM Validation Metrics
# Total games played
total_games = games_df.shape[0]

# Win/Loss record
total_wins = games_df[games_df["Result"] == "W"].shape[0]
total_losses = games_df[games_df["Result"] == "L"].shape[0]

# Top goal scorer
top_goal_scorer = players_df.sort_values(by="Goals", ascending=False).iloc[0]

# Highest average points per game (PPG = (Goals + Assists) / Games Played)
players_df["Points_Per_Game"] = players_df["Points"] / players_df["Games_Played"]
top_ppg_player = players_df.sort_values(by="Points_Per_Game", ascending=False).iloc[0]

# Closest game (smallest absolute score difference)
games_df["Goal_Diff"] = (games_df["SU_Score"] - games_df["Opponent_Score"]).abs()
closest_game = games_df.sort_values("Goal_Diff").iloc[0]

# Most goals scored in a game
most_goals_game = games_df.sort_values("SU_Score", ascending=False).iloc[0]

# Most consistent scorer (highest Goals per Game)
players_df["Goals_Per_Game"] = players_df["Goals"] / players_df["Games_Played"]
most_consistent = players_df.sort_values(by="Goals_Per_Game", ascending=False).iloc[0]

# Top playmaker (most assists)
top_assist_player = players_df.sort_values(by="Assists", ascending=False).iloc[0]

# Narrow losses (≤3 goals)
games_df["Margin"] = games_df["SU_Score"] - games_df["Opponent_Score"]
narrow_losses = games_df[(games_df["Result"] == "L") & (games_df["Margin"] >= -3)]
num_narrow_losses = narrow_losses.shape[0]

# Largest win (highest positive margin)
largest_win = games_df[games_df["Result"] == "W"].sort_values(by="Margin", ascending=False).iloc[0]


# Extended Strategic Analysis (Coaching Insights)
# Season totals and averages for offense vs. defense
total_goals_scored = games_df["SU_Score"].sum()
total_goals_allowed = games_df["Opponent_Score"].sum()
avg_goals_scored = total_goals_scored / total_games if total_games else float("nan")
avg_goals_allowed = total_goals_allowed / total_games if total_games else float("nan")

# 1-goal improvement simulation in narrow losses
offense_flips = int((narrow_losses["Margin"] + 1 >= 0).sum())
defense_flips = int((narrow_losses["Margin"] + 1 >= 0).sum())

# Game-changer player identification
player_flip_count = {player: offense_flips for player in players_df["Player"]}
game_changer_player = max(player_flip_count, key=player_flip_count.get)
game_changer_potential = player_flip_count[game_changer_player]

# Offensive catalyst (highest Points/Game among players with ≥5 games)
eligibility_mask = players_df["Games_Played"] >= 5
if eligibility_mask.any():
    catalyst_row = players_df.loc[eligibility_mask].sort_values("Points_Per_Game", ascending=False).iloc[0]
    catalyst_player = catalyst_row["Player"]
    catalyst_ppg = float(catalyst_row["Points_Per_Game"])
else:
    catalyst_player = top_ppg_player["Player"]
    catalyst_ppg = float(top_ppg_player["Points_Per_Game"])

# Correlation checks (if data available)
corrs = {}
if "Shots" in players_df.columns and "Goals" in players_df.columns:
    corrs["Shots_vs_Goals_r"] = round(players_df["Shots"].corr(players_df["Goals"]), 3)
if "Turnovers" in players_df.columns and "Points" in players_df.columns:
    corrs["Turnovers_vs_Points_r"] = round(players_df["Turnovers"].corr(players_df["Points"]), 3)

# Output
print("=== Original Statistics ===")
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

print("\n=== Extended Strategic Analysis ===")
print(f"Total Goals Scored: {total_goals_scored}")
print(f"Total Goals Allowed: {total_goals_allowed}")
print(f"Avg Goals Scored/Game: {avg_goals_scored:.2f}")
print(f"Avg Goals Allowed/Game: {avg_goals_allowed:.2f}")
print(f"Narrow Losses (≤3 goals): {num_narrow_losses}")

print("\n1-Goal Improvement Simulation on Narrow Losses")
print(f"  Offense (+1 SU goal): potential flips = {offense_flips}")
print(f"  Defense (-1 opp goal): potential flips = {defense_flips}")

print("\nGame-Changer Identification")
print(f"  Flip-focused (heuristic): {game_changer_player} ({game_changer_potential} potential flips)")
print(f"  Offensive catalyst (PPG, ≥5 GP): {catalyst_player} ({catalyst_ppg:.2f} PPG)")

if corrs:
    print("\nCorrelations (players)")
    for k, v in corrs.items():
        print(f"  {k}: r = {v}")
else:
    print("\nCorrelations (players): relevant columns not found; skipped.")
