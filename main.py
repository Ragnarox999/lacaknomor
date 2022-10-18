import phonenumbers
import opencage
import folium
from myphone import number 

from phonnumbers import geocoder

pepnumber = phonenumbers.parse(number)
location = geocoder.description_for_number(pepnumber, "en")
print(location)

from phonenumbers import carrier
service_pro = phonnumbers.parse(number)
print(carrier.name_for_number(service_pro, "en"))

from opencage.geocoder import OpenCageGeocode

key = 'a9c5b28233c43f8bd91a9030c674898d'

geocoder = OpenCageGeocode(key)
query = str(location)
result = geocoder.geocode(query)
#print(result)

lat = results[0]['geometry']['lat']
lng = result[0]['geometry']['lng']

print(lat,lng)

myMap folium.Map(location[lat,lng], zoom_start=9)
folium.marker([lat, lang]. popup=location).add_to(myMap)
mayMap.save("Mylocation.html")
