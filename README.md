 IPL Toss Analysis – Power BI

This project analyzes IPL toss outcomes to uncover trends in decisions (bat/field), venue patterns, and their impact on match results. The workflow includes Python preprocessing of raw JSON files into a cleaned CSV, followed by Power BI dashboards for visualization.

 Workflow

  Raw Data – JSON files for each match (provided in data_raw/)
  
  Preprocessing – clean.py script converts JSON → CSV
  
  Processed Data – Cleaned dataset (data_processed/data_cleaned.csv)
  
  Visualization – Power BI dashboard (IPL Toss analysis.pbix)

 Tools Used

  Python (pandas, json, os) – Data cleaning & CSV generation

  Power BI – Data modeling and interactive dashboards

  Project Structure
   📁 IPL-Toss-Analysis
   
 ┣ 📁 data_raw/              # Raw JSON files (one per match)
 
 ┣ 📁 data_processed/        # Cleaned CSV dataset
 
 ┃ ┗ data_cleaned.csv
 
 ┣ 📄 clean.py               # Python preprocessing script
 
 ┣ 📊 IPL Toss analysis.pbix # Power BI dashboard
 
 ┗ 📄 README.md              # Documentation


Getting Started

Clone the repo:

    git clone https://github.com/Stalinselvan/ipl-toss-analysis.git
    cd ipl-toss-analysis


Run preprocessing (if needed):

    python clean.py


This will generate data_cleaned.csv in data_processed/

Open IPL Toss analysis.pbix in Power BI Desktop and explore the dashboards.
<img width="2000" height="1116" alt="image" src="https://github.com/user-attachments/assets/59823354-fce2-43e5-bbb9-2879b729f24a" />
<img width="2005" height="1127" alt="image" src="https://github.com/user-attachments/assets/e21fa560-33b9-44c8-b8b5-53757fe6159c" />
<img width="1994" height="1129" alt="image" src="https://github.com/user-attachments/assets/cf328088-8ca7-412f-a618-c013cbb270f9" />

 Author

Stalin S
📧 stalinselvan6@gmail.com 

