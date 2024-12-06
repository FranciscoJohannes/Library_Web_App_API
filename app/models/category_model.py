import uuid
from sqlalchemy.dialects.mysql import CHAR
from app.extension import db


class CategoryModel(db.Model):
    __tablename__ = 'category'

    category_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    category_uuid = db.Column(CHAR(45), default=lambda: str(uuid.uuid4()), unique=True, nullable=False)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.TEXT, nullable=False)
    Field = db.Column(db.DateTime, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    deleted_at = db.Column(db.DateTime, nullable=True)