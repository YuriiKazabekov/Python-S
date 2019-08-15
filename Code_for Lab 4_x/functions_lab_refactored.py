import math
import sys

planet_data = {"orbital_radius":{"Mercury": 58, "Venus": 108, "Earth": 150, "Mars": 228, "Jupiter": 778, "Saturn": 1429, "Uranus": 2871, "Neptune": 4504},
"orbital_speed": {"Mercury": 47.87, "Venus": 35.02, "Earth": 29.78, "Mars": 24.13, "Jupiter": 13.07, "Saturn": 9.69, "Uranus": 6.81, "Neptune": 5.43}}

planet1 = input("Planet 1: ")
planet2 = input("Planet 2: ")

def days_in_year(planet):
	'''
	Takes the name of planet as input, returns the number of days in a year on this planer (int)
	'''
	orbital_radius = planet_data['orbital_radius'][planet] * 1000000
	orbital_speed = planet_data['orbital_speed'][planet]
	
	planet_year = 2 * math.pi * orbital_radius / orbital_speed / (60 * 60 * 24)
	
	print ("The {} days in a year on {}".format(int(planet_year), planet))
	
	return int(planet_year)
	
def bigger_year():
	'''
	Determins which year is bigger of two given planets. Return the planet name with the bigger year.
	'''
	planet_days1 = days_in_year(planet1)
	planet_days2 = days_in_year(planet2)
	 
	is_bigger = planet1 if planet_days1 > planet_days2 else planet2
	
	print("The {} year is bigger".format(is_bigger))
	
bigger_year()
