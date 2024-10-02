import pandas as pd
import numpy as np
import pickle
import matplotlib.pyplot as plt

with open('map.pkl', 'rb') as f:
    fig = pickle.load(f)
df = pd.read_csv("data/final_data.csv")

df = df[df["how_many_legoshops"]==0]
df.set_index('name', inplace=True)

def find_closest_city(city):
    distances = np.sqrt(((df[['latitude', 'longitude']]
                          .astype(float) 
                          - city[['latitude', 'longitude']]
                          .astype(float))**2)
                          .sum(axis=1))
    return distances.idxmin()

route = ["Kraków"]
starting_city = df.loc["Kraków"]

for _ in range(30):
    closest_city_name = find_closest_city(starting_city)
    closest_city = df.loc[closest_city_name]
    
    plt.plot([starting_city['longitude'], closest_city['longitude']], 
             [starting_city['latitude'], closest_city['latitude']])
    
    route.append(closest_city_name)
    starting_city = closest_city
    df.drop(closest_city_name, inplace=True)

print(route)
plt.show()
