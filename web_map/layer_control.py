import folium
import pandas

def get_icon_color(elev):
    if elev <= 1000:
        return "green"
    elif 1000 <= elev < 2000:
        return "blue"
    elif 2000 <= elev < 3000:
        return "orange"
    else:
        return "red"

v_data = pandas.read_csv("Volcanoes_USA.txt")
latitudes = list(v_data["LAT"])
longitudes = list(v_data["LON"])
elevations = list(v_data["ELEV"])
names = list(v_data["NAME"])
locations = list(v_data["LOCATION"])
statuses = list(v_data["STATUS"])
types = list(v_data["TYPE"])

fgv = folium.FeatureGroup(name="volcanoes")
for lat, lon, el, nm, loc, stat, tp in zip(latitudes, longitudes, elevations, names, locations, statuses, types):
    popup = "Name: " + nm + " " + "Location: " + loc + " " + "Status: " + stat + " " + "Type: " + tp + " " + "Elevation: " + str(el) + " m"
    # fg.add_child(folium.Marker(location=[lat, lon], popup=folium.Popup(popup, parse_html=True), icon=folium.Icon(color=get_icon_color(el))))
    fgv.add_child(folium.CircleMarker(location=[lat, lon],
        radius=6,
        color='grey',
        fill=True,
        popup=folium.Popup(popup, parse_html=True),
        fill_opacity=0.7,
        fill_color=get_icon_color(el)))

fgp = folium.FeatureGroup("population")
fgp.add_child(folium.GeoJson(data=open("world.json", 'r', encoding="utf-8-sig").read(),
    style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
        else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000
        else 'red'}))

map = folium.Map(location=[38.862483, -100.404581], zoom_start=5, tiles="Mapbox Bright")
map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("layer_control.html")
