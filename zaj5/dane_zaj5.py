

# In[ ]:


import matplotlib.pyplot as plt
import random
import numpy as np

# Generujemy dane:
n = 25 # liczba studentow
x1 = np.random.randint(0, 50, n) # losowa liczba od 0 do 50 | study_hours
x2 = np.random.randint(2, 12, n) # losowa liczba od 2 do 12 | sleep_hours
x3 = np.random.uniform(0, 5, n) # rozkład jednostajny od 0 do 5 | coffee_liters

x1, x2, x3


# In[ ]:


# Generujemy punkty
# Wymyślona zależność: liczba punktów zależy od 2 * liczba godzin nauki + 3 * liczba godzin snu, dodajemy duży szum
# Następnie normalizacja do zakresu 0-100 i pozostawienie liczb całkowitych
points = (x1 * 2 + x2 * 3) + np.random.normal(0, 20, n)
points = ((points - np.min(points)) / (np.max(points) - np.min(points)) * 100).astype(int)

# Oceny według liczby punktów
grades = []
for p in points:
    if p < 50:
        grades.append(2)
    elif p < 65:
        grades.append(3)
    elif p < 85:
        grades.append(4)
    else:
        grades.append(5)
grades = np.array(grades)
        
points, grades


# In[ ]:


# Oglądamy dane

plt.figure(figsize=(15, 15))

plt.subplot(3, 2, 1)
plt.scatter(x1, points, color='blue')
plt.xlabel("study_hours")
plt.ylabel("points")

plt.subplot(3, 2, 2)
plt.scatter(x1, grades, color='green')
plt.xlabel("study_hours")
plt.ylabel("grades")

plt.subplot(3, 2, 3)
plt.scatter(x2, points, color='blue')
plt.xlabel("sleep_hours")
plt.ylabel("points")

plt.subplot(3, 2, 4)
plt.scatter(x2, grades, color='green')
plt.xlabel("sleep_hours")
plt.ylabel("grades")

plt.subplot(3, 2, 5)
plt.scatter(x3, points, color='blue')
plt.xlabel("coffee_liters")
plt.ylabel("points")

plt.subplot(3, 2, 6)
plt.scatter(x3, grades, color='green')
plt.xlabel("coffee_liters")
plt.ylabel("grades")


plt.show()


# In[ ]:


# Przystępujemy do regresji 1D - przygotowanie danych
from sklearn import linear_model

# Opcja 1 - podział danych ręcznie

# Podział 80/20, więc dla 25 osób bierzemy 20 wyników do trenowania, 5 do testowania
# Dane są nieposortowane, więc możemy po prostu skorzystać z indeksowania

x_train = x1[:-5].reshape(-1, 1) # pierwsze 20, czyli od 0 do -5 [od końca] (można też normalnie: x1[0:20])
x_test = x1[-5:].reshape(-1, 1)
y_train = points[:-5].reshape(-1, 1)
y_test = points[-5:].reshape(-1, 1)
#array.reshape(-1,1) dodajemy, żeby wymiary do funkcji obliczających regresję się zgadzały

regr = linear_model.LinearRegression()
regr.fit(x_train, y_train)
print("coef, intercept:\n", regr.coef_, regr.intercept_) # współczynniki regresji (dla 1D - współczynniki prostej)
# y = {regr.coef_} * [x_i] + {regr.intercept_} 

y_pred = regr.predict(x_test) # predykcja dla danych testowych

# porównujemy czy wyniki predykcji się w miarę zgadzają z danymi z pomiarów
print("Test\n", y_test)
print("Pred\n", y_pred)

# Miary regresji - współczynnik R^2, błędy MSE, RMSE, MAE - liczone z definicji
RR = regr.score(x_test, y_test)
print("R^2:", RR)

mse = np.mean( (y_pred - y_test)**2 )
rmse = np.sqrt(mse)
mae = np.mean(np.abs(y_pred - y_test))
print(mse, mae)

# In[ ]:


# Opcja 2 - korzystamy z dobrodziejstw scikit-learn

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x1.reshape(-1,1), points.reshape(-1,1), test_size=0.2, random_state=1)
# ta funkcja dodatowo pozwala na losowość podziału danych - co może też zaburzyć wyniki!

regr = linear_model.LinearRegression()
regr.fit(x_train, y_train)
print("coef, intercept:\n", regr.coef_, regr.intercept_)

y_pred = regr.predict(x_test)
print("Test\n", y_test)
print("Pred\n", y_pred)

RR = regr.score(x_test, y_test)
print("R^2:", RR)

# miary błędów z gotowych funkcji w scikit-learn
from sklearn.metrics import mean_squared_error, mean_absolute_error

mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
mae = mean_absolute_error(y_test, y_pred)
print(mse, mae)


# In[ ]:


#Rysujemy wykres dla regresji 1D

plt.plot(x1, points, 'k.') # wszystkie dane
plt.plot(x_train, y_train, 'mo') # tylko dane trenujące
plt.plot(x_test, y_test, 'bo') # tylko dane testowe
plt.plot(x_test, y_pred, 'g*-') # dopasowana prosta
plt.xlabel("study_hours")
plt.ylabel("points")
plt.show()


# In[ ]:


# Regresja 2D 

x = np.column_stack((x1, x2))

x_train, x_test, y_train, y_test = train_test_split(x, points.reshape(-1,1), test_size=0.2, random_state=1)

regr = linear_model.LinearRegression()
regr.fit(x_train, y_train)
print("coef, intercept:\n", regr.coef_, regr.intercept_)

y_pred = regr.predict(x_test)
print("Test\n", y_test)
print("Pred\n", y_pred)

RR = regr.score(x_test, y_test)
print("R^2:", RR)

# miary błędów z gotowych funkcji w scikit-learn
from sklearn.metrics import mean_squared_error, mean_absolute_error

mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
mae = mean_absolute_error(y_test, y_pred)
print(mse, mae)


# In[ ]:


# Regresja 3D 

x = np.column_stack((x1, x2, x3))

x_train, x_test, y_train, y_test = train_test_split(x, points.reshape(-1,1), test_size=0.2, random_state=1)

regr = linear_model.LinearRegression()
regr.fit(x_train, y_train)
print("coef, intercept:\n", regr.coef_, regr.intercept_)

y_pred = regr.predict(x_test)
print("Test\n", y_test)
print("Pred\n", y_pred)

RR = regr.score(x_test, y_test)
print("R^2:", RR)

# miary błędów z gotowych funkcji w scikit-learn
from sklearn.metrics import mean_squared_error, mean_absolute_error

mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
mae = mean_absolute_error(y_test, y_pred)
print(mse, mae)

# %%
