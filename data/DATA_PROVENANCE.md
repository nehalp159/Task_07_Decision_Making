# Data Provenance

## Dataset
- **Name**: Syracuse Women’s Lacrosse 2025 Season Statistics  
- **Source**: Publicly available via SU Athletics official site ([cuse.com](https://cuse.com))  
- **Files**: `syracuse_wlax_stats_2025.csv`, `syracuse_wlax_stats_2025.xlsx`  

## Collection
- Data collected from official game box scores and season summaries.  
- Covers 19 games from the 2025 season.  
- Includes offensive and defensive performance metrics (shots, goals, turnovers, saves, etc.).  

## Validation
- Descriptive statistics reproduced in **Python**, then compared with **Pandas** and **Polars** outputs (Task 05).  
- Discrepancies (e.g., Copilot miscounting “Team” rows) were corrected and documented.  
- Bootstrapping applied to confirm confidence intervals for shot accuracy.  

## Limitations
- Does not include player wellness, fitness, or injury data.  
- Does not capture qualitative aspects (team morale, coaching strategies).  
- Potential bias: statistics reflect only **on-field performance**, not full player contribution.  

## Usage in This Repo
- Serves as the empirical backbone for **Task 07 decision report**.  
- Underpins the AI-generated narrative (Task 06) and the final **stakeholder recommendations** (Task 07).  
