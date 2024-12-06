from datetime import datetime
from app.models.progress_model import ProgressModel
from app.extension import db


class ProgressRepository:

    @staticmethod
    def create_progress(data):
        progress = ProgressModel(**data)
        db.session.add(progress)
        db.session.commit()

    @staticmethod
    def get_progress_by_uuid(progress_id):
        return ProgressModel.query.filter_by(progress_id=progress_id).first()

    @staticmethod
    def get_all():
        return ProgressModel.query.filter_by(deleted_at=None).all()

    @staticmethod
    def update_progress(progress, data):
        for key, value in data.items():
            setattr(progress, key, value)
        db.session.commit()
        return progress

    @staticmethod
    def delete_progress(progress):
        progress.deleted_at = datetime.utcnow()
        db.session.commit()