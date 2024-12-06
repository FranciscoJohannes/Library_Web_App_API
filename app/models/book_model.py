import uuid
from sqlalchemy.dialects.mysql import CHAR
from app.extension import db


class BookModel(db.Model):
    __tablename__ = 'book'

    book_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    book_uuid = db.Column(CHAR(45), default=lambda: str(uuid.uuid4()), unique=True, nullable=False)
    title = db.Column(db.String(255), nullable=False)
    author = db.Column(db.String(255), nullable=False)
    genre = db.Column(db.String(255), nullable=False)
    publication_date = db.Column(db.DateTime, nullable=False)
    ISBN = db.Column(db.String(255), nullable=False)
    language = db.Column(db.String(255), nullable=False)
    summary = db.Column(db.TEXT, nullable=False)
    cover_image_url = db.Column(db.String(255), nullable=False)
    source_url = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    deleted_at = db.Column(db.DateTime, nullable=True)