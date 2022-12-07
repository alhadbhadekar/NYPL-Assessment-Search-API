from flask import Blueprint, jsonify
from src.constants.http_status_codes import HTTP_200_OK, HTTP_400_BAD_REQUEST
from src.processor.processor import processor
import re

search = Blueprint("search", __name__, url_prefix="/api/v1/search")

@search.get("/<string:text>")
def get_search(text):

    regex= re.compile('[@_!#$%^&*()<>?/\|}{~:]')

    if (regex.search(text) != None):
        return jsonify({
                'error': 'bad input, has special characters'
            }), HTTP_400_BAD_REQUEST

    response, status_code = processor(text)

    if status_code != HTTP_200_OK:
        return jsonify({
                'error': 'internal server error'
            }), status_code

    return response, HTTP_200_OK