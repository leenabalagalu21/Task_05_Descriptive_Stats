# Task_05_Descriptive_Stats
This project explores the reasoning capabilities of Large Language Models (LLMs) like ChatGPT when prompted with natural language questions about structured sports data. Specifically, it analyzes the 2025 Syracuse Women’s Lacrosse season using two datasets:

syracuse_lacrosse_2025_cleaned.csv: Game-level results (scores, opponents, date, win/loss, location). 

syracuse_lacrosse_2025_player_stats.csv: Player-level statistics (goals, assists, games played, turnovers, accuracy, etc.).

The goal is to challenge an LLM to answer basic, analytical, and strategic questions using prompt engineering, and then validate or correct the model’s responses with Python.
---

## 💬 Sample LLM Prompts and Outcomes

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

---

## 💡 Interesting Insights from the Data

- **Top Performer Efficiency**: Olivia Adamson played only 3 games but scored 10 goals and 6 assists—making her the most efficient offensive contributor (5.33 points per game).
- **Elite Playmaker**: Emma Ward not only led in assists but also contributed significantly to the team’s goal generation, with a combined offensive total of 76 (Goals + Assists).
- **Tight Competition**: 5 of Syracuse’s 9 losses were by a margin of 3 goals or fewer, suggesting close contests and high potential to flip outcomes.
- **Biggest Victory**: The most dominant win came against UALBANY with a score of 21–9.
- **Consistent Finisher**: Emma Muchnick led the team in total goals (34) and maintained a solid scoring rhythm throughout the season.
- **Correlation Confidence**: A 0.99 Pearson correlation between shots and goals validates that shot volume is a strong predictor of scoring—helpful for coaching focus.

---

## 🛠️ Technologies Used

- **Language Model:** ChatGPT-4 (OpenAI)
- **Scripting:** Python 3.10
  - `pandas` for data manipulation
  - `matplotlib` / `seaborn` (optional) for visualizations
- **Dataset:** 2025 Syracuse Women’s Lacrosse Team stats
- **Word Processing:** Microsoft Word for reflective report


---

## 🧠 Reflections & Findings

- **Strengths of LLMs:**
  - Excellent at basic stats, simple max/min queries
  - Strong with domain-specific language (e.g., “playmaker” → assists)
- **Weaknesses:**
  - Struggles with ambiguous prompts like “most improved”
  - Needs metrics explicitly defined for derived/statistical questions
- **Prompt Engineering Tactics:**
  - Define ambiguous terms (e.g., "impact", "consistency")
  - Break down multi-part questions
  - Use follow-ups to refine logic and get better answers
---

