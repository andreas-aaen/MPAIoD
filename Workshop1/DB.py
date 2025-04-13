import pandas as pd
import sqlite3

# Indlæs datasættet
df = pd.read_csv('NFL.csv')

# Split data til to datasæt
player_df = df[['Player', 'Year', 'Age', 'School', 'Player_Type', 'Position_Type', 'Position']].copy()
metrics_df = df[['Player', 'Height', 'Weight', 'Sprint_40yd', 'Vertical_Jump', 'Bench_Press_Reps',
                 'Broad_Jump', 'Agility_3cone', 'Shuttle', 'BMI', 'Drafted..tm.rnd.yr.', 'Drafted']].copy()

# Gem Player Database
conn1 = sqlite3.connect('players.db')
player_df.to_sql('players', conn1, if_exists='replace', index=False)
conn1.close()

# Gem Metrics Database
conn2 = sqlite3.connect('metrics.db')
metrics_df.to_sql('metrics', conn2, if_exists='replace', index=False)
conn2.close()

print("Databaser oprettet.")
