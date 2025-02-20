from flask import Blueprint, render_template, request, jsonify
from .services import interpret_query

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/api/query', methods=['POST']) 
def query():
    try:
        # 1Verificar si la solicitud tiene JSON válido
        if not request.is_json:
            return jsonify({'error': 'La solicitud debe ser en formato JSON.'}), 400
        
        data = request.get_json()  # Obtener JSON
        user_input = data.get('input')

        # 2️ Validar que el input no sea vacío
        if not user_input:
            return jsonify({'error': 'No se proporcionó una consulta válida.'}), 400

        # 3️ Llamar a Mistral
        response_text = interpret_query(user_input)

        # 4️ Devolver respuesta
        return jsonify({'response': response_text})

    except Exception as e:
        # 5️ Manejo de errores inesperados
        return jsonify({'error': f'Ocurrió un error en el servidor: {str(e)}'}), 500
