from folium import Map, Marker, Icon, FeatureGroup, LayerControl
ca = Map(location=[36.778259, -119.417931],zoom_start=6)
la = Map(location=[34.052235, -118.243683],zoom_start=8)
z = Map(location=[34.052235, -118.243683],zoom_start=11)
m = Map(location=[34.052187,-118.243425],zoom_start=15) # ,tiles='stamentoner')
# Function to create marker and legend:
def marker(legend,lst,icon_prefix,icon,col,map_toadd):
    legend = FeatureGroup(name=legend).add_to(map_toadd)
    for coor in lst[1]:
        ih = Marker(location=coor, icon=Icon(color=col, prefix=icon_prefix,icon=icon)).add_to(legend)