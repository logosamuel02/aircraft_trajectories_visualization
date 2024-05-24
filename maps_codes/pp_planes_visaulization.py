# -*- coding: utf-8 -*-

import pandas as pd
import ast
import folium


df = pd.read_csv("DATASET.csv")

h = 18
cell = f"hour{h}"

m = folium.Map( 
    location=[40.965, -5.664], 
    zoom_start=2, 
) 

airs = df['carrier'].unique()
colors = ["red", "yellow", "green", "blue", "orange", "purple", "pink"]
dic_airs = {x:y for x,y in zip(airs, colors)}

print(dic_airs)
for i,row in df.iterrows():
    try:
        pop = f"{row['code_i']} to {row['code_f']} \n {row['carrier']} \n {row['number']}"
        folium.Marker(ast.literal_eval(row[cell]), popup=pop, icon=folium.Icon(color=dic_airs[row["carrier"]])).add_to(m) 
    except:
        pass
    
m.save("MAPA.html")

