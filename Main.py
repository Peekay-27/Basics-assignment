from Models import load_management
from utils import display_neighborhood,display_location_area


Power_supply = input(" Enter Your Location: ") 
neighborhood = {"Madina":455, "Sesemi":431, "East Legon":200, "North legon": 155, "Pantang":190}

management = load_management(neighborhood)
display_neighborhood(neighborhood)
print("\n Total Load: management.total_load ")
if management.total_load() > 500:
    management.shed_load()
    
location_area = management.get_location_area()
display_location_area(location_area)
print("\n Final Load:", management.total_load())