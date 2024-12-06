from flask import abort, jsonify
from flask_smorest import Blueprint
from app.repository.progress_repo import ProgressRepository
from app.schema.progress_schema import ProgressSchema

progress_blp = Blueprint('progress', 'progress', url_prefix='/progress', description="Operation for progress")


@progress_blp.route("/", methods=['POST'])
@progress_blp.arguments(ProgressSchema)
@progress_blp.response(201, ProgressSchema)
def create_progress(data):
    progress = ProgressRepository.create_progress(data)
    return progress


@progress_blp.route("/<string:progress_id>", methods=['GET'])
@progress_blp.response(200, ProgressSchema)
def get_progress_by_id(progress_id):
    progress = ProgressRepository.get_progress_by_uuid(progress_id)

    if not progress:
        return jsonify({"message": "not found"}), 404
    return progress


@progress_blp.route("/", methods=['GET'])
@progress_blp.response(200, ProgressSchema(many=True))
def get_all_progress():
    progress = ProgressRepository.get_all()
    return progress


@progress_blp.route("/<string:progress_id>", methods=['PUT'])
@progress_blp.arguments(ProgressSchema)
@progress_blp.response(200, ProgressSchema)
def update_progress(data, progress_id):
    progress = ProgressRepository.get_progress_by_uuid(progress_id)

    if not progress:
        abort(description="Progress not found"), 404

    updated_progress = ProgressRepository.update_progress(progress, data)
    return updated_progress


@progress_blp.route("/<string:progress_id>", methods=['DELETE'])
@progress_blp.response(204)
def delete_progress(progress_id):
    progress = ProgressRepository.get_progress_by_uuid(progress_id)

    if not progress:
        abort( description="Progress Not Found"), 404

    ProgressRepository.delete_progress(progress)
    return ''