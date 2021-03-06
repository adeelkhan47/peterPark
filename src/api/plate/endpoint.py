import re

from flask import request
from flask_restx import Resource

from common.helper import error_message
from common.helper import response_structure
from model.plate import Plate
from . import api, schema


@api.route("")
class PlateOperation(Resource):
    @api.doc("Get all plates")
    @api.marshal_list_with(schema.GetPlates)
    def get(self):
        args = request.args.copy()

        if "plate:like" in args.keys() and "owner_name:like" in args.keys():
            A, count = Plate.filtration({"plate:like": args["plate:like"]})
            B, count = Plate.filtration({"owner_name:like": args["owner_name:like"]})
            A = set(A)
            B = set(B)
            all_users = A.union(B)
            return response_structure(list(all_users), len(all_users)), 200

        all_users, count = Plate.filtration(args)
        return response_structure(all_users, count), 200

    @api.expect(schema.PlateExpect, validate=True)
    @api.marshal_list_with(schema.GetPlate)
    def post(self):
        payload = api.payload.copy()
        plate = payload["plate"]
        if re.match(r"^([A-Z]{1,3}-[A-Z]{1,2}([1-9][0-9]{1,3})?)$", plate):
            plate = Plate(**payload)
            plate.insert()
            return response_structure(plate), 201
        else:
            return error_message("Invalid Plate Number"), 422


@api.route("/<int:id>")
class GetPlateById(Resource):
    @api.doc("Get plate by id")
    @api.marshal_list_with(schema.GetPlate)
    def get(self, id):
        plate = Plate.query_by_id(id)
        return response_structure(plate), 200

    @api.doc("Delete plate by id")
    def delete(self, id):
        Plate.delete(id)
        return "ok", 200

    @api.doc("Update plate by id")
    @api.marshal_list_with(schema.GetPlate, skip_none=True)
    @api.expect(schema.PlatePatchExpect, validate=True)
    def patch(self, id):
        payload = api.payload
        data = payload.copy()
        Plate.update(id, data)
        plate = Plate.query_by_id(id)
        return response_structure(plate), 200
