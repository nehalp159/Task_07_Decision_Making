# Task 07: Ethical Decision Making

## Author
Nehal Pawar
Research Analyst, Syracuse University
September 2025

---

## Project Description
This task builds on Task 05 (Descriptive Statistics and LLMs) and Task 06 (Deep Fake Interview) to produce a **stakeholder-facing decision report**.  
The emphasis is on **ethical decision-making**, **workflow transparency**, and **documentation of attempts**, rather than only the final outcome.  

The target audience is the **Syracuse Women’s Lacrosse coaching staff and athletic director**.  
The report provides **tiered recommendations (low, medium, high risk)** while highlighting issues of **bias, fairness, and reproducibility**.

---

## Objectives
- Translate LLM outputs and Python validation into an actionable decision-making framework.  
- Document the workflow, including successes, failures, and ethical considerations.  
- Provide transparent recommendations that balance **risk, performance, and fairness**.  

---

## Dataset / Input
- **Primary Data**: Syracuse Women’s Lacrosse 2025 player statistics.  
- **Validation Data**: Python descriptive statistics (from Task 05).  
- **LLM Outputs**: ChatGPT, Claude, Copilot, Gemini results (Task 05).  
- **Deep Fake Media**: Generated audio/video interviews (Task 06).  

Limitations: dataset excludes wellness, morale, and injury context, which may bias recommendations.

---

## Methodology
1. **Data Validation** – compared LLM outputs with Python ground truth (Task 05).  
2. **LLM Comparisons** – summarized differences across four models.  
3. **Decision Framework** – structured recommendations into low/medium/high-risk actions.  
4. **Ethics Analysis** – documented risks of bias, deep fakes, and reproducibility issues (Task 06).  
5. **Final Report** – synthesized findings into a stakeholder-ready document (`report.md`).  

---

## Project Structure
```
Task_07_Decision_Making/
├── README.md                  # Overview of Task 7
├── report.md                  # Stakeholder-facing decision report
├── data/
│   └── DATA_PROVENANCE.md
├── scripts/
│   ├── validate_stats.py
│   ├── generate_audio_gtts.py
│   ├── generate_waveform_video.py
│   └── overlay_captions.py
├── llm_transcripts/
│   ├── questions.md
│   ├── *_results.md
│   ├── summary_*.md
│   ├── interviewer_lines.txt
│   ├── guest_lines.txt
│   └── ATTEMPTS_LOG.md
├── ethics/
│   └── ETHICS_AND_DISCLOSURE.md
└── outputs/
    ├── AI_Street_Interview_Final.mp4
    ├── audiogram*.mp4
    ├── dialogue_aac.m4a
    ├── guest_lines.mp3
    └── interviewer_lines.mp3
```

---

## Requirements
- Python 3.10+  
- `ffmpeg` installed on system path  
- Dependencies listed in `scripts/requirements.txt`  

---

## Installation Instructions
```bash
git clone <repo_link>
cd Task_07_Decision_Making
pip install -r scripts/requirements.txt
```

---

## How to Reproduce
1. **Task 5 validation**: run `python scripts/validate_stats.py`  
2. **Task 6 generation**: run  
   - `python scripts/generate_audio_gtts.py`  
   - `python scripts/generate_waveform_video.py`  
   - `python scripts/overlay_captions.py`  
   Input lines are in `llm_transcripts/`  

Outputs will appear in the `outputs/` folder.

---

## Tools Used
- Python (Pandas, NumPy, Matplotlib)  
- Large Language Models (ChatGPT, Claude, Copilot, Gemini)  
- FFmpeg for media processing  

---

## Key Findings
- LLMs show variance in descriptive outputs; Python validation ensures accuracy.  
- Clear offensive and defensive performance trends were identified.  
- Tiered recommendations (low, medium, high risk) provide flexible decision-making.  

---

## Results / Artifacts
- **Stakeholder Report**: `report.md`  
- **Deep Fake Interview**: final video and audiograms (`outputs/`)  
- **Full Workflow Documentation**: transcripts, logs, and Python outputs (`llm_transcripts/`)  

---

## Ethics & Disclosure
- **Bias & Fairness**: AI models may embed bias; statistical validation was used to mitigate.  
- **Transparency**: All outputs and scripts are documented for reproducibility.  
- **Deep Fakes**: Media outputs are labeled as synthetic and not intended for deceptive use.  

---

## Challenges Encountered
- Aligning inconsistent LLM outputs with validated statistics.  
- Handling missing or incomplete contextual data (e.g., wellness, injuries).  
- Technical complexity of generating synchronized captions in Task 6.  

---

## Future Improvements
- Include additional datasets (wellness, injury reports) for better decision-making context.  
- Develop automated bias detection dashboards.  
- Expand ethical guidelines for AI-assisted sports analytics.  

---

## Overall Conclusion
Task 07 demonstrates how **descriptive statistics, LLMs, and ethical considerations** can be combined to support **transparent and fair decision-making**.  
The workflow highlights both the potential and the limitations of AI-assisted recommendations in sports analytics.  

---

## Contact
For questions, contact: nepawar@syr.edu  

---

## Acknowledgments
- Syracuse University - Research guidance  
- Syracuse Women’s Lacrosse - Contextual dataset inspiration  
- OpenAI, Anthropic, Microsoft, Google - LLM outputs used in comparisons  

Under Professor Jonathan's guidance, the project was completed as part of Syracuse University's research requirements.
