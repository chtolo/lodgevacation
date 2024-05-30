# Utiliser une image de base officielle de Python
FROM python:3.9-slim

# Définir le répertoire de travail à l'intérieur du conteneur
WORKDIR /app

# Copier les fichiers requirements.txt (ou équivalent) dans le conteneur
COPY backend/requirements.txt /app/requirements.txt

# Installer les dépendances Python
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copier l'ensemble du code de l'application dans le conteneur
COPY backend /app

# Exposer le port sur lequel l'application va tourner
EXPOSE 5000

# Définir la variable d'environnement pour indiquer à Flask de démarrer
ENV FLASK_APP=app.py
# Définir les variables d'environnement pour MySQL
ENV MYSQL_HOST=db
ENV MYSQL_USER=root
ENV MYSQL_PASSWORD=password
ENV MYSQL_DB=mydb
# Démarrer l'application
CMD ["flask", "run", "--host=0.0.0.0"]
