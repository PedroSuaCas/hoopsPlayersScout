from flask import Blueprint, render_template, request, jsonify
from .services import interpret_query

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/api/query', methods=['POST'])
def query():
    user_input = request.json.get('input')
    response_text = interpret_query(user_input)
    return jsonify({'response': response_text})
