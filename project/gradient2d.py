import pandas as pd
import numpy as np
import matplotlib
from matplotlib import pyplot as plt
import seaborn as sns
import warnings
from IPython.display import set_matplotlib_formats
import matplotlib.image as mpimg
import pickle
from matplotlib.animation import FuncAnimation

warnings.filterwarnings("ignore")
set_matplotlib_formats('svg')
# sns.set_style(style="darkgrid")

df = pd.read_csv("data/final_data.csv")

df['population'] = df['population'] / df['population'].max()
df['how_many_legoshops'] = df['how_many_legoshops'] / df['how_many_legoshops'].max()

# Inicjalizacja pozycji samochodzika
car_position = [np.random.uniform(df['latitude'].min(), df['latitude'].max()), 
                np.random.uniform(df['longitude'].min(), df['longitude'].max())]

# car_position = [np.cfloat(df.query("name=='Kraków'")["latitude"]), 
#                 np.cfloat(df.query("name=='Kraków'")["longitude"]), ]

learning_rate = 0.01  
iterations = 1000  

lat_min, lat_max = 49.0, 54.9
lon_min, lon_max = 14.1, 24.1

MAX_N, MAX_S, MAX_W, MAX_E = 54.8399, 49.0025, 14.1226, 24.1455
fig, ax = plt.subplots(figsize=(7, 7))
img = plt.imread("assets/Poland.png")
plt.imshow(img, extent=[MAX_W, MAX_E, MAX_S, MAX_N], aspect="auto", alpha=.3)
plt.xticks(range(14, 25))
plt.yticks(range(49, 55))

norm_pop = (df['population']-df['population'].min())/(df['population'].max()-df['population'].min())
min_size, max_size = 10, 300
scaled_sizes = min_size + (max_size - min_size) * norm_pop

point_colors = list(df["how_many_legoshops"].apply(lambda x: "red" if x>=1 else "black"))
step = 1.  # both axis tick step

plt.scatter(data=df, x="longitude", y="latitude", c=point_colors, s=scaled_sizes, 
            edgecolors='white', linewidth=1)
car_dot, = plt.plot([], [], 'bo', markersize=10)  # Samochodzik jako niebieski kropka

def update(i):
    global car_position
    gradients = np.zeros(2)
    
    for _, city in df.iterrows():
        distance = np.sqrt((car_position[0] - city['latitude'])**2 + (car_position[1] - city['longitude'])**2)
        
        grad = np.array([car_position[0] - city['latitude'], car_position[1] - city['longitude']])
        grad /= distance  # normalization
        
        grad *= city['population']
        
        if city['how_many_legoshops'] > 0 and distance < 0.01:  
            grad *= -1  
        
        gradients += grad
    

    gradients = gradients / np.linalg.norm(gradients)
    
    car_position += learning_rate * gradients
    
    car_position[0] = max(min(car_position[0], lat_max), lat_min)
    car_position[1] = max(min(car_position[1], lon_max), lon_min)
    
    car_dot.set_data(car_position[1], car_position[0])

ani = FuncAnimation(fig, update, frames=range(iterations), repeat=False)

plt.show()