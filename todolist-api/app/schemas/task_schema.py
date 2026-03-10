from marshmallow import Schema, fields

class TaskSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    completed = fields.Bool()
    created_at = fields.DateTime()

class TaskCreateSchema(Schema):
    title = fields.Str(required=True)

class TaskCompleteSchema(Schema):
    completed = fields.Bool(required=True)