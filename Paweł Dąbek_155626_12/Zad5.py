from bs4 import BeautifulSoup
import urllib3
import pandas as pd
from zad4 import get_data_from_page

column_names = ["Tytuł", "Platforma", "Data wydania", "Ocena"]
final_df = pd.DataFrame(columns=column_names)
frames = []

for x in range(0, 10):
    url = "https://www.metacritic.com/browse/games/genre/metascore/strategy/all?view=detailed&page=" + str(x)
    http = urllib3.PoolManager()
    page = http.request("GET", url)
    soup = BeautifulSoup(page.data, 'lxml')

    t, p, rd, s = get_data_from_page()

    d = {"Tytuł": t, "Platforma": p, "Data wydania": rd,
         "Ocena": s}
    df = pd.DataFrame(data=d)
    frames.append(df)

final_df = pd.concat(frames).reset_index(drop=True)
top_10_PC = final_df.loc[final_df["Platforma"] == "PC"].head(10)
print(top_10_PC.reset_index())