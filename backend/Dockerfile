# Utiliser une image officielle de Python comme image de base
FROM python:3.9-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier le fichier requirements.txt dans le conteneur
COPY requirements.txt .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste de l'application dans le conteneur
COPY . .

# Exposer le port sur lequel l'application va tourner
EXPOSE 5000

# Définir la commande pour lancer l'application
CMD ["python", "app.py"]
