from flask import abort, jsonify
from flask_smorest import Blueprint
from app.schema.category_schema import CategorySchema
from app.repository.category_repo import CategoryRepository

category_blp = Blueprint('categories', 'categories', url_prefix='/categories', description="Operation for categories")


@category_blp.route("/", methods=['POST'])
@category_blp.arguments(CategorySchema)
@category_blp.response(201, CategorySchema)
def create_category(data):
    category = CategoryRepository.create_category(data)
    return category

@category_blp.route("/<string:category_id>", methods=['GET'])
@category_blp.response(200, CategorySchema)
def get_category_by_id(category_id):
    category = CategoryRepository.get_category_by_uuid(category_id)

    if not category:
        return jsonify({"message": "not found"}), 404
    return category

@category_blp.route("/", methods=['GET'])
@category_blp.response(200, CategorySchema(many=True))
def get_all_categories():
    category = CategoryRepository.get_all()
    return category

@category_blp.route("/<string:category_id>", methods=['PUT'])
@category_blp.arguments(CategorySchema)
@category_blp.response(200, CategorySchema)
def update_category(data, category_id):
    category = CategoryRepository.get_category_by_uuid(category_id)

    if not category:
        abort(description="Category not found"), 404

    updated_category = CategoryRepository.update_category(category, data)
    return updated_category

@category_blp.route("/<string:category_id>", methods=['DELETE'])
@category_blp.response(204)
def delete_category(category_id):
    category = CategoryRepository.get_category_by_uuid(category_id)

    if not category:
        abort(description="Category Not Found"), 404

    CategoryRepository.delete_category(category)
    return ''