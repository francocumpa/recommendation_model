# Sistema de Recomendación de Productos

Este proyecto implementa un sistema de recomendación de productos utilizando un modelo de Machine Learning. El sistema analiza el historial de compras de los usuarios para sugerir productos que podrían ser de su interés. La aplicación está construida con Python y cuenta con una interfaz web interactiva desarrollada con Streamlit.

## Demo

*Puedes encontrar una demostración en vivo de la aplicación en el siguiente enlace:*

**[Link a la Demo](https://recsys-rn9d.onrender.com/)** 

(Puede tardar unos 50s a veces porque se usa un servidor gratuito).

## Instalación

Para ejecutar este proyecto localmente, sigue estos pasos:

1.  **Clonar el repositorio:**
    ```bash
    git clone https://github.com/francocumpa/recommendation_model.git
    cd recommendation_model
    ```

2.  **Crear un entorno virtual (recomendado):**
    ```bash
    conda create -n recsys python=3.11
    conda activate recsys
    ```

3.  **Instalar las dependencias:**
    El proyecto requiere **Python 3.11**. Asegúrate de tenerlo instalado.
    ```bash
    pip install -r requirements.txt
    ```

## Uso

Una vez completada la instalación, puedes iniciar la aplicación Streamlit con el siguiente comando:

```bash
streamlit run app.py
```

Esto abrirá una nueva pestaña en tu navegador con la interfaz de la aplicación. Desde allí, podrás seleccionar un usuario para ver sus compras anteriores y las recomendaciones generadas por el modelo.

## Modelo

El sistema de recomendación se basa en un modelo de **Alternating Least Squares (ALS)** de la librería `implicit`. 
Se usa ALS debido a que es mejor a cosine similarity en cuanto a escalamiento, descubrir patrones ocultos y manejo de datos dispersos.

##
El proceso de desarrollo se detalla en el notebook `Recommendation_Model.ipynb` y se resume en los siguientes pasos:

1.  **Ingeniería de Características:** Se crea una puntuación (`score`) heurística para medir el interés del usuario en un producto, basada en si el producto fue reordenado y su posición en el carrito de compras.
2.  **Construcción de la Matriz:** Se construye una matriz dispersa de interacciones usuario-producto utilizando la puntuación generada.
3.  **Entrenamiento del Modelo:** Se entrena el modelo ALS con la matriz de interacciones para aprender los factores latentes de usuarios y productos.
4.  **Generación de Recomendaciones:** El modelo entrenado se utiliza para predecir y recomendar los productos más relevantes para un usuario específico, excluyendo aquellos que ya ha comprado.
5.  **Serialización:** El modelo y los artefactos necesarios (diccionarios de mapeo, datos de compras) se guardan en la carpeta `artifacts/` para ser utilizados por la aplicación web.
