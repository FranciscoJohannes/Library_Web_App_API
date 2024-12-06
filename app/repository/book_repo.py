from datetime import datetime
from app.models.book_model import BookModel
from app.extension import db


class BookRepository:

    @staticmethod
    def create_book(data):
        book = BookModel(**data)
        db.session.add(book)
        db.session.commit()

    @staticmethod
    def get_book_by_uuid(book_uuid):
        return BookModel.query.filter_by(book_uuid=book_uuid).first()

    @staticmethod
    def get_all():
        return BookModel.query.filter_by(deleted_at=None).all()

    @staticmethod
    def update_book(book, data):
        for key, value in data.items():
            setattr(book, key, value)
        db.session.commit()
        return book

    @staticmethod
    def delete_book(book):
        book.deleted_at = datetime.utcnow()
        db.session.commit()