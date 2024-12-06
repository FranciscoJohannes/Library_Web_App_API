from flask import abort, jsonify
from flask_smorest import Blueprint
from app.repository.book_repo import BookRepository
from app.schema.book_schema import BookSchema

book_blp = Blueprint('books', 'books', url_prefix='/books', description="Operation for books")


@book_blp.route("/", methods=['POST'])
@book_blp.arguments(BookSchema)
@book_blp.response(201, BookSchema)
def create_book(data):
    book = BookRepository.create_book(data)
    return book


@book_blp.route("/<string:book_id>", methods=['GET'])
@book_blp.response(200, BookSchema)
def get_book_by_id(book_id):
    book = BookRepository.get_book_by_uuid(book_id)
    if not book:
        return jsonify({"message": "not found"}), 404
    return book


@book_blp.route("/", methods=['GET'])
@book_blp.response(200, BookSchema(many=True))
def get_all_users():
    book = BookRepository.get_all()
    return book


@book_blp.route("/<string:book_id>", methods=['PUT'])
@book_blp.arguments(BookSchema)
@book_blp.response(200, BookSchema)
def update_book(data, book_id):
    book = BookRepository.get_book_by_uuid(book_id)
    if not book:
        abort(description="Book not found"), 404
    updated_book = BookRepository.update_book(book, data)
    return updated_book


@book_blp.route("/<string:book_id>", methods=['DELETE'])
@book_blp.response(204)
def delete_user(book_id):
    book = BookRepository.get_book_by_uuid(book_id)

    if not book:
        abort( description="Book Not Found"), 404
    BookRepository.delete_book(book)
    return ''