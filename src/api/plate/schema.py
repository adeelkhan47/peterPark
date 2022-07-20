from flask_restx import fields

from . import api

PlateExpect = api.model(
    "PlateExpect",
    {
        "plate": fields.String(required=True),
        "start_date": fields.DateTime(required=False, dt_format='rfc822'),
        "end_date": fields.DateTime(required=False, dt_format='rfc822'),
        "owner_name": fields.String(required=False)
    }
)
PlatePatchExpect = api.model(
    "PlatePatchExpect",
    {
        "plate": fields.String(required=False),
        "start_date": fields.DateTime(required=False, dt_format='rfc822'),
        "end_date": fields.DateTime(required=False, dt_format='rfc822'),
        "owner_name": fields.String(required=False)
    }
)

Plate = api.model(
    "Plate",
    {
        "id": fields.Integer(),
        "plate": fields.String(allow_null=True),
        "start_date": fields.DateTime(allow_null=True),
        "end_date": fields.DateTime(allow_null=True),
        "owner_name": fields.String(allow_null=True),
    },
)

error = api.model(
    "Error",
    {
        "msg": fields.String(),
    },
)

GetPlates = api.model(
    "GetAllPlates",
    {
        "total_rows": fields.Integer(),
        "objects": fields.Nested(Plate, as_list=True, skip_none=True),
        "error": fields.Nested(error, skip_none=True, allow_null=False),
    },
)
GetPlate = api.model(
    "GetPlate",
    {
        "objects": fields.Nested(Plate, skip_none=True),
        "error": fields.Nested(error, skip_none=True, allow_null=False),

    },
)
