from marshmallow import Schema, fields, ValidationError

# Custom validator for item IDs list
def validate_item_ids(value):
    if not isinstance(value, list) or not all(isinstance(i, int) for i in value):
        raise ValidationError("item_ids must be a list of integers.")

# Order Schema for validation
class OrderSchema(Schema):
    order_id = fields.Integer(required=True)
    user_id = fields.Integer(required=True)
    item_ids = fields.List(fields.Integer(), required=True, validate=validate_item_ids)
    total_amount = fields.Float(required=True)
