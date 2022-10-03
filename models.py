from marshmallow import Schema, fields, validates_schema, ValidationError

VALID_CMD_PARAMS = ('filter', 'sort', 'map', 'unique', 'limit') #'regex') for 24hw

class RequestParams(Schema):
    cmd = fields.String(required=True)
    value = fields.String(required=True)

    @validates_schema
    def validates_cmd_params(self, values, *args, **kwargs):
        if values['cmd'] not in VALID_CMD_PARAMS:
            raise ValidationError('Invalid: "cmd" contains invalid value')


class BatchRequestParams(Schema):
    queries = fields.Nested(RequestParams, many=True)



