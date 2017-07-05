import folium
#creating a map 
map=folium.Map(location=[45,-121],zoom_start=12)
#adding marker to map
map.add_child(folium.Marker(location=[45.32,-121.66],popup='Mt hood'))
map.add_child(folium.Marker(location=[44,-120.66],popup='Mt hood'))
#saving the map as html file
map.save(outfile='test.html',close_file=True)