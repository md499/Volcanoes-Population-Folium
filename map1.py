import folium
import pandas
 
data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
name = list(data["NAME"])
loca = list(data["LOCATION"])



html = """
Volcano:%s
Height:%s m
Location:%s

"""

def color_producer(elevation):
    if elevation < 1000:
        return "blue"
    elif 1000 <= elevation < 3000:
        return "orange"
    else:
        return "red"




map = folium.Map(location=[38.58, -99.09], zoom_start=5, tiles="Stamen Terrain")


fgv=folium.FeatureGroup(name="Volcanoes")
for lt, ln, el, name, lc in zip(lat, lon, elev, name, loca):
    iframe = folium.IFrame(html=html % (name,el,lc), width=200, height=100)
    fgv.add_child(folium.CircleMarker(location=[lt, ln], radius= 9, popup=folium.Popup(iframe), fill_color=color_producer(el), color= "grey", fill_opacity=0.9))
    

fgp=folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(open('world.json', encoding='utf-8-sig').read(),style_function = lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000 else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}, name= "Population", tooltip = folium.GeoJsonTooltip(fields=('NAME', 'POP2005'),aliases=('Country','Population'), localize =True), show=True)).add_to(map)


map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("Map1.html")




#fg.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(iframe), icon = folium.Icon(color = color_producer(el))))


