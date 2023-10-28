# Utiliza la imagen oficial de Python como base
FROM python:3

# Establece el directorio de trabajo en /app
WORKDIR /app

# Instala Flask y otras dependencias
RUN pip install flask

# Copia tu aplicación Flask al contenedor
COPY . .

# Expone el puerto en el que Flask se ejecutará (por defecto es el puerto 5000)
EXPOSE 5000

# Comando para ejecutar la aplicación Flask
CMD ["python", "app.py"]
