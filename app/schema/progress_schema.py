from marshmallow import Schema, fields

class ProgressSchema(Schema):
    progress_id = fields.Int(dump_only=True)
    progress_uuid = fields.Str(dump_only=True)
    user_id = fields.Int(required=True)
    book_id = fields.Int(required=True)
    chapter_id = fields.Int(required=True)
    progress_percentage = fields.Decimal(required=True)
    last_read_at = fields.DateTime(required=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
    deleted_at = fields.DateTime(dump_only=True)