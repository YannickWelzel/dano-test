import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# --- Konfiguration ---
csv_file_path = 'supplier_data.csv'
output_image_path = 'risk_types_analysis_colored.png' # Neuer Dateiname für das farbige Diagramm
risk_level_to_analyze = 'Hoch'
# -------------------

# --- Risikokategorisierung ---
# Ordnen Sie hier die bereinigten Risiko-Namen den Kategorien zu
social_risks = [
    'ChildLabor', 'ForcedLabor', 'WorkplaceSafety', 
    'FreedomOfAssociation', 'Discrimination', 'Wage', 'LandRights'
]
ecological_risks = [
    'Pollution', 'WaterUsage', 'Deforestation'
]
# ---------------------------

try:
    # 1. Daten aus der CSV-Datei einlesen
    df = pd.read_csv(csv_file_path)

    # 2. Risikospalten identifizieren
    risk_columns = [col for col in df.columns if col.endswith('Risk')]

    # 3. Häufigkeit des Risikolevels 'Hoch' zählen
    high_risk_counts = {}
    for col in risk_columns:
        count = df[col].value_counts().get(risk_level_to_analyze, 0)
        clean_name = col.replace('Risk', '')
        high_risk_counts[clean_name] = count

    risk_series = pd.Series(high_risk_counts).sort_values(ascending=True)

    # 4. Farben basierend auf der Kategorie zuweisen
    colors = []
    for risk_name in risk_series.index:
        if risk_name in social_risks:
            colors.append('royalblue') # Blauton für soziale Risiken
        elif risk_name in ecological_risks:
            colors.append('forestgreen') # Grünton für ökologische Risiken
        else:
            colors.append('grey') # Fallback-Farbe

    # 5. Horizontales Balkendiagramm erstellen
    fig, ax = plt.subplots(figsize=(12, 8))
    risk_series.plot(kind='barh', ax=ax, color=colors)

    # 6. Titel und Achsenbeschriftungen
    ax.set_title(f'Häufigkeit der Risikoart mit Bewertung "{risk_level_to_analyze}"', fontsize=16)
    ax.set_xlabel(f'Anzahl der Lieferanten mit Risiko "{risk_level_to_analyze}"', fontsize=12)
    ax.set_ylabel('Risikoart', fontsize=12)

    # 7. Legende hinzufügen
    social_patch = mpatches.Patch(color='royalblue', label='Soziales Risiko')
    ecological_patch = mpatches.Patch(color='forestgreen', label='Ökologisches Risiko')
    ax.legend(handles=[social_patch, ecological_patch], loc='lower right')

    # Füge die genaue Anzahl an das Ende jedes Balkens hinzu
    for index, value in enumerate(risk_series):
        ax.text(value, index, f' {value}', va='center')

    plt.tight_layout()

    # 8. Diagramm als Bilddatei speichern
    plt.savefig(output_image_path, dpi=300, bbox_inches='tight')

    print(f"Das farbige Diagramm der Risikoarten wurde erfolgreich als '{output_image_path}' gespeichert.")

except FileNotFoundError:
    print(f"Fehler: Die Datei '{csv_file_path}' wurde nicht gefunden.")
except Exception as e:
    print(f"Ein unerwarteter Fehler ist aufgetreten: {e}")
