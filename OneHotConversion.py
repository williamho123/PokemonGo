import keras.utils
import numpy as np

"""The attributes are ordered as such:
latitude, longitude, appearedLocalTime, appearedTimeOfDay, terrainType, closeToWater,
city, continent, weather, temperature, windSpeed, windBearing, pressure, population_density,
urban, suburban, midurban, rural, gymDistanceKm, pokestopDistanceKm, class
"""
def GenerateDataAndLablesFromCsv(filename):
	raw_data = np.genfromtxt(filename, delimiter=',')
	lat, long, aLT, aTD, tT, cTW, city, cont, weath, temp, wS, wB, press, pD, urb, suburb, midurb, rural, gDKm, pDKm, cl = raw_data.T
	converted_data = np.column_stack((lat, long))
	converted_data = np.column_stack((converted_data, aLT))
	converted_data = np.column_stack((converted_data, aTD))
	converted_data = np.column_stack((converted_data, tT))
	converted_data = np.column_stack((converted_data, cTW))
	city = keras.utils.to_categorical(city)
	converted_data = np.column_stack((converted_data, city))

	continent = keras.utils.to_categorical(cont)
	converted_data = np.column_stack((converted_data, continent))
	weather = keras.utils.to_categorical(weath)

	converted_data = np.column_stack((converted_data, weather))
	converted_data = np.column_stack((converted_data, temp))
	converted_data = np.column_stack((converted_data, wS))
	converted_data = np.column_stack((converted_data, wB))
	converted_data = np.column_stack((converted_data, press))
	converted_data = np.column_stack((converted_data, pD))
	converted_data = np.column_stack((converted_data, urb))
	converted_data = np.column_stack((converted_data, suburb))
	converted_data = np.column_stack((converted_data, midurb))
	converted_data = np.column_stack((converted_data, rural))
	converted_data = np.column_stack((converted_data, gDKm))
	converted_data = np.column_stack((converted_data, pDKm))
	converted_data = np.column_stack((converted_data, cl))

	return converted_data

GenerateDataAndLablesFromCsv('./data/DataV5.csv')
