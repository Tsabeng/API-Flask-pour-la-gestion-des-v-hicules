from flask import Blueprint, request, jsonify
from models import db, Vehicule, vehicule_schema, vehicules_schema

vehicule_bp = Blueprint("vehicule_bp", __name__)

# Tester si mon api fonctionne bien
@vehicule_bp.route('/test', methods=['GET'])
def test():
    return {"message": "API fonctionne !"}, 200

#  Recuperer tous les vehicules
@vehicule_bp.route('/vehicules', methods=['GET'])
def get_vehicules():
    vehicules = Vehicule.query.all()
    return vehicules_schema.jsonify(vehicules), 200

#  Ajouter un vehicule
@vehicule_bp.route('/vehicules', methods=['POST'])
def add_vehicule():
    data = request.get_json()

    if Vehicule.query.get(data['registrationNumber']):
        return jsonify({"error": "Ce numéro d'immatriculation existe déjà"}), 400
    
    new_vehicule = Vehicule(
        registrationNumber=data['registrationNumber'], 
        marque=data['marque'], 
        modele=data['modele'], 
        year=data['year'], 
        prix=data['prix']
    )

    db.session.add(new_vehicule)
    db.session.commit()
    return vehicule_schema.jsonify(new_vehicule), 201

# Mettre a jour un vehicule
@vehicule_bp.route('/vehicules/<string:registrationNumber>', methods=['PUT'])
def update_vehicule(registrationNumber):
    vehicule = Vehicule.query.get(registrationNumber)
    if not vehicule:
        return jsonify({"error": "Véhicule non trouvé"}), 404

    data = request.get_json()
    vehicule.marque = data.get("marque", vehicule.marque)
    vehicule.modele = data.get("modele", vehicule.modele)
    vehicule.year = data.get("year", vehicule.year)
    vehicule.prix = data.get("prix", vehicule.prix)

    db.session.commit()
    return vehicule_schema.jsonify(vehicule), 200

#  Supprimer un vehicule
@vehicule_bp.route('/vehicules/<string:registrationNumber>', methods=['DELETE'])
def delete_vehicule(registrationNumber):
    vehicule = Vehicule.query.get(registrationNumber)
    if not vehicule:
        return jsonify({"error": "Véhicule non trouvé"}), 404

    db.session.delete(vehicule)
    db.session.commit()
    return jsonify({"message": "Véhicule supprimé"}), 200

#  Rechercher un vehicule par son immatriculation
@vehicule_bp.route('/vehicules/search/registration/<string:registrationNumber>', methods=['GET'])
def search_by_registration(registrationNumber):
    vehicule = Vehicule.query.get(registrationNumber)
    if vehicule:
        return vehicule_schema.jsonify(vehicule), 200
    return jsonify({"error": "Véhicule non trouvé"}), 404

#  Rechercher des vehicules par prix max
@vehicule_bp.route('/vehicules/search/price/<float:price>', methods=['GET'])
def search_by_price(price):
    vehicules = Vehicule.query.filter(Vehicule.prix <= price).all()
    return vehicules_schema.jsonify(vehicules), 200
