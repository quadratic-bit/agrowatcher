from app.models.database import db
from app.models.users import User  # noqa
from app import create_app


db.create_all(app=create_app())
