import folium
#creating a map 
map=folium.Map(location=[45,-121],zoom_start=12)
#saving the map as html file
map.save(outfile='test.html',close_file=True)