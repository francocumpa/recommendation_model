import joblib
import streamlit as st
import pandas as pd
import numpy as np

# Encabezado y presentación
st.title('🎯 Product Recommender System Using Machine Learning')
st.markdown("""
    Bienvenido a nuestro sistema de recomendaciones de productos. Elija un usuario y obtenga recomendaciones personalizadas.
    🎁
""")

# Cargar el modelo ALS
model_cargado = joblib.load('./artifacts/modelo_als.pkl')

# Cargar la matriz dispersa de usuario-producto (mat_iu)
mat_iu_cargada = joblib.load('./artifacts/matriz_ui.pkl')

# Cargar diccionarios necesarios
product_id_to_name = pd.read_pickle('./artifacts/product_id_to_name.pkl')
user_to_num = joblib.load('./artifacts/user_to_num.pkl')
num_to_product = joblib.load('./artifacts/num_to_product.pkl')
last_purchases = joblib.load('./artifacts/last_purchases.pkl')

# Función para obtener las últimas compras del usuario
def obtener_ultimas_compras(user_id):
    last_purchases_user = last_purchases[last_purchases['user_id'] == user_id]
    if not last_purchases_user.empty:
        return last_purchases_user[['product_id', 'product_name']]
    else:
        return "El usuario no tiene compras registradas."

# Función para obtener recomendaciones de productos
def obtener_recomendaciones(user_id, N=10):
    user_index = user_to_num.get(user_id)
    
    if user_index is not None:
        # Obtener las recomendaciones
        ids, scores = model_cargado.recommend(user_index, mat_iu_cargada[user_index], N=N, filter_already_liked_items=True)

        # Convertir las recomendaciones a productos reales
        recs_real = [(int(num_to_product[i]), float(s)) for i, s in zip(ids, scores)]
        
        # Obtener los nombres de los productos recomendados
        recomendaciones = [(pid, product_id_to_name.get(pid, None), score) for pid, score in recs_real]
        return recomendaciones
    else:
        return "El usuario no está registrado."


# Entrada de búsqueda
search = st.text_input("Buscar id de usuario...")

# Solo traemos coincidencias
if search:
    filtered_users = [
    u for u in user_to_num.keys() if search.isdigit() and search in str(u)][:50]

else:
    filtered_users = []

selected_user = st.selectbox("Posibles coincidencias", filtered_users)


# Botón para mostrar las recomendaciones
if st.button('Mostrar Recomendaciones'):
    recomendaciones = obtener_recomendaciones(selected_user)
    
    if isinstance(recomendaciones, str):
        st.error(recomendaciones)  # Mostrar mensaje de error si no hay recomendaciones
    else:
        st.subheader('🎉 Recomendaciones para ti:')
        
        # Mostrar las recomendaciones en grupos de 3
        for i in range(0, len(recomendaciones), 3):
            cols = st.columns(3)
            grupo_recomendaciones = recomendaciones[i:i+3]

            for j, rec in enumerate(grupo_recomendaciones):
                with cols[j]:
                    st.write(f"**{rec[1]}**")
                    st.write(f"⭐ {rec[2] * 100:.2f} score")

# Visualizar las últimas compras del usuario seleccionado
st.subheader(f"Últimas compras de {selected_user}:")
ultimas_compras = obtener_ultimas_compras(selected_user)

if isinstance(ultimas_compras, str):
    st.write(ultimas_compras)
else:
    st.write(ultimas_compras[['product_id', 'product_name']])

st.markdown("""
    ** El score es una medida heurística a partir de los datos implícitos 
    del orden en que se agregaron las compras al carrito y de si se realizó un reorden."
            
""")
