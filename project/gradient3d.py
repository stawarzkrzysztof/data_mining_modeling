import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.stats import multivariate_normal
import pandas as pd
from matplotlib.animation import FuncAnimation

df = pd.read_csv("data/final_data.csv")
df = df.query("how_many_legoshops == 0")

krk = df[df["name"] == "Kraków"]
krk_lat = float(krk["latitude"])
krk_lon = float(krk["longitude"])

df = df.query("name != 'Kraków'")

longitude = np.array(df["longitude"])
latitude = np.array(df["latitude"])
population = np.array(df["population"])

# change grid number
grid_x, grid_y = np.meshgrid(np.linspace(min(longitude), max(longitude), 1000),
                             np.linspace(min(latitude), max(latitude), 1000))

grid_z = np.zeros_like(grid_x)

for lon, lat, pop in zip(longitude, latitude, population):
    mean = [lon, lat]
    cov = np.eye(2) / 10  # <- change gauss steapness 
    gaussian_distribution = multivariate_normal(mean, cov)
    grid_z += pop * gaussian_distribution.pdf(np.dstack((grid_x, grid_y)))

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d', computed_zorder=False)

ax.plot_surface(grid_x, grid_y, grid_z)

x_idx = np.abs(grid_x[0] - krk_lon).argmin()
y_idx = np.abs(grid_y[:, 0] - krk_lat).argmin()
krk_z = grid_z[y_idx, x_idx]

ax.scatter(krk_lon, krk_lat, krk_z, c="red", s=50)

ax.set_xlabel('Długość geograficzna')
ax.set_ylabel('Szerokość geograficzna')
ax.set_zlabel('Populacja')

def gradient(x, y, z):
    dx = x[1:, 1:] - x[:-1, :-1]
    dy = y[1:, 1:] - y[:-1, :-1]
    dz = z[1:, 1:] - z[:-1, :-1]
    return dx, dy, dz

def gradient_ascent(x_start, y_start, z_start, dx, dy, dz, num_iterations=100):
    path = [(x_start, y_start, z_start)]
    for _ in range(num_iterations):
        grad_x = np.interp(x_start, dx[0], dx[1])
        grad_y = np.interp(y_start, dy[0], dy[1])
        grad_z = np.interp(z_start, dz[0], dz[1])
        x_start += grad_x
        y_start += grad_y
        z_start += grad_z
        path.append((x_start, y_start, z_start))
    return np.array(path)

dx, dy, dz = gradient(grid_x, grid_y, grid_z)
path = gradient_ascent(krk_lon, krk_lat, krk_z, dx, dy, dz)
line, = ax.plot([], [], [], lw=2)

def init():
    line.set_data([], [])
    line.set_3d_properties([])
    return line,

def animate(i):
    line.set_data(path[:i, 0], path[:i, 1])
    line.set_3d_properties(path[:i, 2])
    return line,

ani = FuncAnimation(fig, animate, init_func=init, frames=len(path), interval=200, blit=True)
plt.show()
