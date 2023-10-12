from datetime import datetime, timedelta
from flask import Flask, make_response, jsonify, request, redirect, url_for
from flask_migrate import Migrate
from flask_cors import CORS
from models import db, Hero, Power, HeroPower

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

CORS(app, supports_credentials=True, origins=["http://localhost:3000"])


# Route to get heroes 
@app.route('/heroes', methods=['GET'])
def get_heroes():
    heroes = Hero.query.all()
    hero_data = [{'id': hero.id, 'name': hero.name, 'supername': hero.supername, 'image_url': hero.image_url} for hero in heroes]  
    return jsonify(hero_data)


#Route for getting heroes by id
@app.route('/heroes/<int:id>', methods=['GET'])
def get_hero(id):
    hero = Hero.query.filter_by(id=id).first()
    if hero is not None:
        # Use joinedload to load related powers with the hero in a single query
        hero_data = {
            'name': hero.name,
            'supername': hero.supername,
            'image_url': hero.image_url,
            'powers': [{'name': hp.power.name, 'description': hp.power.description} for hp in hero.powers]
        }
        return jsonify(hero_data)
    else:
        return jsonify({'message': 'Hero not found'}), 404



#Route to update a specific hero by id
@app.route('/heroes/<int:id>/update', methods=['PUT'])
def update_hero(id):
    # Retrieve the hero to update
    hero = Hero.query.get(id)

    if not hero:
        return jsonify({"error": "Hero not found"}), 404

    # Parse JSON data from the request
    data = request.get_json()

    # Update hero data based on the JSON input
    if 'name' in data:
        hero.name = data['name']
    if 'supername' in data:
        hero.supername = data['supername']
    # Update other attributes as needed

    # Commit the changes to the database
    db.session.commit()

    return jsonify({"message": "Hero updated successfully"})

# Route to add a new hero
@app.route('/add_hero', methods=['POST'])
def add_hero():
    data = request.get_json()
    name = data.get('name')
    supername = data.get('supername')
    image_url = data.get('image_url')

    if not name or not supername or not image_url:
        return jsonify({'error': 'Missing name, supername, or image_url'}), 400

    # Check if the name is unique before adding to the database
    if Hero.query.filter_by(name=name).first():
        return jsonify({'error': 'Hero with this name already exists'}), 400

    new_hero = Hero(
        name=name,
        supername=supername,
        image_url=image_url,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )
    db.session.add(new_hero)
    db.session.commit()
    return jsonify({'message': 'Hero added successfully'}), 201


#route to delete a hero
@app.route('/heroes/<int:id>/delete', methods=['DELETE'])
def delete_hero(id):
    try:
        # Query the hero by ID
        hero = Hero.query.get(id)

        if hero is None:
            return jsonify({'error': 'Hero not found'}), 404

        # Remove the hero's associations with powers
        hero_powers = HeroPower.query.filter_by(hero_id=id).all()
        for hero_power in hero_powers:
            db.session.delete(hero_power)

        # Delete the hero
        db.session.delete(hero)
        db.session.commit()

        return jsonify({'message': 'Hero and associated powers deleted successfully'}), 200

    except Exception as e:
        return jsonify({'error': 'An error occurred while deleting the hero'}), 500

# GET /powers
@app.route('/powers', methods=['GET'])
def get_powers():
    powers = Power.query.all()
    power_data = [{'id': power.id, 'name': power.name, 'description': power.description} for power in powers]
    return jsonify(power_data)

# Route to add a new power
@app.route('/add_power', methods=['POST'])
def add_power():
    data = request.get_json()
    name = data.get('name')
    description = data.get('description')

    if not name or not description:
        return jsonify({'error': 'Missing name or description'}), 400

    # Check if the name is unique before adding to the database
    if Power.query.filter_by(name=name).first():
        return jsonify({'error': 'Power with this name already exists'}), 400

    new_power = Power(name=name, description=description, created_at=datetime.utcnow(), updated_at=datetime.utcnow())  
    db.session.add(new_power)
    db.session.commit()
    return jsonify({'message': 'Power added successfully'}), 201


# # Route to get a specific power by ID
# @app.route('/powers/<int:id>', methods=['GET'])
# def get_power_by_id(id):
#     power = Power.query.get(id)
#     if power is None:
#         return jsonify({'error': 'Power not found'}), 404

#     power_data = {
#         'id': power.id,
#         'name': power.name,
#         'description': power.description
#     }
#     return jsonify(power_data), 200

    

# # Route to update a specific power by ID
# @app.route('/powers/<int:id>/update', methods=['PUT'])
# def update_power(id):
#     try:
#         power = Power.query.get(id)
#         if power is None:
#             return jsonify({'error': 'Power not found'}), 404

#         data = request.get_json()
#         if 'name' in data:
#             power.name = data['name']
#         if 'description' in data:
#             power.description = data['description']
#         db.session.commit()

#         return jsonify({'message': 'Power updated successfully'}), 200

#     except Exception as e:
#         return jsonify({'error': str(e)}), 500


# # Delete a power by its ID and remove associations from heroes
# @app.route('/powers/<int:id>/delete', methods=['DELETE'])
# def delete_power(id):
#     power = Power.query.get(id)

#     if not power:
#         return jsonify({"error": "Power not found"}), 404

#     # Find all hero_power records associated with this power
#     hero_powers = HeroPower.query.filter_by(power_id=id).all()

#     # Delete these associations
#     for hero_power in hero_powers:
#         db.session.delete(hero_power)

#     # Delete the power
#     db.session.delete(power)
#     db.session.commit()

#     return jsonify({"message": "Power deleted successfully"})


# POST /heropowers
@app.route('/hero_powers', methods=['POST'])
def create_hero_power():
    try:
        data = request.get_json()
        strength = data.get('strength')
        hero_id = data.get('hero_id')
        power_id = data.get('power_id')
        
        # Check if the hero and power exist in the database
        hero = Hero.query.get(hero_id)
        power = Power.query.get(power_id)
        
        if not (hero and power):
            return jsonify({'error': 'Invalid hero_id or power_id'}), 400
        
        # Create a new HeroPower association
        hero_power = HeroPower(strength=strength, hero=hero, power=power)
        db.session.add(hero_power)
        db.session.commit()
        
        return jsonify({'message': 'HeroPower association created successfully'}), 201
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(port=5555, debug=True)
