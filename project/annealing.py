import pandas as pd
import numpy as np
from scipy.spatial import distance_matrix
from random import randint
import copy
import matplotlib.pyplot as plt
import pickle

df = pd.read_csv('data/final_data.csv')
df = df[df['how_many_legoshops'] == 0].reset_index(drop=True)

coordinates = df[['latitude', 'longitude']].to_numpy()
distance_matrix_result = distance_matrix(coordinates, coordinates)
distance = pd.DataFrame(distance_matrix_result)

def cost(route):
    return sum([distance.iloc[route[i-1]][route[i]] for i in range(1, len(route))])

def simulated_annealing(route, T=100, alpha=0.999, stopping_T=0.0001, stopping_iter=100000):
    iter = 1
    while T >= stopping_T and iter < stopping_iter:
        candidate = list(route)
        l = randint(2, len(route) - 1)
        i = randint(0, len(route) - l)
        candidate[i:(i+l)] = reversed(candidate[i:(i+l)])
        F = cost(route)
        F_new = cost(candidate)
        if np.random.rand() < np.exp((F - F_new) / T):
            route = copy.deepcopy(candidate)
        T *= alpha
        iter += 1
    return route

start_city = df[df['name'] == 'Kraków'].index[0]
remaining_cities = list(set(df.index) - {start_city})
route = [start_city] + remaining_cities + [start_city]

optimal_route = simulated_annealing(route)
optimal_cost = cost(optimal_route)

print(f'Optymalna trasa: {optimal_route}')
print(f'Koszt optymalnej trasy: {optimal_cost}')

with open('map.pkl', 'rb') as f:
    fig = pickle.load(f)
    
for i in optimal_route:
    try:
        x1 = df.iloc[i, 3]
        x2 = df.iloc[i+1, 3]
        y1 = df.iloc[i, 4]
        y2 = df.iloc[i+1, 4]
        plt.plot([y1, y2], [x1, x2])
    except:
        break
plt.show()