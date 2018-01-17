import folium

fg = folium.FeatureGroup("population")
fg.add_child(folium.GeoJson(data=open("world.json", 'r', encoding="utf-8-sig").read(),
    style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
        else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000
        else 'red'}))

map = folium.Map(tiles="Mapbox Bright")
map.add_child(fg)
map.save("population.html")
