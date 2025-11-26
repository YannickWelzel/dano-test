import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

# --- Konfiguration ---
csv_file_path = 'supplier_data.csv'
output_image_path = 'risk_portfolio_analysis.png'
# -------------------

try:
    # 1. Daten aus der CSV-Datei einlesen
    df = pd.read_csv(csv_file_path)

    # 2. Diagramm erstellen
    fig, ax = plt.subplots(figsize=(14, 9))
    ax.scatter(df['OverallRiskScore'], df['UmsatzvolumenEUR'], alpha=0.7, edgecolors='w', s=80)

    # 3. Titel und Achsenbeschriftungen hinzufügen
    ax.set_title('Risiko-Portfolio-Analyse: Lieferantenrisiko vs. Umsatzvolumen', fontsize=16)
    ax.set_xlabel('Gesamtrisiko-Score (OverallRiskScore)', fontsize=12)
    ax.set_ylabel('Umsatzvolumen in EUR', fontsize=12)
    ax.grid(True, which='both', linestyle='--', linewidth=0.5)

    # 4. Y-Achse formatieren, um die Lesbarkeit zu verbessern (keine wissenschaftliche Notation)
    ax.get_yaxis().set_major_formatter(mticker.FuncFormatter(lambda x, p: format(int(x), ',')))
    plt.xticks(range(int(df['OverallRiskScore'].min()) -1, int(df['OverallRiskScore'].max()) + 2))

    # 5. Jeden Punkt mit der SupplierID beschriften
    for i, txt in enumerate(df['SupplierID']):
        ax.annotate(txt, (df['OverallRiskScore'][i], df['UmsatzvolumenEUR'][i]),
                    textcoords="offset points",
                    xytext=(0,10),
                    ha='center',
                    fontsize=8)

    # 6. Quadrantenlinien basierend auf Medianen hinzufügen
    median_risk = df['OverallRiskScore'].median()
    median_umsatz = df['UmsatzvolumenEUR'].median()
    ax.axvline(x=median_risk, color='grey', linestyle='--', lw=1.5)
    ax.axhline(y=median_umsatz, color='grey', linestyle='--', lw=1.5)
    
    # Quadranten beschriften
    plt.text(median_risk + 0.1, ax.get_ylim()[1], ' Hohes Risiko', color='red', va='top', ha='left')
    plt.text(median_risk - 0.1, ax.get_ylim()[1], ' Geringeres Risiko', color='green', va='top', ha='right')
    
    # 7. Diagramm als Bilddatei speichern
    plt.savefig(output_image_path, dpi=300, bbox_inches='tight')

    print(f"Das Diagramm wurde erfolgreich als '{output_image_path}' gespeichert.")

except FileNotFoundError:
    print(f"Fehler: Die Datei '{csv_file_path}' wurde nicht gefunden. Stellen Sie sicher, dass das Skript im selben Ordner wie die CSV-Datei liegt.")
except Exception as e:
    print(f"Ein unerwarteter Fehler ist aufgetreten: {e}")
