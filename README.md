# Mediterranean Fishing Activity Tracker
## Visualizzazione dell'attività di pesca nel Mediterraneo Occidentale

Un progetto per esplorare e visualizzare i dati di Global Fishing Watch nel Mediterraneo, con focus sull'area tra Sardegna, Baleari e costa catalana.

---

## 🎯 Obiettivi del Progetto

- Visualizzare l'attività di pesca nel Mediterraneo occidentale
- Analizzare i pattern temporali (stagionalità, trend)
- Identificare le aree più pescate
- Comparare attività tra diversi paesi (Spagna, Italia, Francia)

---

## 🛠️ Setup

### Prerequisiti
```bash
# Crea ambiente virtuale
python -m venv venv
source venv/bin/activate  # Su Windows: venv\Scripts\activate

# Installa dipendenze
pip install -r requirements.txt
```

### Ottieni API Key
1. Vai su https://globalfishingwatch.org/our-apis/
2. Crea account gratuito
3. Genera API token
4. Crea file `.env`:
```
GFW_API_TOKEN=your_token_here
```

---

## 📁 Struttura Progetto

```
mediterranean-fishing/
│
├── .env                    # API token (NON committare!)
├── .gitignore             
├── README.md              
├── requirements.txt       
│
├── data/                   # Dati scaricati (git ignored)
│   └── raw/
│
├── notebooks/              # Jupyter per esplorazione (to-do)
│   └── exploration.ipynb
│
├── src/
│   ├── __init__.py
│   ├── data_fetcher.py    # Scarica dati da GFW
│   ├── analyzer.py        # Analisi dati (to-do)
│   └── visualizer.py      # Creazione visualizzazioni
│
└── outputs/                # Mappe e grafici (git ignored)
    ├── maps/
    └── charts/
```
---

## 📊 Prossimi Step

### Quick Wins:
1. ✅ Setup ambiente e scarica primi dati
2. ✅ Prima visualizzazione
3. ✅ GitHub con README

### Miglioramenti Fase 2:
- [ ] Aggiunta layer Marine Protected Areas
- [ ] Filtro per tipo di pesca (trawling, longline, etc)
- [ ] Analisi stagionalità
- [ ] Identificare hotspots

### Fase 3 - Portfolio Project:
- [ ] Dashboard interattiva
- [ ] API per query custom per visualizzazione e report automatici
- [ ] Deploy online
- [ ] Documentazione completa

---

## 📚 Risorse Utili

**Documentazione GFW:**
- API Docs: https://globalfishingwatch.org/our-apis/documentation
- Python Client: https://github.com/GlobalFishingWatch/gfwapi-python-client
- Datasets: https://globalfishingwatch.org/datasets-and-code/

**Dataset Complementari:**
- Marine Protected Areas: https://www.protectedplanet.net/
- Sea Surface Temperature: NOAA datasets
- Bathymetry: GEBCO

**WILDLABS:**
- Aggiunta feedback sull'analisi e apri a proposte di reports

---

## 🚨 Note Importanti

1. **API Limits**: Il piano gratuito ha limiti di rate e volume
2. **Performance**: Per grandi volumi usa chunking e caching