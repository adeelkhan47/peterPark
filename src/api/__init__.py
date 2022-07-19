from http import HTTPStatus

from flask import Blueprint
from flask_restx import Api
from werkzeug.exceptions import BadRequest, Forbidden, NotFound, Unauthorized

from common.helper import error_message
from model.base import db
from .plate.endpoint import api as plate_api

blueprint = Blueprint("api", __name__)

api = Api(blueprint, title="PeterPark Api's", version="0.1", description="REST")

api.add_namespace(plate_api)


@api.errorhandler(NotFound)
def handle_not_found_error(exception_cause):
    """
    Catch not found error exception globally and respond with 404.
    :param exception_cause:
    :return objects, response Code:
    """
    return error_message(exception_cause.description), HTTPStatus.NOT_FOUND


@api.errorhandler(BadRequest)
def handle_bad_request_error(exception_cause):
    """
    Catch bad request error exception globally and respond with 400.
    :param exception_cause:
    :return objects, response Code:
    """

    return error_message(exception_cause.description), HTTPStatus.BAD_REQUEST


@api.errorhandler(Unauthorized)
def handle_unauthorized_error(exception_cause):
    """
    Catch unauthorized globally and respond with 401.
    :param exception_cause:
    :return objects , response Code:
    """
    return error_message(exception_cause.description), HTTPStatus.UNAUTHORIZED


@api.errorhandler(Forbidden)
def handle_forbidden_error(exception_cause):
    """
    Catch forbidden globally and respond with 403.
    :param exception_cause:
    :return objects , response Code:
    """

    return error_message(exception_cause.description), HTTPStatus.FORBIDDEN


@api.errorhandler(Exception)
def handle_internal_server_error(exception_cause):
    """
    Catch internal server error exception globally and respond with 500.
    :param exception_cause:
    :return objects , response Code:
    """
    db.session.rollback()
    return error_message("internal server error"), HTTPStatus.INTERNAL_SERVER_ERROR
