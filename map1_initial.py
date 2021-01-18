import folium
import pandas

data= pandas.read_csv("Volcanoes.txt")
lat=list(data["LAT"])
lon=list(data["LON"])
elev=list(data["ELEV"])

html = """
Volcano name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m
"""
 

map=folium.Map(location=[38.58,-99.09], zoom_start= 6, tiles= "Stamen Terrain")
fg= folium.FeatureGroup(name="My Map")

for lt,ln,el in zip(lat, lon, elev):
    iframe = folium.IFrame(html=html % (name, name, el), width=200, height=100)
    fg.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(iframe), icon = folium.Icon(color = "purple")))
 
   # fg.add_child(folium.Marker(location= [lt,ln], popup=str(el) + " m", icon=folium.Icon(color="purple")))

   

#for lt,ln in zip(lat, lon):
    #fg.add_child(folium.Marker(location= [lt,ln], popup="Hi I am a Marker", icon=folium.Icon(color="purple")))

#for coordinates in [[38.2,-99.1],[39.2,-97.1]]:
   # fg.add_child(folium.Marker(location= coordinates, popup="Hi I am a Marker!", icon=folium.Icon(color="purple")))

#map.add_child(folium.Marker(location=[38.2,-99.1], popup="Hi I am a Marker!", icon=folium.Icon(color="purple")))
#map.add_child(folium.Marker(location=[37.2,-97.1], popup="Hi I am a Marker!", icon=folium.Icon(color="purple")))


map.add_child(fg)

map.save("Map1.html")

