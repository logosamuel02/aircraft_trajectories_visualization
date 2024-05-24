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
    if row["code_i"] == code:
        if len(row[cell]) > 2:
            x = int(row["inicial_hour"])
            y = int(row["final_hour"])
            line = []
            for j in range(x, y+1):
                c = f"hour{str(j)}"
                line.append(ast.literal_eval(row[c]))
            folium.PolyLine(line, color=dic_airs[row['carrier']]).add_to(m)
            
            #pop = f"{row['code_i']} to {row['code_f']} \n {row['carrier']} \n {row['number']}"
            #folium.Circle(ast.literal_eval(row[cell]), popup=pop, radius = 1000,color = dic_airs[row["carrier"]]).add_to(m)
    
m.save("MAPA4.html")

