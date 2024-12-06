from marshmallow import Schema, fields

class BookSchema(Schema):
    book_id = fields.Int(dump_only=True)
    book_uuid = fields.Str(dump_only=True)
    title = fields.Str(required=True)
    author = fields.Str(required=True)
    genre = fields.Str(required=True)
    publication_date = fields.DateTime(required=True)
    ISBN = fields.Str(required=True)
    language = fields.Str(required=True)
    summary = fields.Str(required=True)
    cover_image_url = fields.Str(required=True)
    source_url = fields.Str(required=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
    deleted_at = fields.DateTime(dump_only=True)