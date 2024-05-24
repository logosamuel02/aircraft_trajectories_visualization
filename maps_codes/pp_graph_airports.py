# -*- coding: utf-8 -*-

import pandas as pd
import ast
import folium


df = pd.read_csv("DATASET.csv")

code = 'FRA'
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
    ini = ast.literal_eval(row["coords_i"])
    fin = ast.literal_eval(row["coords_f"])
    folium.PolyLine([ini,fin], color="grey", weight=1).add_to(m)
    folium.Circle(ini, color="red", radius=30).add_to(m)
    folium.Circle(fin, color="red",radius=30).add_to(m)
            
            #pop = f"{row['code_i']} to {row['code_f']} \n {row['carrier']} \n {row['number']}"
            #folium.Circle(ast.literal_eval(row[cell]), popup=pop, radius = 1000,color = dic_airs[row["carrier"]]).add_to(m)
    
m.save("MAPA5.html")

