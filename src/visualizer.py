import plotly.express as px
import folium
from folium.plugins import HeatMap


class FishingVisualizer:
    """Crea visualizzazioni dei dati di pesca"""

    def __init__(self, df):
        self.df = df

    def create_heatmap(self, output_path="outputs/maps/fishing_heatmap.html"):
        """Mappa di calore dell'attività di pesca"""

        # Centro mappa sul Mediterraneo
        m = folium.Map(
            location=[41.5, 5.0],  # Centro tra Sardegna e Barcellona
            zoom_start=6,
            tiles="OpenStreetMap",
        )

        # Prepara dati per heatmap
        # Assumendo colonne 'lat', 'lon', 'hours'
        heat_data = [
            [row["lat"], row["lon"], row["hours"]] for idx, row in self.df.iterrows()
        ]

        HeatMap(
            heat_data,
            min_opacity=0.3,
            radius=15,
            blur=20,
            max_zoom=10,
        ).add_to(m)

        # Aggiungi layer con confini MPAs se disponibili
        # self._add_mpa_layer(m)

        m.save(output_path)
        print(f"Mappa salvata: {output_path}")
        return m

    def plot_temporal_trends(self):
        """Grafico trends temporali"""

        # Assumendo colonna 'date' e 'hours'
        daily = self.df.groupby("date")["hours"].sum().reset_index()

        fig = px.line(
            daily,
            x="date",
            y="hours",
            title="Attività di Pesca nel Tempo - Mediterraneo Occidentale",
            labels={"hours": "Ore di Pesca", "date": "Data"},
        )

        fig.update_layout(
            xaxis_title="Data", yaxis_title="Ore di Pesca Totali", hovermode="x unified"
        )

        fig.write_html("outputs/charts/temporal_trends.html")
        fig.show()
        return fig

    def plot_country_comparison(self):
        """Confronto attività per paese"""

        # Assumendo colonna 'flag' per paese
        by_country = self.df.groupby("flag")["hours"].sum().reset_index()
        by_country = by_country.sort_values("hours", ascending=False)

        fig = px.bar(
            by_country,
            x="flag",
            y="hours",
            title="Attività di Pesca per Paese",
            labels={"flag": "Bandiera", "hours": "Ore di Pesca Totali"},
            color="hours",
            color_continuous_scale="Blues",
        )

        fig.write_html("outputs/charts/country_comparison.html")
        fig.show()
        return fig

    def plot_spatial_distribution(self):
        """Scatter plot geografico con intensità"""

        fig = px.scatter_geo(
            self.df,
            lat="lat",
            lon="lon",
            color="hours",
            size="hours",
            hover_data=["flag", "vessel_name"],
            title="Distribuzione Geografica Attività di Pesca",
            color_continuous_scale="Reds",
        )

        # Zoom sul Mediterraneo
        fig.update_geos(
            scope="europe", center=dict(lat=41.5, lon=5.0), projection_scale=8
        )

        fig.write_html("outputs/charts/spatial_distribution.html")
        fig.show()
        return fig
