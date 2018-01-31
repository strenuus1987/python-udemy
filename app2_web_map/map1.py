import folium
map = folium.Map(location=[50.432690, 30.489874], zoom_start=10, tiles="Mapbox Bright")

feature_group = folium.FeatureGroup(name = "My Map")

for coordinates in [[50.2, 30.1], [52.2, 31.1], [49.2, 29.1]]:
    feature_group.add_child(folium.Marker(location=coordinates, popup="Hi I am a marker", icon=folium.Icon(color='green')))

map.add_child(feature_group)

map.save("Map1.html")
