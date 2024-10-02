import pandas as pd
import numpy as np
from scipy.spatial import distance_matrix
from sklearn.utils import shuffle
import random

df = pd.read_csv('data/final_data.csv')

df = df[df['how_many_legoshops'] == 0].reset_index(drop=True)

df = df.sort_values(by='population', ascending=False)

df['coordinates'] = list(zip(df.latitude, df.longitude))
cities = df['coordinates'].tolist()
dist_matrix = distance_matrix(cities, cities)

def cost(route):
    return sum(dist_matrix[i, j] for i, j in zip(route[:-1], route[1:]))

def genetic_algorithm(df, n_generations, n_population):
    population = [shuffle(df.index.tolist()) for _ in range(n_population)]
    for _ in range(n_generations):
        population = sorted(population, key=cost)
        next_gen = population[:2]
        for _ in range(n_population - 2):
            parents = random.sample(population[:10], 2)
            split = np.random.randint(1, len(df)-1)
            child = np.concatenate((parents[0][:split], parents[1][split:]))
            next_gen.append(child)
        population = next_gen
    return min(population, key=cost)

route = genetic_algorithm(df, n_generations=1000, n_population=100)
with open("genetic_shit.txt", 'w') as f:
    f.write(str(route))
df.to_csv("genetic_more_shit.csv")
