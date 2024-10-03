from marshmallow import fields, Schema

class ExpenseSchema(Schema):
    id = fields.Int(dump_only=True)
    user_id=fields.Int(required=True)
    amount=fields.Float(required=True)
    category=fields.str(required=True)
    date=fields.Date(requried=True)
    description=fields.Str(required=True)


