"""
Script principale per analizzare attività di pesca
nel Mediterraneo occidentale
"""

import os
import asyncio
from src.data_fetcher import GFWDataFetcher
from src.visualizer import FishingVisualizer


def main():
    # Crea cartelle output se non esistono
    os.makedirs("data/raw", exist_ok=True)
    os.makedirs("outputs/maps", exist_ok=True)
    os.makedirs("outputs/charts", exist_ok=True)

    print("=== Mediterranean Fishing Activity Tracker ===\n")

    # 1. Scarica dati
    print("Step 1: Download dati da Global Fishing Watch...")
    fetcher = GFWDataFetcher()

    df = asyncio.run(
        fetcher.get_fishing_effort(
            start_date="2025-06-18",
            end_date="2025-06-27",
            bbox={
                "type": "Polygon",
                "coordinates": [
                    [[0.5, 38.5], [9.5, 38.5], [9.5, 44], [0.5, 44], [0.5, 38.5]]
                ],
            },  # Sardegna, Baleari, Catalogna in geoJSON
        )
    )

    if df is None or df.empty:
        print("Errore: nessun dato scaricato")
        print("\nNOTA: Consulta la documentazione GFW API per:")
        print("- Parametri corretti della funzione get_fishing_effort")
        print("- Limiti del piano gratuito")
        print("- Formato dati restituiti")
        return

    # Salva dati raw
    df.to_csv("data/raw/fishing_data.csv", index=False)
    print(f"\nDati salvati: {len(df)} record\n")

    # 2. Analisi esplorativa
    print("Step 2: Analisi esplorativa...")
    print(df.head())
    print(f"\nColonne disponibili: {df.columns.tolist()}")
    print(f"\nPaesi presenti: {df['flag'].unique() if 'flag' in df.columns else 'N/A'}")

    # 3. Visualizzazioni
    print("\nStep 3: Creazione visualizzazioni...")
    viz = FishingVisualizer(df)

    print("- Creando heatmap...")
    viz.create_heatmap()

    print("- Creando grafico temporale...")
    viz.plot_temporal_trends()

    print("- Creando confronto per paese...")
    viz.plot_country_comparison()

    print("\n✅ Completato! Controlla la cartella outputs/")


if __name__ == "__main__":
    main()
