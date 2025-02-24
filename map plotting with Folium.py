import folium as fl
import pandas as pd
import json

df = pd.read_csv("D:\Open Classroom\web-map-master\web-map-master\stadium.csv", encoding = "latin1")

lat = list(df["LAT"])
lon = list(df["LON"])
sno = list(df["sno"])
name = list(df["NAME"])
loc = list(df["LOCATION"])
web = list(df["website"])
pic = list(df["picture"])
cap = list(df["capacity"])

fg = fl.FeatureGroup("my map")

#fg = json.load(open("D:\Open Classroom\web-map-master\web-map-master\india_states.json"))

fg.add_child(fl.GeoJson(data = (open("D:\Open Classroom\web-map-master\web-map-master\india_states.json", mode = "r", encoding='utf-8').read())))

for lt, ln, sn, nm, lc, wb, pc, cp in zip(lat, lon, sno, name, loc, web, pic, cap):
	fg.add_child(fl.Marker(location = [lt, ln], popup = "<b> name: </b>" + nm + "</br><b> capacity: </b>" + str(cp) + "<br><b> wikipedia link: </b><a href>" + wb + "click here</a>" + "<br> <img src=" + str(pic) + "height = 142 width = 290>", icon = fl.Icon(color = 'green')))

map = fl.Map(location = [21.1458, 79.0882], zoom_start = 5)

map.add_child(fg)
map.save("testmap.html") 
#"<br> <img src="+pic+" height=142 width=290>",icon=folium.Icon(color='green')