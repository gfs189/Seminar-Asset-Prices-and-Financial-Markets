# Data Analysis Project

## Project Structure

```
quarto-project/
├── index.qmd              # Main file — assembles all chapters
├── _quarto.yml            # Quarto configuration
├── chapters/
│   ├── 01_introduction.qmd   ← Person A
│   ├── 02_data.qmd           ← Person A
│   ├── 03_analysis.qmd       ← Person B
│   ├── 04_results.qmd        ← Person B
│   └── 05_conclusion.qmd     ← Shared
├── src/
│   ├── data_loader.py        ← Person A
│   ├── analysis.py           ← Person B
│   └── visualisation.py      ← Person B
├── data/
│   ├── raw/                  # Original data (not tracked by git)
│   └── processed/            # Cleaned data
├── figures/                  # Saved plots
└── .gitignore
```

## Division of Work

| File | Owner |
|------|-------|
| `chapters/01_introduction.qmd` | Person A |
| `chapters/02_data.qmd` | Person A |
| `src/data_loader.py` | Person A |
| `chapters/03_analysis.qmd` | Person B |
| `chapters/04_results.qmd` | Person B |
| `src/analysis.py` | Person B |
| `src/visualisation.py` | Person B |
| `chapters/05_conclusion.qmd` | Shared |

## Git Workflow

```bash
# Before starting work each day:
git pull origin main

# Work on your own branch:
git checkout -b feature/your-name-description

# Commit often:
git add .
git commit -m "Add EDA section to chapter 3"
git push origin feature/your-name-description

# When done, open a Pull Request into main
```

## Rendering

```bash
# Render the full project
quarto render

# Preview with live reload
quarto preview
```
