# 🚀 API Flask pour la gestion des véhicules

## 📌 Description
Cette API permet de gérer une base de données de véhicules avec Flask et SQLAlchemy.

## 📂 Installation
1. **Cloner le projet** :
   ```bash
   git clone git@github.com:Tsabeng/Projet-Groupe5-Testing-.git
   cd Projet-Groupe5-Testing-


2. **Créer un environnement virtuel** :

python -m venv venv
source venv/bin/activate   #  Linux/Mac
venv\Scripts\activate      #  Windows

3. **Installer les dépendances** :

pip install -r requirements.txt

4. **Initialiser la base de données** :

flask db init
flask db migrate -m "Initial migration"
flask db upgrade

5. **Lancer le serveur** :

    flask run

## 🔧 Endpoints

    GET /api/vehicules : Liste tous les véhicules

    POST /api/vehicules : Ajoute un véhicule

    GET /api/vehicules/<id> : Récupère un véhicule spécifique

    PUT /api/vehicules/<id> : Met à jour un véhicule

    DELETE /api/vehicules/<id> : Supprime un véhicule




  **Comment utiliser**

    📌 Récupérer tous les véhicules

curl -X GET http://127.0.0.1:5000/api/vehicules

   📌 Ajouter un véhicule

curl -X POST http://127.0.0.1:5000/api/vehicules \
-H "Content-Type: application/json" \
-d '{
  "registrationNumber": "XYZ123",
  "marque": "BMW",
  "modele": "X5",
  "year": 2022,
  "prix": 80.0
}'

✅ Si l'ajout est réussi, l'API doit renvoyer une confirmation avec un statut 201 Created.

  📌 Modifier un véhicule

curl -X PUT http://127.0.0.1:5000/api/vehicules/XYZ123 \
-H "Content-Type: application/json" \
-d '{
  "prix": 75.0
}'

📌 Supprimer un véhicule

curl -X DELETE http://127.0.0.1:5000/api/vehicules/XYZ123

✅ L'API doit renvoyer un statut 200 OK ou 204 No Content.


📌 Rechercher un véhicule par immatriculation

curl -X GET http://127.0.0.1:5000/api/vehicules/search/registration/XYZ123

✅ L'API doit retourner les détails du véhicule.


📌 Rechercher par prix maximum


curl -X GET http://127.0.0.1:5000/api/vehicules/search/price/70