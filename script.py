import folium
import pandas

#reading data from text file using pandas
df=pandas.read_csv("Volcanoes-USA.txt")
#creating a map 
map=folium.Map(location=[45.372,-121.697],zoom_start=4,tiles='Stamen Terrain')

#adding marker to map
for lat,lon,name in zip(df['LAT'], df['LON'], df['NAME']):
 map.add_child(folium.Marker(location=[lat,lon],popup=name))


#saving the map as html file
map.save(outfile='test.html',close_file=True)