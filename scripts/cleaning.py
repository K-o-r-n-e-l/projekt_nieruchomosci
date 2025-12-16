import pandas as pd
from loading_data import loading_data
import os


df_apps, df_rent = loading_data()




print("\nBraki danych (ilość pustych pól) dla df_apps:")
print(df_apps.isnull().sum())



print("\nBraki danych (ilość pustych pól) dla df_rent:")
print(df_rent.isnull().sum())


df_apps = df_apps.fillna("unknown")
df_rent = df_rent.fillna("unknown")



if __name__ == '__main__':
    sciezka_zapis_apps = os.path.join("..", "data", "processed", "mieszkania_sell.csv")
    sciezka_zapis_apps_rent = os.path.join("..", "data", "processed", "mieszkania_sell_rent.csv")
    df_apps.to_csv(sciezka_zapis_apps, index=False)
    print(f"💾 Zapisano połączony plik w: {sciezka_zapis_apps}")
    df_rent.to_csv(sciezka_zapis_apps_rent, index=False)
    print(f"💾 Zapisano połączony plik w: {sciezka_zapis_apps_rent}")