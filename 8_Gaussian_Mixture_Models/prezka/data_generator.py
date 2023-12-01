import numpy as np
import pandas as pd
from sklearn.datasets import make_spd_matrix
from scipy.stats import multivariate_normal

# Ustalamy ziarno losowości dla powtarzalności wyników
np.random.seed(0)

# Generujemy dane z dwóch różnych rozkładów Gaussa
n_samples = 500
mean1 = [0, 0]
mean2 = [2, 2]
cov1 = [[0.5, 0], [0, 0.5]]  # Sferyczny kształt
cov2 = [[7, 0], [0, .5]]  # Wydłużony kształt

# Generujemy próbki
x1, y1 = np.random.multivariate_normal(mean1, cov1, n_samples).T
x2, y2 = np.random.multivariate_normal(mean2, cov2, n_samples).T

# Łączymy próbki
x = np.concatenate((x1, x2))
y = np.concatenate((y1, y2))

# Tworzymy DataFrame
df = pd.DataFrame({'X': x, 'Y': y})

# Zapisujemy do pliku CSV
df.to_csv('DataVille.csv', index=False)
