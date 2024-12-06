import uuid
from sqlalchemy.dialects.mysql import CHAR
from app.extension import db


class ProgressModel(db.Model):
    __tablename__ = 'progress'

    progress_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    progress_uuid = db.Column(CHAR(45), default=lambda: str(uuid.uuid4()), unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    book_id = db.Column(db.Integer, db.ForeignKey('book.book_id'))
    chapter_id = db.Column(db.Integer, nullable=False)
    progress_percentage = db.Column(db.DECIMAL, nullable=False)
    last_read_at = db.Column(db.DateTime, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    deleted_at = db.Column(db.DateTime, nullable=True)