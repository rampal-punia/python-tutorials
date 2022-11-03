from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="app-name-here")
location = geolocator.geocode("Paris")

print(f"Address: {location.address}")
# Output: Address: Paris, Île-de-France, France métropolitaine, France

print(f"Lat, Lon: {location.latitude, location.longitude}")
# Lat, Lon: (48.8588897, 2.3200410217200766)

print(location.raw)
# {'place_id': 297522875, 'licence': 'Data © OpenStreetMap contributors,
#  ODbL 1.0. https://osm.org/copyright', 'osm_type': 'relation', 'osm_id': 7444,
#  'boundingbox': ['48.8155755', '48.902156', '2.224122', '2.4697602'],
# 'lat': '48.8588897', 'lon': '2.3200410217200766', 'display_name': 'Paris,
# Île-de-France, France métropolitaine, France', 'class': 'boundary',
# 'type': 'administrative', 'importance': 0.9417101715588673,
# 'icon': 'https://nominatim.openstreetmap.org/ui/mapicons/poi_boundary_administrative.p.20.png'}
