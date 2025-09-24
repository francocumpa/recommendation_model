# Usar la imagen de python
FROM python:3.11.3

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Expose port 8501
EXPOSE 8501

# Ejecutar comando en el contenedor
CMD ["streamlit", "run", "app.py"]
