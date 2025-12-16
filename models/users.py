import uuid
from db import db
import marshmallow as ma
from sqlalchemy.dialects.postgresql import UUID

class Users(db.Model):
    __tablename__ = "Users"

    user_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(50), nullable=False, default="user")
    is_active = db.Column(db.Boolean, default=True)

    caretaker = db.relationship("Caretakers", uselist=False, back_populates="user")
    tokens = db.relationship("AuthTokens", back_populates="user")

    def __init__(self, username, email, password_hash, role="user", is_active=True):
        self.username = username
        self.email = email
        self.password_hash = password_hash
        self.role = role
        self.is_active = is_active

    def new_user_obj():
        return Users('', '', '', 'user', True)

class UsersSchema(ma.Schema):
    class Meta:
        fields = ['user_id', 'username', 'email', 'role', 'is_active', 'caretaker']

    user_id = ma.fields.UUID()
    username = ma.fields.String()
    email = ma.fields.String()
    role = ma.fields.String()
    is_active = ma.fields.Boolean()
    caretaker = ma.fields.Nested('CaretakersSchema', exclude=['user'])

user_schema = UsersSchema()
users_schema = UsersSchema(many=True)