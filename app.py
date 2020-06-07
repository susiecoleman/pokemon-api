from flask import Flask, request, jsonify
from search.pokemon import search_pokemon
from werkzeug.exceptions import BadRequest, InternalServerError
import logging

app = Flask(__name__)

@app.route('/', methods=['GET'])
def app_status_check():
    return "200 OK"

@app.route('/pokemon', methods=['GET'])
def get_pokemon():
    query = request.args.get("q")
    if not query:
        return BadRequest("Missing Query Param")
    try:
        return jsonify({
            "pokemon": search_pokemon(query)}
            )
    except Exception as e:
        logging.error(f'Unable to fulfil request to /pokemon endpoint with query param ${query}. Exception: {e}')
        return InternalServerError("Unable to handle request")
