import folium
import pandas

#reading data from text file using pandas
df=pandas.read_csv("Volcanoes-USA.txt")

avr_lat=df['LAT'].mean()
avr_lon=df['LON'].mean()

#creating a map 
map=folium.Map(location=[avr_lat,avr_lon],zoom_start=4,tiles='Stamen Terrain')

#adding marker to map
for lat,lon,name in zip(df['LAT'], df['LON'], df['NAME']):
 map.add_child(folium.Marker(location=[lat,lon],popup=name))


#saving the map as html file
map.save(outfile='test.html',close_file=True)