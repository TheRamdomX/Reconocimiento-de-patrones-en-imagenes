# Reconocimiento de Patrones en Imágenes

Este repositorio contiene los materiales y notebooks del curso electivo universitario **Reconocimiento de Patrones en Imágenes**. El curso explora técnicas fundamentales y avanzadas para el análisis, procesamiento y reconocimiento de patrones en imágenes digitales, utilizando Python y librerías como OpenCV, NumPy, Matplotlib y scikit-image.

## Estructura del repositorio

- `IMG/`: Carpeta con imágenes de ejemplo utilizadas en los notebooks.
- `Clases/Clase_X.ipynb`: Notebooks de cada clase, con ejemplos prácticos y explicaciones.

## Resumen de clases

### Clase 1

- **Tema:** Carga y visualización de imágenes, conversión de formatos de color, cálculo y graficado de histogramas, acceso a píxeles específicos.

### Clase 2

- **Tema:** Selección de regiones de interés (ROI), umbralización, análisis de canales de color y conversión a HSV.

### Clase 3

- **Tema:**  Momentos, Centro de masa, Momento Central y de Hu para caracterización geométrica.

### Clase 4

- **Tema:** Procesamiento de imágenes binarias, detección de contornos, representación de contornos con números complejos, Transformada Rápida de Fourier (FFT) aplicada a contornos.

### Clase 5

- **Tema:** Momentos geométricos para caracterización de formas, análisis cromático de imágenes a color, umbralización y segmentación.

### Clase 6

- **Tema:** Procesamiento de matrices de intensidad, cálculo de momentos centrales y de Hu, escalado de imágenes.

### Clase 7

- **Tema:** Matriz de co-ocurrencia de niveles de gris (GLCM), extracción de características de textura, normalización de imágenes.

### Clase 8

- **Tema:** Extracción y visualización de características de textura en colecciones de imágenes, agrupamiento y análisis comparativo de texturas.

### Clase 9

- **Tema:** Segmentación mediante etiquetado de regiones, extracción de características (área y orientación), filtrado y visualización de gotas según criterios geométricos.

### Clase 10

- **Tema:** Repaso general de los contenidos del curso. Carga y visualización de imágenes, procesamiento, segmentación, extracción de características y análisis de textura.

### Clase 11

- **Tema:** Análisis de Componentes Principales (KLT/PCA). Centrado de datos, cálculo de la matriz de covarianza, autovalores y autovectores, proyección sobre ejes principales y reconstrucción con pérdida de información.

### Clase 12

- **Tema:** Vector Quantization (VQ) y generación de codebooks. Implementación de VQ con divisiones binarias de centroides, cálculo de distancias euclidianas y visualización de codebooks sobre datos 2D.

### Clase 13

- **Tema:** Cálculo y visualización de medias por cluster y análisis exploratorio de datos multiclase. Separación de datos por clase y representación gráfica de centros y medias.

### Clase 14

- **Tema:** Extracción de características de textura mediante Haralick (GLCM). Cálculo de propiedades como contraste, disimilitud, homogeneidad, ASM y energía; comparación de combinaciones de características y cálculo del índice de Fisher.

### Clase 15

- **Tema:** Selección de características y criterio de Fisher. Implementación de funciones para calcular el índice de Fisher sobre conjuntos de texturas y búsqueda de la mejor combinación de características.

### Clase 16

- **Tema:** Ejemplo completo de extracción y clasificación con K-Vecinos Cercanos. Extracción de momentos invariantes de Hu y excentricidad desde regiones segmentadas (ej. `sopa_letras.png`), construcción de dataset y clasificación con KNN, incluyendo matriz de confusión.

### Clase 17

- **Tema:** Linear Discriminant Analysis (LDA). Cálculo de medias por clase, matrices de covarianza intraclase e interclase, inversión de la matriz combinada y uso de la regla discriminante para asignación de nueva data.

### Clase 18

- **Tema:** Árboles de decisión e información. Cálculo de tablas de clases por atributo, entropía, ganancia de información y construcción básica de un árbol de decisión (junto con un ejemplo práctico usando scikit-learn sobre el dataset Iris).

---

## Requisitos

- Python 3.12+
- Instalar dependencias en el entorno virtual `myenv`:

```bash
pip install opencv-python numpy matplotlib scikit-image pandas scikit-learn
```

## Tarea 1

Descripción: esta tarea procesa una imagen de ejemplo (`IMG/sopa_letras.png`) para detectar regiones (letras), calcular momentos geométricos y de Hu, características basadas en perímetro, área, redondez y excentricidad, y finalmente crear un DataFrame con las características de cada región.

## Tarea 2

Descripción: este notebook realiza un análisis completo sobre la imagen `IMG/rice.png`, que incluye carga y visualización en color y gris, cálculo de color promedio, umbralización y etiquetado de regiones, extracción de descriptores geométricos (área, perímetro), gradiente promedio en perímetro, medidas de contraste (K1, K2, K3) y momentos invariantes de Hu. También incluye análisis de resultados y discusión sobre el efecto del ruido y la umbralización en el etiquetado de regiones.


