# Importar librerías para procesamiento y visualización de imágenes
import cv2
import matplotlib.pyplot as plt

# Cargar la imagen en color
img = cv2.imread('../IMG/sopa_letras.png')

# Convertir la imagen a escala de grises para simplificar el análisis
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Mostrar la imagen en escala de grises
plt.figure()
plt.imshow(gray, cmap='gray')
plt.title('Imagen en escala de grises')
plt.axis('off')
plt.show()

# Aplicar umbral binario inverso para separar gotas del fondo
ret, bw = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)

# Mostrar la imagen binarizada
plt.figure()
plt.imshow(bw, cmap='gray')
plt.title('Imagen binarizada (letras vs fondo)')
plt.axis('off')
plt.show()

# Importar funciones para etiquetado y análisis de regiones
from skimage.measure import label, regionprops
import numpy as np

# Etiquetar cada objeto en la imagen binaria
eq = label(bw)

# Extraer propiedades de las regiones etiquetadas
sts = regionprops(label_image=eq)

# Convertir la matriz de etiquetas a un array de NumPy para facilitar su manipulación
eq = np.array(eq)

# Imprimir el número de regiones detectadas
print('Número de regiones detectadas:', np.max(eq))

# Visualizar etiquetas y ejemplos de regiones específicas
fig, ax = plt.subplots(nrows=1, ncols=3)
fig.set_figwidth(10)
ax[0].imshow(eq)
ax[0].set_title('Etiquetas')
ax[1].imshow(eq == 10)
ax[1].set_title('Región 10')
ax[2].imshow(eq == 20)
ax[2].set_title('Región 20')
for a in ax:
    a.axis('off')
plt.show()

def Momento (r, s, img):
    R = np.argwhere(img != 0)
    if R.size == 0:
        return 0.0
    i = R[:,0].astype(float)
    j = R[:,1].astype(float)

    return np.sum((i**r) * (j**s))

def Momento_central(r, s, img):
    R = np.argwhere(img != 0)
    if R.size == 0:
        return 0.0
    i = R[:,0].astype(float)
    j = R[:,1].astype(float)
    m00 = Momento(0,0,img)
    if m00 == 0:
        return 0.0
    i0 = Momento(1,0,img)/ m00
    j0 = Momento(0,1,img)/ m00

    return np.sum((i - i0)**r * (j - j0)**s)

def Momento_Hu (r, s, img):
    t = (r + s)/2.0 + 1.0
    mu00 = Momento_central(0,0,img)
    if mu00 == 0:
        return 0.0
    return Momento_central(r, s, img) / (mu00**t)

def compute_Fhis(mask):
    mu00 = Momento_central(0,0,mask)
    if mu00 == 0:
        return [0.0, 0.0, 0.0, 0.0]
    n20 = Momento_Hu(2,0,mask)
    n02 = Momento_Hu(0,2,mask)
    n11 = Momento_Hu(1,1,mask)
    n30 = Momento_Hu(3,0,mask)
    n12 = Momento_Hu(1,2,mask)
    n21 = Momento_Hu(2,1,mask)
    n03 = Momento_Hu(0,3,mask)

    F1 = n20 + n02
    F2 = (n20 - n02)**2 + 4*(n11**2)
    F3 = (n30 - 3*n12)**2 + (3*n21 - n03)**2
    F4 = (n30 + n12)**2 + (n21 + n03)**2

    return [F1, F2, F3, F4]

Fhis = [compute_Fhis(s.image) for s in sts]
Fhi1 = [f[0] for f in Fhis]
Fhi2 = [f[1] for f in Fhis]
Fhi3 = [f[2] for f in Fhis]
Fhi4 = [f[3] for f in Fhis]

def compute_perimeters(eq):
    perimeters = []
    max_label = int(np.max(eq))
    for lab in range(1, max_label + 1):
        mask = (eq == lab).astype(np.uint8)  
        res = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        contours = res[0] if len(res) == 2 else res[1]
        perim = sum(float(cv2.arcLength(cnt, True)) for cnt in contours)
        perimeters.append(perim)
    return perimeters

perimeters = compute_perimeters(eq) 

areas = [s.area for s in sts]

def compute_redondez(areas, perimeters):
    d = [4 * np.pi * a / (p**2) if p != 0 else 0 for a, p in zip(areas, perimeters)]
    return d

redondez = compute_redondez(areas, perimeters)

elipses = [s.eccentricity for s in sts]

import pandas as pd

df = pd.DataFrame(columns= ['Fhi1', 'Fhi2', 'Fhi3', 'Fhi4', 'Perimetro', 'redondez', 'Elipse'])

max_label = int(np.max(eq))
rows = []
for i in range(1, max_label + 1):
    mask = (eq == i).astype(np.uint8)
    Fhi1, Fhi2, Fhi3, Fhi4 = compute_Fhis(mask)
    rows.append({'Fhi1': Fhi1, 'Fhi2': Fhi2, 'Fhi3': Fhi3, 'Fhi4': Fhi4, 'Perimetro': perimeters[i-1], 'redondez': redondez[i-1], 'Elipse': elipses[i-1]})

df = pd.DataFrame(rows, columns=['Fhi1', 'Fhi2', 'Fhi3', 'Fhi4', 'Perimetro', 'redondez', 'Elipse'])
print(df)