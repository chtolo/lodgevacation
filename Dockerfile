# Utiliser l'image de base Python 3.10
FROM python:3.10-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers requis dans le conteneur
COPY requirements.txt .
COPY . .

# Installer les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Installer MySQL client
RUN apt-get update && apt-get install -y default-libmysqlclient-dev

# Exposer le port sur lequel l'application Flask s'exécutera
EXPOSE 5000

# Définir les variables d'environnement pour MySQL
ENV MYSQL_HOST=localhost
ENV MYSQL_USER=root
ENV MYSQL_PASSWORD=
ENV MYSQL_DB=mydb

# Commande pour démarrer l'application Flask
CMD ["python", "app.py"]
