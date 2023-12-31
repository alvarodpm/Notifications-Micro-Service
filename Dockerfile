# Usa una imagen de Python como base
FROM python:3.9

# Copiar archivo Python al contenedor
COPY notifications.py /app/notifications.py

# Instalar las dependencias necesarias
RUN pip install kafka-python

# Establecer el directorio de trabajo
WORKDIR /app

# Ejecutar el script Python cuando se inicie el contenedor
CMD ["python", "notifications.py"]
