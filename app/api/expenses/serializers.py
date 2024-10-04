from marshmallow import fields, Schema

class ExpenseSchema(Schema):
    id = fields.Int(dump_only=True)  # Include id as a read-only field
    amount = fields.Float(required=True)
    category = fields.Str(required=True)
    date = fields.Date(required=True)
    description = fields.Str(required=True)


