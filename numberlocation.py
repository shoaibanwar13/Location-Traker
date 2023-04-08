import phonenumbers

from number import number
from phonenumbers import geocoder,timezone,carrier
import folium
mynumber=phonenumbers.parse(number)
yourlocation=geocoder.description_for_number(mynumber,"en")
print(yourlocation)
Key="feacb2590cab4513be053a2be968e01a"


from phonenumbers import carrier

service_provider=phonenumbers.parse(number)
print(carrier.name_for_number(service_provider,"en"))
from opencage.geocoder import OpenCageGeocode
geocoder=OpenCageGeocode(Key)
query=str(yourlocation)
result=geocoder.geocode(query)
print(result)
lat=result[0]['geometry']['lat']
lng=result[0]['geometry']['lng']
print(lat,lng)
myMap=folium.Map(location=[lat,lng],zoom_start=9)
folium.Marker([lat,lng],popup=yourlocation).add_to((myMap))
myMap.save("myLocation.html")
