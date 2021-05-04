from typing import Tuple

from flask import Blueprint

authentication_api = Blueprint('authorization', __name__)


@authentication_api.route('/registration', methods=['POST'])
def registration() -> Tuple[dict, int]:
    return {
        'endpoint': 'registration/',
        'request_method': 'POST',
        'status': 'not implemented'
    }, 201


@authentication_api.route('/sign-in', methods=['POST'])
def sign_in() -> Tuple[dict, int]:
    return {
        'endpoint': 'sign-in/',
        'request_method': 'POST',
        'status': 'not implemented'
    }, 200


@authentication_api.route('/sign-out', methods=['POST'])
def sign_out() -> Tuple[dict, int]:
    return {
        'endpoint': 'sign-out/',
        'request_method': 'POST',
        'status': 'not implemented'
    }, 200


@authentication_api.route('/refresh', methods=['POST'])
def refresh() -> Tuple[dict, int]:
    return {
        'endpoint': 'refresh/',
        'request_method': 'POST',
        'status': 'not implemented'
    }, 200
