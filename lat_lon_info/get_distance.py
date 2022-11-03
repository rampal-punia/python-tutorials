'''Python geopy example codes
From latitude, longitude to the location name.
'''

from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="app-name-here")
location = geolocator.reverse([48.8588897, 2.3200410217200766])

print(location)
# Output: 3, Rue Casimir Périer, Quartier des Invalides, Paris 7e Arrondissement,
# Faubourg Saint-Germain, Paris, Île-de-France, France métropolitaine, 75007, France
