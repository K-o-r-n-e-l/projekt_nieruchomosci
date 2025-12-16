import pandas as pd
import numpy as np
from loading_data import loading_data


df_apps, df_rent = loading_data()




print("\nBraki danych (ilość pustych pól):")
print(df_apps.isnull().sum())


df_apps = df_apps.fillna("unknown")