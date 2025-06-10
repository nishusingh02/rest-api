from flask import Blueprint, request, jsonify
from .models import App
from .database import db

app_bp = Blueprint('app_bp', __name__)

@app_bp.route('/add-app', methods=['POST'])
def add_app():
    data = request.get_json()
    new_app = App(
        app_name=data['app_name'],
        version=data['version'],
        description=data['description']
    )
    db.session.add(new_app)
    db.session.commit()
    return jsonify({'message': 'App added successfully', 'id': new_app.id}), 201

@app_bp.route('/get-app/<int:id>', methods=['GET'])
def get_app(id):
    app = App.query.get_or_404(id)
    return jsonify({
        'id': app.id,
        'app_name': app.app_name,
        'version': app.version,
        'description': app.description
    })

@app_bp.route('/delete-app/<int:id>', methods=['DELETE'])
def delete_app(id):
    app = App.query.get_or_404(id)
    db.session.delete(app)
    db.session.commit()
    return jsonify({'message': 'App deleted successfully'})

@app_bp.route('/', methods=['GET'])
def home():
    return jsonify({'message': 'Welcome to the App API!'})


# ...existing code...

@app_bp.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    prompt = data.get('prompt')
    if not prompt:
        return jsonify({'error': 'Prompt is required'}), 400

    # For now, just echo the prompt. Replace this with your AI logic.
    answer = f"You said: {prompt}"

    return jsonify({'answer': answer})

# ...existing code...