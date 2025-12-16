import pandas as pd
import glob
import os



def loading_data():
    

    # 1. Definiujemy wzorzec ścieżki
    # ".." - wyjdź folder wyżej
    # "data/raw" - wejdź do danych
    # "apartments_pl_*.csv" - znajdź wszystko co zaczyna się od "apartments_pl_" i kończy ".csv"
    sciezka = os.path.join("..", "data", "raw", "apartments_pl_*.csv")
    sciezka_rent = os.path.join("..", "data", "raw", "apartments_rent_pl_*.csv")
    
    # 2. Glob tworzy listę wszystkich plików pasujących do wzorca
    appartaments_files = glob.glob(sciezka)
    appartaments_rent_files = glob.glob(sciezka_rent)
    
    
    # Zabezpieczenie: sprawdź czy cokolwiek znaleziono
    if len(appartaments_files) == 0 or len(appartaments_rent_files) == 0:
        print("❌ Nie znaleziono plików! Sprawdź ścieżkę.")
    else:
        # 3. Wczytujemy wszystkie pliki do listy (List Comprehension)
        # To jest pętla w jednej linii - bardzo "Pythonic" sposób
        appartaments = [pd.read_csv(file) for file in appartaments_files]
        appartaments_rent = [pd.read_csv(file) for file in appartaments_rent_files]
        # 4. Łączymy (konkatenacja) w jedną wielką ramkę
        # ignore_index=True jest WAŻNE - inaczej miałbyś powtórzone indeksy (0,1,2... 0,1,2...)
        df_apps = pd.concat(appartaments, ignore_index=True)
        df_rent = pd.concat(appartaments_rent, ignore_index = True)
    
       
        if __name__ == '__main__':
            
            # Opcjonalnie: Zapisz połączony plik do folderu processed, żeby nie robić tego za każdym razem
            sciezka_zapis_apps = os.path.join("..", "data", "processed", "mieszkania_sell.csv")
            sciezka_zapis_apps_rent = os.path.join("..", "data", "processed", "mieszkania_sell_rent.csv")
            
            # Tworzymy folder processed jeśli nie istnieje
            os.makedirs(os.path.dirname(sciezka_zapis_apps), exist_ok=True)
            os.makedirs(os.path.dirname(sciezka_zapis_apps_rent), exist_ok=True)
            
            df_apps.to_csv(sciezka_zapis_apps, index=False)
            print(f"💾 Zapisano połączony plik w: {sciezka_zapis_apps}")
            df_rent.to_csv(sciezka_zapis_apps_rent, index=False)
            print(f"💾 Zapisano połączony plik w: {sciezka_zapis_apps_rent}")
            
    return df_apps, df_rent


loading_data()