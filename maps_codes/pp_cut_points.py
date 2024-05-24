# -*- coding: utf-8 -*-

import pandas as pd
import geo_2024 as geo
import ast
import folium
import itertools


def get_segments(polyline):

    number_of_vertices = len(polyline)

    segments = []
    for count in range(1, number_of_vertices):
        p_1 = polyline[count - 1]
        p_2 = polyline[count]

        segments.append([p_1, p_2])

    return segments

df = pd.read_csv("DATASET.csv")

code = 'FRA'
h = 7
cell = f"hour{h}"

m = folium.Map( 
    location=[40.965, -5.664], 
    zoom_start=2, 
) 

airs = df['carrier'].unique()
colors = ["red", "yellow", "green", "blue", "orange", "purple", "pink"]
dic_airs = {x:y for x,y in zip(airs, colors)}

lines = []
for i,row in df.iterrows():
    if len(row[cell]) > 2:
        ini = ast.literal_eval(row["coords_i"])
        fin = ast.literal_eval(row["coords_f"])
        lines.append([ini,fin])
    
    #folium.PolyLine([ini,fin], color="grey", weight=1).add_to(m)
    #folium.Circle(ini, color="red", radius=30).add_to(m)
    #folium.Circle(fin, color="red",radius=30).add_to(m)
            
            #pop = f"{row['code_i']} to {row['code_f']} \n {row['carrier']} \n {row['number']}"
            #folium.Circle(ast.literal_eval(row[cell]), popup=pop, radius = 1000,color = dic_airs[row["carrier"]]).add_to(m)
  
number_of_polylines = len(lines)

print(number_of_polylines)

pairs = list(itertools.combinations(range(number_of_polylines), 2))

# Compute all intersections

intersections = []

for pair in pairs:

    segments_1 = get_segments(lines[pair[0]])
    segments_2 = get_segments(lines[pair[1]])
    
    count = 0

    for segment_1 in segments_1:
        p_1, p_2 = segment_1

        for segment_2 in segments_2:
            p_3, p_4 = segment_2

            # Intersection
            intersection = geo.utilities.intersect(p_1, p_2, p_3, p_4)

            if intersection is None:
                continue
            
            if intersection[-1] == True:
                intersections.append(intersection[:2])


for i in lines:
    folium.PolyLine(i, color="grey", weight=1).add_to(m)


for i in intersections:
    folium.Circle(i, color="green",radius=30).add_to(m)

m.save("MAPA2.html")

