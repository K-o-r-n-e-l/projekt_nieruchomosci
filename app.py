import streamlit as st
import pandas as pd
import os

# 1. Konfiguracja strony (musi być na samym początku)
st.set_page_config(page_title="Analiza Nieruchomości", layout="wide")

# 2. Funkcja do wczytywania danych (z cache, żeby nie ładować za każdym razem od nowa)
@st.cache_data
def load_data():
    # Ścieżka do Twojego wyczyszczonego pliku
    path = os.path.join("data", "processed", "mieszkania_sell.csv")
    df = pd.read_csv(path)
    return df

# Wczytujemy dane
df = load_data()

# --- PASEK BOCZNY (FILTRY) ---
st.sidebar.header("Filtry")

# Filtr miasta
dostepne_miasta = sorted(df['city'].unique())
miasto = st.sidebar.selectbox("Wybierz miasto", dostepne_miasta, index=dostepne_miasta.index("Warszawa") if "Warszawa" in dostepne_miasta else 0)

# Filtr ceny
min_price = int(df['price'].min())
max_price = int(df['price'].max())

ceny = st.sidebar.slider("Zakres cenowy (zł)", min_price, max_price, (min_price, 1000000))

# --- GŁÓWNA CZĘŚĆ STRONY ---
st.title(f"📍 Rynek Nieruchomości: {miasto}")

# Filtrujemy dane
maska = (df['city'] == miasto) & (df['price'] >= ceny[0]) & (df['price'] <= ceny[1])
df_filtered = df[maska]

# Pokazujemy podstawowe statystyki (Metryki)
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Liczba ofert", len(df_filtered))
with col2:
    srednia_cena = df_filtered['price'].mean()
    st.metric("Średnia cena", f"{srednia_cena:,.0f} zł".replace(",", " "))
with col3:
    srednia_metr = df_filtered['price_per_m2'].mean()
    st.metric("Średnia cena za m²", f"{srednia_metr:,.0f} zł".replace(",", " "))

# --- MAPA (To jest Twój atut geoprzestrzenny!) ---
st.subheader("Mapa ofert")
# Streamlit automatycznie szuka kolumn 'latitude' i 'longitude'
st.map(df_filtered)

# --- TABELA ---
with st.expander("Pokaż szczegółowe dane (Tabela)"):
    st.dataframe(df_filtered[['city', 'price', 'squareMeters', 'floor', 'buildYear']])
