import os
import json
import pandas as pd

data_folder = r"D:\projects\ipl_male_json"  

files = [f for f in os.listdir(data_folder) if f.endswith(".json")]
matches = []

for file in files:
    with open(os.path.join(data_folder, file), 'r') as f:
        data = json.load(f)
        info = data.get("info", {})

        match = {
            "match_id": file.replace(".json", ""),
            "season": info.get("dates", [None])[0][:4],
            "venue": info.get("venue", None),
            "city": info.get("city", None),
            "team1": info.get("teams", [None, None])[0],
            "team2": info.get("teams", [None, None])[1],
            "toss_winner": info.get("toss", {}).get("winner", None),
            "toss_decision": info.get("toss", {}).get("decision", None),
            "winner": info.get("outcome", {}).get("winner", None)
        }
        matches.append(match)

import pandas as pd
df = pd.DataFrame(matches)
print(df.head())
df.to_csv("ipl_match_summary.csv", index=False)
