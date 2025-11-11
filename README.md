
# PRECISION Quarto Workflow (Demo)

Kleines Demo-Repo mit Quarto-Website, Test-Notebook und GitHub-Actions-Pipeline.

## Quickstart (lokal)

1. [Quarto installieren](https://quarto.org/docs/get-started/).
2. Python-Umgebung: `pip install -r requirements.txt` (oder manuell: pandas, numpy, matplotlib, jupyter, nbconvert).
3. Notebook rendern: `jupyter nbconvert --to html --output-dir notebooks notebooks/test_analysis.ipynb`
4. Website bauen: `quarto render`
5. Lokal ansehen: `quarto preview`

## Snapshots

- Interaktiv im Notebook (siehe Funktion `save_snapshot()`), oder
- CLI: `python snapshot_notebook.py --src notebooks/test_analysis.ipynb --message "Vor Abbildung 2"`

## CI/CD

- GitHub Actions rendern Site bei jedem Push auf `main` und veröffentlichen sie via GitHub Pages.

