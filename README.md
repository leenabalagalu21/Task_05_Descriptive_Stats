# Task_05_Descriptive_Stats
This project explores the reasoning capabilities of Large Language Models (LLMs) like ChatGPT when prompted with natural language questions about structured sports data. Specifically, it analyzes the 2025 Syracuse Women’s Lacrosse season using two datasets:

syracuse_lacrosse_2025_cleaned.csv: Game-level results (scores, opponents, date, win/loss, location). 

syracuse_lacrosse_2025_player_stats.csv: Player-level statistics (goals, assists, games played, turnovers, accuracy, etc.).

The goal is to challenge an LLM to answer basic, analytical, and strategic questions using prompt engineering, and then validate or correct the model’s responses with Python.The project also extends into deeper statistical analysis to uncover performance trends and coaching insights.
---

## Basic LLM Prompts and Outcomes

| Prompt | LLM Response Summary | Python Validated? |
|--------|----------------------|-------------------|
| How many games were played? | 19 | Yes |
| What is the win/loss record? | 10W – 9L | Yes |
| Who scored the most goals? | Emma Muchnick (34) | Yes |
| Highest points per game? | Olivia Adamson (5.33) | Yes |
| Closest game? | Stanford (14–13) | Yes |
| Largest win? | UALBANY (21–9) | Yes |
| Most improved player? | Initially wrong; final: Olivia Adamson | Manually defined metric |
| Should coach focus on offense or defense? | Initially vague; clarified after stats provided | Partially validated |
| Correlation between shots and goals? | r = 0.99 | Yes |
| Top playmaker? | Emma Ward (46 assists) | Yes |
| Avg. goals scored & allowed per game? |	13.63 scored, 12.53 allowed	| Yes |
| Offensive vs. defensive strength?	| Offense stronger; shots–goals r = 0.99	| Yes |
| 1 more goal per loss — new record? |	13–6	| Yes |
| Do top scorers contribute more in wins?	| Yes — 57% in wins vs 42% in losses |Yes |



---

## Interesting Insights from the Data

- **Top Performer Efficiency**: Olivia Adamson played only 3 games but scored 10 goals and 6 assists—making her the most efficient offensive contributor (5.33 points per game).
- **Elite Playmaker**: Emma Ward not only led in assists but also contributed significantly to the team’s goal generation, with a combined offensive total of 76 (Goals + Assists).
- **Tight Competition**: 5 of Syracuse’s 9 losses were by a margin of 3 goals or fewer, suggesting close contests and high potential to flip outcomes.
- **Biggest Victory**: The most dominant win came against UALBANY with a score of 21–9.
- **Consistent Finisher**: Emma Muchnick led the team in total goals (34) and maintained a solid scoring rhythm throughout the season.
- **Correlation Confidence**: A 0.99 Pearson correlation between shots and goals validates that shot volume is a strong predictor of scoring—helpful for coaching focus.
- **Balanced Scoring vs. Defense** : The team averaged 13.63 goals scored and 12.53 goals allowed per game, showing a slight offensive edge.
- **Impact of Small Gains** : If Syracuse had scored one more goal in each loss, their record would improve from 10–9 to 13–6.
- **Clutch Factor of Top Scorers** : Top scorers contributed 57% of total points in wins, compared to only 42% in losses, indicating the team wins when star players are more involved.
- **Offense Over Defense** : Both the strong correlation between shots and goals and the scoring averages suggest that boosting offensive production could yield better outcomes than focusing solely on defense.

---

## 🛠️ Technologies Used

- **Language Model:** ChatGPT-4 (OpenAI)
- **Scripting:** Python 3.10
  - `pandas` for data manipulation
  - `matplotlib` / `seaborn` (optional) for visualizations
- **Dataset:** 2025 Syracuse Women’s Lacrosse Team stats
- **Word Processing:** Microsoft Word for reflective report


---
## Visualizations

- **Goals Scored vs. Conceded per Game** : Highlights offensive vs. defensive performance and close losses.
- **Top Goal Scorers** : Shows total goals, confirming Emma Muchnick’s dominance.
- **Goals per Game by Player** : Reveals efficient scorers like Olivia Adamson despite fewer appearances.
- **Shots vs. Goals Correlation** : Scatter plot confirms strong positive relationship (r = 0.99).

---

## Reflections & Findings

- **Strengths of LLMs:**
  - Very good at answering basic statistical and ranking queries (e.g., total games, top scorer, win/loss record).
  - Correctly maps domain-specific terms like “playmaker” to assists and “closest game” to smallest score margin.
  - Handles correlation questions effectively when the metric is explicitly stated.
- **Weaknesses:**
  - Struggles with ambiguous prompts (e.g., “most improved player” or “should coach focus on offense or defense”) unless the metric is defined.
  - Can produce plausible but wrong answers if conditions are not explicitly clarified (e.g., narrow losses initially miscounted).
  - Needs step-by-step refinement for multi-part analytical queries.
- **Prompt Engineering Tactics:**
  - Define ambiguous terms – Clearly specify what metrics should be used for subjective terms.
           Example: “Consistency” → Goals per game
           Example: “Impact” → Points per game (Goals + Assists)
  - Break down multi-part questions – Separate broad prompts into smaller, measurable parts.
           Example: “Should coach focus on offense or defense?” → Compare average goals scored vs. allowed.
  - Use iterative follow-ups – Refine unclear or incorrect responses by providing constraints and context.
           Example: Re-asking “narrow losses” with both loss condition and goal margin defined.
    
---

