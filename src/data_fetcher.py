import os
from datetime import datetime
import pandas as pd
from dotenv import load_dotenv
import gfwapiclient as gfw

load_dotenv()


class GFWDataFetcher:
    """Fetcher per dati Global Fishing Watch"""

    def __init__(self):
        token = os.getenv("GFW_API_TOKEN")
        if not token:
            raise ValueError("GFW_API_TOKEN non trovato in .env")
        self.client = gfw.Client(access_token=token)

    async def get_fishing_effort(self, start_date, end_date, bbox):
        """
        Scarica dati fishing effort.

        bbox: geoJSON
        """

        print(f"Scaricando dati da {start_date} a {end_date}...")
        print(f"Area: {bbox}")

        try:
            # Nota: la sintassi esatta dipende dalla versione API
            # Consulta la doc ufficiale per parametri precisi
            data = await self.client.fourwings.create_fishing_effort_report(
                dataset="public-global-fishing-effort:latest",
                start_date=start_date,
                end_date=end_date,
                spatial_resolution="LOW",  # o 'high' per più dettaglio
                group_by="FLAG",
                temporal_resolution="DAILY",
                filters=["flag in ('ESP', 'FRA', 'ITA')"],
                geojson=bbox,
            )

            df = data.df()
            print(f"Scaricati {len(df)} record")
            return df

        except Exception as e:
            print(f"Errore durante download: {e}")
            print("Consulta la documentazione API per parametri aggiornati")
            return None

    def get_vessels_in_area(self, bbox=None, date=None):
        """Scarica informazioni sulle navi nell'area"""
        if bbox is None:
            bbox = [0.5, 38.5, 9.5, 44.0]

        if date is None:
            date = datetime.now().strftime("%Y-%m-%d")

        try:
            vessels = self.client.vessels.search_vessels(bbox=bbox, date=date)
            return pd.DataFrame(vessels)
        except Exception as e:
            print(f"Errore: {e}")
            return None
