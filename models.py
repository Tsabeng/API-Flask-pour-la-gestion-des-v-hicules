from db import db, ma

class Vehicule(db.Model):
    registrationNumber = db.Column(db.String(20), primary_key=True)  
    marque = db.Column(db.String(100), nullable=False) 
    modele = db.Column(db.String(100), nullable=False)  
    year = db.Column(db.Integer, nullable=False) 
    prix = db.Column(db.Float, nullable=False)  

# Schema de serialisation des vehicules
class VehiculeSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Vehicule  
        load_instance = True 

# transformer les objets en JSON
vehicule_schema = VehiculeSchema()
vehicules_schema = VehiculeSchema(many=True)  
