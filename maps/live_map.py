import folium

def create_map(lat,lon):

    m = folium.Map(location=[lat,lon],zoom_start=10)

    folium.Marker(
        [lat,lon],
        popup="High Disaster Risk Area",
        icon=folium.Icon(color="red")
    ).add_to(m)

    folium.Circle(
        radius=5000,
        location=[lat,lon],
        color="red",
        fill=True
    ).add_to(m)

    m.save("disaster_map.html")
