#universidad del valle - Inteligencia Artificial
#Tema: Aprendizaje Analogico
#importar las bibliotecas necesarias
from Sklearn.Neighbors import Nearest.Neighbors
import numpy as np

#Datos conocidos  (entrenamiento)
X_train = np.array ([[1, 2],[2, 3], [3, 4], [4, 5], [5, 6]])

#Datos desconocidos (nuevas observaciones)
X_unknown = np.array ([[1.5, 2.5], [3.5, 4.5]])

#crear y ajustar el modelo de vecinos  más cercanos (Nearest Neigbhbors)
model = NearestNeighbors (n_neighbors=2)
model.fit(X_train)
#encontrar los  vecinoos mas cercanos  para las nuevas obcervaciones
distances, indices = model.kneighbors(X_unknown)

#Imprimir los vecinos mas cercanos encontrados 
for i in range (len(X_unknown)):
    print ("para la observacion", X_unknown[i], "los vecinos mas cercanos son:", X_train[indices[i]])
